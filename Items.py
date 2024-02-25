import typing

from BaseClasses import Item
from .Names import ItemName
from .Subclasses import ItemData
    
RequiredProps_Table = {
    ItemName.LungfishCall: ItemData(1, 1),
    ItemName.GloriasTrophy: ItemData(1, 2),
    ItemName.StraightJacket: ItemData(1, 3),
    ItemName.LobatoPainting: ItemData(1, 4),
    ItemName.Cake: ItemData(1, 5),
    ItemName.Button: ItemData(1, 365),
    ItemName.CobwebDuster: ItemData(1, 367),
    
}

MMProps_Table = {
    ItemName.PropSign: ItemData(1, 7),
    ItemName.PropFlowers: ItemData(1, 8),
    ItemName.PropPlunger: ItemData(1, 9),
    ItemName.PropHedgeTrimmers: ItemData(1, 10),
    ItemName.PropRollingPin: ItemData(1, 11),
    ItemName.PropWaterCan: ItemData(1, 12),
}

THProps_Table = {
    ItemName.Candle1: ItemData(1, 13),
    ItemName.Candle2: ItemData(1, 14),
    ItemName.Megaphone: ItemData(1, 15),
}    

WWProps_Table = {
    ItemName.FredsLetter: ItemData(1, 16),
    ItemName.PricelessCoin: ItemData(1, 17),
    ItemName.Musket: ItemData(1, 18),
}
    
PsiPowers_Table = {
    ItemName.Marksmanship1: ItemData(1, 19),
    ItemName.Marksmanship2: ItemData(1, 20),
    ItemName.Marksmanship3: ItemData(1, 21),
    ItemName.Pyrokinesis1: ItemData(1, 22),
    ItemName.Pyrokinesis2: ItemData(1, 23),
    ItemName.Confusion1: ItemData(1, 24),
    ItemName.Confusion2: ItemData(1, 25),
    ItemName.Levitation1: ItemData(1, 26),
    ItemName.Levitation2: ItemData(1, 27),
    ItemName.Levitation3: ItemData(1, 28),
    ItemName.Telekinesis1: ItemData(1, 29),
    ItemName.Telekinesis2: ItemData(1, 30),
    ItemName.Invisibility1: ItemData(1, 31),
    ItemName.Invisibility2: ItemData(1, 32),
    ItemName.Clairvoyance1: ItemData(1, 33),
    ItemName.Clairvoyance2: ItemData(1, 34),
    ItemName.Shield1: ItemData(1, 35),
    ItemName.Shield2: ItemData(1, 36),
    ItemName.Shield3: ItemData(1, 37),       
}

MaxAmmo_Table = {
    ItemName.AmmoUp1: ItemData(1, 38),       
    ItemName.AmmoUp2: ItemData(1, 39),       
    ItemName.AmmoUp3: ItemData(1, 40),       
    ItemName.AmmoUp4: ItemData(1, 41),       
    ItemName.AmmoUp5: ItemData(1, 42),       
    ItemName.AmmoUp6: ItemData(1, 43),       
}

MaxLives_Table = {
    ItemName.MaxLivesUp1: ItemData(1, 44),
    ItemName.MaxLivesUp2: ItemData(1, 45),       
    ItemName.MaxLivesUp3: ItemData(1, 46),       
    ItemName.MaxLivesUp4: ItemData(1, 47),       
    ItemName.MaxLivesUp5: ItemData(1, 48),       
    ItemName.MaxLivesUp6: ItemData(1, 49),       
}

ConfusionAmmo_Table = {
    ItemName.ConfusionUp1: ItemData(1, 50),       
    ItemName.ConfusionUp2: ItemData(1, 51),       
    ItemName.ConfusionUp3: ItemData(1, 52),       
    ItemName.ConfusionUp4: ItemData(1, 53),       
}

ChallengeMarker_Table = {
    ItemName.ChallengeMarker1: ItemData(1, 54),
    ItemName.ChallengeMarker2: ItemData(1, 55),
    ItemName.ChallengeMarker3: ItemData(1, 56),
    ItemName.ChallengeMarker4: ItemData(1, 57),
    ItemName.ChallengeMarker5: ItemData(1, 58),
    ItemName.ChallengeMarker6: ItemData(1, 59),
    ItemName.ChallengeMarker7: ItemData(1, 60),
    ItemName.ChallengeMarker8: ItemData(1, 61),
    ItemName.ChallengeMarker9: ItemData(1, 62),
    ItemName.ChallengeMarker10: ItemData(1, 63), 
}

