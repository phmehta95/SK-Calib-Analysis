import ROOT
from array import array
import math
import argparse
import sys
import os
import analysisFuncs as F
import getConsts as Consts
import getPlots as Plots

def GetHist(name,title):
    h = ROOT.TH1F(name,name,60,0,12)
    h.SetTitle(title)
    #h.SetStats(0)
    h.SetLineColor(1)
    h.SetMarkerColor(1)
    return h

infile = '/hepstore/pritchard/SuperK/wtr.080434.root'
inTree = ROOT.TChain('tqtree')
inTree.AddFile(infile)

### The individual timing cuts for each of the 19 channels
### These were found by considering a plot of charge vs time
timeCuts = [['h1','Board 1, Channel 1', 295, 315],
            ['h2','Board 1, Channel 2', 550, 570],
            ['h3','Board 1, Channel 3', 600, 620],
            ['h4','Board 1, Channel 4', 680, 700],
            ['h5','Board 1, Channel 5', 750, 770],
            ['h6','Board 1, Channel 6', 960, 980],
            ['h7','Board 1, Channel 7', 1015, 1025],
            ['h8','Board 1, Channel 8', 1055, 1070],
            ['h9','Board 2, Channel 1', 1100, 1120],
            ['h10','Board 2, Channel 2', 1160, 1180],
            ['h11','Board 2, Channel 3', 1230, 1250],
            ['h12','Board 2, Channel 4', 1270, 1290],
            ['h13','Board 2, Channel 5', 1320, 1340],
            ['h14','Board 2, Channel 6', 1400, 1420],
            ['h15','Board 2, Channel 7', 1450, 1470],
            ['h16','Board 2, Channel 8', 1540, 1560],
            ['h17','Spare channel 1', 1670, 1690],
            ['h18','Spare channel 2', 1710, 1730],
            ['h19','Spare channel 3', 1775, 1782]]

### Empty lists to store the histogram, mean, sigma, and associated uncertainties
### for each of the 19 monitor fibres
hists = []
means = []
meanErrs = []
sigmas = []
sigmaErrs = []

can = ROOT.TCanvas('can','can',1200,900)
can.Divide(5,4)
for i in range(len(timeCuts)):
    can.cd(i+1)
    h = GetHist(timeCuts[i][0],timeCuts[i][1])
    ### Plot the charge distribution for our monitor QBEE channel (11256)
    inTree.Draw('mon_charge_vec>>'+timeCuts[i][0],'mon_cable_vec==11256 && totSeconds>'+str(timeCuts[i][2])+'&&totSeconds<'+str(timeCuts[i][3]),'E1')
    hists.append(h)
    h.Fit('gaus','','E1')
    gauss = h.GetFunction('gaus')
    means.append(gauss.GetParameter(1))
    meanErrs.append(gauss.GetParError(1))
    sigmas.append(gauss.GetParameter(2))
    sigmaErrs.append(gauss.GetParError(2))
    can.Update()

for i in range(len(means)):
    print i,means[i],meanErrs[i],sigmas[i],sigmaErrs[i]
