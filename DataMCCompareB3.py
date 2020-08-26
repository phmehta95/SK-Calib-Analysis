import ROOT
from array import array
from ROOT import TMath
from ROOT import TH1F, TF1, TLine
import math
 
#Comparing B4 MC with Sept Data -z profile
B1File = ROOT.TFile("/user/pmehta/Completed_MC_zoom_sk5/435.mc.pos5.1.7_0.8_0.5_10.dat_Completed.root")
B2File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_zoom_full__y_rebin/Run_081990_Complete.root')
B1Hist = B1File.Get('QwZPosBeam')
B2Hist = B2File.Get('QwZPosBeam')
B1Hist.SetStats(0)
B1Hist.SetFillStyle(0)
B1Hist.SetMarkerStyle(8)
B1Hist.SetMarkerSize(2)
B2Hist.SetStats(0)
B2Hist.SetFillStyle(0)
B2Hist.SetMarkerStyle(8)
B2Hist.SetMarkerSize(2)
B2Hist.SetMarkerColor(2)
can = ROOT.TCanvas('can','can',1200,900)
B1Hist.SetTitle('Overlayed beam spot z profile for B4 collimator for MC and September data')
B1Hist.SetMaximum(12000000)
B1Hist.SetMinimum(0)
B1Hist.DrawNormalized('E1')
B2Hist.DrawNormalized('SAME')
#B1Line = TLine(-676.65,0.0,-676.65,12000000.0)
B1Line = TLine(-676.65,0.0,-676.65,0.53)
B1Line.SetLineColor(4)
B1Line.SetLineWidth(3)
B1Line.SetLineStyle(9)
B1Line.Draw()
B1Hist.SetName("B1Hist")
B2Hist.SetName("B2Hist")
legend = ROOT.TLegend(0.12,0.75,0.3,0.9)
legend.AddEntry(B1Hist,"B4 MC","lp")
legend.AddEntry(B2Hist,"September data","lp")
legend.Draw()

#Comparing B4 MC with Sept Data -y profile
B3File = ROOT.TFile("/user/pmehta/Completed_MC_zoom_sk5/435.mc.pos5.1.7_0.8_0.5_10.dat_Completed.root")
B4File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_zoom_full__y_rebin/Run_081990_Complete.root')
B3Hist = B1File.Get('QwPosBeamY')
B4Hist = B2File.Get('QwPosBeamY')
B3Hist.SetStats(0)
B3Hist.SetFillStyle(0)
B3Hist.SetMarkerStyle(8)
B3Hist.SetMarkerSize(2)
B4Hist.SetStats(0)
B4Hist.SetFillStyle(0)
B4Hist.SetMarkerStyle(8)
B4Hist.SetMarkerSize(2)
B4Hist.SetMarkerColor(2)
can1 = ROOT.TCanvas('can1','can1',1200,900)
B3Hist.SetTitle('Overlayed beam spot y profile for B4 collimator for MC and September data')
B3Hist.SetMaximum(12000000)
B3Hist.SetMinimum(0)
B3Hist.DrawNormalized('E1')
B4Hist.DrawNormalized('SAME')
#B1Line = TLine(-676.65,0.0,-676.65,12000000.0)
B3Line = TLine(-768.14,0.0,-768.14,0.53)
B3Line.SetLineColor(4)
B3Line.SetLineWidth(3)
B3Line.SetLineStyle(9)
B3Line.Draw()
B3Hist.SetName("B3Hist")
B4Hist.SetName("B4Hist")
legend1 = ROOT.TLegend(0.12,0.75,0.3,0.9)
legend1.AddEntry(B3Hist,"B4 MC","lp")
legend1.AddEntry(B4Hist,"September data","lp")
legend1.Draw()