BrainJar_Table = {
    ItemName.BrainJarElton: ItemData(1, 64), 
    ItemName.BrainJarBobby: ItemData(1, 65), 
    ItemName.BrainJarDogen: ItemData(1, 66), 
    ItemName.BrainJarBenny: ItemData(1, 67), 
    ItemName.BrainJarElka: ItemData(1, 68), 
    ItemName.BrainJarKitty: ItemData(1, 69), 
    ItemName.BrainJarChloe: ItemData(1, 70), 
    ItemName.BrainJarFranke: ItemData(1, 71), 
    ItemName.BrainJarJT: ItemData(1, 72), 
    ItemName.BrainJarQuentin: ItemData(1, 73), 
    ItemName.BrainJarVernon: ItemData(1, 74), 
    ItemName.BrainJarMilka: ItemData(1, 75), 
    ItemName.BrainJarCrystal: ItemData(1, 76), 
    ItemName.BrainJarClem: ItemData(1, 77), 
    ItemName.BrainJarNils: ItemData(1, 78), 
    ItemName.BrainJarMaloof: ItemData(1, 79), 
    ItemName.BrainJarMikhail: ItemData(1, 80), 
    ItemName.BrainJarPhoebe: ItemData(1, 81), 
    ItemName.BrainJarChops: ItemData(1, 82), 
}

ScavHunt_Table = {
    ItemName.GoldDoubloon: ItemData(1, 83), 
    ItemName.EagleClaw: ItemData(1, 84), 
    ItemName.DiversHelmet: ItemData(1, 85), 
    ItemName.PsyComic: ItemData(1, 86), 
    ItemName.WoodPipe: ItemData(1, 87), 
    ItemName.TurkeySandwich: ItemData(1, 88), 
    ItemName.VoodooDoll: ItemData(1, 89), 
    ItemName.MinerSkull: ItemData(1, 90), 
    ItemName.PirateScope: ItemData(1, 91), 
    ItemName.GoldenAcorn: ItemData(1, 92), 
    ItemName.GlassEye: ItemData(1, 93), 
    ItemName.Egg: ItemData(1, 94), 
    ItemName.FertilityIdol: ItemData(1, 95), 
    ItemName.DinosaurBone: ItemData(1, 96), 
    ItemName.Fossil: ItemData(1, 97), 
    ItemName.GoldWatch: ItemData(1, 98), 
}

SuitcaseTags_Table = {
    ItemName.SuitcaseTag1: ItemData(1, 99), 
    ItemName.SuitcaseTag2: ItemData(1, 100), 
    ItemName.SuitcaseTag3: ItemData(1, 101), 
    ItemName.SuitcaseTag4: ItemData(1, 102), 
    ItemName.SuitcaseTag5: ItemData(1, 103), 
    ItemName.SuitcaseTag6: ItemData(1, 104), 
    ItemName.SuitcaseTag7: ItemData(1, 105), 
    ItemName.SuitcaseTag8: ItemData(1, 106), 
    ItemName.SuitcaseTag9: ItemData(1, 107), 
    ItemName.SuitcaseTag10: ItemData(1, 108),  
}

PurseTags_Table = {
    ItemName.PurseTag1: ItemData(1, 109), 
    ItemName.PurseTag2: ItemData(1, 110), 
    ItemName.PurseTag3: ItemData(1, 111), 
    ItemName.PurseTag4: ItemData(1, 112), 
    ItemName.PurseTag5: ItemData(1, 113), 
    ItemName.PurseTag6: ItemData(1, 114), 
    ItemName.PurseTag7: ItemData(1, 115), 
    ItemName.PurseTag8: ItemData(1, 116), 
    ItemName.PurseTag9: ItemData(1, 117), 
    ItemName.PurseTag10: ItemData(1, 118), 
}

HatboxTags_Table = {
    ItemName.HatboxTag1: ItemData(1, 119), 
    ItemName.HatboxTag2: ItemData(1, 120), 
    ItemName.HatboxTag3: ItemData(1, 121), 
    ItemName.HatboxTag4: ItemData(1, 122), 
    ItemName.HatboxTag5: ItemData(1, 123), 
    ItemName.HatboxTag6: ItemData(1, 124), 
    ItemName.HatboxTag7: ItemData(1, 125), 
    ItemName.HatboxTag8: ItemData(1, 126), 
    ItemName.HatboxTag9: ItemData(1, 127), 
    ItemName.HatboxTag10: ItemData(1, 128), 
}

