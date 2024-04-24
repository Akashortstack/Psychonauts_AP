from __future__ import annotations
import os
import sys
import asyncio
import logging
from typing import Dict, Any, Set, List

import ModuleUpdate
ModuleUpdate.update()
import Utils
from .Items import (
    item_dictionary_table,
    item_counts,
    AP_ITEM_OFFSET,
    reverse_item_dictionary_table,
    find_item_name_from_psy_id,
)
from .Locations import AP_LOCATION_OFFSET, all_fillable_locations
from .PsychoSeed import gen_psy_ids, PSY_NON_LOCAL_ID_START

logger = logging.getLogger("Client")

if __name__ == "__main__":
    Utils.init_logging("PsychonautsClient", exception_logger="Client")

from NetUtils import NetworkItem, ClientStatus
from CommonClient import gui_enabled, logger, get_base_parser, ClientCommandProcessor, \
    CommonContext, server_loop

# using this to find the folder game was launched from
# then find ModData folder there
def find_moddata_folder(root_directory):
    moddata_folder = os.path.join(root_directory, "ModData")
    if os.path.exists(moddata_folder):
        return moddata_folder
    else:
        print_error_and_close("PsychonautsClient couldn't find ModData folder. "
                                  "Unable to infer required game_communication_path")


def print_error_and_close(msg):
    logger.error("Error: " + msg)
    Utils.messagebox("Error", msg, error=True)
    sys.exit(1)

class PsychonautsClientCommandProcessor(ClientCommandProcessor):
    def _cmd_resync(self):
        """Manually trigger a resync."""
        self.output(f"Syncing items.")
        self.ctx.syncing = True
    
    def _cmd_deathlink(self):
        """Toggles Deathlink"""
        if isinstance(self.ctx, PsychonautsContext):
            self.ctx.deathlink_status = not self.ctx.deathlink_status
            if self.ctx.deathlink_status:
                self.output(f"Deathlink enabled.")
            else:
                self.output(f"Deathlink disabled.")

