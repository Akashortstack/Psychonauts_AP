import typing

from BaseClasses import Location, Item

class PSYLocation(Location):
    game: str = "Psychonauts"


class LocationData(typing.NamedTuple):
    locid: int


class PSYItem(Item):
    game: str = "Psychonauts"


class ItemData(typing.NamedTuple):
    quantity: int = 0
    # Matches item number from base randomizer
    psyid: int = 0
    
    