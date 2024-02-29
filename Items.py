import typing

from BaseClasses import Item
from .Names import ItemName
    
RequiredProps_Table = {
    ItemName.LungfishCall: 1,
    ItemName.GloriasTrophy: 2,
    ItemName.StraightJacket: 3,
    ItemName.LobotoPainting: 4,
    ItemName.Cake: 5,
    ItemName.Button: 362, # game rando id 365
    ItemName.CobwebDuster: 364, # game rando id 367
}

MMProps_Table = {
    ItemName.PropSign: 7,
    ItemName.PropFlowers: 8,
    ItemName.PropPlunger: 9,
    ItemName.PropHedgeTrimmers: 10,
    ItemName.PropRollingPin: 11,
    ItemName.PropWaterCan: 12,
}

THProps_Table = {
    ItemName.Candle1: 13,
    ItemName.Candle2: 14,
    ItemName.Megaphone: 15,
}    

WWProps_Table = {
    ItemName.FredsLetter: 16,
    ItemName.PricelessCoin: 17,
    ItemName.Musket: 18,
}
    
PsiPowers_Table = {
    ItemName.Marksmanship1: 19,
    ItemName.Marksmanship2: 20,
    ItemName.Marksmanship3: 21,
    ItemName.Pyrokinesis1: 22,
    ItemName.Pyrokinesis2: 23,
    ItemName.Confusion1: 24,
    ItemName.Confusion2: 25,
    ItemName.Levitation1: 26,
    ItemName.Levitation2: 27,
    ItemName.Levitation3: 28,
    ItemName.Telekinesis1: 29,
    ItemName.Telekinesis2: 30,
    ItemName.Invisibility1: 31,
    ItemName.Invisibility2: 32,
    ItemName.Clairvoyance1: 33,
    ItemName.Clairvoyance2: 34,
    ItemName.Shield1: 35,
    ItemName.Shield2: 36,
    ItemName.Shield3: 37,       
}

MaxAmmo_Table = {
    ItemName.AmmoUp1: 38,       
    ItemName.AmmoUp2: 39,       
    ItemName.AmmoUp3: 40,       
    ItemName.AmmoUp4: 41,       
    ItemName.AmmoUp5: 42,       
    ItemName.AmmoUp6: 43,       
}

MaxLives_Table = {
    ItemName.MaxLivesUp1: 44,
    ItemName.MaxLivesUp2: 45,       
    ItemName.MaxLivesUp3: 46,       
    ItemName.MaxLivesUp4: 47,       
    ItemName.MaxLivesUp5: 48,       
    ItemName.MaxLivesUp6: 49,       
}

ConfusionAmmo_Table = {
    ItemName.ConfusionUp1: 50,       
    ItemName.ConfusionUp2: 51,       
    ItemName.ConfusionUp3: 52,       
    ItemName.ConfusionUp4: 53,       
}

ChallengeMarker_Table = {
    ItemName.ChallengeMarker1: 54,
    ItemName.ChallengeMarker2: 55,
    ItemName.ChallengeMarker3: 56,
    ItemName.ChallengeMarker4: 57,
    ItemName.ChallengeMarker5: 58,
    ItemName.ChallengeMarker6: 59,
    ItemName.ChallengeMarker7: 60,
    ItemName.ChallengeMarker8: 61,
    ItemName.ChallengeMarker9: 62,
    ItemName.ChallengeMarker10: 63, 
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
    ItemName.SuitcaseTag1: 99, 
    ItemName.SuitcaseTag2: 100, 
    ItemName.SuitcaseTag3: 101, 
    ItemName.SuitcaseTag4: 102, 
    ItemName.SuitcaseTag5: 103, 
    ItemName.SuitcaseTag6: 104, 
    ItemName.SuitcaseTag7: 105, 
    ItemName.SuitcaseTag8: 106, 
    ItemName.SuitcaseTag9: 107, 
    ItemName.SuitcaseTag10: 108,  
}