SteamerTags_Table = {
    ItemName.SteamerTag1: ItemData(1, 129), 
    ItemName.SteamerTag2: ItemData(1, 130), 
    ItemName.SteamerTag3: ItemData(1, 131), 
    ItemName.SteamerTag4: ItemData(1, 132), 
    ItemName.SteamerTag5: ItemData(1, 133), 
    ItemName.SteamerTag6: ItemData(1, 134), 
    ItemName.SteamerTag7: ItemData(1, 135), 
    ItemName.SteamerTag8: ItemData(1, 136), 
    ItemName.SteamerTag9: ItemData(1, 137), 
    ItemName.SteamerTag10: ItemData(1, 138),     
}

DuffleTags_Table = {
    ItemName.DuffleTag1: ItemData(1, 139), 
    ItemName.DuffleTag2: ItemData(1, 140), 
    ItemName.DuffleTag3: ItemData(1, 141), 
    ItemName.DuffleTag4: ItemData(1, 142), 
    ItemName.DuffleTag5: ItemData(1, 143), 
    ItemName.DuffleTag6: ItemData(1, 144), 
    ItemName.DuffleTag7: ItemData(1, 145), 
    ItemName.DuffleTag8: ItemData(1, 146), 
    ItemName.DuffleTag9: ItemData(1, 147), 
    ItemName.DuffleTag10: ItemData(1, 148),    
}

Suitcase_Table = {
    ItemName.Suitcase1: ItemData(1, 149), 
    ItemName.Suitcase2: ItemData(1, 150), 
    ItemName.Suitcase3: ItemData(1, 151), 
    ItemName.Suitcase4: ItemData(1, 152), 
    ItemName.Suitcase5: ItemData(1, 153), 
    ItemName.Suitcase6: ItemData(1, 154), 
    ItemName.Suitcase7: ItemData(1, 155), 
    ItemName.Suitcase8: ItemData(1, 156), 
    ItemName.Suitcase9: ItemData(1, 157), 
    ItemName.Suitcase10: ItemData(1, 158),  
}

Purse_Table = {
    ItemName.Purse1: ItemData(1, 159), 
    ItemName.Purse2: ItemData(1, 160), 
    ItemName.Purse3: ItemData(1, 161), 
    ItemName.Purse4: ItemData(1, 162), 
    ItemName.Purse5: ItemData(1, 163), 
    ItemName.Purse6: ItemData(1, 164), 
    ItemName.Purse7: ItemData(1, 165), 
    ItemName.Purse8: ItemData(1, 166), 
    ItemName.Purse9: ItemData(1, 167), 
    ItemName.Purse10: ItemData(1, 168),  
}

Hatbox_Table = {
    ItemName.Hatbox1: ItemData(1, 169), 
    ItemName.Hatbox2: ItemData(1, 170), 
    ItemName.Hatbox3: ItemData(1, 171), 
    ItemName.Hatbox4: ItemData(1, 172), 
    ItemName.Hatbox5: ItemData(1, 173), 
    ItemName.Hatbox6: ItemData(1, 174), 
    ItemName.Hatbox7: ItemData(1, 175), 
    ItemName.Hatbox8: ItemData(1, 176), 
    ItemName.Hatbox9: ItemData(1, 177), 
    ItemName.Hatbox10: ItemData(1, 178),     
}

Steamertrunk_Table = {
    ItemName.Steamertrunk1: ItemData(1, 179), 
    ItemName.Steamertrunk2: ItemData(1, 180), 
    ItemName.Steamertrunk3: ItemData(1, 181), 
    ItemName.Steamertrunk4: ItemData(1, 182), 
    ItemName.Steamertrunk5: ItemData(1, 183), 
    ItemName.Steamertrunk6: ItemData(1, 184), 
    ItemName.Steamertrunk7: ItemData(1, 185), 
    ItemName.Steamertrunk8: ItemData(1, 186), 
    ItemName.Steamertrunk9: ItemData(1, 187), 
    ItemName.Steamertrunk10: ItemData(1, 188), 
}

