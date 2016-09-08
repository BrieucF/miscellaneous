import os
import sys
# Do not forget to complie the CommPlotProducer each time you change smth !! : gROOT->ProcessLine(".L /home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/CommPlotProducer.C++");

#  You changed trigger in CommPlotProducer as well as nHi criteria for tracks !!!

isMuEn = 0
ptTrig = 40 
jetPtMin = 60 
jetPtMax = 250 
#ptTrig = 200
#jetPtMin =  230
#jetPtMax = 500 
#outRootFileDir = "/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/QCDinc_7414_25ns_ptHat80to600_Trig"+str(ptTrig)+"_Plot"+str(jetPtMin)+"_"+str(jetPtMax)+"_PUrew_withData2015D_256630_258750_fullStat/"
outRootFileDir = "/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/runIISpring16MINIAOD_v3_full_"+str(ptTrig)+"_Plot"+str(jetPtMin)+"_"+str(jetPtMax)+'_dataPostTrackerHIPFIX_2016FG_278801onwards_PURew_oldTrackSel/'
#outRootFileDir = "/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/dataPostICHEP_2016E_276812_278310_"+str(ptTrig)+"_Plot"+str(jetPtMin)+"_"+str(jetPtMax)+'/'
#outRootFileDir = "/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/dummy"

#outRootFileDir = "/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/muEnQCD_ptBin20to300_star1_TrigDijet20_Jet60_250_PUReweighted_goldenJSON/"
#isMuEn = 1
#ptTrig = 20
#jetPtMin = 60
#jetPtMax = 250

#PUreweightingFile = "/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/QCDinc_7414_25ns_ptHat80to600_Trig200_Plot220_500_noPUrew_withData2015D_256630_258750_fullStat/hadded.root"# "/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/QCDinc_7414_25ns_ptHat15to470_Trig40_Plot50_250_noPUrew_withData2015D_256630_258750_fullStat/hadded.root"#"/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/QCDinc_748_25ns_ptHat15to600_Trig"+str(ptTrig)+"_Plot"+str(jetPtMin)+"_"+str(jetPtMax)+"_noPUrew/hadded_Pt15To470_JetHT.root" #Need full path !
#PUreweightingFile = "/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/QCDinc_748_25ns_ptHat15to600_Trig"+str(ptTrig)+"_Plot"+str(jetPtMin)+"_"+str(jetPtMax)+"_noPUrew/hadded_Pt120To600_JetHT.root" #Need full path !
#PUreweightingFile = "/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/QCDinc_761_runIIFall15MiniAODv1_full_"+str(ptTrig)+"_Plot"+str(jetPtMin)+"_"+str(jetPtMax)+"/hadded.root"
#PUreweightingFile = "/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/runIISpring16AODSIM_v1_resubmit3_full_40_Plot50_250_pthat_15_470_notPUrew/allhadded.root"

#PUreweightingFile = "/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/dataPostICHEP_2016E_276812_278310_40_Plot60_250/allhadded.root" #/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/runIISpring16MINIAOD_v2_full_40_Plot50_250_pthat_15_470_noPURew/allhadded.root" # "/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/pileUp_hist_2016B_271036_27443_xsec71300.root"
officialPU = 0  # true or false
PUreweightingFile = "/home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/runIISpring16MINIAOD_v3_full_40_Plot60_250_dataPostTrackerHIPFIX_2016FG_278801onwards_notPURew_NewTrackSel/allhadded.root"

fullStat = True

