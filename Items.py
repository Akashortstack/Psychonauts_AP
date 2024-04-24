from typing import Dict, List, Union

from .Names import ItemName
    
RequiredProps_Table = {
    ItemName.LungfishCall: 1,
    ItemName.GloriasTrophy: 2,
    ItemName.StraightJacket: 3,
    ItemName.LobotoPainting: 4,
    ItemName.Cake: 5,
    ItemName.LilisBracelet: 6,
    ItemName.OarsmansBadge: 253,
    ItemName.SashaButton: 254,
    ItemName.CobwebDuster: 256,
    ItemName.SquirrelDinner: 257,
}

MindUnlocks_Table = {
    ItemName.CoachMind: 258,
    ItemName.SashaMind: 259,
    ItemName.MillaMind: 260,
    ItemName.LindaMind: 261,
    ItemName.BoydMind: 262,
    ItemName.GloriaMind: 263,
    ItemName.FredMind: 264,
    ItemName.EdgarMind: 265,
    ItemName.OlyMind: 266,
}

MMProps_Table = {
    ItemName.PropSign: 7,
    ItemName.PropFlowers: 8,
    ItemName.PropPlunger: 9,
    ItemName.PropHedgeTrimmers: 10,
    ItemName.PropRollingPin: 11,
}

THProps_Table = {
    ItemName.Candle: 13,
    ItemName.Megaphone: 15,
}    

WWProps_Table = {
    ItemName.FredsLetter: 16,
    ItemName.PricelessCoin: 17,
    ItemName.Musket: 18,
}
    
PsiPowers_Table = {
    ItemName.Marksmanship: 19,
    ItemName.Pyrokinesis: 22,
    ItemName.Confusion: 24,
    ItemName.Levitation: 26,
    ItemName.Telekinesis: 29,
    ItemName.Invisibility: 31,
    ItemName.Clairvoyance: 33,
    ItemName.Shield: 35,
}

MaxAmmo_Table = {
    ItemName.AmmoUp: 38,
}

MaxLives_Table = {
    ItemName.MaxLivesUp: 44,
}

ConfusionAmmo_Table = {
    ItemName.ConfusionUp: 50,
}

ChallengeMarker_Table = {
    ItemName.ChallengeMarker: 54,
}

BrainJar_Table = {
    ItemName.BrainJarElton: 64, 
    ItemName.BrainJarBobby: 65, 
    ItemName.BrainJarDogen: 66, 
    ItemName.BrainJarBenny: 67, 
    ItemName.BrainJarElka: 68, 
    ItemName.BrainJarKitty: 69, 
    ItemName.BrainJarChloe: 70, 
    ItemName.BrainJarFranke: 71, 
    ItemName.BrainJarJT: 72, 
    ItemName.BrainJarQuentin: 73, 
    ItemName.BrainJarVernon: 74, 
    ItemName.BrainJarMilka: 75, 
    ItemName.BrainJarCrystal: 76, 
    ItemName.BrainJarClem: 77, 
    ItemName.BrainJarNils: 78, 
    ItemName.BrainJarMaloof: 79, 
    ItemName.BrainJarMikhail: 80, 
    ItemName.BrainJarPhoebe: 81, 
    ItemName.BrainJarChops: 82, 
}

ScavHunt_Table = {
    ItemName.GoldDoubloon: 83, 
    ItemName.EagleClaw: 84, 
    ItemName.DiversHelmet: 85, 
    ItemName.PsyComic: 86, 
    ItemName.WoodPipe: 87, 
    ItemName.TurkeySandwich: 88, 
    ItemName.VoodooDoll: 89, 
    ItemName.MinerSkull: 90, 
    ItemName.PirateScope: 91, 
    ItemName.GoldenAcorn: 92, 
    ItemName.GlassEye: 93, 
    ItemName.Egg: 94, 
    ItemName.FertilityIdol: 95, 
    ItemName.DinosaurBone: 96, 
    ItemName.Fossil: 97, 
    ItemName.GoldWatch: 98, 
}

SuitcaseTags_Table = {
    ItemName.SuitcaseTag: 99,
}

PurseTags_Table = {
    ItemName.PurseTag: 109,
}

HatboxTags_Table = {
    ItemName.HatboxTag: 119,
}

SteamerTags_Table = {
    ItemName.SteamerTag: 129, 
}

DuffleTags_Table = {
    ItemName.DuffleTag: 139,
}

Suitcase_Table = {
    ItemName.Suitcase: 149,
}

Purse_Table = {
    ItemName.Purse: 159,
}

Hatbox_Table = {
    ItemName.Hatbox: 169, 
}

Steamertrunk_Table = {
    ItemName.Steamertrunk: 179,
}

Dufflebag_Table = {
    ItemName.Dufflebag: 189,
}

Vault_Table = {
    ItemName.Vault: 199, 
}

