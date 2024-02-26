import logging
from typing import List

from BaseClasses import Tutorial, ItemClassification
from Fill import fill_restrictive
from worlds.LauncherComponents import Component, components, Type, launch_subprocess
from worlds.AutoWorld import World, WebWorld
from .Items import *
from .Locations import *
from .Names import ItemName, LocationName, RegionName
from .Options import PsychonautsOptions
from .Regions import create_regions, connect_regions
from .Rules import *
from .Subclasses import PSYItem
from .PsychoSeed import gen_psy_seed

# If we need a custom client, call for it here
# def launch_client():
    # from .Client import launch
    # launch_subprocess(launch, name="PSYClient")

# components.append(Component("PSY Client", "PSYClient", func=launch_client, component_type=Type.CLIENT))


class PsychonautsWeb(WebWorld):
    tutorials = [Tutorial(
            "Multiworld Setup Guide",
            "A guide to playing Psychonauts with Archipelago.",
            "English",
            # File does not exist yet!!!
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

    required_client_version = (0, 4, 4)
    options_dataclass = PsychonautsOptions
    options: PsychonautsOptions
    item_name_to_id = {item: item_id
                       for item_id, item in enumerate(item_dictionary_table.keys(), 0x130000)}
    location_name_to_id = {item: location
                           for location, item in enumerate(all_locations.keys(), 0x130000)}

    item_name_groups = item_groups
    location_name_groups = location_groups

    plando_locations: Dict[str, str]
    filler_items: List[str]
    item_quantity_dict: Dict[str, int]
    local_items: Dict[int, int]
    total_locations: int

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)


    def fill_slot_data(self) -> dict:

        slot_data = self.options.as_dict("Goal")
        
        return slot_data

    def create_item(self, name: str) -> Item:
        """
        Returns created PSYItem
        """
        # data = item_dictionary_table[name]
        if name in progression_set:
            item_classification = ItemClassification.progression
        elif name in useful_set:
            item_classification = ItemClassification.useful
        else:
            item_classification = ItemClassification.filler
        created_item = PSYItem(name, item_classification, self.item_name_to_id[name], self.player)

        return created_item

    def create_event_item(self, name: str) -> Item:
        item_classification = ItemClassification.progression
        created_item = PsyItem(name, item_classification, None, self.player)
        return created_item

    def create_items(self) -> None:
        """
        Fills ItemPool 
        """

        itempool = [self.create_item(item) for item, data in self.item_quantity_dict.items() for _ in range(data)]

        # Creating filler for unfilled locations
        itempool += [self.create_filler() for _ in range(self.total_locations - len(itempool))]

        self.multiworld.itempool += itempool


    def generate_early(self) -> None:
        """
        Determines the quantity of items and maps plando locations to items.
        """
        # Item: Quantity Map
        self.total_locations = len(all_locations.keys())

        self.item_quantity_dict = {item: data.quantity for item, data in item_dictionary_table.items()}

        # Dictionary to mark locations with their plandoed item

        self.plando_locations = dict()
        self.starting_invo_verify()


        self.set_excluded_locations()


    def pre_fill(self):
        """
        Plandoing Events and Fill_Restrictive
        """

        for location, item in self.plando_locations.items():
            self.multiworld.get_location(location, self.player).place_locked_item(
                    self.create_item(item))

    def create_regions(self):
        """
        Creates the Regions and Connects them.
        """
        create_regions(self)
        connect_regions(self)

    def set_rules(self):
        """
        Sets the Logic for the Regions and Locations.
        """
        universal_logic = Rules.PsyWorldRules(self)
        universal_logic.set_psy_rules()

    # PsychoSeed.py needs to be functional to output a seed/patch file
    # Example found in /docs
    def generate_output(self, output_directory: str):
        """
        Generates the seed file for Randomizer Scripts folder 
        """
        gen_psy_seed(self, output_directory)