if not isMuEn :
    baseDir = "/storage/data/cms/store/user/brfranco/bTag/runIIspring16_QCDinc_25ns_BTAG80X_v3_HIP_IVFTrue/"
    filePattern = "JetTree_mc_INDEX.root"
    if fullStat : 
        fileList = {
                # "Name pt hat bin" : [fileNameTemplate, minNum, numberOfCrabJobs (the + 1 will be done later)]
                
                "Pt-15to30" : [baseDir+"Pt-15to30/"+filePattern, 1, 120],
                "Pt-30to50" : [baseDir+"Pt-30to50/"+filePattern, 1, 118],
                "Pt-50to80" : [baseDir+"Pt-50to80/"+filePattern, 1, 124],
                "Pt-80to120" : [baseDir+"Pt-80to120/"+filePattern, 1, 90],
                "Pt-120to170" : [baseDir+"Pt-120to170/"+filePattern, 1, 83],
                "Pt-170to300" : [baseDir+"Pt-170to300/"+filePattern, 1, 79],
                "Pt-300to470" : [baseDir+"Pt-300to470/"+filePattern, 1, 69],

                #"Pt-470to600" : [baseDir+"Pt-470to600/"+filePattern, 1, 93],
                #"Pt-600to800" : [baseDir+"Pt-600to800/"+filePattern, 1, 95],
                #"Pt-800to1000" : [baseDir+"Pt-800to1000/"+filePattern, 1, 95],
                #"Pt-1000to1400" : [baseDir+"Pt-1000to1400/"+filePattern, 1, 68],

                #"data_JetHT_2016E_8012_run_276812_278310" : ["/storage/data/cms/store/user/brfranco/bTag/JetHT_PostICHEP_10_09_2016/JetHT/crab_JetHT_2016-08-10_1470832681333/160810_123835/0000/JetTree_data_INDEX.root", 1, 512],
                #"data_JetHT_2016E_8012_run_276812_278310" : ["/storage/data/cms/store/user/brfranco/bTag/JetHT_PostICHEP_10_09_2016_NewTrackSel/JetHT/crab_JetHT_2016-08-19_1471615910423/160819_141206/0000/JetTree_data_INDEX.root", 1, 512],
                "data_JetHT_2016F_8012_run_278801onwards" : ["/storage/data/cms/store/user/brfranco/bTag/JetHT_PostHIPFIX_278801_NewTrackSel/JetHT/crab_JetHT_2016-08-19_1471615874360/160819_141130/0000/JetTree_data_INDEX.root", 1, 51],
                "data_JetHT_2016G_8012_run_278801onwards" : ["/storage/data/cms/store/user/brfranco/bTag/JetHT_PostHIPFIX_278801_NewTrackSel/JetHT/crab_JetHT_2016-08-19_1471615891897/160819_141149/0000/JetTree_data_INDEX.root", 1, 124],


        }
    else :
        fileList = {
                #"Pt-15to30" : [baseDir+"Pt-15to30/"+filePattern, 117],
                #"Pt-30to50" : [baseDir+"Pt-30to50/"+filePattern, 117],
                #"Pt-50to80" : [baseDir+"Pt-50to80/"+filePattern, 116],
                #"Pt-80to120" : [baseDir+"Pt-80to120/"+filePattern, 85],
                #"Pt-120to170" : [baseDir+"Pt-120to170/"+filePattern, 77],
                #"Pt-170to300" : [baseDir+"Pt-170to300/"+filePattern, 79],
                #"Pt-300to470" : [baseDir+"Pt-300to470/"+filePattern, 68],
                #"Pt-470to600" : [baseDir+"Pt-470to600/"+filePattern, 49],
                #"Pt-600to800" : [baseDir+"Pt-470to600/"+filePattern, 47],
                #"Pt-800to1000" : [baseDir+"Pt-470to600/"+filePattern, 43],
                #"Pt-1000to1400" : [baseDir+"Pt-470to600/"+filePattern, 34],
                #"data_JetHT_2015D_Run2015D_05Oct2015_v1" : ["root://eoscms.cern.ch//eos/cms/store/group/phys_btag/Commissioning/CMSSW_7_4_14/Data/JetHT/Run2015D_05Oct2015_v1/JetTree_data_FatJets_Subjets_INDEX.root", 513],
                #"data_JetHT_2015D_Run2015D_PromptReco_v4" : ["root://eoscms.cern.ch//eos/cms/store/group/phys_btag/Commissioning/CMSSW_7_4_14/Data/JetHT/Run2015D_PromptReco_v4/JetTree_data_FatJets_Subjets_INDEX.root", 538]
                #"data_JetHT_2015D_PromptReco_v4_full" : ["/storage/data/cms/store/user/brfranco/bTag/2015D/JetHT/crab_JetHT_Run2015D-PromptReco-v4_2015-12-03_1449161731443/151203_170207/0000/JetTree_data_INDEX.root", 428]
                #"Pt-600to800" : [baseDir+"Pt-600to800/"+filePattern, 53],
                #"Pt-800to1000" : [baseDir+"Pt-800to1000/"+filePattern, 77],
                #"data_JetHT_2015D_prompt_256630-256869" : ["root://eoscms.cern.ch//eos/cms/store/group/phys_btag/Commissioning/CMSSW_7_4_8/Data/JetHT/Run2015D_PromptReco_256630-256869/JetTree_data_FatJets_Subjets_INDEX.root", 154]
        }

