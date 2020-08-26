import ROOT
from array import array
from ROOT import TMath
from ROOT import TH1F, TF1, TLine
import math

#Read in files with different sigbm values
B1File = ROOT.TFile("/hepstore/pmehta/sigbm_test/Sigbm1000_new/Completed_sigbm_test/435.mc.pos5.1.7_0.8_0.5_10.dat_Completed.root")
B2File = ROOT.TFile("/hepstore/pmehta/sigbm_test/Sigbm2000/Completed_sigbm_test/435.mc.pos5.1.7_0.8_0.5_10.dat_Completed.root")
#B3File = ROOT.TFile("/hepstore/pmehta/sigbm_test/Sigbm3000/Completed_sigbm_test/435.mc.pos5.1.7_0.8_0.5_10.dat_Completed.root")
#B4File = ROOT.TFile("/hepstore/pmehta/sigbm_test/Sigbm4000/Completed_sigbm_test/435.mc.pos5.1.7_0.8_0.5_10.dat_Completed.root")
#B5File = ROOT.TFile("/hepstore/pmehta/sigbm_test/Sigbm5000/Completed_sigbm_test/435.mc.pos5.1.7_0.8_0.5_10.dat_Completed.root")
#B6File = ROOT.TFile("/hepstore/pmehta/sigbm_test/Sigbm6000/Completed_sigbm_test/435.mc.pos5.1.7_0.8_0.5_10.dat_Completed.root")
#B7File = ROOT.TFile("/hepstore/pmehta/sigbm_test/Sigbm7000/Completed_sigbm_test/435.mc.pos5.1.7_0.8_0.5_10.dat_Completed.root")
#B8File = ROOT.TFile("/hepstore/pmehta/sigbm_test/Sigbm8000/Completed_sigbm_test/435.mc.pos5.1.7_0.8_0.5_10.dat_Completed.root")
#B9File = ROOT.TFile("/hepstore/pmehta/sigbm_test/Sigbm000/Completed_sigbm_test/435.mc.pos5.1.7_0.8_0.5_10.dat_Completed.root")
#B10File = ROOT.TFile("/hepstore/pmehta/sigbm_test/Sigbm5000/Completed_sigbm_test/435.mc.pos5.1.7_0.8_0.5_10.dat_Completed.root")

#Get z-posiiton beam profile plots
B1Hist = B1File.Get('QwPosBeam')
B2Hist = B2File.Get('QwPosBeam')
#B3Hist = B3File.Get('QwPosBeam')
#B4Hist = B4File.Get('QwPosBeam')
#B5Hist = B5File.Get('QwPosBeam')
#B6Hist = B6File.Get('QwPosBeam')
#B7Hist = B7File.Get('QwPosBeam')
#B8Hist = B8File.Get('QwPosBeam')
#B9Hist = B9File.Get('QwZPosBeam')
#B10Hist = B10File.Get('QwZPosBeam')

#Set histogram contents for B1File
B1Hist.SetStats(0)
B1Hist.SetFillStyle(0)
B1Hist.SetMarkerStyle(8)
B1Hist.SetMarkerSize(1)

#Set histogram contents for B2File
B2Hist.SetStats(0)
B2Hist.SetFillStyle(0)
B2Hist.SetMarkerStyle(8)
B2Hist.SetMarkerSize(1)
B2Hist.SetMarkerColor(2)
"""
#Set histogram contents for B3File
B3Hist.SetStats(0)
B3Hist.SetFillStyle(0)
B3Hist.SetMarkerStyle(8)
B3Hist.SetMarkerSize(1)
B3Hist.SetMarkerColor(3)
#Set histogram contents for B4File
B4Hist.SetStats(0)
B4Hist.SetFillStyle(0)
B4Hist.SetMarkerStyle(8)
B4Hist.SetMarkerSize(1)
B4Hist.SetMarkerColor(4)
#Set histogram contents for B5File
B5Hist.SetStats(0)
B5Hist.SetFillStyle(0)
B5Hist.SetMarkerStyle(8)
B5Hist.SetMarkerSize(1)
B5Hist.SetMarkerColor(5)
#Set histogram contents for B6File
B6Hist.SetStats(0)
B6Hist.SetFillStyle(0)
B6Hist.SetMarkerStyle(8)
B6Hist.SetMarkerSize(1)
B6Hist.SetMarkerColor(6)
#Set histogram contents for B7File
B7Hist.SetStats(0)
B7Hist.SetFillStyle(0)
B7Hist.SetMarkerStyle(8)
B7Hist.SetMarkerSize(1)
B7Hist.SetMarkerColor(7)
#Set histogram contents for B8File
B8Hist.SetStats(0)
B8Hist.SetFillStyle(0)
B8Hist.SetMarkerStyle(8)
B8Hist.SetMarkerSize(1)
B8Hist.SetMarkerColor(8)
#Set histogram contents for B9File
#B9Hist.SetStats(0)
#B9Hist.SetFillStyle(0)
#B9Hist.SetMarkerStyle(8)
#B9Hist.SetMarkerSize(1)
#B9Hist.SetMarkerColor(9)
#Set histogram contents for B10File
#B10Hist.SetStats(0)
#B10Hist.SetFillStyle(0)
#B10Hist.SetMarkerStyle(8)
#B10Hist.SetMarkerSize(1)
#B10Hist.SetMarkerColor(11)
"""
#Make histogram canvas and draw histograms
can = ROOT.TCanvas('can','can',1200,900)
B1Hist.SetTitle('Overlayed beam spot z profile for B4 MC with different sigbm values')
B1Hist.Fit("gaus","","",-1700,1700)
B1Hist.Draw('E1')
B1Line = TLine(-676.65,0.0,-676.65,185000.0)
B1Line.SetLineColor(4)
B1Line.SetLineWidth(3)
B1Line.SetLineStyle(9)
B1Line.Draw()

B2Hist.Fit("gaus","","",-1700,1700)
B2Hist.Draw('E1''SAME')
"""
B3Hist.Draw('SAME')
B4Hist.Draw('SAME')
B5Hist.Draw('SAME')
B6Hist.Draw('SAME')
B7Hist.Draw('SAME')
B8Hist.Draw('SAME')
#B9Hist.Draw('SAME')
#B10Hist.Draw('SAME')

#Make legend
B1Hist.SetName("B1Hist")
B2Hist.SetName("B2Hist")
B3Hist.SetName("B3Hist")
B4Hist.SetName("B4Hist")
B5Hist.SetName("B5Hist")
B6Hist.SetName("B6Hist")
B7Hist.SetName("B7Hist")
B8Hist.SetName("B8Hist")
#B9Hist.SetName("B9Hist")
#B10Hist.SetName("B10Hist")

#legend = ROOT.TLegend(0.12,0.75,0.3,0.9)
#legend.AddEntry(B1Hist,"Sigbm25","lp")
#legend.AddEntry(B2Hist,"Sigbm50","lp")
#legend.AddEntry(B2Hist,"Sigbm100","lp")
#legend.AddEntry(B2Hist,"Sigbm200","lp")
#legend.AddEntry(B2Hist,"Sigbm300","lp")
#legend.AddEntry(B2Hist,"Sigbm400","lp")
#legend.AddEntry(B2Hist,"Sigbm500","lp")
#legend.AddEntry(B2Hist,"Sigbm600","lp")
#legend.AddEntry(B2Hist,"Sigbm1000","lp")
#legend.AddEntry(B2Hist,"Sigbm5000","lp")
#legend.Draw()
"""
