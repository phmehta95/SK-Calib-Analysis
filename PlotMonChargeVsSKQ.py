import ROOT
from array import array
import math

# Function to calculate mean and standard deviation of an array of values
def getMeanSD(vals):
    tot = 0.0
    rms = 0.0
    for i in vals:
        tot+=float(i)
    mean = float(tot/float(len(vals)))
    # Now standard deviation
    totSD = 0.0
    for i in vals:
        totSD+=((mean-float(i))*(mean-float(i)))
    SD = math.sqrt(totSD/(float(len(vals))-1))
    
    return mean,SD

### Input file
infile = '/hepstore/pritchard/SuperK/SKDeploymentTests/July2019/CalibRuns/wtr.081411.root'

### Define some constants based on the run
SKChargeMax = 1200 # maximum charge in SK in PE, to cut outliers
eLows = [5000,40000,70000,115000,150000,195000]  # The low end event number for each intensity
eHighs = [30000,62000,105000,145000,185000,225000] # The high end event number for each intensity

tree = ROOT.TChain('tqtree')
tree.AddFile(infile)

nevents = tree.GetEntries()
#nevents = 1000

mon_channel = 11256
monCharge = array('d',[])
SKCharge = array('d',[])
event = array('d',[])

for i in range(nevents):
    tree.GetEntry(i)
    for j in range(len(tree.mon_cable_vec)):
        if tree.mon_cable_vec[j]==mon_channel:
            monQ = tree.mon_charge_vec[j]
            monCharge.append(monQ)
            # Now sum up all of the PMT hits charge
            sumQ = 0
            charges = tree.charge_vec
            for h in range(len(charges)):
                sumQ+=charges[h]
            SKCharge.append(sumQ)
            event.append(i)

### Now plot monitor charge against SK charge
can = ROOT.TCanvas('can','can',1200,900)
gr = ROOT.TGraph(len(monCharge),monCharge,SKCharge)
gr.SetMarkerStyle(8)
gr.SetMarkerSize(0.2)
gr.GetXaxis().SetTitle('Monitor reading (AU)')
gr.GetYaxis().SetTitle('Total SK ID charge (P.E.)')
gr.SetMaximum(1200)
gr.SetMinimum(0)
gr.GetYaxis().SetTitleOffset(1.3)
gr.SetTitle('Total charge in SK vs Monitor charge reading')
gr.Draw('AP')


### Following code is to plot both on the same graph with 2 y-axes
ROOT.gROOT.ForceStyle(0)
c1 = ROOT.TCanvas("c1","c1",200,10,700,500)
pad = ROOT.TPad("pad","",0,0,1,1)
pad.SetFillColor(0)
pad.SetGrid()
pad.Draw()
pad.cd()
# draw a frame to define the range
hr = c1.DrawFrame(0,0,max(event)*1.1,SKChargeMax)
hr.SetYTitle("Total charge in SK (P.E.)")
hr.SetXTitle("Event number")
hr.GetXaxis().SetTitleOffset(1.3)
pad.GetFrame().SetFillColor(0)
pad.GetFrame().SetBorderSize(12)

# Plot 1 - Monitor QBEE vs elapsed time
gr1 = ROOT.TGraph(len(event),event,SKCharge)
gr1.SetMarkerColor(1)
gr1.SetMarkerStyle(8)
gr1.SetMarkerSize(0.2)
gr1.Draw("P")

# create a transparent pad drawn on top of the main pad
c1.cd()
overlay = ROOT.TPad("overlay","",0,0,1,1)
overlay.SetFillStyle(0)
overlay.SetFillColor(0)
overlay.SetFrameFillStyle(0)
overlay.Draw("FA")
overlay.cd()