else : 
    baseDir = "root://sbgse1.in2p3.fr:8446/dpm/in2p3.fr/home/cms/phedex/store/user/kskovpen/BTV/25ns_COM/QCD_Pt_15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"
    filePattern = "JetTree_mc_*1.root"
    fileList = {
            #"Pt_20to30" : baseDir+"QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/crab_QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v2_2015-08-05/150805_115943/0000/"+filePattern,
            #"Pt_30to50" : baseDir+"QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/crab_QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1_2015-08-05/150805_122531/0000/"+filePattern,
            #"Pt_50to80" : baseDir+"QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/crab_QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1_2015-08-05/150805_122556/0000/"+filePattern,
            #"Pt_80to120" : baseDir+"QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/crab_QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1_2015-08-05/150805_120012/0000/"+filePattern,
            #"Pt_120to170" : baseDir+"QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/crab_QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1_2015-08-05/150805_120036/0000/"+filePattern,
            #"Pt_170to300" : baseDir+"QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/crab_QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v2_2015-08-05/150805_120233/0000/"+filePattern,
            "data_BTagMu" : "/storage/data/cms/store/user/brfranco/bTag/2015B/BTagMu/crab_BTagMu_Run2015B-PromptReco-v1_2015-08-26/150826_091138/0000/JetTree_data_*"
    }


if not (os.path.isdir(outRootFileDir)) :
    os.system("mkdir "+outRootFileDir)
condorDir = outRootFileDir+"/condor/"
if not (os.path.isdir(condorDir)) :
    os.system("mkdir " + condorDir)
nJob = 0
for ptBin in fileList.keys() :
    print ptBin
    for index in xrange(fileList[ptBin][1], fileList[ptBin][2]+1):
        shFileName = condorDir + '/parallelCondor_'+ptBin+'_isMuEn_'+str(isMuEn)+'_'+str(index)+'.sh'
        f = open(shFileName,'w')
        f.write('#! /bin/sh \n')
        f.write('source /nfs/soft/root/setup_sl6/root.sh\n')
        f.write('source /nfs/soft/grid/ui_sl6/setup/grid-env.sh\n')
        charForChain = fileList[ptBin][0].replace("INDEX",str(index))
        # NB : no space allowed in function call below !!
        f.write('root -b -q /home/fynu/bfrancois/bTag/CMSSW_7_4_5/src/RecoBTag/PerformanceMeasurements/test/BTagAnalyzerMacros/runCode_parallel.C\(\\\"'+charForChain+'\\\",0,\\\"'+outRootFileDir+"/"+ptBin+"_"+str(index)+'\\\",'+str(isMuEn)+','+str(ptTrig)+','+str(jetPtMin)+','+str(jetPtMax)+',\\\"'+PUreweightingFile+'\\\",'+str(officialPU)+'\)')
        f.close()
        os.system('chmod +x ' + shFileName)

        cmdFileName = condorDir + '/parallelCondor_'+ptBin+'_isMuEn_'+str(isMuEn)+'_'+str(index)+'.cmd'
        cmd = open(cmdFileName,'w')
        cmd.write('# here goes your shell script\nexecutable     = '+shFileName+'\n')
        cmd.write('# here you specify where to put .log, .out and .err files\noutput         = '+condorDir+'/parallelCondor_'+ptBin+'_isMuEn_'+str(isMuEn)+'_'+str(index)+'.out\nerror          = '+condorDir+'parallelCondor_'+ptBin+'_isMuEn_'+str(isMuEn)+'_'+str(index)+'.err\nlog            = '+ condorDir + '/parallelCondor_'+ptBin+'_isMuEn_'+str(isMuEn)+'_'+str(index)+'.log\n\n')
        cmd.write('# the following two parameters enable the file transfer mechanism\n# and specify that the output files should be transferred back\n# to the submit machine from the remote machine where the job executes\nshould_transfer_files   = YES\nwhen_to_transfer_output = ON_EXIT\n\n')
        cmd.write('# the following two parameters are required for the ingrid cluster\nuniverse       = vanilla\n')
        #cmd.write('x509userproxy = /tmp/x509up_u1271  \n ')
        cmd.write('requirements   = (CMSFARM =?= TRUE)\n#for Madgraph users replace the previous line by:\n#requirements   = (MADGRAPH =?= TRUE)\n\nqueue 1\n')
        cmd.close()
        os.system('chmod +x ' + cmdFileName)
        os.system('condor_submit ' + cmdFileName)
        nJob += 1
print "Submitted %s jobs."%nJob
    