Dufflebag_Table = {
    ItemName.Dufflebag1: ItemData(1, 189), 
    ItemName.Dufflebag2: ItemData(1, 190), 
    ItemName.Dufflebag3: ItemData(1, 191), 
    ItemName.Dufflebag4: ItemData(1, 192), 
    ItemName.Dufflebag5: ItemData(1, 193), 
    ItemName.Dufflebag6: ItemData(1, 194), 
    ItemName.Dufflebag7: ItemData(1, 195), 
    ItemName.Dufflebag8: ItemData(1, 196), 
    ItemName.Dufflebag9: ItemData(1, 197), 
    ItemName.Dufflebag10: ItemData(1, 198), 
}

Vault_Table = {
    ItemName.Vault1: ItemData(1, 199), 
    ItemName.Vault2: ItemData(1, 200), 
    ItemName.Vault3: ItemData(1, 201), 
    ItemName.Vault4: ItemData(1, 202), 
    ItemName.Vault5: ItemData(1, 203), 
    ItemName.Vault6: ItemData(1, 204), 
    ItemName.Vault7: ItemData(1, 205), 
    ItemName.Vault8: ItemData(1, 206), 
    ItemName.Vault9: ItemData(1, 207), 
    ItemName.Vault10: ItemData(1, 208), 
    ItemName.Vault11: ItemData(1, 209), 
    ItemName.Vault12: ItemData(1, 210), 
    ItemName.Vault13: ItemData(1, 211), 
    ItemName.Vault14: ItemData(1, 212), 
    ItemName.Vault15: ItemData(1, 213), 
    ItemName.Vault16: ItemData(1, 214), 
    ItemName.Vault17: ItemData(1, 215), 
    ItemName.Vault18: ItemData(1, 216), 
    ItemName.Vault19: ItemData(1, 217),   
}

AHSmall_Table = {
    ItemName.AHSmall1: ItemData(1, 218), 
    ItemName.AHSmall2: ItemData(1, 219), 
    ItemName.AHSmall3: ItemData(1, 220), 
    ItemName.AHSmall4: ItemData(1, 221), 
    ItemName.AHSmall5: ItemData(1, 222), 
    ItemName.AHSmall6: ItemData(1, 223), 
    ItemName.AHSmall7: ItemData(1, 224), 
    ItemName.AHSmall8: ItemData(1, 225), 
    ItemName.AHSmall9: ItemData(1, 226), 
    ItemName.AHSmall10: ItemData(1, 227), 
    ItemName.AHSmall11: ItemData(1, 228), 
    ItemName.AHSmall12: ItemData(1, 229), 
    ItemName.AHSmall13: ItemData(1, 230), 
    ItemName.AHSmall14: ItemData(1, 231), 
    ItemName.AHSmall15: ItemData(1, 232), 
    ItemName.AHSmall16: ItemData(1, 233), 
    ItemName.AHSmall17: ItemData(1, 234), 
    ItemName.AHSmall18: ItemData(1, 235), 
    ItemName.AHSmall19: ItemData(1, 236), 
    ItemName.AHSmall20: ItemData(1, 237), 
    ItemName.AHSmall21: ItemData(1, 238), 
    ItemName.AHSmall22: ItemData(1, 239), 
    ItemName.AHSmall23: ItemData(1, 240), 
    ItemName.AHSmall24: ItemData(1, 241), 
    ItemName.AHSmall25: ItemData(1, 242), 
    ItemName.AHSmall26: ItemData(1, 243), 
    ItemName.AHSmall27: ItemData(1, 244), 
    ItemName.AHSmall28: ItemData(1, 245), 
    ItemName.AHSmall29: ItemData(1, 246), 
    ItemName.AHSmall30: ItemData(1, 247),     
}

AHLarge_Table = {
    ItemName.AHLarge1: ItemData(1, 248), 
    ItemName.AHLarge2: ItemData(1, 249), 
    ItemName.AHLarge3: ItemData(1, 250), 
    ItemName.AHLarge4: ItemData(1, 251), 
    ItemName.AHLarge5: ItemData(1, 252), 
}