class PsychonautsContext(CommonContext):
    command_processor: int = PsychonautsClientCommandProcessor
    game = "Psychonauts"
    items_handling = 0b111  # full remote

    max_item_counts: Dict[int, int]
    non_local_received_item_counts: Dict[int, int]  # server state
    local_psy_location_to_local_psy_item_id: Dict[int, int]  # server state
    local_psy_item_ids: Set[int]  # server state
    has_local_location_data: bool  # server state
    pending_received_items: List[NetworkItem]  # server state
    cheated_local_psy_locations: Set[int]  # server state

    def __init__(self, server_address, password):
        super(PsychonautsContext, self).__init__(server_address, password)
        self.send_index: int = 0
        self.syncing = False
        self.awaiting_bridge = False
        self.got_deathlink = False
        self.deathlink_status = False

        # The maximum number of each item that Psychonauts can receive before it runs out of unique IDs for that item.
        self.max_item_counts = {item_dictionary_table[item_name] + AP_ITEM_OFFSET: count
                                for item_name, count in item_counts.items()}
        # The number of times each item has been received from a non-local location.
        self.non_local_received_item_counts = {item_id: 0 for item_id in self.max_item_counts.keys()}

        # When connecting to a server, the contents of self.locations_scouted are sent in a LocationScouts request,
        # filling self.locations_info once the LocationsInfo response is received.
        # Scout all local locations so that the client can figure out the Psychonauts item IDs of all locally placed
        # items.
        # Note: Event locations cannot be scouted.
        self.locations_scouted.update(location_id + AP_LOCATION_OFFSET
                                      for location_id in all_fillable_locations.values())

        # These are read from self.locations_info after the response from the initial request of scouting all local
        # locations:
        # Mapping from Psychonauts location ID to Psychonauts item ID for all locally placed items.
        self.local_psy_location_to_local_psy_item_id = {}
        # Set of Psychonauts item IDs of locally placed items. These IDs cannot be used when receiving non-local items.
        self.local_psy_item_ids = set()

        # Used to specify whether local location data has been read from scouted locations.
        self.has_local_location_data = False

        # Items cannot be received by Psychonauts before the client has received the local location data, so this list
        # is used to store, in order, all received items that still need to be received by Psychonauts.
        self.pending_received_items = []

        # Keep track of cheated local items sent via server command so that receiving multiple cheated items at once
        # will correctly send a unique Psychonauts item ID for each cheated item.
        # The locations of the cheated local items could be added to `self.checked_locations` instead, but the locations
        # technically haven't been checked until Psychonauts receives the item and then tells the client that it has
        # checked the location that item was at.
        self.cheated_local_psy_locations = set()

        options = Utils.get_settings()
        root_directory = options["psychonauts_options"]["root_directory"]
        
        # self.game_communication_path: files go in this path to pass data between us and the actual game
        moddata_folder = find_moddata_folder(root_directory)
        self.game_communication_path = moddata_folder

    def reset_server_state(self):
        super().reset_server_state()
        # Disconnecting and reconnecting aside, the client could instead get connected to a different server to before,
        # so all the old data specific to the previous connection must be reset to its initial state as if this is the
        # first time the client is connecting to a server.
        self.non_local_received_item_counts = {item_id: 0 for item_id in self.max_item_counts.keys()}
        self.local_psy_location_to_local_psy_item_id = {}
        self.local_psy_item_ids = set()
        self.has_local_location_data = False
        self.pending_received_items = []
        self.cheated_local_psy_locations = set()

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(PsychonautsContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def connection_closed(self):
        await super(PsychonautsContext, self).connection_closed()
        for root, dirs, files in os.walk(self.game_communication_path):
            for file in files:
                if "Items" not in file and "Deathlink" not in file:
                    os.remove(root+"/"+file)

    @property
    def endpoints(self):
        if self.server:
            return [self.server]
        else:
            return []

    async def shutdown(self):
        await super(PsychonautsContext, self).shutdown()
        for root, dirs, files in os.walk(self.game_communication_path):
            for file in files:
                if "Items" not in file and "Deathlink" not in file:
                    os.remove(root+"/"+file)

    def calc_psy_ids_from_scouted_local_locations(self):
        # Attempt to figure out the Psychonauts IDs for all locally placed items.
        location_tuples = []
        for psy_location_id in all_fillable_locations.values():
            ap_location_id = psy_location_id + AP_LOCATION_OFFSET
            scouted_network_item = self.locations_info.get(ap_location_id)
            if scouted_network_item is None:
                # Some or all of the requested location info has not been received yet.
                # Generally, this shouldn't happen because sending a LocationScouts request for all local locations
                # is one of the first things the client does after connecting to a server.
                return False
            is_local_item = scouted_network_item.player == self.slot
            if is_local_item:
                item_name = reverse_item_dictionary_table[scouted_network_item.item - AP_ITEM_OFFSET]
            else:
                item_name = None
            location_tuples.append((is_local_item, item_name, psy_location_id))

        # All the information needed to figure out the Psychonaunts item IDs of locally placed items has been
        # acquired.

        # Note that event item locations are not provided here and are not real locations that can be scouted. The
        # event locations have no effect on the generated Psychonauts IDs of local items, so the event item
        # locations can be omitted from the calculation.
        psy_id_tuples = gen_psy_ids(location_tuples)

        # Convert the list of tuples into a dict and filter out items from other worlds.
        self.local_psy_location_to_local_psy_item_id = {location_id: item_id for location_id, item_id
                                                        in psy_id_tuples if item_id < PSY_NON_LOCAL_ID_START}
        self.local_psy_item_ids = set(self.local_psy_location_to_local_psy_item_id.values())

        return True

    def receive_local_item(self, ap_location_id, ap_item_id, base_psy_item_id, max_psy_item_id):
        """
        Receive an item from the local world.
        """
        # Locally placed items must write the exact Psychonauts item ID they were placed as.
        # Writing locally placed items is required for resuming an in-progress slot from a new save file without having
        # to manually collect the local items again.
        psy_location_id = ap_location_id - AP_LOCATION_OFFSET
        if psy_location_id not in self.local_psy_location_to_local_psy_item_id:
            # This should not happen unless AP can send dummy local location IDs for locations that do not exist.
            logger.error("Error: Local item received from non-existent local location '%s'", ap_location_id)
            return

        # Get the Psychonauts item id for the item at this local location.
        local_item_psy_id = self.local_psy_location_to_local_psy_item_id[psy_location_id]
        # Check that the Psychonauts ID matches the item AP thinks is at this location.
        if base_psy_item_id <= local_item_psy_id <= max_psy_item_id:
            # Tell Psychonauts it has received the item.
            with open(os.path.join(self.game_communication_path, "ItemsReceived.txt"), 'a') as f:
                f.write(f"{local_item_psy_id}\n")
        else:
            # This should not happen unless the scouted location data is incorrect or the Psychonauts item IDs have been
            # incorrectly calculated from the scouted location data.
            ap_item_name = reverse_item_dictionary_table.get(base_psy_item_id, f"Unknown {ap_item_id}")
            expected_item_name = find_item_name_from_psy_id(local_item_psy_id)
            if expected_item_name is None:
                expected_item_name = f"Unknown {local_item_psy_id + AP_ITEM_OFFSET}"
            logger.error("Error: Tried to receive item '%s' from local location '%i', but the item should be '%s'"
                         " according to scouted location info.", ap_item_name, ap_location_id, expected_item_name)

    def receive_non_local_item(self, ap_location_id, ap_item_id, base_psy_item_id, max_psy_item_id):
        """
        Receive an item from another world.
        """
        psy_item_id = None
        if ap_location_id == -1:
            # The item was sent by a cheat command.

            # Attempt to find a local copy that has yet to be collected and send that so that all non-local copies of
            # the item can still be sent.
            # The local copies of each item could be found and stored in advance instead of iterating here, but sending
            # items through cheat commands shouldn't happen often.
            for psy_location_id in self.local_psy_location_to_local_psy_item_id.keys():
                ap_item_id_at_location = self.locations_info[psy_location_id + AP_LOCATION_OFFSET].item
                if (ap_item_id_at_location == ap_item_id
                        and ap_location_id not in self.checked_locations
                        and psy_location_id not in self.cheated_local_psy_locations):
                    psy_item_id = self.local_psy_location_to_local_psy_item_id[psy_location_id]
                    # If multiple items from cheat commands are received at once, e.g. the cheat command is used
                    # multiple times before the client has connected, then self.checked_locations won't be updated after
                    # the first cheated item, so an extra set is used to keep track of cheated local locations
                    # containing local items.
                    self.cheated_local_psy_locations.add(psy_location_id)
                    break

        if psy_item_id is None:
            # For non-local received items, the Psychonauts ID is incremented for each copy of that received so far, so
            # that each item received produces a unique Psychonauts ID.

            # Count of this item received from other worlds so far.
            item_count_received = self.non_local_received_item_counts[ap_item_id]
            psy_item_id = base_psy_item_id + item_count_received
            # Psychonauts has a limited number of IDs for each duplicate of an item, so check if it's possible to
            # receive more of this item.
            if psy_item_id in self.local_psy_item_ids or psy_item_id > max_psy_item_id:
                # Locally placed Psychonauts items are placed starting from that item's maximum ID and decrementing the
                # ID for each item placed, so reaching the Psychonauts ID of a locally placed item means that all
                # available copies of this item have been received or placed locally.
                #
                # Alternatively, if there were no locally placed copies of the item, then Psychonauts will only have run
                # out of IDs for the item once the maximum ID for that item has been reached.
                item_name = reverse_item_dictionary_table.get(base_psy_item_id, f"Unknown item {ap_item_id}")
                logger.warning("Warning: Could not receive item '%s' because Psychonauts has run out of unique IDs for"
                               " non-local copies of that item. This should only happen when items have been sent using"
                               " server cheat commands.", item_name)
                return

            # Increment the received count for this item, so that the next received copy of this item uses the next ID.
            self.non_local_received_item_counts[ap_item_id] = item_count_received + 1

        # Tell Psychonauts it has received the item.
        with open(os.path.join(self.game_communication_path, "ItemsReceived.txt"), 'a') as f:
            f.write(f"{psy_item_id}\n")

    def receive_item(self, network_item: NetworkItem):
        if not self.has_local_location_data:
            raise RuntimeError("receive_item() was called before local location data has been received and processed")

        ap_item_id = network_item.item
        # Subtract the AP item offset to get the base item ID for Psychonauts.
        base_psy_item_id = ap_item_id - AP_ITEM_OFFSET

        # The maximum number of times this item can be received by Psychonauts due to Psychonauts having a limited
        # number of unique IDs per item.
        max_item_count = self.max_item_counts[ap_item_id]
        # Maximum Psychonauts ID for this item when there are multiple copies.
        max_psy_item_id = base_psy_item_id + max_item_count - 1

        # Check if the item was placed locally.
        if network_item.player == self.slot:
            self.receive_local_item(network_item.location, ap_item_id, base_psy_item_id, max_psy_item_id)
        else:
            self.receive_non_local_item(network_item.location, ap_item_id, base_psy_item_id, max_psy_item_id)

    def on_package(self, cmd: str, args: dict):
        if cmd in {"Connected"}:
            if not os.path.exists(self.game_communication_path):
                os.makedirs(self.game_communication_path)
            # create ItemsCollected.txt if it doesn't exist yet
                
            # Path to the ItemsCollected.txt file inside the ModData folder
            items_collected_path = os.path.join(self.game_communication_path, "ItemsCollected.txt")
            if not os.path.exists(items_collected_path):
                with open(items_collected_path, 'w') as f:
                    f.write(f"")
                    f.close()
            # empty ItemsReceived.txt to avoid appending duplicate items lists
            with open(os.path.join(self.game_communication_path, "ItemsReceived.txt"), 'w') as f:
                f.write(f"")
                f.close()
            for ss in self.checked_locations:
                filename = f"send{ss}"
                with open(os.path.join(self.game_communication_path, filename), 'w') as f:
                    f.close()
        if cmd in {"ReceivedItems"}:
            start_index = args["index"]
            if start_index != len(self.items_received):
                if self.has_local_location_data:
                    receive_item = self.receive_item
                else:
                    # Received items cannot be processed yet, so store them for later.
                    # This typically happens when reconnecting to a server where some items have already been received
                    # because the server will immediately send all items received so far.
                    receive_item = self.pending_received_items.append
                for item in args['items']:
                    network_item = NetworkItem(*item)
                    receive_item(network_item)

        if cmd in {"RoomUpdate"}:

            if "checked_locations" in args:
                for ss in self.checked_locations:
                    filename = f"send{ss}"
                    with open(os.path.join(self.game_communication_path, filename), 'w') as f:
                        f.close()

        if cmd == "LocationInfo":
            if not self.has_local_location_data:
                # It could be the response to the initial LocationScouts request that was sent out to get all local
                # location data.
                # Try to set up the local item data and receive any pending received items.
                if self.calc_psy_ids_from_scouted_local_locations():
                    # Items can now be received.
                    self.has_local_location_data = True
                    if self.pending_received_items:
                        for network_item in self.pending_received_items:
                            self.receive_item(network_item)
                        self.pending_received_items.clear()

    def run_gui(self):
        """Import kivy UI system and start running it as self.ui_task."""
        from kvui import GameManager

        class PsychonautsManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Psychonauts Client"

        self.ui = PsychonautsManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def on_deathlink(self, data: Dict[str, Any]):
        self.got_deathlink = True
        super().on_deathlink(data)

async def game_watcher(ctx: PsychonautsContext):
    from worlds.psychonauts.Locations import all_locations
    while not ctx.exit_event.is_set():
        # Check for DeathLink toggle
        await ctx.update_death_link(ctx.deathlink_status)

        if ctx.syncing == True:
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False
        
        # Check for Deathlink to send to player
        if ctx.got_deathlink:
            ctx.got_deathlink = False
            with open(os.path.join(ctx.game_communication_path, "DeathlinkIn.txt"), 'a') as f:
                f.write("DEATH\n")
                f.close()
        
        # Check for Deathlinks from player
        with open(os.path.join(ctx.game_communication_path, "DeathlinkOut.txt"), 'r+') as f:
            RazDied = f.read()
            if RazDied:
                # Move the file pointer to the beginning
                f.seek(0)
                # Empty the file by writing an empty string
                f.truncate(0)
                if "DeathLink" in ctx.tags:
                    await ctx.send_death(death_text = f"{ctx.player_names[ctx.slot]} became lost in thought!")
            f.close
        
        sending = []
        # Initialize an empty table
        collected_table = []
        victory = False
        
        # Open the file in read mode
        with open(os.path.join(ctx.game_communication_path, "ItemsCollected.txt"), 'r') as f:
            collected_items = f.readlines()            
            # Iterate over each line in the file
            for line in collected_items:
                # Convert the line to a float and add it to the table
                value = float(line.strip())
                # Keep track of already collected values
                if value not in collected_table:
                    # add the base_id 42690000
                    sending = sending+[(int(value + AP_LOCATION_OFFSET))]
                    collected_table.append(value)
            f.close()

        for root, dirs, files in os.walk(ctx.game_communication_path):
            for file in files:
                if file.find("victory.txt") > -1:
                    victory = True
                    
        ctx.locations_checked = sending
        message = [{"cmd": 'LocationChecks', "locations": sending}]
        await ctx.send_msgs(message)
        if not ctx.finished_game and victory == True:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True
        await asyncio.sleep(0.1)


def launch():
    async def main(args):
        ctx = PsychonautsContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        progression_watcher = asyncio.create_task(
            game_watcher(ctx), name="PsychonautsProgressionWatcher")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await progression_watcher

        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="Psychonauts Client, for text interfacing.")

    args, rest = parser.parse_known_args()
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()



