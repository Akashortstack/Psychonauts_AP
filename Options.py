import typing
from dataclasses import dataclass
from Options import Choice, Range, Toggle, ItemDict, PerGameCommonOptions,

class StartingLevitation(Toggle):
    """Start with Levitation Level 1"""
    display_name = "Start with Levitation"
    default = False

class InstantDeathMode(Toggle):
    """Take damage, die instantly"""
    display_name = "Instant Death Mode"
    default = False

@dataclass
class PsychonautsOptions(PerGameCommonOptions):
    StartingLevitation: StartingLevitation
    InstantDeathMode: InstantDeathMode