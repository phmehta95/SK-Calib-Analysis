import ROOT
import datetime
from array import array

f = ROOT.TFile('/hepstore/pritchard/SuperK/SKDeploymentTests/AutoCalibTests/wtr.081959.root','update')
tree = f.Get('tqtree')

totSeconds = array('d',[0.0]) ; tree.Branch('totSeconds',totSeconds,'totSeconds/D')
## hour = array('d',[0.0]) ; tree.SetBranchAddress('hour',hour)
## minute = array('d',[0.0]) ; tree.SetBranchAddress('minute',minute)
## second = array('d',[0.0]) ; tree.SetBranchAddress('second',second)
## millisecond = array('d',[0.0]) ; tree.SetBranchAddress('millisecond',millisecond)

nentries = tree.GetEntries()

for i in range(nentries):
    diff_s = 0
    tree.GetEntry(i)
    day = int(tree.day)
    month = int(tree.month)
    year = int(tree.year)
    hour = int(tree.hour)
    minute = int(tree.minute)
    second = int(tree.second)
    millisecond = int(tree.millisecond)
    microsecond = millisecond*1000
    if i==0:
        #start_time = datetime.timedelta(hours=int(hour),minutes=int(minute),seconds=int(second),milliseconds=int(millisecond))
        start_time = datetime.datetime(year,month,day,hour,minute,second,microsecond)
    #event_time = datetime.timedelta(hours=int(hour),minutes=int(minute),seconds=int(second),milliseconds=int(millisecond))
    event_time = datetime.datetime(year,month,day,hour,minute,second,microsecond)
    diff = (event_time-start_time)
    diff_us = diff.microseconds + (diff.seconds*100000.0) + (diff.days*24*60*60*100000.0)
    diff_s = diff_us/100000.0
    totSeconds[0] = diff_s
    print diff_s
    tree.Fill()

tree.Print()
tree.Write()