# Plot 2 - Power meter vs elapsed time
gr2 = ROOT.TGraph(len(event),event,monCharge)
gr2.SetMarkerColor(ROOT.kRed)
gr2.SetMarkerStyle(8)
gr2.SetMarkerSize(0.2)
gr2.SetName("gr2")
xmin = pad.GetUxmin()
ymin = 0
xmax = pad.GetUxmax()
ymax = max(monCharge)*1.2
hframe = overlay.DrawFrame(xmin,ymin,xmax,ymax)
hframe.GetXaxis().SetLabelOffset(99)
hframe.GetYaxis().SetTickLength(0)
hframe.GetYaxis().SetLabelOffset(99)
gr2.Draw("P")

# Draw an axis on the right side
axis = ROOT.TGaxis(xmax,ymin,xmax, ymax,ymin,ymax,510,"+L")
axis.SetLineColor(2)
axis.SetLabelColor(2)
axis.SetTitleColor(2)
axis.SetTitle('Monitor PMT reading (AU)')
axis.Draw()


### Final step is to calculate averages for the different intensities
eCent = array('d',[])
eCentErr = array('d',[])
SKAvg = array('d',[])
SKAvgErr = array('d',[])
MonQAvg = array('d',[])
MonQAvgErr = array('d',[])

for i in range(len(eLows)):
    eCent.append((float(eLows[i])-float(eHighs[i]))/2.0)
    eCentErr.append(0)
    ### make new array to use for calculating mean/rms
    SKArray = array('d',[])
    MonArray = array('d',[])
    for j in range(len(SKCharge)):
        if event[j] < eHighs[i] and event[j] > eLows[i]:
            if SKCharge[j] < SKChargeMax:
                SKArray.append(SKCharge[j])
    for k in range(len(monCharge)):
        if event[k] < eHighs[i] and event[k] > eLows[i]:
            MonArray.append(monCharge[k])
    # Use the function to calculate the mean and rms for this time period
    SKMean, SKRMS = getMeanSD(SKArray)
    MonMean, MonRMS = getMeanSD(MonArray)
    # Fill the results into the respective arrays
    SKAvg.append(SKMean)
    SKAvgErr.append(SKRMS)
    MonQAvg.append(MonMean)
    MonQAvgErr.append(MonRMS)

#canSK = ROOT.TCanvas('canSK','canSK',900,600)
## hSK = ROOT.TH1F('hSK','hSK',100,0.0,1000.0)
## hMon = ROOT.TH1F('hMon','hMon',20,1170.0,1320.0)
## for i in range(len(event)):
##     if i>eLows[3] and i<eHighs[3]:
##         hSK.Fill(SKCharge[i])
##         hMon.Fill(monCharge[i])

## canSK = ROOT.TCanvas('canSK','canSK',900,600)
## hSK.SetTitle('Charge in SK')
## hSK.SetStats(0)
## hSK.GetYaxis().SetTitleOffset(1.3)
## hSK.GetXaxis().SetTitle('Charge in SK (P.E.)')
## hSK.GetYaxis().SetTitle('Events (/10P.E.)')
## hSK.Fit('gaus')
## hSK.Draw('E1')

## canMon = ROOT.TCanvas('canMon','canMon',900,600)
## hMon.SetTitle('Charge from monitor PMT')
## hMon.SetStats(0)
## hMon.GetYaxis().SetTitleOffset(1.3)
## hMon.GetXaxis().SetTitle('Charge of monitor (AU)')
## hMon.GetYaxis().SetTitle('Events (/7.5AU)')
## hMon.Fit('gaus')
## hMon.Draw('E1')

canMean = ROOT.TCanvas('canMean','canMean',900,600)
grMean = ROOT.TGraphErrors(len(SKAvg),SKAvg,MonQAvg,SKAvgErr,MonQAvgErr)
grMean.GetXaxis().SetTitle('Charge in SK (P.E.)')
grMean.GetYaxis().SetTitle('Monitor QBEE charge (AU)')
grMean.SetTitle('Avg Monitor QBEE reading vs Avg charge in SK')
grMean.SetMarkerStyle(8)
grMean.SetMarkerSize(0.2)
grMean.SetMarkerColor(1)
grMean.SetLineColor(1)
grMean.Draw('AP')
#grMean.Fit('pol1')
