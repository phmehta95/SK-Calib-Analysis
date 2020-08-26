import ROOT
from array import array
import datetime

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
    

PowerMeterFile = '/hepstore/pritchard/SuperK/SKDeploymentTests/July2019/CalibRuns/POWERMETER_CalibRun_81409.txt'
PMtxtfile = open(PowerMeterFile,'r')

PMVals = array('d',[])
totSeconds_PM = array('d',[])

lineCount = 0
for line in PMtxtfile:
    lineCount+=1
    # Skip the first 2 lines as they are info about the Power Meter settings
    if lineCount<3:
        continue
    else:
        vals = line.split('\t') # Power meter txt file helpfully has tabs around power reading
        PMVal = float(vals[1])
        time = vals[0]#.split(' ')[1] # Split the date and time to get the time reading
        # Take the time from the first reading as the start time
        if lineCount==3:
            startTime = getDatetime(time)
        PMtime = getDatetime(time)
        totSecs = (PMtime - startTime).total_seconds()
        PMVals.append(PMVal)
        totSeconds_PM.append(totSecs)

### Plot power meter reading vs elapsed time
PMVsTime = ROOT.TGraph(len(totSeconds_PM),totSeconds_PM,PMVals)
PMVsTime.SetTitle('Power meter reading vs seconds passed')
PMVsTime.GetXaxis().SetTitle('Time (s)')
PMVsTime.GetYaxis().SetTitle('Power meter reading (W)')
PMVsTime.SetMarkerStyle(8)
PMVsTime.SetMarkerSize(0.2)
PMVsTime.SetMarkerColor(2)
PMVsTime.GetXaxis().SetLimits(0,800)

can2 = ROOT.TCanvas('can2','can2',900,600)
PMVsTime.Draw('AP')


        
