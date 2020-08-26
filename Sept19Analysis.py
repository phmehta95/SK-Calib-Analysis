import ROOT
from array import array
from ROOT import TMath
from ROOT import TH1F, TF1, TLine
import math

### Short function for drawing lines on plots at constant x
def GetLine(val,colour,mini,maxi):
    ymax = maxi
    ymin = mini
    line = ROOT.TLine(val,ymin,val,ymax)
    line.SetLineColor(colour)
    line.SetLineWidth(5)
    line.SetLineStyle(2)
    return line

injPosZ = [1302.95,666.65,-111.05,-676.65,-1312.95]



B1File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_zoom_full/Run_081987_Complete.root')
B1Hist = B1File.Get('QwZPosBeam')
#B2File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_zoom_full/Run_081988_Complete.root')
#B2Hist = B2File.Get('QwZPosBeam')
#B3File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_zoom_full/Run_081989_Complete.root')
#B3Hist = B3File.Get('QwZPosBeam')
#B4File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_zoom_full/Run_081990_Complete.root')
#B4Hist = B4File.Get('QwZPosBeam')
#B5File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_zoom_full/Run_081991_Complete.root')
#B5Hist = B5File.Get('QwZPosBeam')

B1Hist.SetStats(0)
B2Hist.SetStats(0)
B3Hist.SetStats(0)
B4Hist.SetStats(0)
#B5Hist.SetStats(0)

B1Hist.SetFillStyle(0)
B1Hist.SetMarkerStyle(8)
B1Hist.SetMarkerSize(1)
B2Hist.SetLineColor(2)
B2Hist.SetMarkerColor(2)
B2Hist.SetMarkerStyle(8)
B2Hist.SetMarkerSize(1)
B3Hist.SetLineColor(8)
B3Hist.SetMarkerColor(8)
B3Hist.SetMarkerStyle(8)
B3Hist.SetMarkerSize(1)
B4Hist.SetLineColor(4)
B4Hist.SetMarkerColor(4)
B4Hist.SetMarkerStyle(8)
B4Hist.SetMarkerSize(1)
#B5Hist.SetLineColor(6)
#B5Hist.SetMarkerColor(6)
#B5Hist.SetMarkerStyle(8)
#B5Hist.SetMarkerSize(1)
B1Hist.Fit('gaus','goff','',1000,1500)
B2Hist.Fit('gaus','goff','',500,1000)
B3Hist.Fit('gaus','goff','',-400,-20)
B4Hist.Fit('gaus','goff','',-1110, -380)

#Fitting zoomed in data 16/12/19
#B1
can = ROOT.TCanvas('can','can',1200,900)
B1Hist.SetTitle('Beam spot z profile for B1 collimator injector')
#B1Hist.Fit('gaus','goff','',1000,1500)
#B1Hist.SetTitle('Beam spot y profile for all collimator injectors')
#B1Hist.Draw('E1')
#B1Hist.SetMaximum(35.0)
B1Hist.SetMaximum(10000000)
B1Hist.SetMinimum(0)
B1Hist.Draw('E1')
B1Line = TLine(1302.95,0.0,1302.95,10000000.0)
#B1Line = GetLine(injPosZ[0],1,B1Hist.GetMinimum(),B1Hist.GetMaximum())
B1Line.SetLineColor(4)
B1Line.SetLineWidth(3)
B1Line.SetLineStyle(9)
B1Line.Draw()

#B2
can2 = ROOT.TCanvas('can2','can2',1200,900)
B2Hist.SetTitle('Beam spot z profile for B2 collimator injector')
#B1Hist.Fit('gaus','goff','',1000,1500)
#B1Hist.SetTitle('Beam spot y profile for all collimator injectors')
#B1Hist.Draw('E1')
#B1Hist.SetMaximum(35.0)
B2Hist.SetMaximum(2000000)
B2Hist.SetMinimum(0)
B2Hist.Draw('E1')
B2Line = TLine(666.65,0.0,666.65,2000000.0)
#B1Line = GetLine(injPosZ[0],1,B1Hist.GetMinimum(),B1Hist.GetMaximum())
B2Line.SetLineColor(4)
B2Line.SetLineWidth(3)
B2Line.SetLineStyle(9)
B2Line.Draw()

#B3
can3 = ROOT.TCanvas('can3','can3',1200,900)
B3Hist.SetTitle('Beam spot z profile for B3 collimator injector')
#B1Hist.Fit('gaus','goff','',1000,1500)
#B1Hist.SetTitle('Beam spot y profile for all collimator injectors')
#B1Hist.Draw('E1')
#B1Hist.SetMaximum(35.0)
B3Hist.SetMaximum(400000)
B3Hist.SetMinimum(0)
B3Hist.Draw('E1')
B3Line = TLine(-111.15,0.0,-111.15,400000.0)
#B1Line = GetLine(injPosZ[0],1,B1Hist.GetMinimum(),B1Hist.GetMaximum())
B3Line.SetLineColor(4)
B3Line.SetLineWidth(3)
B3Line.SetLineStyle(9)
B3Line.Draw()

#B4
can4 = ROOT.TCanvas('can4','can4',1200,900)
B4Hist.SetTitle('Beam spot z profile for B4 collimator injector')
#B1Hist.Fit('gaus','goff','',1000,1500)
#B1Hist.SetTitle('Beam spot y profile for all collimator injectors')
#B1Hist.Draw('E1')
#B1Hist.SetMaximum(35.0)
B4Hist.SetMaximum(3000000)
B4Hist.SetMinimum(0)
B4Hist.Draw('E1')
B4Line = TLine(-676.65,0.0,-676.65,3000000.0)
#B1Line = GetLine(injPosZ[0],1,B1Hist.GetMinimum(),B1Hist.GetMaximum())
B4Line.SetLineColor(4)
B4Line.SetLineWidth(3)
B4Line.SetLineStyle(9)
B4Line.Draw()

#B5
#can = ROOT.TCanvas('can','can',1200,900)
#B1Hist.SetTitle('Beam spot z profile for B1 collimator injector')
#B1Hist.Fit('gaus','goff','',1000,1500)
#B1Hist.SetTitle('Beam spot y profile for all collimator injectors')
#B1Hist.Draw('E1')
#B1Hist.SetMaximum(35.0)
#B1Hist.SetMaximum(10000000)
#B1Hist.SetMinimum(0)
#B1Hist.Draw('E1')
#B1Line = TLine(1302.95,0.0,1302.95,10000000.0)
#B1Line = GetLine(injPosZ[0],1,B1Hist.GetMinimum(),B1Hist.GetMaximum())
#B1Line.SetLineColor(4)
#B1Line.SetLineWidth(3)
#B1Line.SetLineStyle(9)
#B1Line.Draw()

