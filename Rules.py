from typing import Dict, Callable, TYPE_CHECKING, Set

from BaseClasses import CollectionState, Item
from worlds.generic.Rules import add_item_rule, add_rule

from .Names import LocationName, ItemName, RegionName
from .Items import BrainJar_Table, local_set
from .Locations import deep_arrowhead_locations

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

            RegionName.ASCOInvis: self.has_invisibility,

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
        return state.has(ItemName.Candle, self.player)
    def has_bothcandles(self, state: CollectionState) -> bool:
        return state.has(ItemName.Candle, self.player, 2)
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
        if self.world.options.StartingLevitation == True:
            return True
        else:
            return state.has(ItemName.Levitation, self.player)

    def has_telekinesis(self, state: CollectionState) -> bool:
        return state.has(ItemName.Telekinesis, self.player)

    def has_pyrokinesis(self, state: CollectionState) -> bool:
        return state.has(ItemName.Pyrokinesis, self.player)

    def has_clairvoyance(self, state: CollectionState) -> bool:
        return state.has(ItemName.Clairvoyance, self.player)

    def has_marksmanship(self, state: CollectionState) -> bool:
        return state.has(ItemName.Marksmanship, self.player)

    def has_invisibility(self, state: CollectionState) -> bool:
        return state.has(ItemName.Invisibility, self.player)

    def has_shield(self, state: CollectionState) -> bool:
        return state.has(ItemName.Shield, self.player)

    def has_confusion(self, state: CollectionState) -> bool:
        return state.has(ItemName.Confusion, self.player)

    def has_upperasylumaccess(self, state: CollectionState) -> bool:
        return state.has_all([ItemName.LobotoPainting, ItemName.GloriasTrophy, ItemName.StraightJacket], self.player)

    def has_oleanderbossaccess(self, state: CollectionState) -> bool:
        return state.has_all([ItemName.SashaButton, ItemName.LobotoPainting, ItemName.GloriasTrophy, ItemName.StraightJacket, ItemName.LungfishCall, ItemName.Cake, ItemName.OarsmansBadge], self.player)
    
    def redeemed_brain_goal(self, state: CollectionState, amount) -> bool:
        return amount <= sum([state.count(item_name, self.player) for item_name in BrainJar_Table])
            
    def set_psy_rules(self) -> None:
        multiworld = self.world.multiworld
        player = self.player

        for region in multiworld.get_regions(player):
            if region.name in self.region_rules:
                for entrance in region.entrances:
                    entrance.access_rule = self.region_rules[region.name]

        self.set_psy_goal()

        # Locations which are not included in PsychoSeed generation do not place items into the Psychonauts game world,
        # instead relying on the Archipelago client to tell Psychonauts to spawn in the item as if it were receiving a
        # non-local item, so these locations cannot contain Psychonauts items that can only be placed locally.
        local_only_forbidden: Set[str] = set()

        if self.world.options.DeepArrowheadShuffle:
            # Deep Arrowhead Shuffle locations do not place items into the world.
            local_only_forbidden.update(deep_arrowhead_locations.keys())

            def has_dowsing_rod(state: CollectionState):
                return state.has(ItemName.DowsingRod, player)

            for deep_ah_location_name in deep_arrowhead_locations:
                location = multiworld.get_location(deep_ah_location_name, player)
                add_rule(location, has_dowsing_rod)

        if local_only_forbidden:
            def forbid_local_only(item: Item):
                return item.player != player or item.name not in local_set

            for location_name in local_only_forbidden:
                location = multiworld.get_location(location_name, player)
                add_item_rule(location, forbid_local_only)

    def set_psy_goal(self):
        final_boss_location = self.multiworld.get_location(LocationName.FinalBossEvent, self.player)
        oleander_boss_location = self.multiworld.get_location(LocationName.OleanderBossEvent, self.player)
        redeemed_required_brains = self.multiworld.get_location(LocationName.RedeemedBrainsEvent, self.player)
        # Brain Tank Boss
        if self.world.options.Goal == "braintank":    
            final_boss_location.access_rule = lambda state: self.has_oleanderbossaccess(state) and self.has_pyrokinesis(state)

        # Brain Hunt
        elif self.world.options.Goal == "brainhunt":
            final_boss_location.access_rule = lambda state: self.redeemed_brain_goal(state, self.world.options.BrainsRequired.value )
            redeemed_required_brains.access_rule = lambda state: self.redeemed_brain_goal(state, self.world.options.BrainsRequired.value )

        # Brain Tank Boss AND Brain Hunt
        else: 
            final_boss_location.access_rule = lambda state: self.has_oleanderbossaccess(state) and self.has_pyrokinesis(state) and self.redeemed_brain_goal(state, self.world.options.BrainsRequired.value )
            oleander_boss_location.access_rule = lambda state: self.redeemed_brain_goal(state, self.world.options.BrainsRequired.value )
            redeemed_required_brains.access_rule = lambda state: self.redeemed_brain_goal(state, self.world.options.BrainsRequired.value )

        self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemName.Victory, self.player)
            
