import typing
from dataclasses import dataclass
from Options import Choice, Range, Toggle, ItemDict, PerGameCommonOptions

class StartingLevitation(Toggle):
    """Start with Levitation Level 1"""
    display_name = "Start with Levitation"
    default = False

class StartingMentalMagnet(Toggle):
    """Start with Mental Magnet, pulling health, ammo, and arrowhead drops towards you."""
    display_name = "Start with Mental Magnet"
    default = True

class RandomStartingMinds(Range):
    """Start with a random number of mind unlocking items."""
    display_name = "Random Starting Minds"
    range_start = 0
    range_end = 9
    default = 0

class InstantDeathMode(Toggle):
    """Take damage, die instantly"""
    display_name = "Instant Death Mode"
    default = False

class EasyMillaRace(Toggle):
    """Make the race in Milla's Mind easier by removing Bobby from the race, and increasing player speed to 1.5x"""
    display_name = "Easy Milla Race"
    default = False

class EasyFlightMode(Toggle):
    """Replicate the Levitation Flight Glitch by simply holding down float in the air. No more button mashing.
    WARNING: Makes getting locations out of logic VERY easy."""
    display_name = "Easy Flight Mode"
    default = False

class RequireMeatCircus(Toggle):
    """Require finishing Meat Circus Final Bosses in addition to your goal"""
    display_name = "Require Meat Circus"
    default = True

class BrainsRequired(Range):
    """Number of Brains required to collect to Win, or open final door to Meat Circus Final Bosses.

    If Goal is not Brain Hunt, or Asylum Brain Tank and Brain Hunt, this does nothing."""
    display_name = "Brains Required"
    range_start = 1
    range_end = 19
    default = 10

class Goal(Choice):
    """Win Condition
    Asylum Brain Tank: Climb the Asylum and defeat the Coach Oleander Brain Tank.

    Brain Hunt: Find the required amount of Camper Brains and re-brain them in Ford's Sanctuary.

    Asylum Brain Tank and Brain Hunt: Find the required amount of Camper Brains, and defeat the Coach Oleander Brain Tank."""
    display_name = "Goal"
    option_braintank = 0
    option_brainhunt = 1
    option_braintank_and_brainhunt = 2
    default = 0

@dataclass
class PsychonautsOptions(PerGameCommonOptions):
    StartingLevitation: StartingLevitation
    StartingMentalMagnet: StartingMentalMagnet
    RandomStartingMinds: RandomStartingMinds
    InstantDeathMode: InstantDeathMode
    EasyMillaRace: EasyMillaRace
    EasyFlightMode: EasyFlightMode
    Goal: Goal
    BrainsRequired: BrainsRequired
    RequireMeatCircus: RequireMeatCircus