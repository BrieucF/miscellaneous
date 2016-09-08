#include <iostream>
#include <cmath>
#include <utility>
#include <vector>
#include "stdio.h"
using namespace std;

// for  MuEnriched QCD pythia at 13TeV, provide : 
//  -->  m.Fill_nevent(    0.,n20_30,n30_50,n50_80,n80_120,n120_170,n170-300,n300-470,n470-600,n600-800,n800-1000,n1000-inf);
//
// for Inclusive QCD pythia at 13TeV, provide : 
//  -->  m.Fill_nevent(    0.,n15_30,n30_50,n50_80,n80_120,n120_170,n170-300,n300-470,n470-600,n600-800,n800-1000,n1000-inf);

void runCode_parallel(TString charForChain, Int_t nFile, TString outFileName, bool isMuEn, Int_t TrigerPt, Int_t jetPtMin, Int_t jetPtMax, TString PUreweightingFile = "", bool officialPU = false){
    //TO DO if you change something in CommPlot : dans root gROOT->ProcessLine(".L /home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/CommPlotProducer.C++");
    //Be carefull to the CommPlotProducer you load !
    cout << "LOADING : /home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/CommPlotProducer_C.so" << endl;
    gSystem->Load("/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/CommPlotProducer_C.so");
    TChain *superTree = new TChain("btagana/ttree");
    cout << "1" << endl;
    if (nFile == 0)
    {
        superTree->Add(charForChain);
    }
    else
    {
        for(Int_t i = 0; i < nFile; i++)
        {
            TString index, fileName = charForChain;
            index.Form("%d",i+1);
            cout << index << endl;
            fileName.ReplaceAll("INDEX",index);
            cout << fileName << endl;
            superTree->Add(fileName);
        }
    }
    cout << "2" << endl;
    //Int_t nEvent = superTree->GetEntries();
    cout << "4" << endl;
    CommPlotProducer m(superTree);
    TString trigName = "jet";
    if(!isMuEn)
    {
        m.SetInfo("pythia",0,13);
        //m.Fill_nevent(0., 9800608.,9930948.,9897538.,6986123.,6778942.,6914063.,5874780. , 3928855., 3869318., 3843252., 2999055.);   // Inclusive QCD runIISpring16_MiniAODv2 v3 HIP !!! up to 470 GeV it is ok after not! 
        m.Fill_nevent(0., 9800608., 9930948., 9968391., 6986123., 6339488., 6914063., 5874780., 3928855., 3959746., 3883812., 2999055.);   // Inclusive QCD, almost full stat, runIISpring16_MiniAODv2 v3
        //m.Fill_nevent(0., 9800608., 9930948., 9968391., 6986123., 6863805., 6914063., 5834181., 3928855., 3959746., 3797668., 2999055.);   // Inclusive QCD, almost full stat, runIISpring16_MiniAODv2 v2
        //m.Fill_nevent(0., 9944962., 9949423., 9912583., 3459760., 3458384., 6877100., 2818689., 3885763., 1964124., 3976116., 1487136.);   // Inclusive QCD, almost full stat, runIISpring16
        //m.Fill_nevent(0., 38238558., 38425878., 9808010., 9775350., 6953583., 6848212., 6918735.,  5968947., 3977764., 3979873., 3973214.0);   // For full stat of files eos MC 25 ns Performance CMSSW_7_6_3 qcd inclusive
        //m.Fill_nevent(0., 38027914., 9788460., 9480963., 6111522., 6848212., 6054735., 5522805., 3961690., 3979873., 3973214., 2751549.);   // For full stat of files eos MC 25 ns CMSSW_7_6_1 qcd inclusive
        //m.Fill_nevent(0., 4959532., 4958023., 4983675., 3450292., 3458384., 3364365., 2935627., 1937537., 1964124., 1937216., 1540928.);   // For full stat of files eos MC 25 ns CMSSW_7_4_14 qcd inclusive
        //m.Fill_nevent(0., 4899660., 4958023., 4983675., 3382701., 3449499., 3364365., 2935627., 1776515., 0., 0., 0.);   // For full stat of files eos MC 25 ns CMSSW_7_4_8 qcd inclusive
        //m.Fill_nevent(0., 465376., 525994., 431125., 337429., 344498., 348768., 289820., 173007., 0., 0., 0.);   // For 10% of files eos MC 25 ns CMSSW_7_4_8 qcd inclusive
        //m.Fill_nevent(0., 1676567., 1849521., 1656700., 1020966., 1097903., 894409., 831039., 610248., 0., 0., 0.);   // For number of files indicated on the twiki MC 25 ns CMSSW_7_4_8 qcd inclusive
        //m.Fill_nevent(0., 458048., 580283., 533740., 367411., 401424., 317720., 0., 0., 0., 0., 0.); // newJP calib star1
        cout << "Inclusive QCD" << endl;
        //m.Fill_nevent(0., 514176., 502964., 546305., 350316., 349822., 345746., 308018., 208257., 212648., 0., 0.); //star 1
        //m.Fill_nevent(0.,33168.,45298.,31035.,25511.,25148.,18684.,23927.,11421.,25080.,0.,0.); // JetTree1.root  
        //m.Fill_nevent(0.,4938768.,4954702.,4981450.,3470544.,3455989.,3438065.,2931251.,1939229.,1890256.,0.,0.); // full stat
    }
    else
    {   
        m.SetInfo("pythia",1,13);
        m.Fill_nevent(0., 579682., 432168., 313919., 371584., 410021., 414704., 0., 0., 0., 0., 0.); // for newJP star 1
        cout << "MuEnriched QCD" << endl;
        //m.Fill_nevent(0., 514176., 502964., 546305., 350316., 349822., 345746., 308018., 208257., 212648., 0., 0.); // for 
        trigName = "btag";
    }
    cout << "5" << endl;
    m.SetXS();     // Assign the correct x-sections to QCD pthat bins, depending on SetInfo(), default = use inclusive pythia x-sections for 8 TeV.
    m.SetSumXS();
    cout << "6" << endl;
    //if (PUreweightingFile!= "") m.SetPV();   //It is now done inside the loop function, if the file is something else then ""
    TString name_root = outFileName; // "QCD_INC_13TeV_ptBin15to470_star1_TrigPFjet40_Jet60_300_PUReweighted_goldenJSON"; 
    m.Loop(trigName, TrigerPt, jetPtMin, jetPtMax, name_root, PUreweightingFile, officialPU);    
}


