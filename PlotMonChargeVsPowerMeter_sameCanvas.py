import ROOT
import math
from array import array
import datetime

# This function will convert the time from power meter readings to a datetime object
# to allow calculation of elapsed number of seconds
def getDatetime(time):
    startDate = time.split(' ')[0]
    Day = int(startDate.split('/')[0])
    Month = int(startDate.split('/')[1])
    Year = int(startDate.split('/')[2])
    startTime = time.split(' ')[1]
    startVals = startTime.split(':')
    Hour = int(startVals[0])
    Min = int(startVals[1])
    Sec = int(startVals[2].split('.')[0])
    ms = int(startVals[2].split('.')[1])
    us = int(ms*1000)
    dt = datetime.datetime(Year,Month,Day,Hour,Min,Sec,us)
    return dt

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

##################
# Adjustment Parameters
# Must be done by eye for each calibration run, to account for:
# 1) offset in the start times
# 2) cut off time at the run end
# 3) time windows for each intensity (to allow mean calculations)
##################
tOffset = 5  # this is the time difference from SK end of first intensity to PM end of first intensity (SK - PM)
offTime = 700 # the time for the end of the run
tLows = [10,120,250,395,540]
tHighs = [70,200,330,460,700]

### Below should be the path to the SK data file
SKDataFile = '/hepstore/pritchard/SuperK/SKDeploymentTests/July2019/CalibRuns/wtr.081409.root'
### Below should be the path to the power meter output
PowerMeterFile = '/hepstore/pritchard/SuperK/SKDeploymentTests/July2019/CalibRuns/POWERMETER_CalibRun_81409.txt'

### Make the arrays to store the various data
totSeconds_SK = array('d',[])
monCharge = array('d',[])
totSeconds_PM = array('d',[])
PMVals = array('d',[])

SKDataTree = ROOT.TChain('tqtree')
SKDataTree.AddFile(SKDataFile)

### Fill the SK data arrays from the tree
for i in range(SKDataTree.GetEntries()):
    SKDataTree.GetEntry(i)
    monCable = SKDataTree.mon_cable_vec
    for cab in range(len(monCable)):
        if monCable[cab] == 11256:
           monQ = SKDataTree.mon_charge_vec[cab]
           time = SKDataTree.totSeconds
           totSeconds_SK.append(time)
           monCharge.append(monQ)

### Parse the power meter output file and fill power meter arrays
PMtxtfile = open(PowerMeterFile,'r')
lineCount = 0
for line in PMtxtfile:
    lineCount+=1
    # Skip the first 2 lines as they are info about the Power Meter settings
    if lineCount<3:
        continue
    else:
        vals = line.split('\t') # Power meter txt file helpfully has tabs around power reading
        PMVal = float(vals[1])
        time = vals[0] # Date and time
        # Take the datetime from the first reading as the start time
        if lineCount==3:
            startTime = getDatetime(time)
        PMtime = getDatetime(time)
        totSecs = (PMtime - startTime).total_seconds()
        PMVals.append(PMVal)
        totSeconds_PM.append(totSecs+tOffset) # add the offset here
PMtxtfile.close()

### Following code is to plot both on the same graph with 2 y-axes
ROOT.gROOT.ForceStyle(0)
c1 = ROOT.TCanvas("c1","c1",200,10,700,500)
pad = ROOT.TPad("pad","",0,0,1,1)
pad.SetFillColor(0)
pad.SetGrid()
pad.Draw()
pad.cd()
# draw a frame to define the range
hr = c1.DrawFrame(0,0,offTime,max(monCharge)*1.2)
hr.SetYTitle("Monitor PMT QBEE charge (AU)")
hr.SetXTitle("Time elapsed (s)")
hr.GetXaxis().SetTitleOffset(1.3)
pad.GetFrame().SetFillColor(0)
pad.GetFrame().SetBorderSize(12)

# Plot 1 - Monitor QBEE vs elapsed time
gr1 = ROOT.TGraph(len(totSeconds_SK),totSeconds_SK,monCharge)
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
gr2 = ROOT.TGraph(len(totSeconds_PM),totSeconds_PM,PMVals)
gr2.SetMarkerColor(ROOT.kRed)
gr2.SetMarkerStyle(8)
gr2.SetMarkerSize(0.2)
gr2.SetName("gr2")
xmin = pad.GetUxmin()
ymin = 0
xmax = pad.GetUxmax()
ymax = max(PMVals)*1.2
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
axis.SetTitle('Power Meter Reading (W)')
axis.Draw()

### Final step is to calculate averages for the different intensities
tCent = array('d',[])
tCentErr = array('d',[])
PMAvg = array('d',[])
PMAvgErr = array('d',[])
MonQAvg = array('d',[])
MonQAvgErr = array('d',[])

for i in range(len(tLows)):
    tCent.append((float(tLows[i])-float(tHighs[i]))/2.0)
    tCentErr.append(0)
    ### make new array to use for calculating mean/rms
    PMArray = array('d',[])
    MonArray = array('d',[])
    for j in range(len(PMVals)):
        if totSeconds_PM[j] < tHighs[i] and totSeconds_PM[j] > tLows[i]:
            PMArray.append(PMVals[j])
    for k in range(len(monCharge)):
        if totSeconds_SK[k] < tHighs[i] and totSeconds_SK[k] > tLows[i]:
            MonArray.append(monCharge[k])
    # Use the function to calculate the mean and rms for this time period
    PMMean, PMRMS = getMeanSD(PMArray)
    MonMean, MonRMS = getMeanSD(MonArray)
    # Fill the results into the respective arrays
    PMAvg.append(PMMean)
    PMAvgErr.append(PMRMS)
    MonQAvg.append(MonMean)
    MonQAvgErr.append(MonRMS)

canMean = ROOT.TCanvas('canMean','canMean',900,600)
grMean = ROOT.TGraphErrors(len(PMAvg),PMAvg,MonQAvg,PMAvgErr,MonQAvgErr)
grMean.GetXaxis().SetTitle('Power meter reading (W)')
grMean.GetYaxis().SetTitle('Monitor QBEE charge (AU)')
grMean.SetTitle('Avg Monitor QBEE reading vs Avg Power Meter reading')
grMean.SetMarkerStyle(8)
grMean.SetMarkerSize(0.2)
grMean.SetMarkerColor(1)
grMean.SetLineColor(1)
grMean.Draw('AP')
#grMean.Fit('pol1')
