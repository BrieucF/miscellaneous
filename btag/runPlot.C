{
gROOT->ProcessLine(".L DrawCommPlot_80X.C++");
gROOT->SetBatch();
DrawMC("nPV","#bf{nPV}",0);
//DrawMC("nJet","#bf{nJet}",0);
//DrawMC("nJet","#bf{nJet}",1);
Draw("jet_pt_all","#bf{Jet pT}",1);
Draw("jet_eta","#bf{Jet eta}",0);
Draw("CSVIVF","Jets/0.02","#bf{CSVv2 Discriminator}",0,-1);
Draw("trk_multi_sel03"  ,    "#bf{Number of selected tracks in #Delta R<0.3}",0);
Draw("pfmuon_multi"   ,      "#bf{Number of muons}", 1);
Draw("pfmuon_ptrel"     ,      "#bf{p_{T} rel. of the muon}",0);
Draw("pfmuon_pt",             "#bf{Muon p_{T}}",1);
Draw("TCHP"           ,"#bf{TCHP Discriminator}",1);
Draw("TCHP"           ,"#bf{TCHP Discriminator}",0);
Draw("TCHE"           ,"#bf{TCHE Discriminator}",1);
Draw("TCHE"           ,"#bf{TCHE Discriminator}",0);
Draw("discri_ssche0",      "#bf{SSVHE Discriminator}", 1);
Draw("discri_ssche0",      "#bf{SSVHE Discriminator}", 0);
Draw("SSV",      "#bf{SSVHE Discriminator}", 1);
Draw("track_multi"  ,      "#bf{Number of tracks in the jets}",0);
Draw("trk_multi_sel"  ,    "#bf{Number of selected tracks in the jets}",0);
Draw("track_nHit" ,      "#bf{Number of hits}",0);
Draw("track_HPix"   ,      "#bf{Number of hits in the Pixel}",0);

Draw("track_nHitStrip"   ,      "Number of hits in the Strip",0);
Draw("track_nHitTIB"   ,      "Number of hits in the TIB",0);
Draw("track_nHitTID"   ,      "Number of hits in the TID",0);
Draw("track_nHitTOB"   ,      "Number of hits in the TOB",0);
Draw("track_nHitTEC"   ,      "Number of hits in the TEC",0);
Draw("track_nHitPXB"   ,      "Number of hits in the PXB",0);
Draw("track_nHitPXF"   ,      "Number of hits in the PXF",0);

Draw("track_len"     ,     "#bf{Track decay length}",1);
Draw("track_dist"    , "Tracks/0.0008",     "#bf{Track distance to the jet axis}"   ,1, -1);
Draw("track_dz"     ,      "#bf{Track IP_dz}",1);
Draw("track_pt"     ,      "#bf{Track p_{T}}",1);
Draw("track_pt15"     ,      "#bf{Track p_{T}}",1);
Draw("track_IP"    ,      "#bf{3D IP of tracks}",1);
Draw("track_IPerr"    ,      "#bf{3D IP Error of tracks}",1);
Draw("track_IPs1tr" ,      "#bf{3D IP significance of the first track}",1);
Draw("track_IPs2tr" ,      "#bf{3D IP significance of the second track}",1);
Draw("track_IPs3tr" ,      "#bf{3D IP significance of the third track}",1);
Draw("track_pt15_cut"    ,"#bf{Track p_{T} @N-1 step}",1);
Draw("track_nHit_cut"  ,"#bf{ Number of hits @N-1 step}",0);
Draw("track_chi2_cut"    ,"#bf{Normalized #chi^{2} @N-1 step}",1);
Draw("track_chi2"    ,"#bf{Normalized #chi^{2} of tracks}",1);

Draw("track_HPix_cut"     ,"#bf{number of hits in the Pixel @N-1 step }",0); 
Draw("track_len_cut"      ,"#bf{decay length @N-1 step}",            1);
Draw("track_dist_cut"     ,"#bf{distance to the jet axis @N-1 step}", 1);
Draw("track_dz_cut"      ,"bf{transverse IP @N-1 step}",1);
Draw("track_IP2D_cut"     ,"#bf{IP2D @N-1 step}",1);                     
Draw("track_IP2Ds","track_IP2Ds",0);
Draw("track_IP2Ds","track_IP2Ds",1);

Draw("sv_multi_0","#bf{Number of SV}",1);
Draw("sv_deltaR_jet","#bf{#Delta R(SV direction,jet)}",0);
//Draw("sv_flight3DSig","SVs/4", "#bf{SV 3D flight distance significance}",1, -1);
Draw("tagvarCSV_vertexmass", "SVs/0.4 GeV", "#bf{SV mass [GeV]}", 1, -1);
Draw("tagvarCSV_vertexmass3trk","#bf{SV mass (at least 3 tracks)}", 0);
Draw("tagvarCSV_vertexCategory"    ,      "#bf{Vertex category in CSVv2}",1);
Draw("tagvarCSV_trackEtaRel","#bf{Track Eta Rel}",0);
Draw("tagvarCSV_vertexNTracks","#bf{Number of tracks associated to the SV}",0);
Draw("tagvarCSV_vertexJetDeltaR","#bf{#Delta R(SV direction,jet)}",1);
//Draw("tagvarCSV_vertexmass_cat0", "SVs/0.4 GeV","#bf{SV mass [GeV]}", 0,-1);
Draw("tagvarCSV_vertexmass3trk_cat0","#bf{SV mass (at least 3 tr0acks)}", 0);
Draw("tagvarCSV_vertexJetDeltaR_cat0","#bf{#Delta R(SV direction,jet)}",0);
Draw("tagvarCSV_vertexNTracks_cat0","#bf{Number of SV tracks}",1);
Draw("tagvarCSV_2DsigFlightDist_cat0","#bf{Flight distance significance 2D}",1);
Draw("tagvarCSV_vertexJetDeltaR_cat0","#bf{#Delta R(SV,jet) }", 0);

 //For PAS february 2016

Draw("JP", "Jets/0.05", "#bf{JP Discriminator}",1);
Draw("JBP", "Jets/0.16", "#bf{JBP Discriminator}",1);
Draw("cMVAv2", "Jets/0.04", "#bf{cMVAv2 Discriminator}",1);
Draw("sv_flight3DSig","SVs/4", "#bf{SV 3D flight distance significance}",1, -1);
Draw("track_IPs"    ,"Tracks/0.7",      "#bf{3D IP significance of tracks}",1,-1);
Draw("tagvarCSV_vertexmass_cat0", "SVs/0.4 GeV","#bf{SV mass [GeV]}", 0,-1);
Draw("SoftMu"    ,  "Jets/0.02",    "#bf{SM Discriminator}",1);
Draw("SoftEl"    ,  "Jets/0.02",    "#bf{SE Discriminator}",1);
Draw("CSV","Jets/0.02", "#bf{CSVv2(AVR) Discriminator}", 1);
Draw("CSVIVF","Jets/0.02","#bf{CSVv2 Discriminator}",1);

Draw("SoftMu"    ,      "#bf{SMT Discriminator}",1);
Draw("SoftEl"    ,      "#bf{SET Discriminator}",1);
Draw("pfmuon_ip"    ,      "#bf{IP of the muon}",1);
Draw("pfmuon_deltar"    ,      "#bf{#Delta R(#mu,jet)}",1);
Draw("pfmuon_deltar"    ,      "#bf{#Delta R(#mu,jet)}",0);
Draw("pfelectron_multi","#bf{number of electrons}",1);
Draw("pfelectron_pt","#bf{pT of electrons}",1);
Draw("pfelectron_ptrel","#bf{ptrel of electrons}",0);
Draw("pfelectron_eta","#bf{eta of electrons}",0);
Draw("pfelectron_deltar","#bf{#Delta R(el,jet)}",0);
Draw("pfelectron_ip"    ,      "#bf{IP of the electrons}",1);

Draw("cTagCvsB", "#bf{C-tag CvsB Discriminator}", 1);
Draw("cTagCvsL", "#bf{C-tag CvsL Discriminator}", 1);
Draw("cTagCvsB", "#bf{C-tag CvsB Discriminator}", 0);
Draw("cTagCvsL", "#bf{C-tag CvsL Discriminator}", 0);
}