PurseTags_Table = {
    ItemName.PurseTag1: 109, 
    ItemName.PurseTag2: 110, 
    ItemName.PurseTag3: 111, 
    ItemName.PurseTag4: 112, 
    ItemName.PurseTag5: 113, 
    ItemName.PurseTag6: 114, 
    ItemName.PurseTag7: 115, 
    ItemName.PurseTag8: 116, 
    ItemName.PurseTag9: 117, 
    ItemName.PurseTag10: 118, 
}

HatboxTags_Table = {
    ItemName.HatboxTag1: 119, 
    ItemName.HatboxTag2: 120, 
    ItemName.HatboxTag3: 121, 
    ItemName.HatboxTag4: 122, 
    ItemName.HatboxTag5: 123, 
    ItemName.HatboxTag6: 124, 
    ItemName.HatboxTag7: 125, 
    ItemName.HatboxTag8: 126, 
    ItemName.HatboxTag9: 127, 
    ItemName.HatboxTag10: 128, 
}

SteamerTags_Table = {
    ItemName.SteamerTag1: 129, 
    ItemName.SteamerTag2: 130, 
    ItemName.SteamerTag3: 131, 
    ItemName.SteamerTag4: 132, 
    ItemName.SteamerTag5: 133, 
    ItemName.SteamerTag6: 134, 
    ItemName.SteamerTag7: 135, 
    ItemName.SteamerTag8: 136, 
    ItemName.SteamerTag9: 137, 
    ItemName.SteamerTag10: 138,     
}

DuffleTags_Table = {
    ItemName.DuffleTag1: 139, 
    ItemName.DuffleTag2: 140, 
    ItemName.DuffleTag3: 141, 
    ItemName.DuffleTag4: 142, 
    ItemName.DuffleTag5: 143, 
    ItemName.DuffleTag6: 144, 
    ItemName.DuffleTag7: 145, 
    ItemName.DuffleTag8: 146, 
    ItemName.DuffleTag9: 147, 
    ItemName.DuffleTag10: 148,    
}

Suitcase_Table = {
    ItemName.Suitcase1: 149, 
    ItemName.Suitcase2: 150, 
    ItemName.Suitcase3: 151, 
    ItemName.Suitcase4: 152, 
    ItemName.Suitcase5: 153, 
    ItemName.Suitcase6: 154, 
    ItemName.Suitcase7: 155, 
    ItemName.Suitcase8: 156, 
    ItemName.Suitcase9: 157, 
    ItemName.Suitcase10: 158,  
}

Purse_Table = {
    ItemName.Purse1: 159, 
    ItemName.Purse2: 160, 
    ItemName.Purse3: 161, 
    ItemName.Purse4: 162, 
    ItemName.Purse5: 163, 
    ItemName.Purse6: 164, 
    ItemName.Purse7: 165, 
    ItemName.Purse8: 166, 
    ItemName.Purse9: 167, 
    ItemName.Purse10: 168,  
}

Hatbox_Table = {
    ItemName.Hatbox1: 169, 
    ItemName.Hatbox2: 170, 
    ItemName.Hatbox3: 171, 
    ItemName.Hatbox4: 172, 
    ItemName.Hatbox5: 173, 
    ItemName.Hatbox6: 174, 
    ItemName.Hatbox7: 175, 
    ItemName.Hatbox8: 176, 
    ItemName.Hatbox9: 177, 
    ItemName.Hatbox10: 178,     
}

Steamertrunk_Table = {
    ItemName.Steamertrunk1: 179, 
    ItemName.Steamertrunk2: 180, 
    ItemName.Steamertrunk3: 181, 
    ItemName.Steamertrunk4: 182, 
    ItemName.Steamertrunk5: 183, 
    ItemName.Steamertrunk6: 184, 
    ItemName.Steamertrunk7: 185, 
    ItemName.Steamertrunk8: 186, 
    ItemName.Steamertrunk9: 187, 
    ItemName.Steamertrunk10: 188, 
}

