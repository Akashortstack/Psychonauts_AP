from typing import Mapping, Any, ClassVar, Dict

import settings
from BaseClasses import Tutorial, ItemClassification
from worlds.LauncherComponents import Component, components, Type, launch_subprocess
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Item

from .Items import (
    item_dictionary_table,
    MindUnlocks_Table,
    BrainJar_Table,
    local_set,
    progression_set,
    useful_set,
    item_groups,
    item_counts,
    AP_ITEM_OFFSET
)
from .ItemUtils import repeated_item_names_gen
from .Locations import all_locations, AP_LOCATION_OFFSET, deep_arrowhead_locations, mental_cobweb_locations
from .Names import ItemName, LocationName
from .Options import Goal, PsychonautsOptions, slot_data_options
from . import Regions
from . import Rules
from .Subclasses import PSYItem
from .PsychoSeed import gen_psy_seed

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

    settings: ClassVar[PsychonautsSettings]
    required_client_version = (0, 4, 4)
    options_dataclass = PsychonautsOptions
    options: PsychonautsOptions

    item_name_to_id = {item: id + AP_ITEM_OFFSET for item, id in item_dictionary_table.items()}

    item_name_groups = item_groups

    location_name_to_id = {item: id + AP_LOCATION_OFFSET for item, id in all_locations.items()}

    

    def generate_early(self) -> None:
        """
        Using this to make Baggage local only.
        """ 
        for item in local_set:
            self.options.local_items.value.add(item)

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

    def get_filler_item_name(self) -> str:
        return ItemName.PsiCard

    def create_event_item(self, name: str) -> Item:
        item_classification = ItemClassification.progression
        created_item = PSYItem(name, item_classification, None, self.player)
        return created_item

    @staticmethod
    def _add_deep_arrowhead_shuffle_items(item_counts: Dict[str, int]):
        # The Dowsing Rod is added to the item pool.
        item_counts[ItemName.DowsingRod] += 1

        # Additional small and large arrowhead bundles are added to the pool.
        # Each deep arrowhead has a specific worth of arrowheads given to the player when dug up, the total is 2696.
        # There are currently 49 Deep Arrowhead locations, so the average worth of a deep arrowhead is currently 55.02,
        # more than a small arrowhead bundle (25), but less than a large arrowhead bundle (100).
        # 29 * 25 + 20 * 100 = 2725
        small_count = 29
        large_count = 20
        # To find the optimal combination of small and large arrowhead bundles:
        # # Start with all large bundles and find how many need to be replaced with small bundles to reach the total.
        # total_deep_arrowhead_worth = 2696
        # small_ah_bundle_worth = 25
        # large_ah_bundle_worth = 100
        # # Each time a large bundle is replaced with a small bundle, the total decreases by this much.
        # bundle_difference = large_ah_bundle_worth - small_ah_bundle_worth
        #
        # num_deep_arrowhead_locations = len(deep_arrowhead_locations)
        # excess_arrowheads = large_ah_bundle_worth * num_deep_arrowhead_locations - total_deep_arrowhead_worth
        #
        # # Truncating any remainder using integer division means that when there is not a whole number, the total
        # # worth of arrowheads from added bundles will be slightly more than `total_deep_arrowhead_worth`.
        # small_count = excess_arrowheads // bundle_difference
        # large_count = num_deep_arrowhead_locations - small_count

        # Adjust how many of each item to add to the item pool.
        item_counts[ItemName.AHSmall] += small_count
        item_counts[ItemName.AHLarge] += large_count

    @staticmethod
    def _add_mental_cobweb_shuffle_items(item_counts: Dict[str, int]):
        # A single Mental Cobweb can normally be turned into a PSI Card at the loom in Ford's Sanctuary, so add as many
        # PSI Cards to the pool as Mental Cobweb Locations.
        item_counts[ItemName.PsiCard] += len(mental_cobweb_locations)

    def create_items(self):
        """
        Fills ItemPool 
        """
        num_locations_to_fill = len(self.multiworld.get_unfilled_locations(self.player))

        adjusted_item_counts = item_counts.copy()

        # Pre-collect starting minds and remove them from the item pool.
        num_starting_minds = self.options.RandomStartingMinds.value
        if num_starting_minds > 0:
            mind_unlocks = list(MindUnlocks_Table)
            for _ in range(num_starting_minds):
                # Pop a random mind from the list.
                item = mind_unlocks.pop(self.random.randrange(len(mind_unlocks)))
                # Reduce the number to add to the pool.
                adjusted_item_counts[item] -= 1
                self.multiworld.push_precollected(self.create_item(item))

        # Add items for DeepArrowheadShuffle
        if self.options.DeepArrowheadShuffle:
            self._add_deep_arrowhead_shuffle_items(adjusted_item_counts)

        # Add items for MentalCobwebShuffle
        if self.options.MentalCobwebShuffle:
            self._add_mental_cobweb_shuffle_items(adjusted_item_counts)

        # Create the initial item pool.
        item_pool = list(map(self.create_item, repeated_item_names_gen(item_dictionary_table, adjusted_item_counts)))

        assert len(item_pool) <= num_locations_to_fill, ("The initial item pool cannot be larger than the number of"
                                                         " unfilled locations.")
        num_locations_to_fill -= len(item_pool)

        # Add filler/junk items to fill out the remaining locations.
        # If there are more locations remaining than the desired maximum number of filler items to add, also add the
        # Feather and Watering Can junk items to the pool.
        desired_max_filler = 107  # This is arbitrary based on the max number of Psi Cards placeable in the game world.
        excess = num_locations_to_fill - desired_max_filler
        if excess >= 1:
            item_pool.append(self.create_item(ItemName.Feather))
            num_locations_to_fill -= 1
            if excess >= 2:
                item_pool.append(self.create_item(ItemName.PropWaterCan))
                num_locations_to_fill -= 1

        # Create filler for the remaining locations.
        item_pool.extend(self.create_filler() for _ in range(num_locations_to_fill))

        self.multiworld.itempool += item_pool

    def create_regions(self):
        """
        Creates the Regions and Connects them.
        """
        
        Regions.create_psyregions(self.multiworld, self.player)
        Regions.connect_regions(self.multiworld, self.player)
        Regions.place_events(self)

        if self.options.DeepArrowheadShuffle:
            Regions.create_deep_arrowhead_locations(self.multiworld, self.player)
        if self.options.MentalCobwebShuffle:
            Regions.create_mental_cobweb_locations(self.multiworld, self.player)

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
