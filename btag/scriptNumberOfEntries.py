from ROOT import TChain
import datetime

baseDir = "/storage/data/cms/store/user/brfranco/bTag/runIIspring16_QCDinc_25ns_BTAG80X_v3_HIP_IVFTrue/"
filePattern = "JetTree_mc_INDEX.root" #"JetTree_mc_FatJets_Subjets_INDEX.root" # "JetTree_mc_*.root"
ptBinKeys = ["Pt-15to30", "Pt-30to50", "Pt-50to80", "Pt-80to120", "Pt-120to170", "Pt-170to300", "Pt-300to470", "Pt-470to600", "Pt-600to800", "Pt-800to1000", "Pt-1000to1400"]
fileList = {
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
}

lisOfNevt = []
outputEntries = open("outputEntries_"+str(datetime.date.today())+".txt",'w')
for ptBin in ptBinKeys : 
    tchain = TChain("btagana/ttree")
    for i in xrange(fileList[ptBin][1], fileList[ptBin][2]+1):
        tchain.Add(fileList[ptBin][0].replace("INDEX",str(i)))
    nEntries = tchain.GetEntries()
    print "Ok : number of event in ", ptBin, " is ", nEntries
    lisOfNevt.append(nEntries)
    outputEntries.write(ptBin+" : " + str(nEntries) + "\n")
    tchain.Reset()
print lisOfNevt
print "Written in ", outputEntries
