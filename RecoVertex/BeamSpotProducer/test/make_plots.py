import ROOT
import copy

ROOT.gROOT.SetBatch(True)

flavors = ['vanilla', 'fake', 'fake_covariance', 'fake_position']

variables = ['Chi2Prob_GenTk', 'AbsDistanceOfClosestApproachToBS_GenTk', 'Chi2_GenTk',
            'Chi2oNDFVsEta_ImpactPoint_GenTk', 'Chi2oNDFVsNHits_ImpactPoint_GenTk', 'Chi2oNDFVsPt_ImpactPoint_GenTk']

for var in variables:
    histos = []
    leg = ROOT.TLegend()
    col = 1
    for flavor in flavors:
        infile = ROOT.TFile(flavor+'_141.002/DQM_V0001_R000366727__Global__CMSSW_X_Y_Z__RECO.root')
        histo = infile.Get('DQMData/Run 366727/HLT/Run summary/Tracking/tracks/GeneralProperties/'+var)
        histo = copy.deepcopy(histo)
        histo.SetLineColor(col)
        histo.SetLineWidth(2)
        histos.append(histo)
        leg.AddEntry(histo, flavor, "l")

        #print("color:", col)
        #print("histo entries:", histo.GetEntries())
        col+=1

    can = ROOT.TCanvas()
    for hist in histos:
        hist.Draw("hist same")
    leg.Draw("same")    
    can.SaveAs("plots/"+var+".png")

#    import pdb; pdb.set_trace()