AHSmall_Table = {
    ItemName.AHSmall: 218,
}

AHLarge_Table = {
    ItemName.AHLarge: 248,
}

PsiCards_Table = {
    ItemName.PsiCard: 267
}

OtherItems_Table = {
    ItemName.Feather: 255,
    ItemName.PropWaterCan: 12,    
}

item_dictionary_table = {
    **RequiredProps_Table,
    **MindUnlocks_Table,
    **MMProps_Table,
    **THProps_Table,
    **WWProps_Table,
    **PsiPowers_Table,
    **MaxAmmo_Table,
    **MaxLives_Table,
    **ConfusionAmmo_Table,
    **ChallengeMarker_Table,
    **BrainJar_Table,
    **ScavHunt_Table,
    **SuitcaseTags_Table,
    **PurseTags_Table,
    **HatboxTags_Table,
    **SteamerTags_Table,
    **DuffleTags_Table,
    **Suitcase_Table,
    **Purse_Table,
    **Hatbox_Table,
    **Steamertrunk_Table,
    **Dufflebag_Table,
    **Vault_Table,
    **AHSmall_Table,
    **AHLarge_Table,
    **PsiCards_Table,
    **OtherItems_Table,
}

# Reverse mapping of all items, from item ID to item name.
reverse_item_dictionary_table = {v: k for k, v in item_dictionary_table.items()}

progression_set = {
    **RequiredProps_Table,
    **MindUnlocks_Table,
    **MMProps_Table,
    **THProps_Table,
    **WWProps_Table,
    **PsiPowers_Table,
}

useful_set = {
    **Vault_Table,
    **ChallengeMarker_Table,
    **MaxLives_Table,
    **ScavHunt_Table,
    **SuitcaseTags_Table,
    **PurseTags_Table,
    **HatboxTags_Table,
    **SteamerTags_Table,
    **DuffleTags_Table,
    **Suitcase_Table,
    **Purse_Table,
    **Hatbox_Table,
    **Steamertrunk_Table,
    **Dufflebag_Table,
    **AHLarge_Table,    
}

local_set = {
    # Baggage must be local only
    **Suitcase_Table,
    **Purse_Table,
    **Hatbox_Table,
    **Steamertrunk_Table,
    **Dufflebag_Table,
}

item_groups: Dict[str, List[str]] = {
    "Mind": list(MindUnlocks_Table.keys()),
    "Brain": list(BrainJar_Table.keys()),
    "Scavenger Hunt": list(ScavHunt_Table.keys()),
}

# Start with a dict with a count of 1 for each item and then merge in a dict with the items of which there are multiple.
# Can't use the union operator, `dict1 | dict2`, until Archipelago requires Python 3.9 or newer, so using
# `{**dict1, **dict2}`.
item_counts: Dict[str, int] = {**{k: 1 for k in item_dictionary_table}, **{
    ItemName.Candle: 2,
    ItemName.Marksmanship: 3,
    ItemName.Pyrokinesis: 2,
    ItemName.Confusion: 2,
    ItemName.Levitation: 3,
    ItemName.Telekinesis: 2,
    ItemName.Invisibility: 2,
    ItemName.Clairvoyance: 2,
    ItemName.Shield: 3,
    ItemName.AmmoUp: 6,
    ItemName.MaxLivesUp: 6,
    ItemName.ConfusionUp: 4,
    ItemName.ChallengeMarker: 10,
    ItemName.SuitcaseTag: 10,
    ItemName.PurseTag: 10,
    ItemName.HatboxTag: 10,
    ItemName.SteamerTag: 10,
    ItemName.DuffleTag: 10,
    ItemName.Suitcase: 10,
    ItemName.Purse: 10,
    ItemName.Hatbox: 10,
    ItemName.Steamertrunk: 10,
    ItemName.Dufflebag: 10,
    ItemName.Vault: 19,
    ItemName.AHSmall: 30,
    ItemName.AHLarge: 5,
    ItemName.PsiCard: 107,
}}

# Offset added to Psychonauts IDs to produce AP IDs.
AP_ITEM_OFFSET = 42690000

_max_base_id = max(item_dictionary_table.values())
# The maximum Psychonauts item ID, taking into account that there are multiple of some items.
MAX_PSY_ITEM_ID = _max_base_id + item_counts[reverse_item_dictionary_table[_max_base_id]] - 1
del _max_base_id


def find_item_name_from_psy_id(psy_item_id: int) -> Union[str, None]:
    if 0 < psy_item_id <= MAX_PSY_ITEM_ID:
        # The Psychonauts item ID may have been incremented from its base ID to produce a unique ID, so iterate
        # backwards until the first matching item is found.
        for i in range(psy_item_id, 0, -1):
            if i in reverse_item_dictionary_table:
                return reverse_item_dictionary_table[i]
    # No item with the ID exists.
    return None