Dufflebag_Table = {
    ItemName.Dufflebag1: 189, 
    ItemName.Dufflebag2: 190, 
    ItemName.Dufflebag3: 191, 
    ItemName.Dufflebag4: 192, 
    ItemName.Dufflebag5: 193, 
    ItemName.Dufflebag6: 194, 
    ItemName.Dufflebag7: 195, 
    ItemName.Dufflebag8: 196, 
    ItemName.Dufflebag9: 197, 
    ItemName.Dufflebag10: 198, 
}

Vault_Table = {
    ItemName.Vault1: 199, 
    ItemName.Vault2: 200, 
    ItemName.Vault3: 201, 
    ItemName.Vault4: 202, 
    ItemName.Vault5: 203, 
    ItemName.Vault6: 204, 
    ItemName.Vault7: 205, 
    ItemName.Vault8: 206, 
    ItemName.Vault9: 207, 
    ItemName.Vault10: 208, 
    ItemName.Vault11: 209, 
    ItemName.Vault12: 210, 
    ItemName.Vault13: 211, 
    ItemName.Vault14: 212, 
    ItemName.Vault15: 213, 
    ItemName.Vault16: 214, 
    ItemName.Vault17: 215, 
    ItemName.Vault18: 216, 
    ItemName.Vault19: 217,   
}

AHSmall_Table = {
    ItemName.AHSmall1: 218, 
    ItemName.AHSmall2: 219, 
    ItemName.AHSmall3: 220, 
    ItemName.AHSmall4: 221, 
    ItemName.AHSmall5: 222, 
    ItemName.AHSmall6: 223, 
    ItemName.AHSmall7: 224, 
    ItemName.AHSmall8: 225, 
    ItemName.AHSmall9: 226, 
    ItemName.AHSmall10: 227, 
    ItemName.AHSmall11: 228, 
    ItemName.AHSmall12: 229, 
    ItemName.AHSmall13: 230, 
    ItemName.AHSmall14: 231, 
    ItemName.AHSmall15: 232, 
    ItemName.AHSmall16: 233, 
    ItemName.AHSmall17: 234, 
    ItemName.AHSmall18: 235, 
    ItemName.AHSmall19: 236, 
    ItemName.AHSmall20: 237, 
    ItemName.AHSmall21: 238, 
    ItemName.AHSmall22: 239, 
    ItemName.AHSmall23: 240, 
    ItemName.AHSmall24: 241, 
    ItemName.AHSmall25: 242, 
    ItemName.AHSmall26: 243, 
    ItemName.AHSmall27: 244, 
    ItemName.AHSmall28: 245, 
    ItemName.AHSmall29: 246, 
    ItemName.AHSmall30: 247,     
}

AHLarge_Table = {
    ItemName.AHLarge1: 248, 
    ItemName.AHLarge2: 249, 
    ItemName.AHLarge3: 250, 
    ItemName.AHLarge4: 251, 
    ItemName.AHLarge5: 252, 
}

