import ROOT
from array import array
import math
import datetime

# Function to calculate elapsed seconds since first event
def getTotSeconds(startTime,eventTime):
    diff = (eventTime-startTime)
    diff_us = diff.microseconds + (diff.seconds*100000.0) + (diff.days*24*60*60*100000.0)
    diff_s = diff_us/100000.0
    return diff_s


### Start main script
infile = '/hepstore/pritchard/SuperK/SKDeploymentTests/AutoCalibTests/wtr.081959.root'
tree = ROOT.TChain('tqtree')
tree.AddFile(infile)

mon_channel = 11256 # cable number for monitor PMT

# Set up arrays to store various values
monQ = array('d',[])
monQE = array('d',[])
monT = array('d',[])
SKQ = array('d',[])
SKQE = array('d',[])
totS = array('d',[])
totSE = array('d',[])
event = array('d',[])

# Set up some histograms to fill in the loop
monTHist = ROOT.TH1F('monTHist','monTHist',40,720.0,740.0)
monQHist = ROOT.TH1F('monQHist','monQHist',25,2900.0,2950.0)
SKQHist = ROOT.TH1F('SKQHist','SKQHist',40,400.0,800.0)
SKQOverMonQHist = ROOT.TH1F('SKQOverMonQHist','SKQOverMonQHist',40,0.1,0.3)


nevents = tree.GetEntries()
for i in range(nevents):
    tree.GetEntry(i)
    year = int(tree.year)+1900  # year is stored as 119 for 2019
    month = int(tree.month)
    day = int(tree.day)
    hour = int(tree.hour)
    minute = int(tree.minute)
    second = int(tree.second)
    usecond = int(tree.millisecond)*1000
    eventTime = datetime.datetime(year,month,day,hour,minute,second,usecond)
    if i == 0:
        startTime = eventTime
    totSeconds = getTotSeconds(startTime,eventTime)
    # Look for the monitor PMT in the event
    for j in range(len(tree.mon_cable_vec)):
        if tree.mon_cable_vec[j]==mon_channel:
            monCharge = float(tree.mon_charge_vec[j])
            monTime = float(tree.mon_time_vec[j])
            if monCharge > 5.0:  # make sure we aren't taking noise hits
                # Now sum up all of the PMT hits charge
                sumQ = 0
                charges = tree.charge_vec
                for h in range(len(charges)):
                    sumQ+=float(charges[h])
                SKQ.append(sumQ)
                SKQE.append(math.sqrt(sumQ))
                event.append(i)
                totS.append(totSeconds)
                totSE.append(0.0)
                monQ.append(monCharge)
                monQE.append(5.6)
                monT.append(monTime)
                # Fill the histograms too
                monTHist.Fill(monTime)
                monQHist.Fill(monCharge)
                SKQHist.Fill(sumQ)
                SKQOverMonQHist.Fill(sumQ/monCharge)

### Now plot monitor charge against SK charge
can = ROOT.TCanvas('can','can',1200,900)
gr = ROOT.TGraphErrors(len(monQ),monQ,SKQ,monQE,SKQE)
gr.SetMarkerStyle(8)
gr.SetMarkerSize(0.2)
gr.GetXaxis().SetTitle('Monitor reading (AU)')
gr.GetYaxis().SetTitle('Charge in SK (PE)')
#gr.SetMaximum(3000)
#gr.SetMinimum(2700)
gr.GetYaxis().SetTitleOffset(1.3)
gr.SetTitle('Total charge in SK vs Monitor charge reading')
gr.Draw('APE1')

### Now plot monitor charge against time
can2 = ROOT.TCanvas('can2','can2',1200,900)
gr2 = ROOT.TGraphErrors(len(monQ),totS,monQ,totSE,monQE)
gr2.SetMarkerStyle(8)
gr2.SetMarkerSize(0.2)
gr2.GetXaxis().SetTitle('Elapsed time (s)')
gr2.GetYaxis().SetTitle('Monitor reading (AU)')
gr2.SetMaximum(3000)
gr2.SetMinimum(2700)
gr2.GetYaxis().SetTitleOffset(1.3)
gr2.SetTitle('Monitor PMT reading vs elapsed time')
fit1 = ROOT.TF1('fit1','pol1',0,23000)
gr2.Fit('fit1','R')
gr2.Draw('AP')
fit1.Draw('same')

### Now plot SK charge against time
canSK = ROOT.TCanvas('canSK','canSK',1200,900)
gr3 = ROOT.TGraphErrors(len(SKQ),totS,SKQ,totSE,SKQE)
gr3.SetMarkerStyle(8)
gr3.SetMarkerSize(0.2)
gr3.GetXaxis().SetTitle('Elapsed time (s)')
gr3.GetYaxis().SetTitle('Total SK Charge (PE)')
gr3.SetMaximum(1200)
gr3.SetMinimum(0)
gr3.GetYaxis().SetTitleOffset(1.3)
gr3.SetTitle('Total charge in SK vs elapsed time')
gr3.Draw('APE1')


### Plot the monitor timing histogram
can3 = ROOT.TCanvas('can3','can3',1200,900)
monTHist.SetMarkerStyle(8)
monTHist.SetStats(0)
monTHist.SetMarkerSize(0.2)
monTHist.SetTitle('Monitor PMT timing')
monTHist.GetXaxis().SetTitle('Time of monitor PMT hit (ns)')
monTHist.GetYaxis().SetTitle('Hits (/0.5ns)')
monTHist.Draw('E1')

print "<<<< Monitor Charge histogram >>>>"
### Plot the monitor charge histogram
can4 = ROOT.TCanvas('can4','can4',1200,900)
monQHist.SetMarkerStyle(8)
monQHist.SetStats(0)
monQHist.SetMarkerSize(0.2)
monQHist.SetTitle('Monitor PMT Charge')
monQHist.GetXaxis().SetTitle('Charge of monitor PMT hit (A.U.)')
monQHist.GetYaxis().SetTitle('Hits (/2A.U.)')
monQHist.Fit('gaus')
monQHist.Draw('E1')

print "<<<< SK charge histogram >>>>"
### Plot the monitor charge histogram
can5 = ROOT.TCanvas('can5','can5',1200,900)
SKQHist.SetMarkerStyle(8)
SKQHist.SetStats(0)
SKQHist.SetMarkerSize(0.2)
SKQHist.SetTitle('Total SK Charge')
SKQHist.GetXaxis().SetTitle('Total charge in SK (PE)')
SKQHist.GetYaxis().SetTitle('Hits (/10PE)')
SKQHist.Fit('gaus')
SKQHist.Draw('E1')

print "<<<< SK charge / monitor charge >>>>"
### Plot the monitor charge histogram
can6 = ROOT.TCanvas('can6','can6',1200,900)
SKQOverMonQHist.SetMarkerStyle(8)
SKQOverMonQHist.SetStats(0)
SKQOverMonQHist.SetMarkerSize(0.2)
SKQOverMonQHist.SetTitle('SK Charge divided by Monitor')
SKQOverMonQHist.GetXaxis().SetTitle('SK Charge/Monitor (PE/AU)')
SKQOverMonQHist.GetYaxis().SetTitle('Hits (/0.005PE/AU)')
SKQOverMonQHist.Fit('gaus')
SKQOverMonQHist.Draw('E1')

### Finally, print out the event rate
totEvents = float(len(totS))
totTime = float(totS[int(totEvents)-1]) - float(totS[0])
timePerEvent = totTime/totEvents

print "The time per event is "+str(timePerEvent)+" seconds"
