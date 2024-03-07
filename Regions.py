

import typing

from BaseClasses import MultiWorld, Region

from .Names import LocationName, RegionName

from .Subclasses import PSYLocation

from .Locations import *


def create_psyregions(world: MultiWorld, player: int):

    regMenu = Region("Menu", player, world)
    locMenu_names = []
    regMenu.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regMenu) for loc_name in locMenu_names]
    world.regions.append(regMenu)

    regCASA = Region(RegionName.CASA, player, world)
    locCASA_names = [
        LocationName.BehindFurnitureCard,
        LocationName.StaircaseLedgesCard,
        LocationName.UpperLedgeFossil,
    ]
    regCASA.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCASA) for loc_name in locCASA_names]
    world.regions.append(regCASA)


    regCAGP = Region(RegionName.CAGP, player, world)
    locCAGP_names = [
        LocationName.TopofGPCCard,
        LocationName.UnderGPCCard,
        LocationName.MountainLionLogBridgeCard,
        LocationName.AboveEntranceLakeCard,
        LocationName.RockWallBehindTreeCard,
        LocationName.RockWallTopPirateScope,
        LocationName.TreeNearFenceCard,
        LocationName.TreeNearGeyserCard,
        LocationName.FenceBehindGPCCard,
        LocationName.NeartheBearCard,
        LocationName.RockyPlatformsBehindGPCRightCard,
        LocationName.RockyPlatformsBehindGPCLeftCard,
        LocationName.TopofLogFlumeCard,
        LocationName.RidetheLogFlumeCard,
        LocationName.BottomofLogFlumeCard,
        LocationName.BigRockNearFordCard,
        LocationName.RuinedCabinChallengeMarker,
        LocationName.BranchSwingingCourseStartCard,
        LocationName.BranchSwingingCourseMidCard,
        LocationName.BranchSwingingCourseEndChallengeMarker,
        LocationName.BranchAboveSquirrelCard,
        LocationName.CreekGrateGlassEye,
    ]
    regCAGP.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCAGP) for loc_name in locCAGP_names]
    world.regions.append(regCAGP)

    regCAGPSquirrel = Region(RegionName.CAGPSquirrel, player, world)
    locCAGPSquirrel_names = [
        LocationName.SquirrelsAcornGoldenAcorn,
    ]
    regCAGPSquirrel.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCAGPSquirrel) for loc_name in locCAGPSquirrel_names]
    world.regions.append(regCAGPSquirrel)

    regCAGPGeyser = Region(RegionName.CAGPGeyser, player, world)
    locCAGPGeyser_names = [
        LocationName.GeyserMinersSkull,
    ]
    regCAGPGeyser.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCAGPGeyser) for loc_name in locCAGPGeyser_names]
    world.regions.append(regCAGPGeyser)

    regCAMA = Region(RegionName.CAMA, player, world)
    locCAMA_names = [
        LocationName.FenceNearKidsCabinsCard,
        LocationName.UnderLodgeFrontStepsCard,
        LocationName.BehindTreeNearLodgeCard,
        LocationName.UndertheLodgeGoldDoubloon,
        LocationName.Loudspeaker1PlatformCard,
        LocationName.UnderLodgeMetalRoofCard,
        LocationName.LoudspeakerTightropeWalkCard,
        LocationName.Loudspeaker2PlatformCard,
        LocationName.LodgeRoofChallengeMarker,
        LocationName.MetalRoofOutcroppingCard,
        LocationName.LoudspeakerAboveStumpCard,
        LocationName.TreePlatformLeftCard,
        LocationName.TreePlatformRightEagleClaw,
        LocationName.RockWallTopCard,
        LocationName.ParkingLotArchCard,
        LocationName.ParkingLotSmallLogCard,
        LocationName.OleandersCarCard,
        LocationName.ParkingLotBasketballHoopCard,
        LocationName.ParkingLotOuthouseCard,
        LocationName.RockNearBenchCard,  
    ]
    regCAMA.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCAMA) for loc_name in locCAMA_names]
    world.regions.append(regCAMA)

    regCAMALev = Region(RegionName.CAMALev, player, world)
    locCAMALev_names = [
        LocationName.ParkingLotHistoryBoardCard,
    ]
    regCAMALev.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCAMALev) for loc_name in locCAMALev_names]
    world.regions.append(regCAMALev)

    regCAKC = Region(RegionName.CAKC, player, world)
    locCAKC_names = [
        LocationName.GrindingontheRootsCard,
        LocationName.UnderStairsCard,
        LocationName.TopotheLoudspeakerCard,
        LocationName.CabinRoof1Card,
        LocationName.TrampolineAboveOuthouseCard,
        LocationName.TrampolinePlatformChallengeMarker,
        LocationName.CabinsOuthouseCard,
        LocationName.BehindCabinCard,
        LocationName.RoofofCabin2Card,
        LocationName.CaveEntranceCard,
        LocationName.DeepCavePathCard,
        LocationName.DeepCaveLadderCard,
    ]
    regCAKC.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCAKC) for loc_name in locCAKC_names]
    world.regions.append(regCAKC)

    regCAKCLev = Region(RegionName.CAKCLev, player, world)
    locCAKCLev_names = [
        LocationName.HighUpTightropeCard,
    ]
    regCAKCLev.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCAKCLev) for loc_name in locCAKCLev_names]
    world.regions.append(regCAKCLev)

    regCAKCPyro = Region(RegionName.CAKCPyro, player, world)
    locCAKCPyro_names = [
        LocationName.CaveRefrigeratorTurkeySandwich,
    ]
    regCAKCPyro.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCAKCPyro) for loc_name in locCAKCPyro_names]
    world.regions.append(regCAKCPyro)

    regCARE = Region(RegionName.CARE, player, world)
    locCARE_names = [
        LocationName.GraveyardBearCard, 
        LocationName.NearBeehiveCard,
        LocationName.MineshaftTrailerEntranceCard,
        LocationName.TightropeStartCard, 
        LocationName.TightropeEndCard, 
        LocationName.RocksNearTrailerCard, 
        LocationName.FireplaceTreeLowerCard, 
        LocationName.FireplaceTreeRockCard, 
        LocationName.SwampSkinnyPolesCard, 
        LocationName.BigLogPlatformCard, 
        LocationName.AboveWaterfallLeftCard, 
        LocationName.AboveWaterfallRightCard, 
        LocationName.BehindtheWaterfallCard, 
        LocationName.WeirdTreeLeftCherryWoodPipe, 
        LocationName.WeirdTreeRightCard, 
        LocationName.LogHillTopCard,
        LocationName.LogHillBehindCard, 
        LocationName.MineshaftGrindRailCard, 
        LocationName.MineshaftUpperEntranceCard, 
        LocationName.MineshaftAboveUpperEntranceCard, 
        LocationName.InsideMineshaftCard, 
        LocationName.MineshaftBearCard, 
        LocationName.SwampBirdsNestCondorEgg, 
        LocationName.CollapsedCaveChallengeMarker, 
    ]
    regCARE.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCARE) for loc_name in locCARE_names]
    world.regions.append(regCARE)

    regCARELev = Region(RegionName.CARELev, player, world)
    locCARELev_names = [
        LocationName.FireplaceTreeTopDinosaurBone, 
    ]
    regCARELev.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCARELev) for loc_name in locCARELev_names]
    world.regions.append(regCARELev)

    regCAREMark = Region(RegionName.CAREMark, player, world)
    locCAREMark_names = [
        LocationName.HornetNestFertilityIdol,
    ]
    regCAREMark.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCAREMark) for loc_name in locCAREMark_names]
    world.regions.append(regCAREMark)

    regCABH = Region(RegionName.CABH, player, world)
    locCABH_names = [
        LocationName.UndertheFirstBridgeCard, 
        LocationName.BehindStumpCard, 
        LocationName.LeftofEntranceRockWallCard, 
        LocationName.PolesonLakeCard, 
        LocationName.BathysphereRoofCard, 
        LocationName.BathysphereDockCard,
        LocationName.MetalRoofAboveFordCard, 
        LocationName.AboveFordRopesCard, 
        LocationName.AboveFordCabinPlatformCard, 
        LocationName.OutsideCougarCaveCard, 
        LocationName.InsideCougarCaveDiversHelmet, 
        LocationName.BulletinBoardBushesCard, 
        LocationName.PinkTreesPlatformLeftCard, 
        LocationName.PinkTreesPlatformRightCard, 
        LocationName.RockWallUpperCard, 
        LocationName.LakeShoreCard, 
        LocationName.TinyIslandCard, 
        LocationName.RockWallGapPsychonautsComic1, 
    ]
    regCABH.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCABH) for loc_name in locCABH_names]
    world.regions.append(regCABH)

    regCABHLev = Region(RegionName.CABHLev, player, world)
    locCABHLev_names = [
        LocationName.TopofBigRockChallengeMarker, 
    ]
    regCABHLev.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCABHLev) for loc_name in locCABHLev_names]
    world.regions.append(regCABHLev)

    regCALI = Region(RegionName.CALI, player, world)
    locCALI_names = [
        LocationName.MainLodgeRaftersVoodooDoll,
    ]
    regCALI.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCALI) for loc_name in locCALI_names]
    world.regions.append(regCALI)

    regCAJA = Region(RegionName.CAJA, player, world)
    locCAJA_names = [
        LocationName.TopofSanctuaryCard, 
        LocationName.BottomofSanctuaryCard, 
    ]
    regCAJA.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regCAJA) for loc_name in locCAJA_names]
    world.regions.append(regCAJA)

    regRANK5to15 = Region(RegionName.RANK5to15, player, world)
    locRANK5to15_names = [
        LocationName.PSIRank05, 
        LocationName.PSIRank10, 
        LocationName.PSIRank15,        
    ]
    regRANK5to15.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regRANK5to15) for loc_name in locRANK5to15_names]
    world.regions.append(regRANK5to15)

    regRANK20to101 = Region(RegionName.RANK20to101, player, world)
    locRANK20to101_names = [
        LocationName.PSIRank20, 
        LocationName.PSIRank25, 
        LocationName.PSIRank30, 
        LocationName.PSIRank35, 
        LocationName.PSIRank40, 
        LocationName.PSIRank45, 
        LocationName.PSIRank50, 
        LocationName.PSIRank55, 
        LocationName.PSIRank60, 
        LocationName.PSIRank65, 
        LocationName.PSIRank70, 
        LocationName.PSIRank75, 
        LocationName.PSIRank80, 
        LocationName.PSIRank85, 
        LocationName.PSIRank90, 
        LocationName.PSIRank95, 
        LocationName.PSIRank101,
    ]
    regRANK20to101.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regRANK20to101) for loc_name in locRANK20to101_names]
    world.regions.append(regRANK20to101)

    regASGR = Region(RegionName.ASGR, player, world)
    locASGR_names = [
        LocationName.RockWallBottom, 
        LocationName.RockWallLadder, 
        LocationName.OutsideFrontGate, 
        LocationName.FountainTop, 
        LocationName.HedgeAlcove, 
        LocationName.AsylumDoorsRight, 
        LocationName.AsylumDoorsLeft, 
        LocationName.CornerNearFence, 
        LocationName.LedgeBeforeGloria,
    ]
    regASGR.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regASGR) for loc_name in locASGR_names]
    world.regions.append(regASGR)

    regASGRLev = Region(RegionName.ASGRLev, player, world)
    locASGRLev_names = [
        LocationName.PillarAboveGate, 
    ]
    regASGRLev.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regASGRLev) for loc_name in locASGRLev_names]
    world.regions.append(regASGRLev)

    regASCO = Region(RegionName.ASCO, player, world)
    locASCO_names = [
        LocationName.AboveElevator, 
        LocationName.CrowsBasket, 
        LocationName.LedgeAboveFredLeft, 
        LocationName.LedgeAboveFredRight, 
        LocationName.LedgeOppositeElevator, 
        LocationName.EdgarsRoom, 
        LocationName.BehindElevator, 
        LocationName.JunkCorner, 
    ]
    regASCO.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regASCO) for loc_name in locASCO_names]
    world.regions.append(regASCO)

    regASCOLev = Region(RegionName.ASCOLev, player, world)
    locASCOLev_names = [
        LocationName.AboveEdgar,
    ]
    regASCOLev.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regASCOLev) for loc_name in locASCOLev_names]
    world.regions.append(regASCOLev)

    regASUP = Region(RegionName.ASUP, player, world)
    locASUP_names = [
        LocationName.BehindMattressWall, 
        LocationName.CheckeredBathroom, 
        LocationName.RoomNearCheckeredBathroom, 
        LocationName.ElevatorShaft, 
        LocationName.RoomLeftOfPipeSlide, 
        LocationName.FloatingInHole, 
        LocationName.NextToHole, 
        LocationName.CrumblingOuterWallPlanks, 
        LocationName.CrumblingOuterWallPillar, 
        LocationName.CrumblingOuterWallBelowPlatform, 
    ]
    regASUP.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regASUP) for loc_name in locASUP_names]
    world.regions.append(regASUP)

    regASUPLev = Region(RegionName.ASUPLev, player, world)
    locASUPLev_names = [
        LocationName.CrumblingOuterWallPlatform, 
        LocationName.RoomAboveTiltedStairs, 
        LocationName.AcidRoomFloor, 
        LocationName.AcidRoomTable, 
        LocationName.AcidRoomWindow, 
        LocationName.AcidRoomOverhang, 
        LocationName.SmallWindowsLedge, 
        LocationName.RoundWoodPlatform,
        LocationName.GrateClimbBottom, 
        LocationName.GrateClimbMid, 
        LocationName.SinkPlatformLeft, 
        LocationName.SinkPlatformRight, 
        LocationName.PipesBelowChairDoor,
    ]
    regASUPLev.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regASUPLev) for loc_name in locASUPLev_names]
    world.regions.append(regASUPLev)

    regASUPTele = Region(RegionName.ASUPTele, player, world)
    locASUPTele_names = [
        LocationName.RoomOppositeChairDoor, 
        LocationName.PipeSlideNearChairDoor, 
        LocationName.RaftersAboveChairDoor,
    ]
    regASUPTele.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regASUPTele) for loc_name in locASUPTele_names]
    world.regions.append(regASUPTele)

    regASLB = Region(RegionName.ASLB, player, world)
    locASLB_names = [
        LocationName.LabCagedCrowLeft, 
        LocationName.LabCagedCrowRight, 
        LocationName.NextToPokeylope, 
        LocationName.LabTopRailingLeft1, 
        LocationName.LabTopRailingLeft2,
        LocationName.LabTopElevator, 
        LocationName.LabTopRailingRight, 
        LocationName.TeaRoom, 
    ]
    regASLB.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regASLB) for loc_name in locASLB_names]
    world.regions.append(regASLB)

    regBBA1 = Region(RegionName.BBA1, player, world)
    locBBA1_names = [
        LocationName.JumpingTutorial1, 
        LocationName.JumpingTutorial2, 
        LocationName.PoleClimbingTutorialFloor, 
        LocationName.BelowTheTripleTrampolines,
    ]
    regBBA1.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regBBA1) for loc_name in locBBA1_names]
    world.regions.append(regBBA1)

    regBBA2 = Region(RegionName.BBA2, player, world)
    locBBA2_names = [
        LocationName.GiantSoldierCutOut, 
        LocationName.DodgingBullets1, 
        LocationName.DodgingBullets2, 
        LocationName.MachineGunTurret, 
        LocationName.PoleSwingingTutorial, 
        LocationName.TrapezePlatform, 
        LocationName.InsidePlaneWreckage,
        LocationName.EndOfObstacleCourseLeft, 
        LocationName.EndOfObstacleCourseRight, 
        LocationName.BasicBrainingComplete, 
    ]
    regBBA2.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regBBA2) for loc_name in locBBA2_names]
    world.regions.append(regBBA2)

    regBBA2Duster = Region(RegionName.BBA2Duster, player, world)
    locBBA2Duster_names = [
        LocationName.TrapezeCobweb, 
    ]
    regBBA2Duster.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regBBA2Duster) for loc_name in locBBA2Duster_names]
    world.regions.append(regBBA2Duster)

    regSACU = Region(RegionName.SACU, player, world)
    locSACU_names = [
        LocationName.OnTheBed, 
        LocationName.OnThePillow, 
        LocationName.BuildingBlocksLeft, 
        LocationName.BuildingBlocksBelow, 
        LocationName.BuildingBlocksRight,
        LocationName.TopOfBedFrame, 
        LocationName.RoundPlatformsBottom, 
        LocationName.RoundPlatformsNearValve, 
        LocationName.SideOfCubeFace3, 
        LocationName.BottomOfShoeboxLadder, 
        LocationName.ShoeboxPedestal, 
        LocationName.ShoeboxTowerTop, 
        LocationName.FlameTowerSteps, 
        LocationName.FlameTowerTop1, 
        LocationName.FlameTowerTop2, 
        LocationName.SashasShootingGalleryComplete,
    ]
    regSACU.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regSACU) for loc_name in locSACU_names]
    world.regions.append(regSACU)


    regSACULev = Region(RegionName.SACULev, player, world)
    locSACULev_names = [
        LocationName.RoundPlatformsFarFromValve, 
    ]
    regSACULev.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regSACULev) for loc_name in locSACULev_names]
    world.regions.append(regSACULev)


    regMIFL = Region(RegionName.MIFL, player, world)
    locMIFL_names = [
        LocationName.IntroRingsTutorial, 
        LocationName.DancingCamperPlatform1, 
        LocationName.DemonRoom, 
        LocationName.WindyLadderBottom, 
        LocationName.PinballPlunger, 
        LocationName.PlungerPartyLedge, 
        LocationName.GrindrailRings, 
        LocationName.CensorHallway, 
        LocationName.PinkBowlBottom, 
        LocationName.PinkBowlSmallPlatform, 
        LocationName.BubblyFanBottom, 
        LocationName.BubblyFanPlatform, 
        LocationName.BubblyFanTop, 
        LocationName.MillasPartyRoom, 
        LocationName.MillasDancePartyComplete, 
    ]
    regMIFL.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regMIFL) for loc_name in locMIFL_names]
    world.regions.append(regMIFL)

    regNIMP = Region(RegionName.NIMP, player, world)
    locNIMP_names = [
        LocationName.OutsideCaravan, 
        LocationName.BehindTheEgg, 
        LocationName.ShadowMonsterPath, 
    ]
    regNIMP.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regNIMP) for loc_name in locNIMP_names]
    world.regions.append(regNIMP)


    regNIMPMark = Region(RegionName.NIMPMark, player, world)
    locNIMPMark_names = [
        LocationName.ShadowMonsterBlueMushrooms, 
        LocationName.LedgeBehindShadowMonster, 
        LocationName.BelowTheSteepLedge, 
        LocationName.ForestPathBlueMushrooms, 
        LocationName.ForestBlueLedge, 
        LocationName.ForestHighPlatform, 
        LocationName.ForestPathThorns, 
        LocationName.BehindThornTowerLeft, 
        LocationName.BehindThornTowerMid, 
        LocationName.BehindThornTowerRight, 
    ]
    regNIMPMark.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regNIMPMark) for loc_name in locNIMPMark_names]
    world.regions.append(regNIMPMark)


    regNIBA = Region(RegionName.NIBA, player, world)
    locNIBA_names = [
        LocationName.BrainTumblerExperimentComplete, 
    ]
    regNIBA.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regNIBA) for loc_name in locNIBA_names]
    world.regions.append(regNIBA)

    regLOMA = Region(RegionName.LOMA, player, world)
    locLOMA_names = [
        LocationName.SkyscraperStart, 
        LocationName.CornerNearJail, 
        LocationName.SkyscraperBeforeDam, 
        
    ]
    regLOMA.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regLOMA) for loc_name in locLOMA_names]
    world.regions.append(regLOMA)


    regLOMAShield = Region(RegionName.LOMAShield, player, world)
    locLOMAShield_names = [
        LocationName.BehindLasersLeft1, 
        LocationName.BehindLasersLeft2, 
        LocationName.BehindLasersRight, 
        LocationName.BlimpHop, 
        LocationName.EndOfDam, 
        LocationName.EndOfDamPlatform, 
        LocationName.SkyscraperAfterDam, 
        LocationName.NearBattleships, 
        LocationName.OnTheBridge, 
        LocationName.GroundAfterBridge, 
        LocationName.SkyscraperAfterBridge, 
        LocationName.TunnelSuitcaseTag, 
        LocationName.FinalSkyscrapersLeft, 
        LocationName.FinalSkyscrapersRight,
        LocationName.KochamaraIntroLeft, 
        LocationName.KochamaraIntroRight,
        LocationName.LungfishopolisComplete, 
    ]
    regLOMAShield.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regLOMAShield) for loc_name in locLOMAShield_names]
    world.regions.append(regLOMAShield)

        
    regMMI1Fridge = Region(RegionName.MMI1Fridge, player, world)
    locMMI1Fridge_names = [
        LocationName.BoydsFridgeClv, 
    ]
    regMMI1Fridge.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regMMI1Fridge) for loc_name in locMMI1Fridge_names]
    world.regions.append(regMMI1Fridge)


    regMMI1BeforeSign = Region(RegionName.MMI1BeforeSign, player, world)
    locMMI1BeforeSign_names = [
        LocationName.FirstHouseDufflebagTag, 
        LocationName.SecondHouseRollingPin, 
        LocationName.CarTrunk1StopSign, 
    ]
    regMMI1BeforeSign.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regMMI1BeforeSign) for loc_name in locMMI1BeforeSign_names]
    world.regions.append(regMMI1BeforeSign)


    regMMI1AfterSign = Region(RegionName.MMI1AfterSign, player, world)
    locMMI1AfterSign_names = [
        LocationName.RoofAfterRoadCrewPurseTag, 
        LocationName.CarTrunk2HedgeTrimmers, 
        LocationName.CarHouseBackyardSteamertrunkTag,
        LocationName.GraveyardPatioVault, 
        LocationName.GraveyardBehindTreeOneUp, 
        LocationName.BehindGraveyardDufflebag, 
        LocationName.HedgeMazeFlowers, 
        LocationName.CarTrunk3WateringCan, 
        LocationName.PostOfficeRoofOneUp, 
    ]
    regMMI1AfterSign.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regMMI1AfterSign) for loc_name in locMMI1AfterSign_names]
    world.regions.append(regMMI1AfterSign)


    regMMI1Hedgetrimmers = Region(RegionName.MMI1Hedgetrimmers, player, world)
    locMMI1Hedgetrimmers_names = [
        LocationName.LandscapersHouseBackyardSuitcaseTag, 
        LocationName.LandscapersHouseTablePurse, 
    ]
    regMMI1Hedgetrimmers.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regMMI1Hedgetrimmers) for loc_name in locMMI1Hedgetrimmers_names]
    world.regions.append(regMMI1Hedgetrimmers)


    regMMI1RollingPin = Region(RegionName.MMI1RollingPin, player, world)
    locMMI1RollingPin_names = [
        LocationName.LandscapersHouseKitchenAmmoUp, 
    ]
    regMMI1RollingPin.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regMMI1RollingPin) for loc_name in locMMI1RollingPin_names]
    world.regions.append(regMMI1RollingPin)


    regMMI1Powerlines = Region(RegionName.MMI1Powerlines, player, world)
    locMMI1Powerlines_names = [
        LocationName.PowerlineIslandSandboxHatboxTag, 
        LocationName.PowerlineIslandLeftMemoryVault, 
        LocationName.PowerlineIslandRightMaxLives, 
    ]
    regMMI1Powerlines.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regMMI1Powerlines) for loc_name in locMMI1Powerlines_names]
    world.regions.append(regMMI1Powerlines)


    regMMI1Duster = Region(RegionName.MMI1Duster, player, world)
    locMMI1Duster_names = [
        LocationName.InsideWebbedGarageHatbox,
        LocationName.PostOfficeLobbySuitcase, 
        LocationName.PostOfficeBasementPlunger, 
    ]
    regMMI1Duster.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regMMI1Duster) for loc_name in locMMI1Duster_names]
    world.regions.append(regMMI1Duster)


    regMMI2 = Region(RegionName.MMI2, player, world)
    locMMI2_names = [
        LocationName.BehindBookDepositorySteamerTrunk,  
    ]
    regMMI2.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regMMI2) for loc_name in locMMI2_names]
    world.regions.append(regMMI2)


    regMMDM = Region(RegionName.MMDM, player, world)
    locMMDM_names = [
        LocationName.MilkmanComplete, 
    ]
    regMMDM.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regMMDM) for loc_name in locMMDM_names]
    world.regions.append(regMMDM)


    regTHMS = Region(RegionName.THMS, player, world)
    locTHMS_names = [
        LocationName.NearTheCriticPurse, 
        LocationName.BelowTheSpotlightSteamertrunkTag, 
        LocationName.BehindStagePurseTag, 
    ]
    regTHMS.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regTHMS) for loc_name in locTHMS_names]
    world.regions.append(regTHMS)


    regTHMSLev = Region(RegionName.THMSLev, player, world)
    locTHMSLev_names = [
        LocationName.InTheAudienceAmmoUp, 
    ]
    regTHMSLev.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regTHMSLev) for loc_name in locTHMSLev_names]
    world.regions.append(regTHMSLev)


    regTHMSDuster = Region(RegionName.THMSDuster, player, world)
    locTHMSDuster_names = [
        LocationName.BehindStageCobwebSuitcase, 
    ]
    regTHMSDuster.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regTHMSDuster) for loc_name in locTHMSDuster_names]
    world.regions.append(regTHMSDuster)


    regTHMSStorage = Region(RegionName.THMSStorage, player, world)
    locTHMSStorage_names = [
        LocationName.StorageRoomFloorVault, 
        LocationName.StorageRoomLeftSteamertrunk, 
        LocationName.StorageRoomRightLowerSuitcaseTag, 
        LocationName.StorageRoomRightUpperCandle1, 
        LocationName.BonitasRoom, 
    ]
    regTHMSStorage.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regTHMSStorage) for loc_name in locTHMSStorage_names]
    world.regions.append(regTHMSStorage)


    regTHCW = Region(RegionName.THCW, player, world)
    locTHCW_names = [
        LocationName.DoghouseSlicersDufflebagTag, 
        LocationName.BigPlatform1Hatbox, 
        LocationName.BigPlatform2Vault, 
        LocationName.BigPlatform3OneUp, 
        LocationName.BigPlatformAboveHatboxTag, 
        LocationName.NextToOatmealDufflebag, 
        LocationName.CandleBasketCandle2, 
        LocationName.CurtainSlideConfusionAmmoUp, 
    ]
    regTHCW.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regTHCW) for loc_name in locTHCW_names]
    world.regions.append(regTHCW)


    regTHFB = Region(RegionName.THFB, player, world)
    locTHFB_names = [
        LocationName.GloriasTheaterComplete,
    ]
    regTHFB.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regTHFB) for loc_name in locTHFB_names]
    world.regions.append(regTHFB)


    regWWMA = Region(RegionName.WWMA, player, world)
    locWWMA_names = [
        LocationName.FredsRoomHatboxTag, 
        LocationName.TheFireplacePricelessCoin, 
        LocationName.GameBoardSuitcaseTag,
        LocationName.OutsideVillager1HouseOneUp, 
        LocationName.SmallArchTopMaxLives, 
        LocationName.SmallArchBelowPurseTag, 
        LocationName.TopOfVillager2sHouseDufflebagTag,
        LocationName.CastleTowerOneUp, 
        LocationName.CastleInsideVault, 
        LocationName.CastleWallSteamertrunk,
        LocationName.HelpTheCarpenter,
    ]
    regWWMA.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regWWMA) for loc_name in locWWMA_names]
    world.regions.append(regWWMA)


    regWWMALev = Region(RegionName.WWMALev, player, world)
    locWWMALev_names = [
        LocationName.TopOfVillager3sHouseAmmoUp, 
        LocationName.TopOfKnightsHouseConfusionAmmoUp, 
    ]
    regWWMALev.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regWWMALev) for loc_name in locWWMALev_names]
    world.regions.append(regWWMALev)


    regWWMACarpRoof = Region(RegionName.WWMACarpRoof, player, world)
    locWWMACarpRoof_names = [
        LocationName.CarpentersRoofVault,
        LocationName.TightropeRoomDufflebag, 
    ]
    regWWMACarpRoof.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regWWMACarpRoof) for loc_name in locWWMACarpRoof_names]
    world.regions.append(regWWMACarpRoof)


    regWWMADuster = Region(RegionName.WWMADuster, player, world)
    locWWMADuster_names = [
        LocationName.UnderTheGuillotineSuitcase, 
        LocationName.FredsHouseBasementHatbox, 
        LocationName.BlacksmithsLeftBuildingPurse, 
    ]
    regWWMADuster.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regWWMADuster) for loc_name in locWWMADuster_names]
    world.regions.append(regWWMADuster)


    regWWMADusterLev = Region(RegionName.WWMADusterLev, player, world)
    locWWMADusterLev_names = [
        LocationName.BlacksmithsRightBuildingSteamertrunkTag, 
    ]
    regWWMADusterLev.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regWWMADusterLev) for loc_name in locWWMADusterLev_names]
    world.regions.append(regWWMADusterLev)


    regWWMADusterLevPyro = Region(RegionName.WWMADusterLevPyro, player, world)
    locWWMADusterLevPyro_names = [
        LocationName.BlacksmithsHaybaleTheMusket, 
    ]
    regWWMADusterLevPyro.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regWWMADusterLevPyro) for loc_name in locWWMADusterLevPyro_names]
    world.regions.append(regWWMADusterLevPyro)


    regWWMAV1 = Region(RegionName.WWMAV1, player, world)
    locWWMAV1_names = [
        LocationName.HelpVillager1, 
    ]
    regWWMAV1.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regWWMAV1) for loc_name in locWWMAV1_names]
    world.regions.append(regWWMAV1)


    regWWMAKnight = Region(RegionName.WWMAKnight, player, world)
    locWWMAKnight_names = [
        LocationName.HelpTheKnight, 
    ]
    regWWMAKnight.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regWWMAKnight) for loc_name in locWWMAKnight_names]
    world.regions.append(regWWMAKnight)


    regWWMAV2 = Region(RegionName.WWMAV2, player, world)
    locWWMAV2_names = [
        LocationName.HelpVillager2, 
    ]
    regWWMAV2.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regWWMAV2) for loc_name in locWWMAV2_names]
    world.regions.append(regWWMAV2)


    regWWMAV3 = Region(RegionName.WWMAV3, player, world)
    locWWMAV3_names = [
        LocationName.HelpVillager3,
        LocationName.WaterlooWorldComplete, 
    ]
    regWWMAV3.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regWWMAV3) for loc_name in locWWMAV3_names]
    world.regions.append(regWWMAV3)


    regBVRB = Region(RegionName.BVRB, player, world)
    locBVRB_names = [
        LocationName.ClubStreetLadySteamertrunk, 
    ]
    regBVRB.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regBVRB) for loc_name in locBVRB_names]
    world.regions.append(regBVRB)


    regBVRBLev = Region(RegionName.BVRBLev, player, world)
    locBVRBLev_names = [
        LocationName.ClubStreetMetalBalconyDufflebagTag, 
        LocationName.HeartStreetHIGHBalconyAmmoUp,
    ]
    regBVRBLev.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regBVRBLev) for loc_name in locBVRBLev_names]
    world.regions.append(regBVRBLev)


    regBVRBTele = Region(RegionName.BVRBTele, player, world)
    locBVRBTele_names = [
        LocationName.ClubStreetGatedSteamerTrunkTag, 
    ]
    regBVRBTele.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regBVRBTele) for loc_name in locBVRBTele_names]
    world.regions.append(regBVRBTele)


    regBVRBDuster = Region(RegionName.BVRBDuster, player, world)
    locBVRBDuster_names = [
        LocationName.AlleywaysLedgeHatboxTag, 
        LocationName.SewersMainVault,
        LocationName.NearDiegosHouseMaxLives, 
        LocationName.DiegosBedSuitcaseTag, 
        LocationName.DiegosRoomHatbox, 
        LocationName.DiegosHouseGrindrailSuitcase, 
        LocationName.GrindrailBalconyConfusionAmmoUp,
    ]
    regBVRBDuster.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regBVRBDuster) for loc_name in locBVRBDuster_names]
    world.regions.append(regBVRBDuster)


    regBVRBGarden = Region(RegionName.BVRBGarden, player, world)
    locBVRBGarden_names = [
        LocationName.TheGardenVault, 
    ]
    regBVRBGarden.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regBVRBGarden) for loc_name in locBVRBGarden_names]
    world.regions.append(regBVRBGarden)


    regBVRBLogs = Region(RegionName.BVRBLogs, player, world)
    locBVRBLogs_names = [
        LocationName.BurnTheLogsDufflebag, 
    ]
    regBVRBLogs.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regBVRBLogs) for loc_name in locBVRBLogs_names]
    world.regions.append(regBVRBLogs)


    regBVES = Region(RegionName.BVES, player, world)
    locBVES_names = [
        LocationName.SanctuaryGroundPurse, 
        LocationName.TigerWrestler, 
        LocationName.DragonWrestler,
    ]
    regBVES.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regBVES) for loc_name in locBVES_names]
    world.regions.append(regBVES)


    regBVESLev = Region(RegionName.BVESLev, player, world)
    locBVESLev_names = [
        LocationName.SanctuaryBalconyPurseTag, 
    ]
    regBVESLev.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regBVESLev) for loc_name in locBVESLev_names]
    world.regions.append(regBVESLev)


    regBVESEagle = Region(RegionName.BVESEagle, player, world)
    locBVESEagle_names = [
        LocationName.EagleWrestler, 
    ]
    regBVESEagle.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regBVESEagle) for loc_name in locBVESEagle_names]
    world.regions.append(regBVESEagle)


    regBVESCobra = Region(RegionName.BVESCobra, player, world)
    locBVESCobra_names = [
        LocationName.CobraWrestler, 
    ]
    regBVESCobra.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regBVESCobra) for loc_name in locBVESCobra_names]
    world.regions.append(regBVESCobra)


    regBVESBoss = Region(RegionName.BVESBoss, player, world)
    locBVESBoss_names = [
        LocationName.BlackVelvetopiaComplete, 
    ]
    regBVESBoss.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regBVESBoss) for loc_name in locBVESBoss_names]
    world.regions.append(regBVESBoss)


    regMCTC = Region(RegionName.MCTC, player, world)
    locMCTC_names = [
        LocationName.EntranceAwningSteamertrunkTag, 
        LocationName.CrumblingPathSteamertrunk, 
        LocationName.CrumblingPathEndRightHatboxTag, 
        LocationName.CrumblingPathEndLeftConfusionAmmoUp, 
    ]
    regMCTC.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regMCTC) for loc_name in locMCTC_names]
    world.regions.append(regMCTC)


    regMCTCEscort = Region(RegionName.MCTCEscort, player, world)
    locMCTCEscort_names = [
        LocationName.OllieEscortFloorSuitcaseTag, 
        LocationName.OllieEscortMiddleHatbox, 
        LocationName.OllieEscortTopLeftVault, 
        LocationName.OllieEscortTopRightPurseTag, 
        LocationName.TunnelOfLoveStartPurse, 
        LocationName.TunnelOfLoveCornerSuitcase, 
        LocationName.TunnelOfLoveRailDufflebagTag, 
        LocationName.NextToTheFatLadyDufflebag,
    ]
    regMCTCEscort.locations += [PSYLocation(player, loc_name, all_locations[loc_name] + 42690000, regMCTCEscort) for loc_name in locMCTCEscort_names]
    world.regions.append(regMCTCEscort)


    regMCTCBoss = Region(RegionName.MCTCBoss, player, world)
    regMCTCBoss.locations += [PSYLocation(player, LocationName.FinalBossEvent, None, regMCTCBoss)]
    world.regions.append(regMCTCBoss)


    # should only have an item if Cobweb Duster vanilla
    #RegionName.FordShop: [
    #    LocationName.ShopCobwebDuster, 
    #],

    # RegionName.DUMMYLOCATIONS
        # NOT COLLECTIBLE
    #    LocationName.DUMMYLOCATION1NOTCOLLECTIBLE, 
    #    LocationName.DUMMYLOCATION2NOTCOLLECTIBLE, 
    #    LocationName.DUMMYLOCATION3NOTCOLLECTIBLE, 


