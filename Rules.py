from typing import Dict, Callable, TYPE_CHECKING

from BaseClasses import CollectionState
from .Names import LocationName, ItemName, RegionName
from .Items import *
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
        self.multiworld = world.multiworld

        self.region_rules = {
            RegionName.CAGP: self.has_button,

            RegionName.RANK5to20: lambda state: sum([
                self.has_button(state),
                self.has_coachmind(state),
                self.has_marksmanship(state) and self.has_sashamind(state),
                self.has_levitation(state) and self.has_millamind(state),
                self.has_lindamind(state),
                self.has_fredmind(state),
                self.has_edgarmind(state) and self.has_cobwebduster(state),
            ]) >=3,

            RegionName.RANK25to40: lambda state: sum([
                self.has_button(state),
                self.has_levitation(state) and self.has_millamind(state),
                self.has_shield(state) and self.has_lindamind(state),
                self.has_marksmanship(state) and self.has_sashamind(state),
                self.has_cobwebduster(state) and (self.has_edgarmind(state) or self.has_olymind(state)),
                self.has_clairvoyance(state) and self.has_propsign(state) and self.has_boydmind(state),
                self.has_telekinesis(state) and self.has_levitation(state) and self.has_oarsmansbadge(state) and self.has_lungfishcall(state) and self.has_upperasylumaccess(state),
                self.has_cobwebduster(state) and self.has_gloriamind(state) and self.has_candle(state) and self.has_pyrokinesis(state) and self.has_invisibility(state) and self.has_megaphone(state),
                self.has_cobwebduster(state) and self.has_fredmind(state) and self.has_pyrokinesis(state) and self.has_telekinesis(state) and self.has_fredsletter(state) and self.has_pricelesscoin(state) and self.has_musket(state),
            ]) >= 3, # Meeting four of these conditions adds ranks to logic

            RegionName.RANK45to60: lambda state: self.has_button(state) and sum([
                self.has_oarsmansbadge(state) and self.has_squirreldinner(state) and self.has_lilibracelet(state),
                self.has_levitation(state) and self.has_millamind(state),
                self.has_shield(state) and self.has_lindamind(state),
                self.has_marksmanship(state) and self.has_sashamind(state),
                self.has_cobwebduster(state) and (self.has_edgarmind(state) or self.has_olymind(state)),
                self.has_clairvoyance(state) and self.has_propsign(state) and self.has_boydmind(state),
                self.has_telekinesis(state) and self.has_levitation(state) and self.has_oarsmansbadge(state) and self.has_lungfishcall(state) and self.has_upperasylumaccess(state),
                self.has_cobwebduster(state) and self.has_gloriamind(state) and self.has_candle(state) and self.has_pyrokinesis(state) and self.has_invisibility(state) and self.has_megaphone(state),
                self.has_cobwebduster(state) and self.has_fredmind(state) and self.has_pyrokinesis(state) and self.has_telekinesis(state) and self.has_fredsletter(state) and self.has_pricelesscoin(state) and self.has_musket(state),
            ]) >= 4, # Having the Button AND Meeting five of these conditions adds ranks to logic

            RegionName.RANK65to80: lambda state: sum([
                self.has_oarsmansbadge(state) and self.has_squirreldinner(state) and self.has_lilibracelet(state),
                self.has_levitation(state) and self.has_millamind(state),
                self.has_shield(state) and self.has_lindamind(state),
                self.has_marksmanship(state) and self.has_sashamind(state),
                self.has_cobwebduster(state) and self.has_edgarmind(state) and self.has_olymind(state),
                self.has_clairvoyance(state) and self.has_propsign(state) and self.has_boydmind(state),
                self.has_telekinesis(state) and self.has_levitation(state) and self.has_oarsmansbadge(state) and self.has_lungfishcall(state) and self.has_upperasylumaccess(state),
                self.has_cobwebduster(state) and self.has_gloriamind(state) and self.has_candle(state) and self.has_pyrokinesis(state) and self.has_invisibility(state) and self.has_megaphone(state),
                self.has_cobwebduster(state) and self.has_fredmind(state) and self.has_pyrokinesis(state) and self.has_telekinesis(state) and self.has_fredsletter(state) and self.has_pricelesscoin(state) and self.has_musket(state),
            ]) >= 6, # Meeting six of these conditions adds ranks to logic

            RegionName.RANK85to101: lambda state: sum([
                self.has_oarsmansbadge(state) and self.has_squirreldinner(state) and self.has_lilibracelet(state),
                self.has_levitation(state) and self.has_millamind(state),
                self.has_shield(state) and self.has_lindamind(state),
                self.has_marksmanship(state) and self.has_sashamind(state),
                self.has_cobwebduster(state) and self.has_edgarmind(state) and self.has_olymind(state),
                self.has_clairvoyance(state) and self.has_propsign(state) and self.has_boydmind(state),
                self.has_telekinesis(state) and self.has_levitation(state) and self.has_oarsmansbadge(state) and self.has_lungfishcall(state) and self.has_upperasylumaccess(state),
                self.has_cobwebduster(state) and self.has_gloriamind(state) and self.has_candle(state) and self.has_pyrokinesis(state) and self.has_invisibility(state) and self.has_megaphone(state),
                self.has_cobwebduster(state) and self.has_fredmind(state) and self.has_pyrokinesis(state) and self.has_telekinesis(state) and self.has_fredsletter(state) and self.has_pricelesscoin(state) and self.has_musket(state),
            ]) >= 7, # Meeting seven of these conditions adds ranks to logic

            RegionName.CAGPSquirrel: self.has_invisibility,

            RegionName.CAGPGeyser: self.has_shield,

            RegionName.CAMALev: self.has_levitation,

            RegionName.CAKC: self.has_lilibracelet,

            RegionName.CAKCLev: self.has_levitation,

            RegionName.CAKCPyro: self.has_pyrokinesis,

            RegionName.CARE: self.has_squirreldinner,

            RegionName.CARELev: self.has_levitation,

            RegionName.CAREMark: self.has_marksmanship,

            RegionName.CABH: self.has_oarsmansbadge,

            RegionName.CABHLev: self.has_levitation,

            RegionName.ASGR: self.has_lungfishcall,

            RegionName.ASGRLev: self.has_levitation,

            RegionName.ASCOLev: self.has_levitation,

            RegionName.ASUP: lambda state: self.has_upperasylumaccess(state),

            RegionName.ASUPLev: self.has_levitation,

            RegionName.ASUPTele: self.has_telekinesis,

            RegionName.ASLBBoss: lambda state: self.has_cake(state) and self.has_pyrokinesis(state),

            RegionName.BBA1: self.has_coachmind,

            RegionName.BBA2Duster: self.has_cobwebduster,

            RegionName.SACU: lambda state: self.has_marksmanship(state) and self.has_sashamind(state),

            RegionName.SACULev: self.has_levitation,

            RegionName.MIFL: lambda state: self.has_levitation(state) and self.has_millamind(state),

            RegionName.NIMPMark: self.has_marksmanship,

            RegionName.NIBA: self.has_levitation,

            RegionName.LOMA: self.has_lindamind,

            RegionName.LOMAShield: self.has_shield,

            RegionName.MMI1Fridge: self.has_boydmind,

            RegionName.MMI1BeforeSign: self.has_clairvoyance,

            RegionName.MMI1AfterSign: self.has_propsign,

            RegionName.MMI1Hedgetrimmers: self.has_prophedgetrimmers,

            RegionName.MMI1RollingPin: self.has_proprollingpin,

            RegionName.MMI1Duster: self.has_cobwebduster,

            RegionName.MMI2: lambda state: self.has_propflowers(state) and self.has_propplunger(state) and self.has_pyrokinesis(state) and self.has_shield(state), 

            RegionName.MMI1Powerlines: self.has_cobwebduster,

            RegionName.MMDM: self.has_invisibility,

            RegionName.THMS: self.has_gloriamind,

            RegionName.THMSLev: self.has_levitation,

            RegionName.THMSDuster: self.has_cobwebduster,

            RegionName.THMSStorage: self.has_invisibility,

            RegionName.THCW: lambda state: self.has_pyrokinesis(state) and self.has_candle(state) and self.has_levitation(state) and self.has_megaphone(state),

            RegionName.THFB: lambda state: self.has_bothcandles(state),

            RegionName.WWMA: self.has_fredmind,

            RegionName.WWMALev: self.has_levitation,

            RegionName.WWMACarpRoof: lambda state: self.has_levitation(state) and self.has_invisibility(state),

            RegionName.WWMADuster: self.has_cobwebduster,

            RegionName.WWMADusterLev: self.has_levitation,

            RegionName.WWMADusterLevPyro: self.has_pyrokinesis,

            RegionName.WWMAV1: self.has_fredsletter,

            RegionName.WWMAKnight: self.has_telekinesis,

            RegionName.WWMAV2: lambda state: self.has_pricelesscoin(state) and self.has_telekinesis(state),

            RegionName.WWMAV3: self.has_musket,

            RegionName.WWMADone: self.has_levitation,

            RegionName.BVRB: self.has_edgarmind,

            RegionName.BVRBLev: self.has_levitation,

            RegionName.BVRBTele: self.has_telekinesis,

            RegionName.BVRBDuster: self.has_cobwebduster,

            RegionName.BVRBLogs: self.has_pyrokinesis,

            RegionName.BVESLev: self.has_levitation,

            RegionName.BVESCobra: self.has_confusion,

            RegionName.BVESBoss: self.has_telekinesis,

            RegionName.MCTC: lambda state: self.has_cobwebduster(state) and self.has_olymind(state),

            RegionName.MCTCLev: self.has_levitation,

            RegionName.MCTCEscort: self.has_telekinesis,

        }

    def has_button(self, state: CollectionState) -> bool:
        return state.has(ItemName.SashaButton, self.player)
    def has_lilibracelet(self, state: CollectionState) -> bool:
        return state.has(ItemName.LilisBracelet, self.player)
    def has_squirreldinner(self, state: CollectionState) -> bool:
        return state.has(ItemName.SquirrelDinner, self.player)
    def has_oarsmansbadge(self, state: CollectionState) -> bool:
        return state.has(ItemName.OarsmansBadge, self.player)
    def has_lungfishcall(self, state: CollectionState) -> bool:
        return state.has(ItemName.LungfishCall, self.player)
    def has_cake(self, state: CollectionState) -> bool:
        return state.has(ItemName.Cake, self.player)
    
    def has_coachmind(self, state: CollectionState) -> bool:
        return state.has(ItemName.CoachMind, self.player)
    def has_sashamind(self, state: CollectionState) -> bool:
        return state.has(ItemName.SashaMind, self.player)
    def has_millamind(self, state: CollectionState) -> bool:
        return state.has(ItemName.MillaMind, self.player)
    def has_lindamind(self, state: CollectionState) -> bool:
        return state.has(ItemName.LindaMind, self.player)
    def has_boydmind(self, state: CollectionState) -> bool:
        return state.has(ItemName.BoydMind, self.player)
    def has_gloriamind(self, state: CollectionState) -> bool:
        return state.has(ItemName.GloriaMind, self.player)
    def has_fredmind(self, state: CollectionState) -> bool:
        return state.has(ItemName.FredMind, self.player)
    def has_edgarmind(self, state: CollectionState) -> bool:
        return state.has(ItemName.EdgarMind, self.player)
    def has_olymind(self, state: CollectionState) -> bool:
        return state.has(ItemName.OlyMind, self.player)
    
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

    def has_oleanderbossaccess(self, state: CollectionState) -> bool:
        return state.has_all([ItemName.SashaButton, ItemName.LobotoPainting, ItemName.GloriasTrophy, ItemName.StraightJacket, ItemName.LungfishCall, ItemName.Cake, ItemName.OarsmansBadge], self.player)
    
    def redeemed_brain_goal(self, state: CollectionState, amount) -> bool:
        return amount <= sum([state.count(item_name, self.player) for item_name in BrainJar_Table])
            
    def set_psy_rules(self) -> None:
        multiworld = self.world.multiworld

        for region in multiworld.get_regions(self.player):
            if region.name in self.region_rules:
                for entrance in region.entrances:
                    entrance.access_rule = self.region_rules[region.name]

        self.set_psy_goal()

    def set_psy_goal(self):
        final_boss_location = self.multiworld.get_location(LocationName.FinalBossEvent, self.player)
        oleander_boss_location = self.multiworld.get_location(LocationName.OleanderBossEvent, self.player)
        redeemed_required_brains = self.multiworld.get_location(LocationName.RedeemedBrainsEvent, self.player)
        # Brain Tank Boss
        if self.multiworld.Goal[self.player] == "braintank":    
            final_boss_location.access_rule = lambda state: self.has_oleanderbossaccess(state) and self.has_pyrokinesis(state)
            if self.multiworld.RequireMeatCircus[self.player]:
                final_boss_location.place_locked_item(self.world.create_event_item("Victory"))
                oleander_boss_location.place_locked_item(self.world.create_event_item("Filler"))
                redeemed_required_brains.place_locked_item(self.world.create_event_item("Filler"))
            else:
                final_boss_location.place_locked_item(self.world.create_event_item("Filler"))
                oleander_boss_location.place_locked_item(self.world.create_event_item("Victory"))
                redeemed_required_brains.place_locked_item(self.world.create_event_item("Filler"))

        # Brain Hunt
        elif self.multiworld.Goal[self.player] == "brainhunt":
            final_boss_location.access_rule = lambda state: self.redeemed_brain_goal(state, self.multiworld.BrainsRequired[self.player].value )
            redeemed_required_brains.access_rule = lambda state: self.redeemed_brain_goal(state, self.multiworld.BrainsRequired[self.player].value )

            if self.multiworld.RequireMeatCircus[self.player]:
                final_boss_location.place_locked_item(self.world.create_event_item("Victory"))
                oleander_boss_location.place_locked_item(self.world.create_event_item("Filler"))
                redeemed_required_brains.place_locked_item(self.world.create_event_item("Filler"))
            else:
                final_boss_location.place_locked_item(self.world.create_event_item("Filler"))
                oleander_boss_location.place_locked_item(self.world.create_event_item("Filler"))
                redeemed_required_brains.place_locked_item(self.world.create_event_item("Victory"))

        # Brain Tank Boss AND Brain Hunt
        else: 
            final_boss_location.access_rule = lambda state: self.has_oleanderbossaccess(state) and self.has_pyrokinesis(state) and self.redeemed_brain_goal(state, self.multiworld.BrainsRequired[self.player].value )
            oleander_boss_location.access_rule = lambda state: self.redeemed_brain_goal(state, self.multiworld.BrainsRequired[self.player].value )
            redeemed_required_brains.access_rule = lambda state: self.redeemed_brain_goal(state, self.multiworld.BrainsRequired[self.player].value )

            if self.multiworld.RequireMeatCircus[self.player]:
                final_boss_location.place_locked_item(self.world.create_event_item("Victory"))
                oleander_boss_location.place_locked_item(self.world.create_event_item("Filler"))
                redeemed_required_brains.place_locked_item(self.world.create_event_item("Filler"))
            else:
                final_boss_location.place_locked_item(self.world.create_event_item("Filler"))
                oleander_boss_location.place_locked_item(self.world.create_event_item("Victory"))
                redeemed_required_brains.place_locked_item(self.world.create_event_item("Filler"))      

        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player) 
            
