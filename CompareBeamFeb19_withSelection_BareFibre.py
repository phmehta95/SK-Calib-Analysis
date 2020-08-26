import ROOT
from array import array

def GetBackgroundFunction(hB1,hB2,hB3,hB4,hB5):
    binCenters = array('d',[])
    binBackground = array('d',[])
    binCount = array('d',[])
    #Set the initial values for the bin centres
    for i in range(hB1.GetNbinsX()+1):
        binCenters.append(hB1.GetBinCenter(i))
        binBackground.append(0.0) # start by setting the background bin to 0 contents
        binCount.append(0.0)
    for i in range(hB1.GetNbinsX()+1):
        cent = hB1.GetBinCenter(i)
        if cent<0.0: # For B1, background is below 0cm
            index = binCenters.index(cent)
            binBackground[index] = binBackground[index] + hB1.GetBinContent(i)
            binCount[index] = binCount[index] + 1
    for i in range(hB2.GetNbinsX()+1):
        cent = hB2.GetBinCenter(i)
        if cent<-500.0: # For B2, background is below -500cm
            index = binCenters.index(cent)
            binBackground[index] = binBackground[index] + hB2.GetBinContent(i)
            binCount[index] = binCount[index] + 1
    for i in range(hB3.GetNbinsX()+1):
        cent = hB3.GetBinCenter(i)
        if cent<-1000.0 or cent>1000.0: # For B2, background is below -1000cm or above 1000cm
            index = binCenters.index(cent)
            binBackground[index] = binBackground[index] + hB3.GetBinContent(i)
            binCount[index] = binCount[index] + 1
    for i in range(hB4.GetNbinsX()+1):
        cent = hB4.GetBinCenter(i)
        if cent>500.0: # For B2, background is above 500cm
            index = binCenters.index(cent)
            binBackground[index] = binBackground[index] + hB4.GetBinContent(i)
            binCount[index] = binCount[index] + 1
    for i in range(hB5.GetNbinsX()+1):
        cent = hB5.GetBinCenter(i)
        if cent>0.0: # For B2, background is above 0cm
            index = binCenters.index(cent)
            binBackground[index] = binBackground[index] + hB5.GetBinContent(i)
            binCount[index] = binCount[index] + 1

    # Now divide each background bin by the number of entries in that bin (ie get the average)
    for i in range(len(binBackground)):
        binBackground[i] = binBackground[i]/binCount[i]
    
    return binCenters,binBackground,binCount

def SubtractBackground(hist,bkgs):
    for i in range(hist.GetNbinsX()+1):
        hist.SetBinContent(i,hist.GetBinContent(i)-bkgs[i])
    return hist

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

B1File = ROOT.TFile('/hepstore/pritchard/SuperK/SKDeploymentTests/Feb2019/KoreanLaserOpticsTest/BareFibre/B1/Completed/wtr.080186_Complete.root')
B1Hist = B1File.Get('QwZPosBeam_Scaled')
B2File = ROOT.TFile('/hepstore/pritchard/SuperK/SKDeploymentTests/Feb2019/KoreanLaserOpticsTest/BareFibre/B2/Completed/wtr.080187_Complete.root')
B2Hist = B2File.Get('QwZPosBeam_Scaled')
B3File = ROOT.TFile('/hepstore/pritchard/SuperK/SKDeploymentTests/Feb2019/KoreanLaserOpticsTest/BareFibre/B3/Completed/wtr.080188_Complete.root')
B3Hist = B3File.Get('QwZPosBeam_Scaled')
B4File = ROOT.TFile('/hepstore/pritchard/SuperK/SKDeploymentTests/Feb2019/KoreanLaserOpticsTest/BareFibre/B4/Completed/wtr.080189_Complete.root')
B4Hist = B4File.Get('QwZPosBeam_Scaled')
B5File = ROOT.TFile('/hepstore/pritchard/SuperK/SKDeploymentTests/Feb2019/KoreanLaserOpticsTest/BareFibre/B5/Completed/wtr.080190_Complete.root')
B5Hist = B5File.Get('QwZPosBeam_Scaled')

B1Hist.SetStats(0)
B2Hist.SetStats(0)
B3Hist.SetStats(0)
B4Hist.SetStats(0)
B5Hist.SetStats(0)

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
B5Hist.SetLineColor(6)
B5Hist.SetMarkerColor(6)
B5Hist.SetMarkerStyle(8)
B5Hist.SetMarkerSize(1)

B1Hist_sub = B1Hist.Clone()
B1Hist_sub.SetName('B1Hist_sub')
B2Hist_sub = B2Hist.Clone()
B2Hist_sub.SetName('B2Hist_sub')
B3Hist_sub = B3Hist.Clone()
B3Hist_sub.SetName('B3Hist_sub')
B4Hist_sub = B4Hist.Clone()
B4Hist_sub.SetName('B4Hist_sub')
B5Hist_sub = B5Hist.Clone()
B5Hist_sub.SetName('B5Hist_sub')

## B1Hist.Fit('gaus','goff','',400,1700)
## B2Hist.Fit('gaus','goff','',0,1500)
## B3Hist.Fit('gaus','goff','',-800,600)
## B4Hist.Fit('gaus','goff','',-1200,-300)
## B5Hist.Fit('gaus','goff','',-1700,-1200)

can = ROOT.TCanvas('can','can',1200,900)
B2Hist.SetTitle('Beam spot z profile for all bare fibre injectors')
B2Hist.SetMaximum(24)
B2Hist.Draw('E1')
B3Hist.Draw('E1same')
B1Hist.Draw('E1same')
B4Hist.Draw('E1same')
B5Hist.Draw('E1same')

