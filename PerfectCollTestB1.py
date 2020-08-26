import ROOT
from array import array
from ROOT import TMath
from ROOT import TH1F, TF1, TLine
import math

#Comparing B4 Warwick MC with Sept Data -z profile
B1File = ROOT.TFile("/user/pmehta/B1_warwick_coll_mie_off/B1_warwick_mie_off_Completed.root")
#B2File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_zoom_full__y_rebin/Run_081987_Complete.root')
#B1Hist = B1File.Get('QwPosBeam')
B1Hist = B1File.Get('QwZPosBeam')
B1Hist.SetStats(0)
B1Hist.SetFillStyle(0)
B1Hist.SetMarkerStyle(8)
B1Hist.SetMarkerSize(1)
B1Line = TLine(1302.95,0.0,1302.95,300000.0)
B1Line.SetLineColor(4)
B1Line.SetLineWidth(3)
B1Line.SetLineStyle(9)
#B1Line.Draw()
#B2Hist.SetStats(0)
#B2Hist.SetFillStyle(0)
#B2Hist.SetMarkerStyle(8)
#B2Hist.SetMarkerSize(2)
#B2Hist.SetMarkerColor(2)
can = ROOT.TCanvas('can','can',1200,900)
B1Hist.SetTitle('Charge weighted beam spot z profile for B1 collimator (Mie scattering turned off) -  Warwick collimator data')
B1Hist.SetMaximum(300000)
B1Hist.SetMinimum(0)
B1Hist.Draw('E1')
B1Line.Draw()
#B1Hist.Fit('gaus','','',-800,-500)
