import ROOT

### Set some booleans to select event sample
KorInjector = False
UKKorLaser  = False
UKLEDPulser = True

if KorInjector:
    fname = '/hepstore/pritchard/SuperK/EventTiming/KorKor_only15001hits.root'
if UKKorLaser:
    fname = '/hepstore/pritchard/SuperK/EventTiming/KorUK_only15001hits.root'
if UKLEDPulser:
    fname = '/user/pritchard/TimingsJuly2019.root'
#    fname = '/hepstore/pritchard/SuperK/EventTiming/UKUK_only15001hits.root'


# Open the file containing the histograms
rfile = ROOT.TFile(fname)

# Get the histograms
time_15001 = rfile.Get('h150')
time_PMTs  = rfile.Get('h140')
time_QBEEs = rfile.Get('h160')
time_mon   = rfile.Get('h170')
time_PMTQw = rfile.Get('h180')

# Plot the relevant histograms together
can = ROOT.TCanvas('can','can',1200,900)
# SK PMTs
time_PMTs.SetStats(0)
time_PMTs.GetXaxis().SetTitle('tiskz time (ns)')
time_PMTs.GetYaxis().SetLabelSize(0.03)
time_PMTs.GetYaxis().SetTitleSize(0.03)
time_PMTs.GetXaxis().SetLabelSize(0.03)
time_PMTs.GetXaxis().SetTitleSize(0.03)
time_PMTs.GetYaxis().SetTitleOffset(1.5)
time_PMTs.GetYaxis().SetTitle('Hits')
#time_PMTs.SetMaximum(time_15001.GetMaximum()*1.1)
if KorInjector:
    time_PMTs.SetTitle('Event timing for Korean optics, Korean laser')
if UKKorLaser:
    time_PMTs.SetTitle('Event timing for UK optics, Korean laser')
if UKLEDPulser:
    time_PMTs.SetTitle('Event timing for UK optics, UK laser')
    time_PMTs.SetMaximum(time_15001.GetMaximum()*1.1)
time_PMTs.Draw()
# Trigger and monitor QBEEs (only for UK electronics)
#if not UKLEDPulser:
#    time_QBEEs.Scale(15)
#    time_15001.Scale(15)
time_QBEEs.SetLineColor(2)
time_QBEEs.Draw('same')
# 15001 periodic trigger
time_15001.SetLineColor(4)
time_15001.Draw('same')

legend = ROOT.TLegend(0.59,0.67,0.88,0.87)
legend.SetFillStyle(1001)
legend.SetFillColor(0)
legend.SetLineColor(1)
legend.SetLineStyle(1)
legend.AddEntry(time_PMTs, 'SK PMTs')
if UKLEDPulser:
    legend.AddEntry(time_QBEEs, 'Triggers and monitor PMT')
else:
    legend.AddEntry(time_QBEEs, 'Monitor PMTs')
legend.AddEntry(time_15001, 'Periodic trigger 15001')
legend.Draw()

can2 = ROOT.TCanvas('can2','can2',1200,900)
time_PMTQw.GetXaxis().SetTitle('tiskz time (ns)')
time_PMTQw.GetYaxis().SetTitle('Charge Weighted Hits (P.E.)')
time_PMTQw.SetStats(0)
time_PMTQw.SetTitle('Charge weighted timing distribution of SK PMT hits')
time_PMTQw.GetYaxis().SetLabelSize(0.03)
time_PMTQw.GetYaxis().SetTitleSize(0.03)
time_PMTQw.GetXaxis().SetLabelSize(0.03)
time_PMTQw.GetXaxis().SetTitleSize(0.03)
time_PMTQw.GetYaxis().SetTitleOffset(1.5)
time_PMTQw.Draw()
