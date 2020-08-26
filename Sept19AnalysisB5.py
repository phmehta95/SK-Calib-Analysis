import ROOT
from array import array
from ROOT import TMath
from ROOT import TH1F, TF1, TLine
import math

#B5File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_zoom_full_1000_events/Run_081991_Complete.root')
#B5File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_zoom_1000_events_y_rebin/Run_081991_Complete.root')
#B5File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_zoom_full__y_rebin/Run_081991_Complete.root')           
#B5File = ROOT.TFile('/hepstore/pmehta/data/RootFilesNov19/Collimator/Completed/Run_082185_Complete.root')
#B5Hist = B5File.Get('QwZPosBeam')
#B5Hist = B5File.Get('QwPosBeamY')
#B5Hist.SetStats(0)
#B5Hist.SetLineColor(6)
#B5Hist.SetMarkerColor(6)
#B5Hist.SetMarkerStyle(8)
#B5Hist.SetMarkerSize(1)
#B5Hist.Fit('gaus','goff','',-1700.0,-1250.0)

#B5
#can = ROOT.TCanvas('can','can',1200,900)
#B5Hist.SetTitle('Beam spot z profile for B5 collimator injector')
#B5Hist.Fit('gaus','goff','',1000,1500)
#B5Hist.SetTitle('Beam spot y profile for B5 collimator injector')
#B5Hist.Draw('E1')
#B1Hist.SetMaximum(35.0)
#B5Hist.SetMaximum(100000)
#B5Hist.SetMaximum(1000000)
#B5Hist.SetMinimum(0)
#B5Hist.Draw('E1')
#B5Line = TLine(-1312.95,0.0,-1312.95,100000.0)
#B5Line = TLine(-1312.95,0.0,-1312.95,1000000.0) #expected z position
#B5Line = TLine(-768.14,0.0,-768.14,1000000.0) #expected y position
#B5Line = GetLine(injPosZ[0],1,B1Hist.GetMinimum(),B1Hist.GetMaximum())
#B5Line.SetLineColor(4)
#B5Line.SetLineWidth(3)
#B5Line.SetLineStyle(9)
#B5Line.Draw()

#Overlayed histograms z profile to ensure no change in Nov/sept data                                                                                                                                              
                                                                                                                                                                                                                   
B2File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_zoom_full__y_rebin/Run_081991_Complete.root')
B3File = ROOT.TFile('/hepstore/pmehta/data/RootFilesNov19/Collimator/Completed_100000/Run_082185_Complete.root')
B2Hist = B2File.Get('QwZPosBeam')
B3Hist = B3File.Get('QwZPosBeam')

B2Hist.SetStats(0)
B2Hist.SetFillStyle(0)
B2Hist.SetMarkerStyle(8)
B2Hist.SetMarkerSize(1)
B3Hist.SetStats(0)
B3Hist.SetFillStyle(0)
B3Hist.SetMarkerStyle(8)
B3Hist.SetMarkerSize(1)
B3Hist.SetMarkerColor(2)
can = ROOT.TCanvas('can','can',1200,900)
B2Hist.SetTitle('Overlayed beam spot z profile for B5 collimator Sept and Nov data')
B2Hist.SetMaximum(1000000)
B2Hist.SetMinimum(0)
B2Hist.Draw('E1')
B3Hist.Draw('SAME')
B2Line = TLine(-1312.95,0.0,-1312.95,1000000.0)
B2Line.SetLineColor(4)
B2Line.SetLineWidth(3)
B2Line.SetLineStyle(9)
B2Line.Draw()
B2Hist.SetName("B2Hist")
B3Hist.SetName("B3Hist")
legend1 = ROOT.TLegend(0.12,0.75,0.3,0.9)
legend1.AddEntry("B2Hist","September data","lp")
legend1.AddEntry("B3Hist","November data","lp")
legend1.Draw()

#Overlayed histograms y profile to ensure no change in Nov/sept data                                                                                                                                              

B4File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_zoom_full__y_rebin/Run_081991_Complete.root')
B5File = ROOT.TFile('/hepstore/pmehta/data/RootFilesNov19/Collimator/Completed_100000/Run_082185_Complete.root')
B4Hist = B2File.Get('QwPosBeamY')
B5Hist = B3File.Get('QwPosBeamY')

B4Hist.SetStats(0)
B4Hist.SetFillStyle(0)
B4Hist.SetMarkerStyle(8)
B4Hist.SetMarkerSize(1)
B5Hist.SetStats(0)
B5Hist.SetFillStyle(0)
B5Hist.SetMarkerStyle(8)
B5Hist.SetMarkerSize(1)
B5Hist.SetMarkerColor(2)
can2 = ROOT.TCanvas('can2','can2',1200,900)
B4Hist.SetTitle('Overlayed beam spot y profile for B5 collimator Sept and Nov data')
B4Hist.SetMaximum(1000000)
B4Hist.SetMinimum(0)
B4Hist.Draw('E1')
B5Hist.Draw('SAME')
B4Line = TLine(-768.14,0.0,-768.14,1000000.0)
B4Line.SetLineColor(4)
B4Line.SetLineWidth(3)
B4Line.SetLineStyle(9)
B4Line.Draw()
B4Hist.SetName("B4Hist")
B5Hist.SetName("B5Hist")
legend = ROOT.TLegend(0.12,0.75,0.3,0.9)
legend.AddEntry("B4Hist","September data","lp")
legend.AddEntry("B5Hist","November data","lp")
legend.Draw()
