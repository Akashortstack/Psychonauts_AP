import logging
from typing import List, Mapping, Any
import settings

from BaseClasses import Tutorial, ItemClassification
from Fill import fill_restrictive
from worlds.LauncherComponents import Component, components, Type, launch_subprocess
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Item
from .Items import *
from .Locations import *
from .Names import ItemName, LocationName, RegionName
from .Options import Goal, PsychonautsOptions, slot_data_options
from .Regions import create_psyregions, connect_regions
from .Rules import *
from .Subclasses import PSYItem
from .PsychoSeed import gen_psy_seed, gen_psy_ids, PSY_NON_LOCAL_ID_START

def launch_client():
    from .Client import launch
    launch_subprocess(launch, name="PSYClient")

components.append(Component("Psychonauts Client", "PSYClient", func=launch_client, component_type=Type.CLIENT))

# borrowed from Wargroove
class PsychonautsSettings(settings.Group):
    class RootDirectory(settings.UserFolderPath):
        """
        Locate the Psychonauts root directory on your system.
        This is used by the Psychonauts client, so it knows where to send communication files to
        """
        description = "Psychonauts root directory"

    root_directory: RootDirectory = RootDirectory("C:\\\\Program Files (x86)\\\\Steam\\\\steamapps\\\\common\\\\Psychonauts")

class PsychonautsWeb(WebWorld):
    tutorials = [Tutorial(
            "Multiworld Setup Guide",
            "A guide to playing Psychonauts with Archipelago.",
            "English",
            # Not finished yet
            "setup_en.md",
            "setup/en",
            ["Akashortstack"]
    )]


class PSYWorld(World):
    """
    Psychonauts is a third-person action platformer game developed by Double Fine Productions, published by Majesco Entertainment, and released in 2005.
    The player follows Razputin, a young boy gifted with Psychic abilities. After sneaking into a secret psychic summer camp, it's up to Raz to explore 
    the minds of other characters, and save his fellow psychic campers from an evil doctor.
    
    """
    game = "Psychonauts"
    web = PsychonautsWeb()

    settings: typing.ClassVar[PsychonautsSettings]
    required_client_version = (0, 4, 4)
    options_dataclass = PsychonautsOptions
    options: PsychonautsOptions

    base_id = 42690001

    item_name_to_id = {item: id + 42690000 for item, id in item_dictionary_table.items()}

    item_name_groups = item_groups

    location_name_to_id = {item: id + 42690000 for item, id in all_locations.items()}

    

    def generate_early(self) -> None:
        """
        Using this to make Baggage local only.
        """ 
        for item in local_set:
            self.multiworld.local_items[self.player].value.add(item)

        # if self.multiworld.StartingLevitation[self.player]:
        #     self.multiworld.push_precollected(self.create_item(ItemName.Levitation1))
       
    def create_item(self, name: str) -> Item:
        """
        Returns created PSYItem
        """
        # TODO: current code fails test/general/test_items: test_create_item
        # Raises AttributeError for all brain jars, fully functional when generating
        if name in BrainJar_Table:
            # make brains filler if BrainHunt not a selected option
            if self.options.Goal == 0:
                item_classification = ItemClassification.filler
            else:
                item_classification = ItemClassification.progression
        elif name in progression_set:
            item_classification = ItemClassification.progression
        elif name in useful_set:
            item_classification = ItemClassification.useful
        else:
            item_classification = ItemClassification.filler

        

        created_item = PSYItem(name, item_classification, self.item_name_to_id[name], self.player)

        return created_item

    def create_event_item(self, name: str) -> Item:
        item_classification = ItemClassification.progression
        created_item = PSYItem(name, item_classification, None, self.player)
        return created_item
    
    def create_event(self, event: str) -> Item:
        # while we are at it, we can also add a helper to create events
        return Item(event, True, None, self.player)

    def create_items(self):
        """
        Fills ItemPool 
        """
        self.mindlock_dict = MindUnlocks_Table.copy()
        self.adjusted_item_pool = self.item_name_to_id.copy()


        for _ in range(self.options.RandomStartingMinds.value):
            visitlocking_set = list(self.mindlock_dict.keys())
            item = self.random.choice(visitlocking_set)
            self.mindlock_dict.pop(item)
            self.adjusted_item_pool.pop(item)
            self.multiworld.push_precollected(self.create_item(item))

        itempool = []

        # Fill the pool with as many items as there are local locations that can have items placed into.
        total_item_count = FILLABLE_LOCATION_COUNT
        created_item_count = 0
        for item_name in self.adjusted_item_pool.keys():
            item_count = item_counts[item_name]
            remaining_items = total_item_count - created_item_count
            number_to_create = min(item_count, remaining_items)

            for _ in range(number_to_create):
                itempool.append(self.create_item(item_name))
            created_item_count += number_to_create

            if number_to_create != item_count:
                # No more items can be created.
                break

        assert len(itempool) == total_item_count

        self.multiworld.itempool += itempool

    def create_regions(self):
        """
        Creates the Regions and Connects them.
        """
        
        create_psyregions(self.multiworld, self.player)
        connect_regions(self.multiworld, self.player)

    def set_rules(self):
        """
        Sets the Logic for the Regions and Locations.
        """
        universal_logic = Rules.PsyRules(self)
        universal_logic.set_psy_rules()
        # place "Victory" at "Final Boss" and set collection as win condition
        # self.multiworld.get_location(LocationName.FinalBossEvent, self.player).place_locked_item(self.create_event_item("Victory"))
        # self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)   

    
    def generate_output(self, output_directory: str):
        """
        Generates the seed file for Randomizer Scripts folder 
        """
        # Creates RandoSeed.lua file for Randomizer Mod
        # Example found in /docs
        gen_psy_seed(self, output_directory)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = {}
        for name, value in self.options.as_dict(*self.options_dataclass.type_hints).items():
            if name in slot_data_options:
                slot_data[name] = value
        return slot_data
