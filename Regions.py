import typing

from BaseClasses import MultiWorld, Region

from .Names import LocationName, RegionName #Events_Table

from .Subclasses import PSYLocation

from . import Locations

PSYREGIONS: typing.Dict[str, typing.List[str]] = {
    "Menu": [],
    RegionName.CASA: [
        LocationName.BehindFurnitureCard,
        LocationName.StaircaseLedgesCard,
        LocationName.UpperLedgeFossil,
    ],

    RegionName.CAGP: [
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
    ],

    RegionName.CAGPSquirrel: [
        LocationName.SquirrelsAcornGoldenAcorn,
    ],

    RegionName.CAGPGeyser: [
        LocationName.GeyserMinersSkull,
    ],

    RegionName.CAMA: [
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
        
    ],

    RegionName.CAMALev: [
        LocationName.ParkingLotHistoryBoardCard,
    ],

    RegionName.CAKC: [
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
    ],

    RegionName.CAKCLev: [
        LocationName.HighUpTightropeCard,
    ],

    RegionName.CAKCPyro: [
        LocationName.CaveRefrigeratorTurkeySandwich,
    ],

    RegionName.CARE: [
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
    ],

    RegionName.CARELev: [
        LocationName.FireplaceTreeTopDinosaurBone, 
    ],

    RegionName.CAREMark: [
        LocationName.HornetNestFertilityIdol,
    ],

    RegionName.CABH: [
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
    ],

    RegionName.CABHLev: [
        LocationName.TopofBigRockChallengeMarker, 
    ],

    RegionName.CALI: [
        LocationName.MainLodgeRaftersVoodooDoll,
    ],

    RegionName.CAJA: [
        LocationName.TopofSanctuaryCard, 
        LocationName.BottomofSanctuaryCard, 
    ],

    RegionName.RANK5to15: [
        LocationName.PSIRank05, 
        LocationName.PSIRank10, 
        LocationName.PSIRank15, 
        
    ],

    RegionName.RANK20to101: [
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
    ],

    RegionName.ASGR: [
        LocationName.RockWallBottom, 
        LocationName.RockWallLadder, 
        LocationName.OutsideFrontGate, 
        LocationName.FountainTop, 
        LocationName.HedgeAlcove, 
        LocationName.AsylumDoorsRight, 
        LocationName.AsylumDoorsLeft, 
        LocationName.CornerNearFence, 
        LocationName.LedgeBeforeGloria,
    ],

    RegionName.ASGRLev: [
        LocationName.PillarAboveGate, 
    ],

    RegionName.ASCO: [
        LocationName.AboveElevator, 
        LocationName.CrowsBasket, 
        LocationName.LedgeAboveFredLeft, 
        LocationName.LedgeAboveFredRight, 
        LocationName.LedgeOppositeElevator, 
        LocationName.EdgarsRoom, 
        LocationName.BehindElevator, 
        LocationName.JunkCorner, 
    ],

    RegionName.ASCOLev: [
        LocationName.AboveEdgar,
    ],

    RegionName.ASUP: [
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
        
    ],

    RegionName.ASUPTele: [
        LocationName.RoomOppositeChairDoor, 
        LocationName.PipeSlideNearChairDoor, 
        LocationName.RaftersAboveChairDoor,
    ],

    RegionName.ASLB: [
        LocationName.LabCagedCrowLeft, 
        LocationName.LabCagedCrowRight, 
        LocationName.NextToPokeylope, 
        LocationName.LabTopRailingLeft1, 
        LocationName.LabTopRailingLeft2,
        LocationName.LabTopElevator, 
        LocationName.LabTopRailingRight, 
        LocationName.TeaRoom, 
    ],

    RegionName.BBA1: [
        LocationName.JumpingTutorial1, 
        LocationName.JumpingTutorial2, 
        LocationName.PoleClimbingTutorialFloor, 
        LocationName.BelowTheTripleTrampolines,
    ],

    RegionName.BBA2: [
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
    ],

    RegionName.BBA2Duster: [
        LocationName.TrapezeCobweb, 
    ],

    RegionName.SACU: [
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
    ],

    RegionName.SACULev: [
        LocationName.RoundPlatformsFarFromValve, 
    ],

    RegionName.MIFL: [
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
    ],
    
    RegionName.NIMP: [
        LocationName.OutsideCaravan, 
        LocationName.BehindTheEgg, 
        LocationName.ShadowMonsterPath, 
        
    ],
    
    RegionName.NIMPMark: [
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
    ],
    
    RegionName.NIBA: [
        LocationName.BrainTumblerExperimentComplete, 
    ],
    
    RegionName.LOMA: [
        LocationName.SkyscraperStart, 
        LocationName.CornerNearJail, 
        LocationName.SkyscraperBeforeDam, 
        
    ],
    
    RegionName.LOMAShield: [
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
    ],
    
    RegionName.MMI1Fridge: [
        LocationName.BoydsFridgeClv, 
    ],
    
    RegionName.MMI1BeforeSign: [
        LocationName.FirstHouseDufflebagTag, 
        LocationName.SecondHouseRollingPin, 
        LocationName.CarTrunk1StopSign, 
    ],

    RegionName.MMI1AfterSign: [
        LocationName.RoofAfterRoadCrewPurseTag, 
        LocationName.CarTrunk2HedgeTrimmers, 
        LocationName.CarHouseBackyardSteamertrunkTag,
        LocationName.GraveyardPatioVault, 
        LocationName.GraveyardBehindTreeOneUp, 
        LocationName.BehindGraveyardDufflebag, 
        LocationName.HedgeMazeFlowers, 
        LocationName.CarTrunk3WateringCan, 
        LocationName.PostOfficeRoofOneUp, 
    ],

    RegionName.MMI1Hedgetrimmers: [
        LocationName.LandscapersHouseBackyardSuitcaseTag, 
        LocationName.LandscapersHouseTablePurse, 
    ],

    RegionName.MMI1RollingPin: [
        LocationName.LandscapersHouseKitchenAmmoUp, 
    ],

    RegionName.MMI1Powerlines: [
        LocationName.PowerlineIslandSandboxHatboxTag, 
        LocationName.PowerlineIslandLeftMemoryVault, 
        LocationName.PowerlineIslandRightMaxLives, 
    ],

    RegionName.MMI1Duster: [
        LocationName.InsideWebbedGarageHatbox,
        LocationName.PostOfficeLobbySuitcase, 
        LocationName.PostOfficeBasementPlunger, 
    ],

    RegionName.MMI2: [
        LocationName.BehindBookDepositorySteamerTrunk,  
    ],

    RegionName.MMDM: [
        LocationName.MilkmanComplete, 
    ],

    RegionName.THMS: [
        LocationName.NearTheCriticPurse, 
        LocationName.BelowTheSpotlightSteamertrunkTag, 
        LocationName.BehindStagePurseTag, 
         
    ],

    RegionName.THMSLev: [
        LocationName.InTheAudienceAmmoUp, 
    ],

    RegionName.THMSDuster: [
        LocationName.BehindStageCobwebSuitcase, 
    ],

    RegionName.THMSStorage: [
        LocationName.StorageRoomFloorVault, 
        LocationName.StorageRoomLeftSteamertrunk, 
        LocationName.StorageRoomRightLowerSuitcaseTag, 
        LocationName.StorageRoomRightUpperCandle1, 
        LocationName.BonitasRoom, 
    ],

    RegionName.THCW: [
        LocationName.DoghouseSlicersDufflebagTag, 
        LocationName.BigPlatform1Hatbox, 
        LocationName.BigPlatform2Vault, 
        LocationName.BigPlatform3OneUp, 
        LocationName.BigPlatformAboveHatboxTag, 
        LocationName.NextToOatmealDufflebag, 
        LocationName.CandleBasketCandle2, 
        LocationName.CurtainSlideConfusionAmmoUp, 
    ],

    RegionName.THFB: [
        LocationName.GloriasTheaterComplete,
    ],

    RegionName.WWMA: [
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
    ],

    RegionName.WWMALev: [
        LocationName.TopOfVillager3sHouseAmmoUp, 
        LocationName.TopOfKnightsHouseConfusionAmmoUp, 
    ],

    RegionName.WWMACarpRoof: [
        LocationName.CarpentersRoofVault,
        LocationName.TightropeRoomDufflebag, 
    ],

    RegionName.WWMADuster: [
        LocationName.UnderTheGuillotineSuitcase, 
        LocationName.FredsHouseBasementHatbox, 
        LocationName.BlacksmithsLeftBuildingPurse, 
    ],

    RegionName.WWMADusterLev: [
        LocationName.BlacksmithsRightBuildingSteamertrunkTag, 
    ],

    RegionName.WWMADusterLevPyro: [
        LocationName.BlacksmithsHaybaleTheMusket, 
    ],

    RegionName.WWMAV1: [
        LocationName.HelpVillager1, 
    ],

    RegionName.WWMAKnight: [
        LocationName.HelpTheKnight, 
    ],

    RegionName.WWMAV2: [
        LocationName.HelpVillager2, 
    ],

    RegionName.WWMAV3: [
        LocationName.HelpVillager3,
        LocationName.WaterlooWorldComplete, 
    ],

    RegionName.BVRB: [
        LocationName.ClubStreetLadySteamertrunk, 
    ],

    RegionName.BVRBLev: [
        LocationName.ClubStreetMetalBalconyDufflebagTag, 
        LocationName.HeartStreetHIGHBalconyAmmoUp,
    ],

    RegionName.BVRBTele: [
        LocationName.ClubStreetGatedSteamerTrunkTag, 
    ],

    RegionName.BVRBDuster: [
        LocationName.AlleywaysLedgeHatboxTag, 
        LocationName.SewersMainVault,
        LocationName.NearDiegosHouseMaxLives, 
        LocationName.DiegosBedSuitcaseTag, 
        LocationName.DiegosRoomHatbox, 
        LocationName.DiegosHouseGrindrailSuitcase, 
        LocationName.GrindrailBalconyConfusionAmmoUp,
    ],

    RegionName.BVRBGarden: [
        LocationName.TheGardenVault, 
    ],

    RegionName.BVRBLogs: [
        LocationName.BurnTheLogsDufflebag, 
    ],

    RegionName.BVES: [
        LocationName.SanctuaryGroundPurse, 
        LocationName.TigerWrestler, 
        LocationName.DragonWrestler,
    ],

    RegionName.BVESLev: [
        LocationName.SanctuaryBalconyPurseTag, 
    ],

    RegionName.BVESEagle: [
        LocationName.EagleWrestler, 
    ],

    RegionName.BVESCobra: [
        LocationName.CobraWrestler, 
    ],

    RegionName.BVESBoss: [
        LocationName.BlackVelvetopiaComplete, 
    ],

    RegionName.MCTC: [
        LocationName.EntranceAwningSteamertrunkTag, 
        LocationName.CrumblingPathSteamertrunk, 
        LocationName.CrumblingPathEndRightHatboxTag, 
        LocationName.CrumblingPathEndLeftConfusionAmmoUp, 
    ],

    RegionName.MCTCEscort: [
        LocationName.OllieEscortFloorSuitcaseTag, 
        LocationName.OllieEscortMiddleHatbox, 
        LocationName.OllieEscortTopLeftVault, 
        LocationName.OllieEscortTopRightPurseTag, 
        LocationName.TunnelOfLoveStartPurse, 
        LocationName.TunnelOfLoveCornerSuitcase, 
        LocationName.TunnelOfLoveRailDufflebagTag, 
        LocationName.NextToTheFatLadyDufflebag,
    ],

    RegionName.MCTCBoss: [
        LocationName.FinalBossEvent,
    ],

    # should only have an item if Cobweb Duster vanilla
    #RegionName.FordShop: [
    #    LocationName.ShopCobwebDuster, 
    #],

    # RegionName.DUMMYLOCATIONS
        # NOT COLLECTIBLE
    #    LocationName.DUMMYLOCATION1NOTCOLLECTIBLE, 
    #    LocationName.DUMMYLOCATION2NOTCOLLECTIBLE, 
    #    LocationName.DUMMYLOCATION3NOTCOLLECTIBLE, 

}

def connect_regions(self):
    multiworld = self.multiworld
    player = self.player
    # connecting every first visit to the GoA
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

        RegionName.ASCO: {RegionName.ASUP, RegionName.ASUPTele, },

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

def create_regions(self):

    multiworld = self.multiworld
    player = self.player
    active_locations = self.location_name_to_id

    # REPLACE create_region TO ACTUALLY WORK
    multiworld.regions += [create_region(multiworld, player, self.location_name_to_id, region, locations) for region, locations in
                        PSYREGIONS.items()]

