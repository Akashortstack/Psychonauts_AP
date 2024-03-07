from typing import Dict, Callable, TYPE_CHECKING

from BaseClasses import CollectionState
from .Names import LocationName, ItemName, RegionName
from worlds.generic.Rules import add_rule, forbid_items, add_item_rule

# I don't know what is going on here, but it works???
# Thanks Jared :)

if TYPE_CHECKING:
    from . import PSYWorld


class PsyRules:
    player: int
    world: "PSYWorld"
    
    region_rules: Dict[str, Callable[[CollectionState], bool]]

    def __init__(self, world: "PSYWorld") -> None:
        self.player = world.player
        self.world = world

        self.region_rules = {
            RegionName.CAGP: self.has_button,

            RegionName.RANK20to101: self.has_button,

            RegionName.CAGPSquirrel: self.has_invisibility,

            RegionName.CAGPGeyser: self.has_shield,

            RegionName.CAMALev: self.has_levitation,

            RegionName.CAKCLev: self.has_levitation,

            RegionName.CAKCPyro: self.has_pyrokinesis,

            RegionName.CARELev: self.has_levitation,

            RegionName.CAREMark: self.has_marksmanship,

            RegionName.CABHLev: self.has_levitation,

            RegionName.ASGR: self.has_lungfishcall,

            RegionName.ASGRLev: self.has_levitation,

            RegionName.ASCOLev: self.has_levitation,

            RegionName.ASUP: lambda state: self.has_upperasylumaccess(state),

            RegionName.ASUPLev: self.has_levitation,

            RegionName.ASUPTele: self.has_telekinesis,

            RegionName.BBA2Duster: self.has_cobwebduster,

            RegionName.SACU: self.has_marksmanship,

            RegionName.SACULev: self.has_levitation,

            RegionName.MIFL: self.has_levitation,

            RegionName.NIMPMark: self.has_marksmanship,

            RegionName.NIBA: self.has_levitation,

            RegionName.LOMAShield: self.has_shield,

            RegionName.MMI1BeforeSign: self.has_clairvoyance,

            RegionName.MMI1AfterSign: self.has_propsign,

            RegionName.MMI1Hedgetrimmers: self.has_prophedgetrimmers,

            RegionName.MMI1RollingPin: self.has_proprollingpin,

            RegionName.MMI1Duster: self.has_cobwebduster,

            RegionName.MMI2: lambda state: self.has_propflowers(state) and self.has_propplunger(state), 

            RegionName.MMI1Powerlines: self.has_cobwebduster,

            RegionName.MMDM: self.has_invisibility,

            RegionName.THMSLev: self.has_levitation,

            RegionName.THMSDuster: self.has_cobwebduster,

            RegionName.THMSStorage: self.has_invisibility,

            RegionName.THCW: lambda state: self.has_pyrokinesis(state) and self.has_candle(state) and self.has_levitation(state),

            RegionName.THFB: lambda state: self.has_bothcandles(state),

            RegionName.WWMALev: self.has_levitation,

            RegionName.WWMACarpRoof: lambda state: self.has_levitation(state) and self.has_invisibility(state),

            RegionName.WWMADuster: self.has_cobwebduster,

            RegionName.WWMADusterLev: self.has_levitation,

            RegionName.WWMADusterLevPyro: self.has_pyrokinesis,

            RegionName.WWMAV1: self.has_fredsletter,

            RegionName.WWMAKnight: self.has_telekinesis,

            RegionName.WWMAV2: lambda state: self.has_pricelesscoin(state) and self.has_telekinesis(state),

            RegionName.WWMAV3: self.has_musket,

            RegionName.BVRBLev: self.has_levitation,

            RegionName.BVRBTele: self.has_telekinesis,

            RegionName.BVRBDuster: self.has_cobwebduster,

            RegionName.BVRBGarden: self.has_telekinesis,

            RegionName.BVRBLogs: self.has_pyrokinesis,

            RegionName.BVESLev: self.has_levitation,

            RegionName.BVESEagle: self.has_cobwebduster,

            RegionName.BVESCobra: self.has_confusion,

            RegionName.BVESBoss: self.has_telekinesis,

            RegionName.MCTC: self.has_cobwebduster,

            RegionName.MCTCEscort: lambda state: self.has_telekinesis(state) and self.has_levitation(state),

            # Requirements to reach this may vary based on future settings, 
            # Completing this region = Victory
            RegionName.MCTCBoss: lambda state: self.has_pyrokinesis(state) and self.has_finalbossaccess(state),

        }

    def has_button(self, state: CollectionState) -> bool:
        return state.has(ItemName.SashaButton, self.player)

    def has_lungfishcall(self, state: CollectionState) -> bool:
        return state.has(ItemName.LungfishCall, self.player)
    
    def has_cake(self, state: CollectionState) -> bool:
        return state.has(ItemName.Cake, self.player)
    
    def has_propsign(self, state: CollectionState) -> bool:
        return state.has(ItemName.PropSign, self.player)
    
    def has_propflowers(self, state: CollectionState) -> bool:
        return state.has(ItemName.PropFlowers, self.player)
    
    def has_propplunger(self, state: CollectionState) -> bool:
        return state.has(ItemName.PropPlunger, self.player)
    
    def has_prophedgetrimmers(self, state: CollectionState) -> bool:
        return state.has(ItemName.PropHedgeTrimmers, self.player)
    
    def has_proprollingpin(self, state: CollectionState) -> bool:
        return state.has(ItemName.PropRollingPin, self.player)

    def has_candle(self, state: CollectionState) -> bool:
        return state.has_any([ItemName.Candle1, ItemName.Candle2], self.player)
    
    def has_bothcandles(self, state: CollectionState) -> bool:
        return state.has_all([ItemName.Candle1, ItemName.Candle2], self.player)
    
    def has_megaphone(self, state: CollectionState) -> bool:
        return state.has(ItemName.Megaphone, self.player)
    
    def has_fredsletter(self, state: CollectionState) -> bool:
        return state.has(ItemName.FredsLetter, self.player)
    
    def has_pricelesscoin(self, state: CollectionState) -> bool:
        return state.has(ItemName.PricelessCoin, self.player)
    
    def has_musket(self, state: CollectionState) -> bool:
        return state.has(ItemName.Musket, self.player)
    
    def has_cobwebduster(self, state: CollectionState) -> bool:
        return state.has(ItemName.CobwebDuster, self.player)  
    
    def has_levitation(self, state: CollectionState) -> bool:
        if self.world.multiworld.StartingLevitation[self.player] == True:
            return True
        else:
            return state.has_any([ItemName.Levitation1, ItemName.Levitation2, ItemName.Levitation3], self.player)

    def has_telekinesis(self, state: CollectionState) -> bool:
        return state.has_any([ItemName.Telekinesis1, ItemName.Telekinesis2], self.player)

    def has_pyrokinesis(self, state: CollectionState) -> bool:
        return state.has_any([ItemName.Pyrokinesis1, ItemName.Pyrokinesis2], self.player)

    def has_clairvoyance(self, state: CollectionState) -> bool:
        return state.has_any([ItemName.Clairvoyance1, ItemName.Clairvoyance2], self.player)

    def has_marksmanship(self, state: CollectionState) -> bool:
        return state.has_any([ItemName.Marksmanship1, ItemName.Marksmanship2, ItemName.Marksmanship3], self.player)

    def has_invisibility(self, state: CollectionState) -> bool:
        return state.has_any([ItemName.Invisibility1, ItemName.Invisibility2], self.player)

    def has_shield(self, state: CollectionState) -> bool:
        return state.has_any([ItemName.Shield1, ItemName.Shield2, ItemName.Shield3], self.player)

    def has_confusion(self, state: CollectionState) -> bool:
        return state.has_any([ItemName.Confusion1, ItemName.Confusion2], self.player)

    def has_upperasylumaccess(self, state: CollectionState) -> bool:
        return state.has_all([ItemName.LobotoPainting, ItemName.GloriasTrophy, ItemName.StraightJacket], self.player)

    def has_finalbossaccess(self, state: CollectionState) -> bool:
        return state.has_all([ItemName.SashaButton, ItemName.LobotoPainting, ItemName.GloriasTrophy, ItemName.StraightJacket, ItemName.LungfishCall, ItemName.Cake], self.player)
        
    def set_psy_rules(self) -> None:
        multiworld = self.world.multiworld

        for region in multiworld.get_regions(self.player):
            if region.name in self.region_rules:
                for entrance in region.entrances:
                    entrance.access_rule = self.region_rules[region.name]
            