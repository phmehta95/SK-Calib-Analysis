import ROOT
from ROOT import TH1F
from ROOT import TF1
from ROOT import TMath
from array import array
import math
from ROOT import gROOT
from ROOT import TFormula


B1File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_zoom_full/Run_081987_Complete.root')
B1Hist = B1File.Get('QwZPosBeam')
B2File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_new/Run_081988_Complete.root')
B2Hist = B2File.Get('QwPosBeamY')
B3File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_new/Run_081989_Complete.root')
B3Hist = B3File.Get('QwPosBeamY')
B4File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_new/Run_081990_Complete.root')
B4Hist = B4File.Get('QwPosBeamY')
B5File = ROOT.TFile('/hepstore/pmehta/data/Sept_2019/Collimator/Completed_new/Run_081991_Complete.root')
B5Hist = B5File.Get('QwPosBeamY')

#/////////////////////
#// For Breit-Wigner//
#////////////////////

#bw =  TF1("mybw",mybw,960, 1500, 3);
#bw.SetParameter(0,1.0)   
#bw.SetParName(0,"const")
#bw.SetParameter(2,50)    
#bw.SetParName(1,"sigma")
#bw.SetParameter(1,1224)  
#bw.SetParName(2,"mean")




#fit_Lorentzian = TF1('fit_Lorentzian', '0.5*[0]*[1]/TMath::Pi())/TMath::Max(1.e-10,(x[0]-[2])*(x[0]-[2])+ .25*[1]*[1]')
#fit_Lorentzian.SetParameters(1.0, 1.0, 1,0)

#Lorenzian Peak function
#def function_lorentzian(x,p):
    #return (0.5*[0]/((TMath.Pi()*((x-[1])*(x-[1])))+ .25*[0]*[0]))

fit_lorentzian = TF1('fit_lorentzian', 'TMath::BreitWigner(x, [1], [0])', 960.0, 1500.0)
fit_lorentzian.SetParameters(50.0, 1224.0)
#fit_lorentzian.SetParameters(0,1)
fit_lorentzian.SetLineColor(4)

B1Hist.Fit('gaus','','',960.0,1500.0)
B1Hist.Fit('fit_lorentzian','+')
#B1Hist.Fit('gaus','','',-1000,0)
#B2Hist.Fit('gaus','','',600,900)
#B1Hist.Fit('gaus','','',-1000,0)
#B3Hist.Fit('gaus','','',-300,-100)
#B1Hist.Fit('gaus','','',-1000,0)
#B4Hist.Fit('gaus','','',-850,-600)
#B1Hist.Fit('gaus','','',-1000,0)
#B5Hist.Fit('gaus','','',-1500,-1300)
#B1Hist.Fit('gaus','','',-1000,0)

#p[1] = 210
#p[2] = 1223.9
#Lorenzian Peak function
#def function_lorentzian(x,p)
#return (0.5*p[1])/(TMath::Pi()*
#(x[0]-p[2])*(x[0]-p[2])
#+ .25*p[1]*p[1]);
#}
#fit_Lorentzian = TF1('fit_Lorentzian', 'function_lorentzian', 960, 1500)
#fit_Lorentzian.SetParameters(210, , 1.0)



can = ROOT.TCanvas('can','can',1200,900)
B1Hist.SetStats(0)
B1Hist.SetFillStyle(0)
B1Hist.SetLineColor(1)
B1Hist.SetMarkerColor(1)
B1Hist.GetYaxis().SetTitleOffset(1.3)
B1Hist.SetMarkerStyle(8)
B1Hist.SetMarkerSize(0.5)
B1Hist.Draw('E1')

can2 = ROOT.TCanvas('can2','can2',1200,900)
B2Hist.SetStats(0)
B2Hist.SetFillStyle(0)
B2Hist.SetLineColor(1)
B2Hist.SetMarkerColor(1)
B2Hist.GetYaxis().SetTitleOffset(1.3)
B2Hist.SetMarkerStyle(8)
B2Hist.SetMarkerSize(0.5)
B2Hist.Draw('E1')

can3 = ROOT.TCanvas('can3','can3',1200,900)
B3Hist.SetStats(0)
B3Hist.SetFillStyle(0)
B3Hist.SetLineColor(1)
B3Hist.SetMarkerColor(1)
B3Hist.GetYaxis().SetTitleOffset(1.3)
B3Hist.SetMarkerStyle(8)
B3Hist.SetMarkerSize(0.5)
B3Hist.Draw('E1')

can4 = ROOT.TCanvas('can4','can4',1200,900)
B4Hist.SetStats(0)
B4Hist.SetFillStyle(0)
B4Hist.SetLineColor(1)
B4Hist.SetMarkerColor(1)
B4Hist.GetYaxis().SetTitleOffset(1.3)
B4Hist.SetMarkerStyle(8)
B4Hist.SetMarkerSize(0.5)
B4Hist.Draw('E1')

can5 = ROOT.TCanvas('can5','can5',1200,900)
B5Hist.SetStats(0)
B5Hist.SetFillStyle(0)
B5Hist.SetLineColor(1)
B5Hist.SetMarkerColor(1)
B5Hist.GetYaxis().SetTitleOffset(1.6)
B5Hist.SetMarkerStyle(8)
B5Hist.SetMarkerSize(0.5)
B5Hist.Draw('E1')

legend = ROOT.TLegend(0.59,0.67,0.88,0.87)
legend.SetFillStyle(1001)
legend.SetFillColor(0)
legend.SetLineColor(1)
legend.SetLineStyle(1)
legend.AddEntry(B1Hist, 'B1 data')
legend.AddEntry(B2Hist, 'B2 data')
legend.AddEntry(B3Hist, 'B3 data')
legend.AddEntry(B4Hist, 'B4 data')
legend.AddEntry(B5Hist, 'B5 data')
#legend.Draw()
