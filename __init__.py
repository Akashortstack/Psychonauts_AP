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
# import this when its finished
# from .PsychoSeed import gen_psy_seed

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

    required_client_version = (0, 4, 4)
    options_dataclass = PsychonautsOptions
    options: PsychonautsOptions
    item_name_to_id = item_dictionary_table

    location_name_to_id = all_locations

    def generate_early(self) -> None:
        """
        Using this to make Baggage local only.
        """ 
        for item in local_set:
            self.multiworld.local_items[self.player].value.add(item)

    def pre_fill(self) -> None:
        
        self.multiworld.get_location(LocationName.FinalBossEvent, self.player).place_locked_item(self.create_item("Victory"))
       
       
    def create_item(self, name: str) -> Item:
        """
        Returns created PSYItem
        """
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

        itempool = [self.create_item(item) for item, data in self.item_name_to_id.items() for _ in range(data)]

        self.multiworld.itempool += itempool

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
    # def generate_output(self, output_directory: str):
    #    """
     #   Generates the seed file for Randomizer Scripts folder 
      #  """
       # gen_psy_seed(self, output_directory)