PsiCards_Table = {
    ItemName.PsiCard1: ItemData(1, 253),
    ItemName.PsiCard2: ItemData(1, 254),
    ItemName.PsiCard3: ItemData(1, 255),
    ItemName.PsiCard4: ItemData(1, 256),
    ItemName.PsiCard5: ItemData(1, 257),
    ItemName.PsiCard6: ItemData(1, 258),
    ItemName.PsiCard7: ItemData(1, 259),
    ItemName.PsiCard8: ItemData(1, 260),
    ItemName.PsiCard9: ItemData(1, 261),
    ItemName.PsiCard10: ItemData(1, 262),
    ItemName.PsiCard11: ItemData(1, 263),
    ItemName.PsiCard12: ItemData(1, 264),
    ItemName.PsiCard13: ItemData(1, 265),
    ItemName.PsiCard14: ItemData(1, 266),
    ItemName.PsiCard15: ItemData(1, 267),
    ItemName.PsiCard16: ItemData(1, 268),
    ItemName.PsiCard17: ItemData(1, 269),
    ItemName.PsiCard18: ItemData(1, 270),
    ItemName.PsiCard19: ItemData(1, 271),
    ItemName.PsiCard20: ItemData(1, 272),
    ItemName.PsiCard21: ItemData(1, 273),
    ItemName.PsiCard22: ItemData(1, 274),
    ItemName.PsiCard23: ItemData(1, 275),
    ItemName.PsiCard24: ItemData(1, 276),
    ItemName.PsiCard25: ItemData(1, 277),
    ItemName.PsiCard26: ItemData(1, 278),
    ItemName.PsiCard27: ItemData(1, 279),
    ItemName.PsiCard28: ItemData(1, 280),
    ItemName.PsiCard29: ItemData(1, 281),
    ItemName.PsiCard30: ItemData(1, 282),
    ItemName.PsiCard31: ItemData(1, 283),
    ItemName.PsiCard32: ItemData(1, 284),
    ItemName.PsiCard33: ItemData(1, 285),
    ItemName.PsiCard34: ItemData(1, 286),
    ItemName.PsiCard35: ItemData(1, 287),
    ItemName.PsiCard36: ItemData(1, 288),
    ItemName.PsiCard37: ItemData(1, 289),
    ItemName.PsiCard38: ItemData(1, 290),
    ItemName.PsiCard39: ItemData(1, 291),
    ItemName.PsiCard40: ItemData(1, 292),
    ItemName.PsiCard41: ItemData(1, 293),
    ItemName.PsiCard42: ItemData(1, 294),
    ItemName.PsiCard43: ItemData(1, 295),
    ItemName.PsiCard44: ItemData(1, 296),
    ItemName.PsiCard45: ItemData(1, 297),
    ItemName.PsiCard46: ItemData(1, 298),
    ItemName.PsiCard47: ItemData(1, 299),
    ItemName.PsiCard48: ItemData(1, 300),
    ItemName.PsiCard49: ItemData(1, 301),
    ItemName.PsiCard50: ItemData(1, 302),
    ItemName.PsiCard51: ItemData(1, 303),
    ItemName.PsiCard52: ItemData(1, 304),
    ItemName.PsiCard53: ItemData(1, 305),
    ItemName.PsiCard54: ItemData(1, 306),
    ItemName.PsiCard55: ItemData(1, 307),
    ItemName.PsiCard56: ItemData(1, 308),
    ItemName.PsiCard57: ItemData(1, 309),
    ItemName.PsiCard58: ItemData(1, 310),
    ItemName.PsiCard59: ItemData(1, 311),
    ItemName.PsiCard60: ItemData(1, 312),
    ItemName.PsiCard61: ItemData(1, 313),
    ItemName.PsiCard62: ItemData(1, 314),
    ItemName.PsiCard63: ItemData(1, 315),
    ItemName.PsiCard64: ItemData(1, 316),
    ItemName.PsiCard65: ItemData(1, 317),
    ItemName.PsiCard66: ItemData(1, 318),
    ItemName.PsiCard67: ItemData(1, 319),
    ItemName.PsiCard68: ItemData(1, 320),
    ItemName.PsiCard69: ItemData(1, 321),
    ItemName.PsiCard70: ItemData(1, 322),
    ItemName.PsiCard71: ItemData(1, 323),
    ItemName.PsiCard72: ItemData(1, 324),
    ItemName.PsiCard73: ItemData(1, 325),
    ItemName.PsiCard74: ItemData(1, 326),
    ItemName.PsiCard75: ItemData(1, 327),
    ItemName.PsiCard76: ItemData(1, 328),
    ItemName.PsiCard77: ItemData(1, 329),
    ItemName.PsiCard78: ItemData(1, 330),
    ItemName.PsiCard79: ItemData(1, 331),
    ItemName.PsiCard80: ItemData(1, 332),
    ItemName.PsiCard81: ItemData(1, 333),
    ItemName.PsiCard82: ItemData(1, 334),
    ItemName.PsiCard83: ItemData(1, 335),
    ItemName.PsiCard84: ItemData(1, 336),
    ItemName.PsiCard85: ItemData(1, 337),
    ItemName.PsiCard86: ItemData(1, 338),
    ItemName.PsiCard87: ItemData(1, 339),
    ItemName.PsiCard88: ItemData(1, 340),
    ItemName.PsiCard89: ItemData(1, 341),
    ItemName.PsiCard90: ItemData(1, 342),
    ItemName.PsiCard91: ItemData(1, 343),
    ItemName.PsiCard92: ItemData(1, 344),
    ItemName.PsiCard93: ItemData(1, 345),
    ItemName.PsiCard94: ItemData(1, 346),
    ItemName.PsiCard95: ItemData(1, 347),
    ItemName.PsiCard96: ItemData(1, 348),
    ItemName.PsiCard97: ItemData(1, 349),
    ItemName.PsiCard98: ItemData(1, 350),
    ItemName.PsiCard99: ItemData(1, 351),
    ItemName.PsiCard100: ItemData(1, 352),
    ItemName.PsiCard101: ItemData(1, 353),
    ItemName.PsiCard102: ItemData(1, 354),
    ItemName.PsiCard103: ItemData(1, 355),
    ItemName.PsiCard104: ItemData(1, 356),
    ItemName.PsiCard105: ItemData(1, 357),
    ItemName.PsiCard106: ItemData(1, 358),
    ItemName.PsiCard107: ItemData(1, 359),
    ItemName.PsiCard108: ItemData(1, 360),
    ItemName.PsiCard109: ItemData(1, 361),
    ItemName.PsiCard110: ItemData(1, 362),
    ItemName.PsiCard111: ItemData(1, 363),    
}

