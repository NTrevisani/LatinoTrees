import FWCore.ParameterSet.Config as cms
import os
#from WWAnalysis.AnalysisStep.wwMuons_cfi import Scenario6_ICHEP2012,Scenario2_KINK_MUONS,Scenario1_LP_MUONS
#from WWAnalysis.AnalysisStep.wwElectrons_cfi import Scenario6_ICHEP,Scenario4_BDT_ELECTRONS,Scenario3_LH_ELECTRONS,Scenario2_LP_ELECTRONS,Scenario1_LP_ELECTRONS

# NB: typedef ObjectMultiplicityCounter<reco::Vertex>    VertexMultiplicityCounter;
nverticesModule = cms.EDProducer("VertexMultiplicityCounter",
    probes = cms.InputTag("REPLACE_ME"),
    objects = cms.InputTag("offlineSlimmedPrimaryVertices"), # miniAOD goodPrimaryVertices
    objectSelection = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
)



# option for PhilJetid
# 4 possible workingpoints
# jetId_WP
# 0 NONE no requirement
# 1 OLD Simple Jet ID
# 2 DZ ID (Not implemented ! )
# 3 HGG CutBased (Not implemented ! )
# 4 MVA LOOSE
# 5 MVA MEDIUM
# 6 MVA TIGHT
# 7 Run II jetID LOOSE
# 8 Run II jetID TIGHT

#jetId_WP="4" ----> FIXME: to be used!
#jetId_WP="0"
#jetId_WP = "7"
# -> DON'T define this here, since it is defined in "stepB.py"

import LatinoTrees.AnalysisStep.globalVariables as globalVariables
jetId_WP = globalVariables.jetId_WP


# JetCuts

CJVminPt = "30."
CJVmaxEta = "4.7"
DphiJetVetominPt = "15."
DphiJetVetominEta = "4.7"

DzBVeto="999999.9"
minPtBVeto="10.0"