bins, bkgs, count = GetBackgroundFunction(B1Hist,B2Hist,B3Hist,B4Hist,B5Hist)
hBkg = ROOT.TH1F('hBkg','hBkg',51,-1800.0,1800.0)
for i in range(hBkg.GetNbinsX()+1):
    hBkg.SetBinContent(i,bkgs[i])
hBkg.SetLineColor(1)
hBkg.SetLineWidth(2)
hBkg.SetMarkerStyle(8)
hBkg.SetMarkerColor(1)
hBkg.SetMarkerSize(1)
#hBkg.Draw('same')

### Target Lines
B1Line = GetLine(injPosZ[0],1,B2Hist.GetMinimum(),B2Hist.GetMaximum())
B2Line = GetLine(injPosZ[1],2,B2Hist.GetMinimum(),B2Hist.GetMaximum())
B3Line = GetLine(injPosZ[2],8,B2Hist.GetMinimum(),B2Hist.GetMaximum())
B4Line = GetLine(injPosZ[3],4,B2Hist.GetMinimum(),B2Hist.GetMaximum())
B5Line = GetLine(injPosZ[4],6,B2Hist.GetMinimum(),B2Hist.GetMaximum())
B1Line.Draw()
B2Line.Draw()
B3Line.Draw()
B4Line.Draw()
B5Line.Draw()

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
#legend.AddEntry(hBkg, 'Background model')
legend.Draw()

### Second Canvas containing the background subtracted plots
## can2 = ROOT.TCanvas('can2','can2',1200,900)
## B1Hist_sub = SubtractBackground(B1Hist_sub,bkgs)
## B2Hist_sub = SubtractBackground(B2Hist_sub,bkgs)
## B3Hist_sub = SubtractBackground(B3Hist_sub,bkgs)
## B4Hist_sub = SubtractBackground(B4Hist_sub,bkgs)
## B5Hist_sub = SubtractBackground(B5Hist_sub,bkgs)
## hBkg_sub = hBkg.Clone()
## hBkg_sub   = SubtractBackground(hBkg_sub,bkgs)

## B1Hist_sub.Draw('E1')
## B2Hist_sub.Draw('E1same')
## B3Hist_sub.Draw('E1same')
## B4Hist_sub.Draw('E1same')
## B5Hist_sub.Draw('E1same')
## hBkg_sub.Draw('same')
## legend.Draw()

## ### B1
## canB1 = ROOT.TCanvas('canB1','canB1',1200,900)
## B1Hist.SetLineColor(1)
## B1Hist.SetMarkerColor(1)
## B1Hist.SetMaximum(B1Hist.GetMaximum()*1.2)
## B1Hist.SetMinimum(B1Hist.GetMinimum()*1.1)
## B1Hist.SetTitle('Background subtracted beam spot plot for B1 bare fibre')
## B1Line = GetLine(injPosZ[0],4,B1Hist.GetMinimum(),B1Hist.GetMaximum())
## #B1Hist.Fit('gaus','','',1000,1500)
## B1Hist.Draw('E1')
## B1Line.Draw()

## ### B2
## canB2 = ROOT.TCanvas('canB2','canB2',1200,900)
## B2Hist.SetLineColor(1)
## B2Hist.SetMarkerColor(1)
## B2Hist.SetMaximum(B2Hist.GetMaximum()*1.2)
## B2Hist.SetMinimum(B2Hist.GetMinimum()*1.1)
## B2Hist.SetTitle('Background subtracted beam spot plot for B2 bare fibre')
## B2Line = GetLine(injPosZ[1],4,B2Hist.GetMinimum(),B2Hist.GetMaximum())
## #B2Hist.Fit('gaus','','',500,1000)
## B2Hist.Draw('E1')
## B2Line.Draw()

## ### B3
## canB3 = ROOT.TCanvas('canB3','canB3',1200,900)
## B3Hist.SetLineColor(1)
## B3Hist.SetMarkerColor(1)
## B3Hist.SetMaximum(B3Hist.GetMaximum()*1.2)
## B3Hist.SetMinimum(B3Hist.GetMinimum()*1.1)
## B3Hist.SetTitle('Background subtracted beam spot plot for B3 bare fibre')
## B3Line = GetLine(injPosZ[2],4,B3Hist.GetMinimum(),B3Hist.GetMaximum())
## #B3Hist.Fit('gaus','','',-500,0)
## B3Hist.Draw('E1')
## B3Line.Draw()

## ### B4
## canB4 = ROOT.TCanvas('canB4','canB4',1200,900)
## B4Hist.SetLineColor(1)
## B4Hist.SetMarkerColor(1)
## B4Hist.SetMaximum(B4Hist.GetMaximum()*1.2)
## B4Hist.SetMinimum(B4Hist.GetMinimum()*1.1)
## B4Hist.SetTitle('Background subtracted beam spot plot for B4 bare fibre')
## B4Line = GetLine(injPosZ[3],4,B4Hist.GetMinimum(),B4Hist.GetMaximum())
## #B4Hist.Fit('gaus','','',-1000,-500)
## B4Hist.Draw('E1')
## B4Line.Draw()

## ### B5
## canB5 = ROOT.TCanvas('canB5','canB5',1200,900)
## B5Hist.SetLineColor(1)
## B5Hist.SetMarkerColor(1)
## B5Hist.SetMaximum(B5Hist.GetMaximum()*1.2)
## B5Hist.SetMinimum(B5Hist.GetMinimum()*1.1)
## B5Hist.SetTitle('Background subtracted beam spot plot for B5 bare fibre')
## B5Line = GetLine(injPosZ[4],4,B5Hist.GetMinimum(),B5Hist.GetMaximum())
## #B5Hist.Fit('gaus','','',-1500,-1200)
## B5Hist.Draw('E1')
## B5Line.Draw()