OtherItems_Table = {
    ItemName.OarsmansBadge: ItemData(1, 364),    
    ItemName.Feather: ItemData(1, 366),    
    ItemName.LilisBracelet: ItemData(1, 6),
    
}

item_dictionary_table = {
    **RequiredProps_Table
    **MMProps_Table
    **THProps_Table
    **WWProps_Table
    **PsiPowers_Table
    **MaxAmmo_Table
    **MaxLives_Table
    **ConfusionAmmo_Table
    **ChallengeMarker_Table
    **BrainJar_Table
    **ScavHunt_Table
    **SuitcaseTags_Table
    **PurseTags_Table
    **HatboxTags_Table
    **SteamerTags_Table
    **DuffleTags_Table
    **Suitcase_Table
    **Purse_Table
    **Hatbox_Table
    **Steamertrunk_Table
    **Dufflebag_Table
    **Vault_Table
    **AHSmall_Table
    **AHLarge_Table
    **PsiCards_Table
    **OtherItems_Table
}

progression_set = {
    item_name for keys in [
        RequiredProps_Table.keys(),
        MMProps_Table.keys(),
        THProps_Table.keys(),
        WWProps_Table.keys(),
        PsiPowers_Table.keys(),
        Events_Table,
    ]
    for item_name in keys
}

useful_set = {
    item_name for keys in [
    MaxAmmo_Table.keys(),
    MaxLives_Table.keys(),
    ConfusionAmmo_Table.keys(),
    ChallengeMarker_Table.keys(),
    BrainJar_Table.keys(),
    ScavHunt_Table.keys(),
    SuitcaseTags_Table.keys(),
    PurseTags_Table.keys(),
    HatboxTags_Table.keys(),
    SteamerTags_Table.keys(),
    DuffleTags_Table.keys(),
    Suitcase_Table.keys(),
    Purse_Table.keys(),
    Hatbox_Table.keys(),
    Steamertrunk_Table.keys(),
    Dufflebag_Table.keys(),
    Vault_Table.keys(),
    AHLarge_Table.keys(),
    ]
    for item_name in keys if item_name not in progression_set
}

local_set = {
    # Baggage must be local only
    item_name for keys in [
    Suitcase_Table.keys(),
    Purse_Table.keys(),
    Hatbox_Table.keys(),
    Steamertrunk_Table.keys(),
    Dufflebag_Table.keys(),]
    for item_name in keys

}


        


