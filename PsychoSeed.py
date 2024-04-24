import os
import Utils
import zipfile
from typing import List, Tuple, Iterable, Union

from .Items import item_dictionary_table, item_counts
from .Locations import all_locations
from worlds.Files import APContainer

PSY_NON_LOCAL_ID_START = 377


class PSYContainer(APContainer):
    game: str = 'Psychonauts'

    def __init__(self, patch_data: str, base_path: str, output_directory: str,
        player=None, player_name: str = "", server: str = ""):
        self.patch_data = patch_data
        self.file_path = base_path
        container_path = os.path.join(output_directory, base_path + ".zip")
        super().__init__(container_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        opened_zipfile.writestr("RandoSeed.lua", self.patch_data)
        super().write_contents(opened_zipfile)


def gen_psy_ids(location_tuples_in: Iterable[Tuple[bool, Union[str, None], int]]) -> List[Tuple[int, int]]:
    """
    Generic Psychonauts ID generator. The input location tuples may come from scouted locations or from generated
    locations.
    """
    # append the item values, need to be in exact order
    # locations are handled by index in table
    # items from other games need to be converted to a new value
    # Starting at 377, +1 each time
    non_local_id = PSY_NON_LOCAL_ID_START

    # Initialize a list to store tuples of location ID and item code
    location_tuples = []

    placed_item_counts = {}

    # Pre-sort the tuples based on location ID to ensure the generated IDs are consistent even if the input is in a
    # different order.
    for is_local_item, local_item_name, location_id in sorted(location_tuples_in, key=lambda t: t[2]):
        if is_local_item:
            if local_item_name == "Victory" or local_item_name == "Filler":
                # It is an event item, such as those used for Victory and Filler event locations.
                itemcode = 999
            else:
                # When there are multiple copies of an item, locally placed items start from the maximum id for that
                # item and count backwards for each item placed.
                # Conversely, as items with multiple copies are received from the multiworld, the received ids start
                # from the minimum id for that item and count upwards for each item received.
                base_item_code = item_dictionary_table[local_item_name]
                item_count = item_counts[local_item_name]
                max_item_code = base_item_code + item_count - 1
                count_placed = placed_item_counts.setdefault(base_item_code, 0)

                itemcode = max_item_code - count_placed
                assert itemcode >= base_item_code, "More '%s' items were placed locally than exist" % local_item_name

                placed_item_counts[base_item_code] = count_placed + 1
        else:
            # item from another game
            itemcode = non_local_id
            non_local_id += 1

        # Append the location ID and item code tuple to the list

        location_tuples.append((location_id, itemcode))

    return location_tuples


def gen_psy_ids_from_filled_locations(self) -> List[Tuple[int, int]]:
    location_tuples = []

    for location in self.multiworld.get_filled_locations(self.player):

        location_id = all_locations[location.name]

        is_local = location.item and location.item.player == self.player
        local_item_name = location.item.name if is_local else None

        location_tuples.append((is_local, local_item_name, location_id))

    return gen_psy_ids(location_tuples)


def gen_psy_seed(self, output_directory):
    # Mod name for Zip Folder
    mod_name = f"AP-{self.multiworld.seed_name}-P{self.player}-{self.multiworld.get_file_safe_player_name(self.player)}"

    # Need to clip off the seed name for Display Version to fit in Randomizer
    rando_display_name = f"AP-P{self.player}-{self.multiworld.get_file_safe_player_name(self.player)}"

    randoseed_parts = []

    # First part of lua code structure
    formattedtext1 = '''function RandoSeed(Ob)
        if ( not Ob ) then
            Ob = CreateObject('ScriptBase')
            Ob.seed = {}
        '''
    randoseed_parts.append(formattedtext1)

    # append mod_name 
    randoseed_parts.append(f"       Ob.seedname = '{rando_display_name}'\n")

    # append startlevitation setting
    if self.multiworld.StartingLevitation[self.player] == False:
        startlevitationsetting = "FALSE"
    else:
        startlevitationsetting = "TRUE"
    randoseed_parts.append(f"           Ob.startlevitation = {startlevitationsetting}\n")

    # append mentalmagnet setting
    if self.multiworld.StartingMentalMagnet[self.player] == False:
        mentalmagnetsetting = "FALSE"
    else:
        mentalmagnetsetting = "TRUE"
    randoseed_parts.append(f"           Ob.mentalmagnet = {mentalmagnetsetting}\n")

    # append lootboxvaults setting
    if self.multiworld.LootboxVaults[self.player] == False:
        lootboxvaultssetting = "FALSE"
    else:
        lootboxvaultssetting = "TRUE"
    randoseed_parts.append(f"           Ob.lootboxvaults = {lootboxvaultssetting}\n")

    # append enemydamagemultiplier setting
    enemydamagemultiplier = self.multiworld.EnemyDamageMultiplier[self.player].value
    randoseed_parts.append(f"           Ob.enemydamagemultiplier = {enemydamagemultiplier}\n")

    # append instantdeath setting
    if self.multiworld.InstantDeathMode[self.player] == False:
        instantdeathsetting = "FALSE"
    else:
        instantdeathsetting = "TRUE"
    randoseed_parts.append(f"           Ob.instantdeath = {instantdeathsetting}\n")

    # append easymillarace setting
    if self.multiworld.EasyMillaRace[self.player] == False:
        easymillarace = "FALSE"
    else:
        easymillarace = "TRUE"
    randoseed_parts.append(f"           Ob.easymillarace = {easymillarace}\n")

    # append easyflight setting
    if self.multiworld.EasyFlightMode[self.player] == False:
        easyflight = "FALSE"
    else:
        easyflight = "TRUE"
    randoseed_parts.append(f"           Ob.easyflight = {easyflight}\n")

    # append requireMC setting
    if self.multiworld.RequireMeatCircus[self.player] == False:
        requireMC = "FALSE"
    else:
        requireMC = "TRUE"
    randoseed_parts.append(f"           Ob.requireMC = {requireMC}\n")

    # append Goal settings
    if self.multiworld.Goal[self.player] == "braintank" or self.multiworld.Goal[self.player] == "braintank_and_brainhunt":
        beatoleander = "TRUE"
    else:
        beatoleander = "FALSE"
    
    if self.multiworld.Goal[self.player] == "brainhunt" or self.multiworld.Goal[self.player] == "braintank_and_brainhunt":
        requirebrainhunt = "TRUE"
    else:
        requirebrainhunt = "FALSE"
    
    randoseed_parts.append(f"           Ob.beatoleander = {beatoleander}\n")
    randoseed_parts.append(f"           Ob.brainhunt = {requirebrainhunt}\n")

    # append Brain Jar Requirement
    brainsrequired = self.multiworld.BrainsRequired[self.player].value
    randoseed_parts.append(f"           Ob.brainsrequired = {brainsrequired}\n")
    
    # Section where default settings booleans are written to RandoSeed.lua
    # adding new settings will remove from this list
    default_seed_settings = '''
        Ob.startcobweb = FALSE
        Ob.startbutton = FALSE
        Ob.randomizecobwebduster = TRUE
        Ob.everylocationpossible = FALSE
        Ob.harderbutton = FALSE
        Ob.beatalllevels = FALSE
        Ob.rank101 = FALSE
        Ob.scavengerhunt = FALSE
        Ob.fasterLO = TRUE
        Ob.earlyelevator = FALSE
        Ob.removetutorials = TRUE
        Ob.createhints = FALSE
        Ob.spoilerlog = FALSE
    '''
    randoseed_parts.append(default_seed_settings)

    location_tuples = gen_psy_ids_from_filled_locations(self)

    # attach more lua code structure first
    formattedtext2 = '''
    end
    
    function Ob:fillTable()
    local SEED_GOES_HERE = {
    
    
    '''
    randoseed_parts.append(formattedtext2)

    # Iterate through the sorted list of tuples and append item codes to randoseed_parts
    for index, (location_id, itemcode) in enumerate(location_tuples):
        randoseed_parts.append(str(itemcode))
        # Format so that each line has 10 values, for readability
        if index > 0 and (index + 1) % 10 == 0:
            randoseed_parts.append(",\n")
        else:
            randoseed_parts.append(", ")


    formattedtext3 = ''' }
        self.seed = SEED_GOES_HERE
        end
        return Ob
    end

    '''

    randoseed_parts.append(formattedtext3)

    # Combine all the parts into one long piece of text
    randoseed = ''.join(randoseed_parts)
    
    mod_dir = os.path.join(output_directory, mod_name + "_" + Utils.__version__)

    mod = PSYContainer(randoseed, mod_dir, output_directory, self.player,
            self.multiworld.get_file_safe_player_name(self.player))
    mod.write()