def connect_regions(multiworld: MultiWorld, player: int):
    PSYRegionConnections: typing.Dict[str, typing.Set[str]] = {
        "Menu":                        {RegionName.CASA},
        #Collective Unconscious connections to everything else
        RegionName.CASA: {RegionName.CAGP, RegionName.CAJA, RegionName.RANK5to15, RegionName.BBA1, RegionName.SACU, RegionName.MIFL, 
            RegionName.NIMP, RegionName.LOMA, RegionName.MMI1Fridge, RegionName.THMS, RegionName.WWMA,
            RegionName.BVRB, RegionName.MCTC, },

        RegionName.RANK5to15: {RegionName.RANK20to101, },

        RegionName.CAGP: {RegionName.CAGPSquirrel, RegionName.CAGPGeyser, RegionName.CAMA, RegionName.CAKC, RegionName.CARE, 
            RegionName.CABH, RegionName.CALI, },

        RegionName.CAMA: {RegionName.CAMALev, },

        RegionName.CAKC: {RegionName.CAKCLev, RegionName.CAKCPyro, },

        RegionName.CARE: {RegionName.CARELev, RegionName.CAREMark, },

        RegionName.CABH: {RegionName.CABHLev, RegionName.ASGR, },

        RegionName.ASGR: {RegionName.ASGRLev, RegionName.ASCO, RegionName.ASCOLev, },

        RegionName.ASCO: {RegionName.ASUP, },

        RegionName.ASUP: {RegionName.ASUPLev, },

        RegionName.ASUPLev: {RegionName.ASUPTele, },

        RegionName.ASUPTele: {RegionName.ASLB, },

        RegionName.BBA1: {RegionName.BBA2, RegionName.BBA2Duster, },

        RegionName.SACU: {RegionName.SACULev, },

        RegionName.NIMP: {RegionName.NIMPMark, RegionName.NIBA, },

        RegionName.LOMA: {RegionName.LOMAShield, },

        RegionName.MMI1Fridge: {RegionName.MMI1BeforeSign, },

        RegionName.MMI1BeforeSign: {RegionName.MMI1AfterSign, },
        
        RegionName.MMI1AfterSign: {RegionName.MMI1Hedgetrimmers, RegionName.MMI1Duster, RegionName.MMI2, },

        RegionName.MMI1Hedgetrimmers: {RegionName.MMI1RollingPin, },

        RegionName.MMI2: {RegionName.MMI1Powerlines, RegionName.MMDM, },

        RegionName.THMS: {RegionName.THMSLev, RegionName.THMSDuster, RegionName.THMSStorage, },

        RegionName.THMSStorage: {RegionName.THCW, },

        RegionName.THCW: {RegionName.THFB, },

        RegionName.WWMA: {RegionName.WWMALev, RegionName.WWMACarpRoof, RegionName.WWMADuster, RegionName.WWMAV1, },

        RegionName.WWMADuster: {RegionName.WWMADusterLev, },

        RegionName.WWMADusterLev: {RegionName.WWMADusterLevPyro, },

        RegionName.WWMAV1: {RegionName.WWMAKnight, RegionName.WWMAV2,},

        RegionName.WWMAV2: {RegionName.WWMAV3, },

        RegionName.BVRB: {RegionName.BVRBLev, RegionName.BVRBTele, RegionName.BVRBDuster, RegionName.BVES, },

        RegionName.BVRBDuster: {RegionName.BVRBGarden, },

        RegionName.BVRBGarden: {RegionName.BVRBLogs, },

        RegionName.BVES: {RegionName.BVESLev, RegionName.BVESEagle,},

        RegionName.BVESEagle: {RegionName.BVESCobra, },

        RegionName.BVESCobra: {RegionName.BVESBoss, },

        RegionName.MCTC: {RegionName.MCTCEscort, },

        RegionName.MCTCEscort: {RegionName.MCTCBoss, },


    }                         

    for source, target in PSYRegionConnections.items():
        source_region = multiworld.get_region(source, player)
        source_region.add_exits(target)




