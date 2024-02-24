from dataclasses import dataclass

from Options import Choice, Range, Toggle, ItemDict, PerGameCommonOptions, StartInventoryPool

from . import default_itempool_option


class StartingLevitation(Toggle):
    """Start with Levitation Level 1"""
    display_name = "Start with Levitation"
    default = False

class CobwebDusterPlacement(Choice):
    """Where Cobweb Duster gets placed"""
    display_name = "Cobweb Duster Placement"
    option_randomize_duster = 0
    option_start_duster = 1
    option_vanilla_duster = 2
    default = 0


class InstantDeathMode(Toggle):
    """Take damage, die instantly"""
    display_name = "Instant Death Mode"
    default = False

@dataclass
class PsychonautsOptions(PerGameCommonOptions):
    start_inventory: StartInventoryPool
    StartingLevitation: StartingLevitation
    CobwebDusterPlacement: CobwebDusterPlacement
    InstantDeathMode: InstantDeathMode