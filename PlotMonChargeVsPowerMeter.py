import ROOT
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

##################
# Adjustment Parameters
# Must be done by eye for each calibration run, to account for:
# 1) offset in the start times
# 2) cut off time at the run end
# 3) time windows for each intensity (to allow mean calculations)
##################
tOffset = 5  # this is the time difference from SK end of first intensity to PM end of first intensity (SK - PM)
offTime = 800 # the time for the end of the run

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

### Plot the monitor charge vs the time passed
MonQVsTime = ROOT.TGraph(len(totSeconds_SK),totSeconds_SK,monCharge)
MonQVsTime.SetTitle('Monitor charge vs seconds passed')
MonQVsTime.GetXaxis().SetTitle('Time (s)')
MonQVsTime.GetYaxis().SetTitle('Monitor charge (A.U.)')
MonQVsTime.SetMarkerStyle(8)
MonQVsTime.SetMarkerSize(0.2)
MonQVsTime.GetXaxis().SetLimits(0,offTime)

can = ROOT.TCanvas('can','can',900,600)
MonQVsTime.Draw('AP')

### Plot power meter reading vs elapsed time
PMVsTime = ROOT.TGraph(len(totSeconds_PM),totSeconds_PM,PMVals)
PMVsTime.SetTitle('Power meter reading vs seconds passed')
PMVsTime.GetXaxis().SetTitle('Time (s)')
PMVsTime.GetYaxis().SetTitle('Power meter reading (W)')
PMVsTime.SetMarkerStyle(8)
PMVsTime.SetMarkerSize(0.2)
PMVsTime.SetMarkerColor(2)
PMVsTime.GetXaxis().SetLimits(0,offTime)

can2 = ROOT.TCanvas('can2','can2',900,600)
PMVsTime.Draw('AP')