stepBTree = cms.EDFilter("GenericTreeProducer",
    src = cms.InputTag(""),
    maxVectorsLength = cms.int32(10),
#stepBTree = cms.EDFilter("ProbeTreeProducer",
# cut = cms.string("q(0)*q(1) > 0 && !isSTA(0) && !isSTA(1) && "+
    #cut = cms.string("q(0)*q(1) < 0 && !isSTA(0) && !isSTA(1) && "+
    cut = cms.string(
                     "1"  
                     #"!isSTA(0) && !isSTA(1) && "+
                     #"leptEtaCut(2.4,2.5) && ptMax > 17 && ptMin > 8"
                     
# previously ...
# "leptEtaCut(2.4,2.5) && ptMax > 20 && ptMin > 10"
# " && triggerMatchingCut('DATASET')"
# "nExtraLep(10) == 0 "
# +" && passesIP"
# +(" && triggerMatchingCut('DATASET')")
    ),
    variables = cms.PSet(
        #hypo = cms.string("hypo()"),
        #lepton1_pt = cms.string("lepton(0).x()"),
        channel = cms.string("channel()"),
        v_lepton1 = cms.string("lepton(0)"),
        v_lepton2 = cms.string("lepton(1)"),
        v_lepton3 = cms.string("lepton(2)"),
        v_lepton4 = cms.string("lepton(3)"),

        v_jet1 = cms.string("jet(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        v_jet2 = cms.string("jet(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        v_jet3 = cms.string("jet(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        v_jet4 = cms.string("jet(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),

        #std_variable_vector_lepton_pt_max3 = cms.string("ptByPt/3"),
        #std_vector_lepton_pt_max3          = cms.string("ptByPt/3"),

        std_vector_lepton_pt           = cms.string("ptByPt"),
        std_vector_lepton_eta          = cms.string("etaByPt"),
        std_vector_lepton_phi          = cms.string("phiByPt"),
        std_vector_lepton_flavour      = cms.string("flavourByPt"),
        std_vector_lepton_isMediumMuon = cms.string("isMediumMuonByPt"),
        std_vector_lepton_isTightMuon  = cms.string("isTightMuonByPt"),
        std_vector_lepton_muSIP3D      = cms.string("muSIP3DByPt"),
        std_vector_lepton_elSIP3D      = cms.string("elSIP3DByPt"),

        std_vector_lepton_id           = cms.string("pdgIdByPt"),

        std_vector_puppijet_pt  = cms.string("leadingSecondJetPt"),
        std_vector_puppijet_eta = cms.string("leadingSecondJetEta"),
        std_vector_puppijet_phi = cms.string("leadingSecondJetPhi"),

        std_vector_jet_pt  = cms.string("leadingJetPt"),
        std_vector_jet_eta = cms.string("leadingJetEta"),
        std_vector_jet_phi = cms.string("leadingJetPhi"),

        mll = cms.string("mll()"),
        ptll = cms.string("pTll()"),
        yll = cms.string("yll()"), #fixed! returns (p4a+p4b).Rapidity()
        pt1 = cms.string("ptMax"),
        pt2 = cms.string("ptMin"),
        pt3 = cms.string("ptByPt(2)"),
        pt4 = cms.string("ptByPt(3)"),
        
        #isTightMuon1 = cms.string("isTightMuon(0)"),
        #isTightMuon2 = cms.string("isTightMuon(1)"),
        #isTightMuon3 = cms.string("isTightMuon(2)"),
        #isTightMuon4 = cms.string("isTightMuon(3)"),
        
        #isSTA1 = cms.string("isSTAByPt(0)"),
        #isSTA2 = cms.string("isSTAByPt(1)"),
        #isSTA3 = cms.string("isSTAByPt(2)"),
        #isSTA4 = cms.string("isSTAByPt(3)"),
        peaking = cms.string("peaking"),
        trigger = cms.string("guillelmoTrigger('DATASET')"),
        nextra = cms.string("nExtraLep(10)"),
        pfRawMet = cms.string("pfRawMet"),
        pfRawSumEt = cms.string("pfRawSumEt"),
        pfRawMetPhi = cms.string("pfRawMetPhi"),
        pfType1Met = cms.string("pfType1Met"),
        pfType1SumEt = cms.string("pfType1SumEt"),
        pfType1Metup = cms.string("pfType1MetUp"),
        pfType1Metdn = cms.string("pfType1MetDn"),
        pfType1Metphi = cms.string("pfType1MetPhi"),
        ppfMet = cms.string("projPfMet"),
        pupMet = cms.string("pupMet"),
        trkMet = cms.string("trkMet"),
# mvamet = cms.string("mvaMet"),
# mvamethi = cms.string("mvaMetPhi"),
# pmvamet = cms.string("projMvaMet"),
        chSumEt = cms.string("chargedMetSmurfSumEt"),
        pfmetMEtSig = cms.string("pfMetMEtSig"),
        pfmetSignificance = cms.string("pfMetSignificance"),
        chmet = cms.string("chargedMetSmurf"),
        chmetphi = cms.string("chargedMetSmurfPhi"),
        pchmet = cms.string("projChargedMetSmurf"),
        dymva0 = cms.string("userFloat('dymva0')"),
        dymva1 = cms.string("userFloat('dymva1')"),
        redmet = cms.string("-9999"),
        predmet = cms.string("-9999"),
        mpmet = cms.string("min(projPfMet,projChargedMetSmurf)"), ##note: min of proj and proj of min are not the same
        imet = cms.string("min(projPfMet,projChargedMetSmurf)*cos(pfRawMetPhi-chargedMetSmurfPhi)"),
        dphill = cms.string("dPhill()"),
        drll = cms.string("dRll()"),
        dphilljet = cms.string("dPhillLeadingJet("+CJVmaxEta+",1,"+jetId_WP+")"),
        dphilljetjet = cms.string("dPhilljetjet("+CJVmaxEta+",1,"+jetId_WP+")"), #WHAT
        dphillmet = cms.string("dPhillMet('PFMET')"),
        dphilmet = cms.string("dPhilMet('PFMET')"),
        dphilmet1 = cms.string("dPhilMetByPt(0,'PFMET')"),
        dphilmet2 = cms.string("dPhilMetByPt(1,'PFMET')"),
        mtw1 = cms.string("mTByPt(0,'PFMET')"),
        mtw2 = cms.string("mTByPt(1,'PFMET')"),
        mth = cms.string("mTHiggs('PFMET')"),
        gammaMRStar = cms.string("gammaMRStar"),
        njet = cms.string("nCentralJets("+CJVminPt+","+CJVmaxEta+",1,"+jetId_WP+")"),
        njetid = cms.string("nCentralJets("+CJVminPt+","+CJVmaxEta+",1,0)"),
        # here we do apply a dz cut cause we are actually counting bjets
        nbjettche = cms.string("bTaggedJetsOver("+CJVminPt+",2.1,'pfTrackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+")"),
        nbjet     = cms.string("bTaggedJetsOver("+CJVminPt+",1.05,'pfJetBProbabilityBJetTags',"+jetId_WP+","+DzBVeto+")"),
        # here we don't apply the dz cut, cause we just use the b-tag value of highest pt jets

        puppijetpt1 = cms.string("leadingSecondJetPt(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
       
        jetpt1 = cms.string("leadingJetPt(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jeteta1 = cms.string("leadingJetEta(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetphi1 = cms.string("leadingJetPhi(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetmass1 = cms.string("leadingJetMass(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetid1 = cms.string("leadingJetId(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetmva1 = cms.string("leadingJetMva(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetbjpb1 = cms.string("leadingJetBtag(0,'pfJetBProbabilityBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jettche1 = cms.string("leadingJetBtag(0,'pfTrackCountingHighEffBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jettchp1 = cms.string("leadingJetBtag(0,'pfTrackCountingHighPurBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jetptd1 = cms.string("leadingJetPtd(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetCHM1 = cms.string("leadingJetChargedHadronMultiplicity(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNHM1 = cms.string("leadingJetNeutralHadronMultiplicity(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetPhM1 = cms.string("leadingJetPhotonMultiplicity(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNChgQC1 = cms.string("leadingJetNChgQC(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNChgptCut1 = cms.string("leadingJetNChgptCut(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNNeutralptCut1 = cms.string("leadingJetNNeutralptCut(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),

        jetpt2 = cms.string("leadingJetPt(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jeteta2 = cms.string("leadingJetEta(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetphi2 = cms.string("leadingJetPhi(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetmass2 = cms.string("leadingJetMass(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetid2 = cms.string("leadingJetId(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetmva2 = cms.string("leadingJetMva(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jettche2 = cms.string("leadingJetBtag(1,'pfTrackCountingHighEffBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jetbjpb2 = cms.string("leadingJetBtag(1,'pfJetBProbabilityBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jettchp2 = cms.string("leadingJetBtag(1,'pfTrackCountingHighPurBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jetptd2 = cms.string("leadingJetPtd(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetCHM2 = cms.string("leadingJetChargedHadronMultiplicity(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNHM2 = cms.string("leadingJetNeutralHadronMultiplicity(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetPhM2 = cms.string("leadingJetPhotonMultiplicity(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNChgQC2 = cms.string("leadingJetNChgQC(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNChgptCut2 = cms.string("leadingJetNChgptCut(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNNeutralptCut2 = cms.string("leadingJetNNeutralptCut(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),

        jetpt3 = cms.string("leadingJetPt(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jeteta3 = cms.string("leadingJetEta(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetphi3 = cms.string("leadingJetPhi(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetmass3 = cms.string("leadingJetMass(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetid3 = cms.string("leadingJetId(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetmva3 = cms.string("leadingJetMva(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jettche3 = cms.string("leadingJetBtag(2,'pfTrackCountingHighEffBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jetbjpb3 = cms.string("leadingJetBtag(2,'pfJetBProbabilityBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jettchp3 = cms.string("leadingJetBtag(2,'pfTrackCountingHighPurBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jetptd3 = cms.string("leadingJetPtd(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetCHM3 = cms.string("leadingJetChargedHadronMultiplicity(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNHM3 = cms.string("leadingJetNeutralHadronMultiplicity(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetPhM3 = cms.string("leadingJetPhotonMultiplicity(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNChgQC3 = cms.string("leadingJetNChgQC(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNChgptCut3 = cms.string("leadingJetNChgptCut(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNNeutralptCut3 = cms.string("leadingJetNNeutralptCut(2,0,"+CJVmaxEta+",1,"+jetId_WP+")"),

        jetpt4 = cms.string("leadingJetPt(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jeteta4 = cms.string("leadingJetEta(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetphi4 = cms.string("leadingJetPhi(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetmass4 = cms.string("leadingJetMass(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetid4 = cms.string("leadingJetId(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetmva4 = cms.string("leadingJetMva(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jettche4 = cms.string("leadingJetBtag(3,'pfTrackCountingHighEffBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jetbjpb4 = cms.string("leadingJetBtag(3,'pfJetBProbabilityBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jettchp4 = cms.string("leadingJetBtag(3,'pfTrackCountingHighPurBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")"),
        jetptd4 = cms.string("leadingJetPtd(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetCHM4 = cms.string("leadingJetChargedHadronMultiplicity(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNHM4 = cms.string("leadingJetNeutralHadronMultiplicity(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetPhM4 = cms.string("leadingJetPhotonMultiplicity(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNChgQC4 = cms.string("leadingJetNChgQC(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNChgptCut4 = cms.string("leadingJetNChgptCut(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        jetNNeutralptCut4 = cms.string("leadingJetNNeutralptCut(3,0,"+CJVmaxEta+",1,"+jetId_WP+")"),


        jetRho = cms.string("getJetRhoIso()"),
        iso1 = cms.string("allIsoByPt(0)/ptByPt(0)"),
        iso2 = cms.string("allIsoByPt(1)/ptByPt(1)"),
        iso3 = cms.string("allIsoByPt(2)/ptByPt(2)"),
        iso4 = cms.string("allIsoByPt(3)/ptByPt(3)"),
        eta1 = cms.string("etaByPt(0)"),
        eta2 = cms.string("etaByPt(1)"),
        eta3 = cms.string("etaByPt(2)"),
        eta4 = cms.string("etaByPt(3)"),
        sceta1 = cms.string("etaSCByPt(0)"),
        sceta2 = cms.string("etaSCByPt(1)"),
        sceta3 = cms.string("etaSCByPt(2)"),
        sceta4 = cms.string("etaSCByPt(3)"),
        phi1 = cms.string("phiByPt(0)"),
        phi2 = cms.string("phiByPt(1)"),
        phi3 = cms.string("phiByPt(2)"),
        phi4 = cms.string("phiByPt(3)"),
        ch1 = cms.string("qByPt(0)"),
        ch2 = cms.string("qByPt(1)"),
        ch3 = cms.string("qByPt(2)"),
        ch4 = cms.string("qByPt(3)"),
        bdt1 = cms.string("leptBdtByPt(0)"),
        bdt2 = cms.string("leptBdtByPt(1)"),
        bdt3 = cms.string("leptBdtByPt(2)"),
        bdt4 = cms.string("leptBdtByPt(3)"),
        lh1 = cms.string("leptLHByPt(0)"),
        lh2 = cms.string("leptLHByPt(1)"),
        lh3 = cms.string("leptLHByPt(2)"),
        lh4 = cms.string("leptLHByPt(3)"),

        eleIdVeto1   = cms.string("leptIdByPt(\"egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-veto\",\"\",0)"),
        eleIdLoose1  = cms.string("leptIdByPt(\"egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-loose\",\"\",0)"),
        eleIdMedium1 = cms.string("leptIdByPt(\"egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-medium\",\"\",0)"),
        eleIdTight1  = cms.string("leptIdByPt(\"egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-tight\",\"\",0)"),

        std_vector_lepton_eleIdVeto   = cms.string("leptIdByPt('egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-veto',''"),
        std_vector_lepton_eleIdLoose  = cms.string("leptIdByPt(\"egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-loose\",\"\""),
        std_vector_lepton_eleIdMedium = cms.string("leptIdByPt(\"egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-medium\",\"\""),
        std_vector_lepton_eleIdTight  = cms.string("leptIdByPt(\"egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-tight\",\"\""),

        pdgid1 = cms.string("pdgIdByPt(0)"),
        pdgid2 = cms.string("pdgIdByPt(1)"),
        pdgid3 = cms.string("pdgIdByPt(2)"),
        pdgid4 = cms.string("pdgIdByPt(3)"),

        nbrem1 = cms.string("nBremByPt(0)"),
        nbrem2 = cms.string("nBremByPt(1)"),
        nbrem3 = cms.string("nBremByPt(2)"),
        nbrem4 = cms.string("nBremByPt(3)"),
        isomva1 = cms.string("mvaIsoByPt(0)"),
        isomva2 = cms.string("mvaIsoByPt(1)"),
        isomva3 = cms.string("mvaIsoByPt(2)"),
        isomva4 = cms.string("mvaIsoByPt(3)"),
        # in the 2012 selection, 2 BJet algorithms are used: softtche and hardbjpb !
        # softbdisc = cms.string("highestBDiscRange(10.0,30.0,'pfTrackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+")"),
        # hardbdisc = cms.string("highestBDiscRange(30.0,999999.,'pfJetBProbabilityBJetTags',"+jetId_WP+","+DzBVeto+",1)"),
        softtche = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+" ,'pfTrackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+")"),
        hardtche = cms.string("highestBDiscRange("+CJVminPt+",999999.,'pfTrackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+",1)"),
        softbjpb = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+" ,'pfJetBProbabilityBJetTags',"+jetId_WP+","+DzBVeto+")"),
        hardbjpb = cms.string("highestBDiscRange("+CJVminPt+",999999.,'pfJetBProbabilityBJetTags',"+jetId_WP+","+DzBVeto+",1)"),
        tightmu = cms.string("passesSmurfMuonID"),
        worstJetLepPt = cms.string("max(matchedJetPt(0, 0.5)/pt(0), matchedJetPt(1, 0.5)/pt(1))"),
        dataset = cms.string("REPLACE_ME"),
        #puAW = cms.InputTag("puWeightA"),  # miniAOD
        #puBW = cms.InputTag("puWeightB"),  # miniAOD
        #puW = cms.InputTag("puWeight"),  # miniAOD
        puW = cms.string("1"),
        kfW = cms.string("1"),
        #kfW = cms.InputTag("ptWeight"),
        baseW = cms.string("REPLACE_ME"),
        #fourW = cms.string("REPLACE_ME"),
        #fermiW = cms.string("REPLACE_ME"),

        trpu = cms.InputTag("nPU:tr"),
        itpu = cms.InputTag("nPU:it"),
        ootpup1 = cms.InputTag("nPU:p1"),
        ootpum1 = cms.InputTag("nPU:m1"),


        effAW = cms.string("1"),
        effBW = cms.string("1"),
        effW = cms.string("1"),
        triggAW = cms.string("1"),
        triggBW = cms.string("1"),
        triggW = cms.string("1"),
        fakeAW = cms.string("1"),
        fakeBW = cms.string("1"),
        fakeW = cms.string("1"),
        #vbf stuff:
        njetvbf = cms.string("nJetVBF(30,"+CJVmaxEta+",1,"+jetId_WP+")"),
        mjj = cms.string("mjj(0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        detajj = cms.string("dEtajj(30,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetpt1 = cms.string("leadingVBFJetPt(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjeteta1 = cms.string("leadingVBFJetEta(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetphi1 = cms.string("leadingVBFJetPhi(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetid1 = cms.string("leadingVBFJetId(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetmva1 = cms.string("leadingVBFJetMva(0,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetpt2 = cms.string("leadingVBFJetPt(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjeteta2 = cms.string("leadingVBFJetEta(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetphi2 = cms.string("leadingVBFJetPhi(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetid2 = cms.string("leadingVBFJetId(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        cjetmva2 = cms.string("leadingVBFJetMva(1,0,"+CJVmaxEta+",1,"+jetId_WP+")"),
        # mc info
        mctruth = cms.string("-1"),

    ),
    flags = cms.PSet(
        #sameflav = cms.string("hypo == 3 || hypo == 6"),
        #zveto = cms.string("abs(mll-91.1876)>15. || hypo == 4 || hypo == 5"),
        # here we do apply a dz cut cause we are actually counting bjets
        bveto_ip       = cms.string("bTaggedJetsBetween(10,30,2.1,'pfTrackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+") == 0"),
        # bveto          = cms.string("bTaggedJetsBetween(10,30,2.1,'pfTrackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+") == 0 && nSoftMu(3) == 0"),
        # bveto_nj       = cms.string("bTaggedJetsBetween(10,30,2.1,'pfTrackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+") == 0 && nSoftMu(3,1) == 0"),
        # bveto_nj30     = cms.string("bTaggedJetsBetween(10,30,2.1,'pfTrackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+") == 0 && nSoftMu(3,30) == 0"),
        # bveto_nj05     = cms.string("bTaggedJetsBetween(10,30,2.1,'pfTrackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+") == 0 && nSoftMu(3,1,0.5) == 0"),
        # bveto_nj3005   = cms.string("bTaggedJetsBetween(10,30,2.1,'pfTrackCountingHighEffBJetTags',"+jetId_WP+","+DzBVeto+") == 0 && nSoftMu(3,30,0.5) == 0"),
        # bveto_mu       = cms.string("nSoftMu(3) == 0"),
        # bveto_munj     = cms.string("nSoftMu(3,1) == 0"),
        # bveto_munj30   = cms.string("nSoftMu(3,30) == 0"),
        # bveto_munj05   = cms.string("nSoftMu(3,1,0.5) == 0"),
        # bveto_munj3005 = cms.string("nSoftMu(3,30,0.5) == 0"),
        dphiveto       = cms.string("passesDPhillJet("+DphiJetVetominPt+","+DphiJetVetominEta+",1,"+jetId_WP+")"),
        #pass2012ICHEP1 = cms.string('passCustomByPt(0,"'+Scenario6_ICHEP2012+'","'+Scenario6_ICHEP+'")'),
        #pass2012ICHEP2 = cms.string('passCustomByPt(1,"'+Scenario6_ICHEP2012+'","'+Scenario6_ICHEP+'")'),
        #pass2012ICHEP3 = cms.string('passCustomByPt(2,"'+Scenario6_ICHEP2012+'","'+Scenario6_ICHEP+'")'),
        #pass2012ICHEP4 = cms.string('passCustomByPt(3,"'+Scenario6_ICHEP2012+'","'+Scenario6_ICHEP+'")'),

# passBDT1 = cms.string('passCustomByPt(0,"'+Scenario2_KINK_MUONS+'","'+Scenario4_BDT_ELECTRONS+'")'),
# passBDT2 = cms.string('passCustomByPt(1,"'+Scenario2_KINK_MUONS+'","'+Scenario4_BDT_ELECTRONS+'")'),
# passLH1 = cms.string('passCustomByPt(0,"'+Scenario2_KINK_MUONS+'","'+Scenario3_LH_ELECTRONS+ '")'),
# passLH2 = cms.string('passCustomByPt(1,"'+Scenario2_KINK_MUONS+'","'+Scenario3_LH_ELECTRONS+ '")'),
# passCB1 = cms.string('passCustomByPt(0,"'+Scenario2_KINK_MUONS+'","'+Scenario2_LP_ELECTRONS+ '")'),
# passCB2 = cms.string('passCustomByPt(1,"'+Scenario2_KINK_MUONS+'","'+Scenario2_LP_ELECTRONS+ '")'),
# passCBOld1 = cms.string('passCustomByPt(0,"'+Scenario1_LP_MUONS +'","'+Scenario1_LP_ELECTRONS+ '")'),
# passCBOld2 = cms.string('passCustomByPt(1,"'+Scenario1_LP_MUONS +'","'+Scenario1_LP_ELECTRONS+ '")'),
# WRONG FOR 2012 SELECTION
# passWW = cms.string("guillelmoTrigger('DATASET') && pfMet > 20 && mll()>20 && (abs(mll-91.1876)>15 || hypo == 4 || hypo == 5) && min(projPfMet,projChargedMetSmurf) && nCentralJets(30,4.7) && (passesDPhillJet||!sameflav) && bTaggedJetsBetween(10,30,2.1,'pfTrackCountingHighEffBJetTags',2.0) == 0 && nSoftMu(3) == 0 && nExtraLep(10)"),

    ),
    addRunLumiInfo = cms.bool(True)
)









def addMuonIdIsoVariables(process,pt):
    if hasattr(pt,"variables"):      
        setattr(pt.variables, "std_vector_lepton_NValidHitsInTrk",      cms.string("muNValidHitsInTrkByPt")),
        setattr(pt.variables, "std_vector_lepton_NValidFractInTrk",     cms.string("muNValidFractInTrkByPt")),
        setattr(pt.variables, "std_vector_lepton_NormChi2GTrk",         cms.string("muNormChi2GTrkByPt")),
        setattr(pt.variables, "std_vector_lepton_NValidHitsSATrk",      cms.string("muNValidHitsSATrkByPt")),
        setattr(pt.variables, "std_vector_lepton_NumOfMatchedStations", cms.string("muNumOfMatchedStationsByPt")),
        setattr(pt.variables, "std_vector_lepton_BestTrackdz",          cms.string("muBestTrackdzByPt")),
        setattr(pt.variables, "std_vector_lepton_BestTrackdxy",         cms.string("muBestTrackdxyByPt")),
        setattr(pt.variables, "std_vector_lepton_NValidPixelHitsInTrk", cms.string("muNValidPixelHitsInTrkByPt")),
        setattr(pt.variables, "std_vector_lepton_NTkLayers",            cms.string("muNTkLayersByPt")),
        setattr(pt.variables, "std_vector_lepton_TrkKink",              cms.string("muTrkKinkByPt")),
        setattr(pt.variables, "std_vector_lepton_Chi2LocalPos",         cms.string("muChi2LocalPosByPt")), 
        setattr(pt.variables, "std_vector_lepton_SegCompatibilty",      cms.string("muSegCompatibiltyByPt")),
        setattr(pt.variables, "std_vector_lepton_chargedHadronIso",     cms.string("chargedHadronIsoByPt")),
        setattr(pt.variables, "std_vector_lepton_chargedParticleIso",   cms.string("chargedParticleIsoByPt")),
        setattr(pt.variables, "std_vector_lepton_neutralHadronIso",     cms.string("neutralHadronIsoByPt")),
        setattr(pt.variables, "std_vector_lepton_photonIso",            cms.string("photonIsoByPt")),
        setattr(pt.variables, "std_vector_lepton_sumPUPt",              cms.string("sumPUPtByPt")),
 
    else:
        raise RuntimeError, "In addMuonIdIsoVariables, %s doesn't look like a ProbeTreeProducer object, it has no 'variables' attribute." % pt


def addEleIdIsoVariables(process,pt):
    if hasattr(pt,"variables"):      
        setattr(pt.variables, "std_vector_electron_dEtaIn" ,                  cms.string("deltaEtaSuperClusterTrackAtVtxByPt")),
        setattr(pt.variables, "std_vector_electron_dPhiIn" ,                  cms.string("deltaPhiSuperClusterTrackAtVtxByPt")),
        setattr(pt.variables, "std_vector_electron_full5x5_sigmaIetaIeta",    cms.string("full5x5_sigmaIetaIetaByPt")),
        setattr(pt.variables, "std_vector_electron_hOverE" ,                  cms.string("hcalOverEcalByPt")),
        setattr(pt.variables, "std_vector_electron_d0",                       cms.string("d0ByPt")),
        setattr(pt.variables, "std_vector_electron_dz",                       cms.string("dzByPt")),
        setattr(pt.variables, "std_vector_electron_ooEmooP",                  cms.string("ooEmooPByPt")),
        setattr(pt.variables, "std_vector_electron_effectiveArea",            cms.string("GetElectronEffectiveAreaByPt")),
        setattr(pt.variables, "std_vector_electron_scEta",                    cms.string("etaSCByPt")),
        setattr(pt.variables, "std_vector_electron_expectedMissingInnerHits", cms.string("expectedMissingInnerHitsByPt")),
        setattr(pt.variables, "std_vector_electron_passConversionVeto",       cms.string("passConversionVetoByPt")),
    else:
        raise RuntimeError, "In addEleIdIsoVariables, %s doesn't look like a ProbeTreeProducer object, it has no 'variables' attribute." % pt



def addJetsVariables(pt,dzCut=99999):
    if hasattr(pt,"variables"):

        pt.variables.std_vector_jet_puid = cms.string("leadingJetPUid")

def addFakeRateVariables(pt):
    if hasattr(pt,"variables"):

        pt.variables.std_vector_lepton_closejet_pt            = cms.string("leadingJetCloseLeptonPt")
        pt.variables.std_vector_lepton_closejet_eta           = cms.string("leadingJetCloseLeptonEta")
        pt.variables.std_vector_lepton_closejet_phi           = cms.string("leadingJetCloseLeptonPhi")
        pt.variables.std_vector_lepton_closejet_PartonFlavour = cms.string("leadingJetCloseLeptonFlavour")
        pt.variables.std_vector_lepton_closejet_drlj          = cms.string("leadingJetCloseLeptonDR")



def addBTaggingVariables(pt,dzCut=99999):
    if hasattr(pt,"variables"):

        pt.variables.softcsvv2ivf = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+" ,'pfCombinedInclusiveSecondaryVertexV2BJetTags',"+jetId_WP+",%f)"%dzCut)
        pt.variables.hardcsvv2ivf = cms.string("highestBDiscRange("+CJVminPt+",999999.,'pfCombinedInclusiveSecondaryVertexV2BJetTags',"+jetId_WP+",%f,1)"%dzCut)
        pt.variables.softssvhe    = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+" ,'pfSimpleSecondaryVertexHighEffBJetTags',"+jetId_WP+",%f)"%dzCut)
        pt.variables.hardssvhe    = cms.string("highestBDiscRange("+CJVminPt+",999999.,'pfSimpleSecondaryVertexHighEffBJetTags',"+jetId_WP+",%f,1)"%dzCut)
        pt.variables.softssvhb    = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+" ,'pfSimpleSecondaryVertexHighPurBJetTags',"+jetId_WP+",%f)"%dzCut)
        pt.variables.hardssvhb    = cms.string("highestBDiscRange("+CJVminPt+",999999.,'pfSimpleSecondaryVertexHighPurBJetTags',"+jetId_WP+",%f,1)"%dzCut)
        pt.variables.softpfcsv    = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+" ,'pfCombinedSecondaryVertexBJetTags',"+jetId_WP+",%f)"%dzCut)
        pt.variables.hardpfcsv    = cms.string("highestBDiscRange("+CJVminPt+",999999.,'pfCombinedSecondaryVertexBJetTags',"+jetId_WP+",%f,1)"%dzCut)
        pt.variables.softcmva     = cms.string("highestBDiscRange("+minPtBVeto+","+CJVminPt+" ,'combinedMVABJetTags',"+jetId_WP+",%f)"%dzCut)
        pt.variables.hardcmva     = cms.string("highestBDiscRange("+CJVminPt+",999999.,'combinedMVABJetTags',"+jetId_WP+",%f,1)"%dzCut)

        pt.variables.std_vector_jet_csvv2ivf  = cms.string("jetcsvv2ivfByPt")
        pt.variables.std_vector_jet_ssvhe     = cms.string("jetssvheByPt")
        pt.variables.std_vector_jet_ssvhb     = cms.string("jetssvhbByPt")
        pt.variables.std_vector_jet_pfcsv     = cms.string("jetpfcsvByPt")
        pt.variables.std_vector_jet_cmva      = cms.string("jetcmvaByPt")
        pt.variables.std_vector_jet_tche      = cms.string("jettcheByPt")
        pt.variables.std_vector_jet_tchp      = cms.string("jettchpByPt")
        pt.variables.std_vector_jet_bjpb      = cms.string("jetbjpbByPt")
        pt.variables.std_vector_jet_softMuPt  = cms.string("jetSoftMuonPtByPt")
        pt.variables.std_vector_jet_softMuEta = cms.string("jetSoftMuonEtaByPt")
        pt.variables.std_vector_jet_softMuPhi = cms.string("jetSoftMuonPhiByPt")
        pt.variables.std_vector_jet_softMuIso = cms.string("jetSoftMuonIsoByPt")
        pt.variables.std_vector_jet_NumberSoftMu = cms.string("jetSoftMuonCountingByPt")

        pt.variables.jetcsvv2ivf1 = cms.string("leadingJetBtag(0,'pfCombinedInclusiveSecondaryVertexV2BJetTags',0,"+CJVmaxEta+",1,1,%f)"%dzCut)
        pt.variables.jetcsvv2ivf2 = cms.string("leadingJetBtag(1,'pfCombinedInclusiveSecondaryVertexV2BJetTags',0,"+CJVmaxEta+",1,1,%f)"%dzCut)
        pt.variables.jetssvhe1 = cms.string("leadingJetBtag(0,'pfSimpleSecondaryVertexHighEffBJetTags',0,"+CJVmaxEta+",1,1,%f)"%dzCut)
        pt.variables.jetssvhe2 = cms.string("leadingJetBtag(1,'pfSimpleSecondaryVertexHighEffBJetTags',0,"+CJVmaxEta+",1,1,%f)"%dzCut)
        pt.variables.jetssvhb1 = cms.string("leadingJetBtag(0,'pfSimpleSecondaryVertexHighPurBJetTags',0,"+CJVmaxEta+",1,1,%f)"%dzCut)
        pt.variables.jetssvhb2 = cms.string("leadingJetBtag(1,'pfSimpleSecondaryVertexHighPurBJetTags',0,"+CJVmaxEta+",1,1,%f)"%dzCut)
        pt.variables.jetpfcsv1 = cms.string("leadingJetBtag(0,'pfCombinedSecondaryVertexBJetTags',0,"+CJVmaxEta+",1,1,%f)"%dzCut)
        pt.variables.jetpfcsv2 = cms.string("leadingJetBtag(1,'pfCombinedSecondaryVertexBJetTags',0,"+CJVmaxEta+",1,1,%f)"%dzCut)
        pt.variables.jetcmva1 = cms.string("leadingJetBtag(0,'combinedMVABJetTags',0,"+CJVmaxEta+",1,1,%f)"%dzCut)
        pt.variables.jetcmva2 = cms.string("leadingJetBtag(1,'combinedMVABJetTags',0,"+CJVmaxEta+",1,1,%f)"%dzCut)

    else:
        raise RuntimeError, "In addBTaggingVariables, %s doesn't look like a ProbeTreeProducer object, it has no 'variables' attribute." % pt

# LHE information
def addLHEVariables(process,pt):
    if hasattr(pt,"variables"):
        setattr(pt.variables, "jetLHEPartonpt1" , cms.string("leadingLHEJetPt(0)")),
        setattr(pt.variables, "jetLHEPartonpid1" , cms.string("leadingLHEJetPID(0)")),
        setattr(pt.variables, "jetLHEPartonphi1" , cms.string("leadingLHEJetPhi(0)")),
        setattr(pt.variables, "jetLHEPartoneta1" , cms.string("leadingLHEJetEta(0)")),
        setattr(pt.variables, "jetLHEPartonpt2" , cms.string("leadingLHEJetPt(1)")),
        setattr(pt.variables, "jetLHEPartonpid2" , cms.string("leadingLHEJetPID(1)")),
        setattr(pt.variables, "jetLHEPartonphi2" , cms.string("leadingLHEJetPhi(1)")),
        setattr(pt.variables, "jetLHEPartoneta2" , cms.string("leadingLHEJetEta(1)")),
        setattr(pt.variables, "jetLHEPartonpt3" , cms.string("leadingLHEJetPt(2)")),
        setattr(pt.variables, "jetLHEPartonpid3" , cms.string("leadingLHEJetPID(2)")),
        setattr(pt.variables, "jetLHEPartonphi3" , cms.string("leadingLHEJetPhi(2)")),
        setattr(pt.variables, "jetLHEPartoneta3" , cms.string("leadingLHEJetEta(2)")),
        setattr(pt.variables, "leptonLHEpt1" , cms.string("leadingLHELeptonPt(0)")),
        setattr(pt.variables, "leptonLHEpid1" , cms.string("leadingLHELeptonPID(0)")),
        setattr(pt.variables, "leptonLHEphi1" , cms.string("leadingLHELeptonPhi(0)")),
        setattr(pt.variables, "leptonLHEeta1" , cms.string("leadingLHELeptonEta(0)")),
        setattr(pt.variables, "leptonLHEpt2" , cms.string("leadingLHELeptonPt(1)")),
        setattr(pt.variables, "leptonLHEpid2" , cms.string("leadingLHELeptonPID(1)")),
        setattr(pt.variables, "leptonLHEphi2" , cms.string("leadingLHELeptonPhi(1)")),
        setattr(pt.variables, "leptonLHEeta2" , cms.string("leadingLHELeptonEta(1)")),
        setattr(pt.variables, "leptonLHEpt3" , cms.string("leadingLHELeptonPt(2)")),
        setattr(pt.variables, "leptonLHEpid3" , cms.string("leadingLHELeptonPID(2)")),
        setattr(pt.variables, "leptonLHEphi3" , cms.string("leadingLHELeptonPhi(2)")),
        setattr(pt.variables, "leptonLHEeta3" , cms.string("leadingLHELeptonEta(2)")),
        setattr(pt.variables, "neutrinoLHEpt1" , cms.string("leadingLHENeutrinoPt(0)")),
        setattr(pt.variables, "neutrinoLHEpid1" , cms.string("leadingLHENeutrinoPID(0)")),
        setattr(pt.variables, "neutrinoLHEphi1" , cms.string("leadingLHENeutrinoPhi(0)")),
        setattr(pt.variables, "neutrinoLHEeta1" , cms.string("leadingLHENeutrinoEta(0)")),
        setattr(pt.variables, "neutrinoLHEpt2" , cms.string("leadingLHENeutrinoPt(1)")),
        setattr(pt.variables, "neutrinoLHEpid2" , cms.string("leadingLHENeutrinoPID(1)")),
        setattr(pt.variables, "neutrinoLHEphi2" , cms.string("leadingLHENeutrinoPhi(1)")),
        setattr(pt.variables, "neutrinoLHEeta2" , cms.string("leadingLHENeutrinoEta(1)")),
        setattr(pt.variables, "neutrinoLHEpt3" , cms.string("leadingLHENeutrinoPt(2)")),
        setattr(pt.variables, "neutrinoLHEpid3" , cms.string("leadingLHENeutrinoPID(2)")),
        setattr(pt.variables, "neutrinoLHEphi3" , cms.string("leadingLHENeutrinoPhi(2)")),
        setattr(pt.variables, "neutrinoLHEeta3" , cms.string("leadingLHENeutrinoEta(2)")),

        setattr(pt.variables, "metLHEpt" , cms.string("LHEMetPt()")),
        setattr(pt.variables, "metLHEphi" , cms.string("LHEMetPhi()")),
        setattr(pt.variables, "metLHEeta" , cms.string("LHEMetEta()")),

        setattr(pt.variables, "higgsLHEpt" , cms.string("higgsLHEPt()")),
        setattr(pt.variables, "higgsLHEeta" , cms.string("higgsLHEEta()")),
        setattr(pt.variables, "higgsLHEphi" , cms.string("higgsLHEPhi()")),
        setattr(pt.variables, "higgsLHEm" , cms.string("higgsLHEmass()")),

    else:
        raise addLHEVariables, "In addLHEVariables, %s doesn't look like a ProbeTreeProducer object, it has no 'variables' attribute." % pt

# gen information
def addGenVariables(process,pt):
    if hasattr(pt,"variables"):
        setattr(pt.variables, "jetGenPartonpt1",  cms.string("leadingGenJetPartonPt(0)")),
        setattr(pt.variables, "jetGenPartonpid1", cms.string("leadingGenJetPartonPID(0)")),
        setattr(pt.variables, "jetGenPartonphi1", cms.string("leadingGenJetPartonPhi(0)")),
        setattr(pt.variables, "jetGenPartoneta1", cms.string("leadingGenJetPartonEta(0)")),
        setattr(pt.variables, "jetGenPartonpt2",  cms.string("leadingGenJetPartonPt(1)")),
        setattr(pt.variables, "jetGenPartonpid2", cms.string("leadingGenJetPartonPID(1)")),
        setattr(pt.variables, "jetGenPartonphi2", cms.string("leadingGenJetPartonPhi(1)")),
        setattr(pt.variables, "jetGenPartoneta2", cms.string("leadingGenJetPartonEta(1)")),
        setattr(pt.variables, "jetGenPartonpt3" , cms.string("leadingGenJetPartonPt(2)")),
        setattr(pt.variables, "jetGenPartonpid3", cms.string("leadingGenJetPartonPID(2)")),
        setattr(pt.variables, "jetGenPartonphi3", cms.string("leadingGenJetPartonPhi(2)")),
        setattr(pt.variables, "jetGenPartoneta3", cms.string("leadingGenJetPartonEta(2)")),

        setattr(pt.variables, "std_vector_leptonGen_pt",      cms.string("genLeptonPt")),
        setattr(pt.variables, "std_vector_leptonGen_eta" ,    cms.string("genLeptonEta")),
        setattr(pt.variables, "std_vector_leptonGen_phi",     cms.string("genLeptonPhi")),
        setattr(pt.variables, "std_vector_leptonGen_pid",     cms.string("genLeptonPID")),
        setattr(pt.variables, "std_vector_leptonGen_status",  cms.string("genLeptonStatus")),
        setattr(pt.variables, "std_vector_leptonGen_index",   cms.string("genLeptonIndex")),
        setattr(pt.variables, "std_vector_leptonGen_mpid" ,   cms.string("genLeptonMotherPID")),
        setattr(pt.variables, "std_vector_leptonGen_mstatus", cms.string("genLeptonMotherStatus")),
        setattr(pt.variables, "std_vector_leptonGen_isHardProcess", cms.string("genLeptonIsHardProcess")),
        setattr(pt.variables, "std_vector_leptonGen_fromHardProcessDecayed", cms.string("genLeptonFromHardProcessDecayed")),
        setattr(pt.variables, "std_vector_leptonGen_fromHardProcessBeforeFSR", cms.string("genLeptonFromHardProcessBeforeFSR")),

        setattr(pt.variables, "std_vector_VBoson_pt",      cms.string("genVBosonPt/30")),
        setattr(pt.variables, "std_vector_VBoson_eta" ,    cms.string("genVBosonEta/30")),
        setattr(pt.variables, "std_vector_VBoson_phi",     cms.string("genVBosonPhi/30")),
        setattr(pt.variables, "std_vector_VBoson_pid",     cms.string("genVBosonPID/30")),
        setattr(pt.variables, "std_vector_VBoson_status",  cms.string("genVBosonStatus/30")),
        setattr(pt.variables, "std_vector_VBoson_isHardProcess", cms.string("genVBosonIsHardProcess/30")),
        setattr(pt.variables, "std_vector_VBoson_fromHardProcessBeforeFSR", cms.string("genVBosonFromHardProcessBeforeFSR/30")),

        setattr(pt.variables, "neutrinoGenpt1" , cms.string("leadingGenNeutrinoPt(0)")),       # to be removed once std vector is validated
        setattr(pt.variables, "neutrinoGenpid1" , cms.string("leadingGenNeutrinoPID(0)")),     # to be removed once std vector is validated
        setattr(pt.variables, "neutrinoGenphi1" , cms.string("leadingGenNeutrinoPhi(0)")),     # to be removed once std vector is validated
        setattr(pt.variables, "neutrinoGeneta1" , cms.string("leadingGenNeutrinoEta(0)")),     # to be removed once std vector is validated
        setattr(pt.variables, "neutrinoGenpt2" , cms.string("leadingGenNeutrinoPt(1)")),       # to be removed once std vector is validated
        setattr(pt.variables, "neutrinoGenpid2" , cms.string("leadingGenNeutrinoPID(1)")),     # to be removed once std vector is validated
        setattr(pt.variables, "neutrinoGenphi2" , cms.string("leadingGenNeutrinoPhi(1)")),     # to be removed once std vector is validated
        setattr(pt.variables, "neutrinoGeneta2" , cms.string("leadingGenNeutrinoEta(1)")),     # to be removed once std vector is validated
        setattr(pt.variables, "neutrinoGenpt3" , cms.string("leadingGenNeutrinoPt(2)")),       # to be removed once std vector is validated
        setattr(pt.variables, "neutrinoGenpid3" , cms.string("leadingGenNeutrinoPID(2)")),     # to be removed once std vector is validated
        setattr(pt.variables, "neutrinoGenphi3" , cms.string("leadingGenNeutrinoPhi(2)")),     # to be removed once std vector is validated
        setattr(pt.variables, "neutrinoGeneta3" , cms.string("leadingGenNeutrinoEta(2)")),     # to be removed once std vector is validated

        setattr(pt.variables, "std_vector_neutrinoGen_pt",      cms.string("leadingGenNeutrinoPt")),
        setattr(pt.variables, "std_vector_neutrinoGen_eta" ,    cms.string("leadingGenNeutrinoEta")),
        setattr(pt.variables, "std_vector_neutrinoGen_phi",     cms.string("leadingGenNeutrinoPhi")),
        setattr(pt.variables, "std_vector_neutrinoGen_pid",     cms.string("leadingGenNeutrinoPID")),
        setattr(pt.variables, "std_vector_neutrinoGen_isHardProcess", cms.string("leadingGenNeutrinoIsHardProcess")),
        setattr(pt.variables, "std_vector_neutrinoGen_fromHardProcessBeforeFSR", cms.string("leadingGenNeutrinoFromHardProcessBeforeFSR")),



        setattr(pt.variables, "higggsGenpt" , cms.string("getHiggsPt()")),

        setattr(pt.variables, "metGenpt" , cms.string("genMetPt()")),
        setattr(pt.variables, "metGeneta", cms.string("genMetEta()")),
        setattr(pt.variables, "metGenphi", cms.string("genMetPhi()")),

        setattr(pt.variables, "std_vector_jetGen_pt" , cms.string("leadingGenJetPt")),
        setattr(pt.variables, "std_vector_jetGen_phi", cms.string("leadingGenJetPhi")),
        setattr(pt.variables, "std_vector_jetGen_eta", cms.string("leadingGenJetEta")),

        setattr(pt.variables, "std_vector_jet_HadronFlavour", cms.string("leadingJetHadronFlavour")),
        setattr(pt.variables, "std_vector_jet_PartonFlavour", cms.string("leadingJetPartonFlavour")),

    else:
        raise addGenVariables, "In addGenVariables, %s doesn't look like a ProbeTreeProducer object, it has no 'variables' attribute." % pt



def addMCweights(process,pt):

        if hasattr(pt,"variables"):
          pt.variables.std_vector_LHE_weight = cms.string("LHEMCweight")
          pt.variables.std_vector_GEN_weight = cms.string("GENMCweight")
          pt.variables.LHE_weight_SM = cms.string("LHEMCweight(-1)")
          pt.variables.GEN_weight_SM = cms.string("GENMCweight(-1)")


def addTau(process,pt):

        if hasattr(pt,"variables"):
          pt.variables.std_vector_tau_pt  = cms.string("leadingTauPt")
          pt.variables.std_vector_tau_eta = cms.string("leadingTauEta")
          pt.variables.std_vector_tau_phi = cms.string("leadingTauPhi")


def addFatJets(process,pt):

        fatjetId_WP = "1"

        if hasattr(pt,"variables"):

            setattr(pt.variables, "fatjetpt1", cms.string("leadingFatJetPt(0,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjeteta1", cms.string("leadingFatJetEta(0,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjetphi1", cms.string("leadingFatJetPhi(0,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettrimmedmass1", cms.string("leadingFatJetTrimmedMass(0,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjetfilteredmass1", cms.string("leadingFatJetFilteredMass(0,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjetprunedmass1", cms.string("leadingFatJetPrunedMass(0,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjetmassdrop1", cms.string("leadingFatJetMassDrop(0,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau2tau11", cms.string("leadingFatJetPrunedTau2Tau1(0,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau11", cms.string("leadingFatJetPrunedTau1(0,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau21", cms.string("leadingFatJetPrunedTau2(0,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau31", cms.string("leadingFatJetPrunedTau3(0,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau41", cms.string("leadingFatJetPrunedTau4(0,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),


            setattr(pt.variables, "fatjetpt2", cms.string("leadingFatJetPt(1,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjeteta2", cms.string("leadingFatJetEta(1,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjetphi2", cms.string("leadingFatJetPhi(1,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettrimmedmass2", cms.string("leadingFatJetTrimmedMass(1,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjetfilteredmass2", cms.string("leadingFatJetFilteredMass(1,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjetprunedmass2", cms.string("leadingFatJetPrunedMass(1,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjetmassdrop2", cms.string("leadingFatJetMassDrop(1,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau2tau12", cms.string("leadingFatJetPrunedTau2Tau1(1,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau12", cms.string("leadingFatJetPrunedTau1(1,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau22", cms.string("leadingFatJetPrunedTau2(1,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau32", cms.string("leadingFatJetPrunedTau3(1,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau42", cms.string("leadingFatJetPrunedTau4(1,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),


            setattr(pt.variables, "fatjetpt3", cms.string("leadingFatJetPt(2,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjeteta3", cms.string("leadingFatJetEta(2,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjetphi3", cms.string("leadingFatJetPhi(2,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettrimmedmass3", cms.string("leadingFatJetTrimmedMass(2,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjetfilteredmass3", cms.string("leadingFatJetFilteredMass(2,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjetprunedmass3", cms.string("leadingFatJetPrunedMass(2,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjetmassdrop3", cms.string("leadingFatJetMassDrop(2,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau2tau13", cms.string("leadingFatJetPrunedTau2Tau1(2,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau13", cms.string("leadingFatJetPrunedTau1(2,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau23", cms.string("leadingFatJetPrunedTau2(2,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau33", cms.string("leadingFatJetPrunedTau3(2,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),
            setattr(pt.variables, "fatjettau43", cms.string("leadingFatJetPrunedTau4(2,0,"+CJVmaxEta+",1,"+fatjetId_WP+")")),




def addQGJets(process,pt):

        if hasattr(pt,"variables"):
         
            pt.variables.std_vector_jet_QGaxis1      = cms.string("leadingJetQGaxis1")
            pt.variables.std_vector_jet_QGaxis2      = cms.string("leadingJetQGaxis2")
            pt.variables.std_vector_jet_QGRMScand    = cms.string("leadingJetQGRMScand")
            pt.variables.std_vector_jet_QGRmax       = cms.string("leadingJetQGRmax")
            pt.variables.std_vector_jet_QGlikelihood = cms.string("leadingJetQGlikelihood")


def addAdditionalJets(process,pt):

        if hasattr(pt,"variables"):

            setattr(pt.variables, "jetpt5", cms.string("leadingJetPt(4,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jeteta5", cms.string("leadingJetEta(4,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetphi5", cms.string("leadingJetPhi(4,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetmass5", cms.string("leadingJetMass(4,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetid5", cms.string("leadingJetId(4,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetmva5", cms.string("leadingJetMva(4,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jettche5", cms.string("leadingJetBtag(4,'pfTrackCountingHighEffBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")")),
            setattr(pt.variables, "jetbjpb5", cms.string("leadingJetBtag(4,'pfJetBProbabilityBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")")),
            setattr(pt.variables, "jettchp5", cms.string("leadingJetBtag(4,'pfTrackCountingHighPurBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")")),
            setattr(pt.variables, "jetptd5", cms.string("leadingJetPtd(4,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetCHM5", cms.string("leadingJetChargedHadronMultiplicity(4,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetNHM5", cms.string("leadingJetNeutralHadronMultiplicity(4,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetPhM5", cms.string("leadingJetPhotonMultiplicity(4,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetNChgQC5", cms.string("leadingJetNChgQC(4,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetNChgptCut5", cms.string("leadingJetNChgptCut(4,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetNNeutralptCut5", cms.string("leadingJetNNeutralptCut(4,0,"+CJVmaxEta+",1,"+jetId_WP+")")),

            setattr(pt.variables, "jetpt6", cms.string("leadingJetPt(5,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jeteta6", cms.string("leadingJetEta(5,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetphi6", cms.string("leadingJetPhi(5,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetmass6", cms.string("leadingJetMass(5,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetid6", cms.string("leadingJetId(5,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetmva6", cms.string("leadingJetMva(5,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jettche6", cms.string("leadingJetBtag(5,'pfTrackCountingHighEffBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")")),
            setattr(pt.variables, "jetbjpb6", cms.string("leadingJetBtag(5,'pfJetBProbabilityBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")")),
            setattr(pt.variables, "jettchp6", cms.string("leadingJetBtag(5,'pfTrackCountingHighPurBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")")),
            setattr(pt.variables, "jetptd6", cms.string("leadingJetPtd(5,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetCHM6", cms.string("leadingJetChargedHadronMultiplicity(5,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetNHM6", cms.string("leadingJetNeutralHadronMultiplicity(5,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetPhM6", cms.string("leadingJetPhotonMultiplicity(5,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetNChgQC6", cms.string("leadingJetNChgQC(5,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetNChgptCut6", cms.string("leadingJetNChgptCut(5,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetNNeutralptCut6", cms.string("leadingJetNNeutralptCut(5,0,"+CJVmaxEta+",1,"+jetId_WP+")")),

            setattr(pt.variables, "jetpt7", cms.string("leadingJetPt(6,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jeteta7", cms.string("leadingJetEta(6,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetphi7", cms.string("leadingJetPhi(6,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetmass7", cms.string("leadingJetMass(6,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetid7", cms.string("leadingJetId(6,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetmva7", cms.string("leadingJetMva(6,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jettche7", cms.string("leadingJetBtag(6,'pfTrackCountingHighEffBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")")),
            setattr(pt.variables, "jetbjpb7", cms.string("leadingJetBtag(6,'pfJetBProbabilityBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")")),
            setattr(pt.variables, "jettchp7", cms.string("leadingJetBtag(6,'pfTrackCountingHighPurBJetTags',0,"+CJVmaxEta+",1,"+jetId_WP+","+DzBVeto+")")),
            setattr(pt.variables, "jetptd7", cms.string("leadingJetPtd(6,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetCHM7", cms.string("leadingJetChargedHadronMultiplicity(6,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetNHM7", cms.string("leadingJetNeutralHadronMultiplicity(6,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetPhM7", cms.string("leadingJetPhotonMultiplicity(6,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetNChgQC7", cms.string("leadingJetNChgQC(6,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetNChgptCut7", cms.string("leadingJetNChgptCut(6,0,"+CJVmaxEta+",1,"+jetId_WP+")")),
            setattr(pt.variables, "jetNNeutralptCut7", cms.string("leadingJetNNeutralptCut(6,0,"+CJVmaxEta+",1,"+jetId_WP+")")),

def addSoftActivityVariables(process,pt):
     if hasattr(pt,"variables"):
         setattr(pt.variables, "sumHtSoft",  cms.string("sumHtTrackJets")),
         setattr(pt.variables, "sumHTSoftDensity", cms.string("sumHtTrackJetsDensity")),

def addIsoStudyVariables(process,pt):
    if hasattr(pt,"variables"):
      for i,l in enumerate(["lep1", "lep2"]):
        setattr(pt.variables, l+"isoMergePf" , cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).userFloat('muSmurfPF') : candByPt({0}).userFloat('eleSmurfPF04')".format(i)))
        setattr(pt.variables, l+"isoRecoTracks" , cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).isolationR03().sumPt : candByPt({0}).dr03TkSumPt".format(i)))
        setattr(pt.variables, l+"isoRecoEcal" , cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).isolationR03().emEt : ".format(i) +
                                                              " ( max(0,candByPt({0}).dr03EcalRecHitSumEt - 1)*candByPt({0}).isEB + (1-candByPt({0}).isEB)*candByPt({0}).dr03EcalRecHitSumEt )".format(i)))
        setattr(pt.variables, l+"isoRecoHCal" , cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).isolationR03().hadEt : candByPt({0}).dr03HcalTowerSumEt ".format(i)))
        setattr(pt.variables, l+"isoRecoHCalFull", cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).isolationR03().hadEt : candByPt({0}).userFloat('hcalFull')".format(i)))
        setattr(pt.variables, l+"isoPfCharged" , cms.string("candByPt({0}).userFloat('pfCharged')".format(i)))
        setattr(pt.variables, l+"isoPfNeutral" , cms.string("candByPt({0}).userFloat('pfNeutral')".format(i)))
        setattr(pt.variables, l+"isoPfPhoton" , cms.string("candByPt({0}).userFloat('pfPhoton')".format(i)))
        setattr(pt.variables, l+"isoSmurfCharged", cms.string("candByPt({0}).userFloat('smurfCharged')".format(i)))
        setattr(pt.variables, l+"isoSmurfNeutral", cms.string("candByPt({0}).userFloat('smurfNeutral')".format(i)))
        setattr(pt.variables, l+"isoSmurfPhoton" , cms.string("candByPt({0}).userFloat('smurfPhoton')".format(i)))
        setattr(pt.variables, l+"isoSmurfNoOverCharged", cms.string("candByPt({0}).userFloat('smurfNoOverCharged')".format(i)))
        setattr(pt.variables, l+"isoSmurfNoOverNeutral", cms.string("candByPt({0}).userFloat('smurfNoOverNeural')".format(i)))
        setattr(pt.variables, l+"isoSmurfNoOverPhoton" , cms.string("candByPt({0}).userFloat('smurfNoOverPhoton')".format(i)))
        for algo in ("JetCone", "FixCone03", "FixCone04", "MaxCone03", "MaxCone04", "SumCone02", "SumCone04"):
            for name in ("Charged", "ChargedNoOvRem"): #, "NeutralHadAll", "NeutralHadPt05", "NeutralHadPt1", "Photons", "PhotonsMuStrip"):
                setattr(pt.variables, "%sjetiso%s%s"%(l,algo,name), cms.string("candByPt(%d).userFloat('jetIso%s%s')"%(i,algo,name)))
    else:
        raise RuntimeError, "In addIsoStudyVariables, %s doesn't look like a ProbeTreeProducer object, it has no 'variables' attribute." % pt
    if not hasattr(process,"isoStudySequence"):
        process.load("WWAnalysis.AnalysisStep.isoStudySequence_cff")

def addExtraPUWeights(process,tree,X,seq):
    print "WARNING, all the distro's haven't been designed yet, don't turn addExtraPUWeights on yet"
    from WWAnalysis.AnalysisStep.pileupReweighting_cfi import lpOld, lpNew, currentOld, currentNew, mcNominal, mcTemplate
    dataDistros = {
        "LPOld": lpOld,
        "LPNew": lpNew,
        "CurrentOld": currentOld,
        "CurrentNew": currentNew,
    }
    mcDistros = {
        "MCNominal": mcNominal,
        "MCTemplate": mcTemplate,
    }
    for data in dataDistros:
        for mc in mcDistros:
            newName = X+mc+data
            setattr(tree.variables, 'pu'+mc+data, cms.InputTag(newName))
            setattr(tree.variables, 'puOOT'+mc+data, cms.InputTag(newName+"OOT"))
            setattr(process, newName, process.puWeight.clone(src = cms.InputTag("ww%s"% (X)), dataDist = dataDistros[data][:], s4Dist = mcDistros[mc][:]))
            setattr(process, newName+"OOT", process.puWeight.clone(src = cms.InputTag("ww%s"% (X)), dataDist = dataDistros[data][:], s4Dist = mcDistros[mc][:], useOOT=True))
            seq += getattr(process, newName)
            seq += getattr(process, newName+"OOT")



########## PHOTON VARIABLES

def addPhotonVariables(process,pt):
    if hasattr(pt,"variables"):
        setattr(pt.variables, "v_photon1" ,    cms.string("photon(0)")),
        setattr(pt.variables, "v_photon2" ,    cms.string("photon(1)")),
        setattr(pt.variables, "v_photon3" ,    cms.string("photon(2)")),
        setattr(pt.variables, "v_photon1id" ,  cms.string("photon_id(0)")),
        setattr(pt.variables, "nPhos" ,        cms.string("nPhos()")),
        setattr(pt.variables, "pho_n_id" ,     cms.string("Pho_n_ID()")),
        setattr(pt.variables, "mllg" ,         cms.string("mllg()")),
        setattr(pt.variables, "mllgid" ,       cms.string("mllg()")),

def addPhotonIDVariables(process,pt):
        setattr(pt.variables, "pho_sietaieta" ,    cms.string("Pho_sigmaIetaIeta(0)")),
        setattr(pt.variables, "pho_HoE" ,          cms.string("Pho_hadronicOverEm(0)")),
        setattr(pt.variables, "pho_chIso" ,        cms.string("Pho_rhoChargedHadronIso(0)")),
        setattr(pt.variables, "pho_nhIso" ,        cms.string("Pho_rhoNeutralHadronIso(0)")),
        setattr(pt.variables, "pho_phIso" ,        cms.string("Pho_rhoPhotonIso(0)")),
        setattr(pt.variables, "pho_passElecVeto" , cms.string("Pho_PassElectronVeto(0)")),
        setattr(pt.variables, "pho_hasPixelSeed",  cms.string("Pho_HasPixelSeed(0)")),



