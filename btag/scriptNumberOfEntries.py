from ROOT import TChain
import datetime
from collections import OrderedDict

baseDir = "/storage/data/cms/store/user/brfranco/bTag/runIIspring16_QCDinc_25ns_BTAG80X_v0/"
filePattern = "JetTree_mc_INDEX.root" #"JetTree_mc_FatJets_Subjets_INDEX.root" # "JetTree_mc_*.root"
fileList = {
    "Pt-15to30" : [baseDir+"Pt-15to30/"+filePattern, 196],
    "Pt-30to50" : [baseDir+"Pt-30to50/"+filePattern, 215],
    "Pt-50to80" : [baseDir+"Pt-50to80/"+filePattern, 212],
    "Pt-80to120" : [baseDir+"Pt-80to120/"+filePattern, 116],
    "Pt-120to170" : [baseDir+"Pt-120to170/"+filePattern, 125],
    "Pt-170to300" : [baseDir+"Pt-170to300/"+filePattern, 182],
    "Pt-300to470" : [baseDir+"Pt-300to470/"+filePattern, 106],
    "Pt-470to600" : [baseDir+"Pt-470to600/"+filePattern, 114],
    "Pt-600to800" : [baseDir+"Pt-600to800/"+filePattern, 76],
    "Pt-800to1000" : [baseDir+"Pt-800to1000/"+filePattern, 112],
    "Pt-1000to1400" : [baseDir+"Pt-1000to1400/"+filePattern, 70],
}
fileList2 = OrderedDict([
    ("Pt-15to30" , [baseDir+"Pt-15to30/"+filePattern, 196]),
    ("Pt-30to50" , [baseDir+"Pt-30to50/"+filePattern, 215]),
    ("Pt-50to80" , [baseDir+"Pt-50to80/"+filePattern, 212]),
    ("Pt-80to120" , [baseDir+"Pt-80to120/"+filePattern, 116]),
    ("Pt-120to170" , [baseDir+"Pt-120to170/"+filePattern, 125]),
    ("Pt-170to300" , [baseDir+"Pt-170to300/"+filePattern, 182]),
    ("Pt-300to470" , [baseDir+"Pt-300to470/"+filePattern, 106]),
    ("Pt-470to600" , [baseDir+"Pt-470to600/"+filePattern, 114]),
    ("Pt-600to800" , [baseDir+"Pt-600to800/"+filePattern, 76]),
    ("Pt-800to1000" , [baseDir+"Pt-800to1000/"+filePattern, 112]),
    ("Pt-1000to1400" , [baseDir+"Pt-1000to1400/"+filePattern, 70]),
])
for ptBin in fileList2.keys() :
    print ptBin


lisOfNevt = []
outputEntries = open("outputEntries_"+str(datetime.date.today())+".txt",'w')
for ptBin in fileList2.keys() : 
    tchain = TChain("btagana/ttree")
    for i in xrange(1, fileList[ptBin][1]+1):
        tchain.Add(fileList[ptBin][0].replace("INDEX",str(i)))
    nEntries = tchain.GetEntries()
    print "Ok : number of event in ", ptBin, " is ", nEntries
    lisOfNevt.append(nEntries)
    outputEntries.write(ptBin+" : " + str(nEntries) + "\n")
    tchain.Reset()
print lisOfNevt
print "Written in ", outputEntries