PsiCards_Table = {
    ItemName.PsiCard1: 253,
    ItemName.PsiCard2: 254,
    ItemName.PsiCard3: 255,
    ItemName.PsiCard4: 256,
    ItemName.PsiCard5: 257,
    ItemName.PsiCard6: 258,
    ItemName.PsiCard7: 259,
    ItemName.PsiCard8: 260,
    ItemName.PsiCard9: 261,
    ItemName.PsiCard10: 262,
    ItemName.PsiCard11: 263,
    ItemName.PsiCard12: 264,
    ItemName.PsiCard13: 265,
    ItemName.PsiCard14: 266,
    ItemName.PsiCard15: 267,
    ItemName.PsiCard16: 268,
    ItemName.PsiCard17: 269,
    ItemName.PsiCard18: 270,
    ItemName.PsiCard19: 271,
    ItemName.PsiCard20: 272,
    ItemName.PsiCard21: 273,
    ItemName.PsiCard22: 274,
    ItemName.PsiCard23: 275,
    ItemName.PsiCard24: 276,
    ItemName.PsiCard25: 277,
    ItemName.PsiCard26: 278,
    ItemName.PsiCard27: 279,
    ItemName.PsiCard28: 280,
    ItemName.PsiCard29: 281,
    ItemName.PsiCard30: 282,
    ItemName.PsiCard31: 283,
    ItemName.PsiCard32: 284,
    ItemName.PsiCard33: 285,
    ItemName.PsiCard34: 286,
    ItemName.PsiCard35: 287,
    ItemName.PsiCard36: 288,
    ItemName.PsiCard37: 289,
    ItemName.PsiCard38: 290,
    ItemName.PsiCard39: 291,
    ItemName.PsiCard40: 292,
    ItemName.PsiCard41: 293,
    ItemName.PsiCard42: 294,
    ItemName.PsiCard43: 295,
    ItemName.PsiCard44: 296,
    ItemName.PsiCard45: 297,
    ItemName.PsiCard46: 298,
    ItemName.PsiCard47: 299,
    ItemName.PsiCard48: 300,
    ItemName.PsiCard49: 301,
    ItemName.PsiCard50: 302,
    ItemName.PsiCard51: 303,
    ItemName.PsiCard52: 304,
    ItemName.PsiCard53: 305,
    ItemName.PsiCard54: 306,
    ItemName.PsiCard55: 307,
    ItemName.PsiCard56: 308,
    ItemName.PsiCard57: 309,
    ItemName.PsiCard58: 310,
    ItemName.PsiCard59: 311,
    ItemName.PsiCard60: 312,
    ItemName.PsiCard61: 313,
    ItemName.PsiCard62: 314,
    ItemName.PsiCard63: 315,
    ItemName.PsiCard64: 316,
    ItemName.PsiCard65: 317,
    ItemName.PsiCard66: 318,
    ItemName.PsiCard67: 319,
    ItemName.PsiCard68: 320,
    ItemName.PsiCard69: 321,
    ItemName.PsiCard70: 322,
    ItemName.PsiCard71: 323,
    ItemName.PsiCard72: 324,
    ItemName.PsiCard73: 325,
    ItemName.PsiCard74: 326,
    ItemName.PsiCard75: 327,
    ItemName.PsiCard76: 328,
    ItemName.PsiCard77: 329,
    ItemName.PsiCard78: 330,
    ItemName.PsiCard79: 331,
    ItemName.PsiCard80: 332,
    ItemName.PsiCard81: 333,
    ItemName.PsiCard82: 334,
    ItemName.PsiCard83: 335,
    ItemName.PsiCard84: 336,
    ItemName.PsiCard85: 337,
    ItemName.PsiCard86: 338,
    ItemName.PsiCard87: 339,
    ItemName.PsiCard88: 340,
    ItemName.PsiCard89: 341,
    ItemName.PsiCard90: 342,
    ItemName.PsiCard91: 343,
    ItemName.PsiCard92: 344,
    ItemName.PsiCard93: 345,
    ItemName.PsiCard94: 346,
    ItemName.PsiCard95: 347,
    ItemName.PsiCard96: 348,
    ItemName.PsiCard97: 349,
    ItemName.PsiCard98: 350,
    ItemName.PsiCard99: 351,
    ItemName.PsiCard100: 352,
    ItemName.PsiCard101: 353,
    ItemName.PsiCard102: 354,
    ItemName.PsiCard103: 355,
    ItemName.PsiCard104: 356,
    ItemName.PsiCard105: 357,
    ItemName.PsiCard106: 358,
    ItemName.PsiCard107: 359,
    ItemName.PsiCard108: 360,
    # Used to fill Dummy Locations in base randomizer
    # ItemName.PsiCard109: 361, # game rando id 361
    # ItemName.PsiCard110: 362,
    # ItemName.PsiCard111: 363,    
}

OtherItems_Table = {
    ItemName.OarsmansBadge: 361, # game rando id 364   
    ItemName.Feather: 363, # game rando id 366   
    ItemName.LilisBracelet: 6,
    
}

item_dictionary_table = {
    **RequiredProps_Table,
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

progression_set = {
    **RequiredProps_Table,
    **MMProps_Table,
    **THProps_Table,
    **WWProps_Table,
    **PsiPowers_Table,
    # **Events_Table,
    
}

useful_set = {
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
        


