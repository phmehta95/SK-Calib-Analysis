import ROOT

B1File = ROOT.TFile('/scratch/pritchard/SKData/Feb19Tests/KoreanLaser/Collimator/Completed/B1Collimator_Completed.root')
B1Hist = B1File.Get('QwZPosBeam')
B2File = ROOT.TFile('/scratch/pritchard/SKData/Feb19Tests/KoreanLaser/Collimator/Completed/B2Collimator_Completed.root')
B2Hist = B2File.Get('QwZPosBeam')
B3File = ROOT.TFile('/scratch/pritchard/SKData/Feb19Tests/KoreanLaser/Collimator/Completed/B3Collimator_Completed.root')
B3Hist = B3File.Get('QwZPosBeam')
B4File = ROOT.TFile('/scratch/pritchard/SKData/Feb19Tests/KoreanLaser/Collimator/Completed/B4Collimator_Completed.root')
B4Hist = B4File.Get('QwZPosBeam')
B5File = ROOT.TFile('/scratch/pritchard/SKData/Feb19Tests/KoreanLaser/Collimator/Completed/B5Collimator_Completed.root')
B5Hist = B5File.Get('QwZPosBeam')

B1Hist.Fit('gaus','','',1000,1500)
B2Hist.Fit('gaus','','',600,900)
B3Hist.Fit('gaus','','',-300,-100)
B4Hist.Fit('gaus','','',-850,-600)
B5Hist.Fit('gaus','','',-1500,-1300)

can = ROOT.TCanvas('can','can',1200,900)
B1Hist.SetStats(0)
B1Hist.SetFillStyle(0)
B1Hist.SetMarkerStyle(8)
B1Hist.SetMarkerSize(0.5)
B1Hist.Draw('E1')

B2Hist.SetLineColor(2)
B2Hist.SetMarkerColor(2)
B2Hist.SetMarkerStyle(8)
B2Hist.SetMarkerSize(0.5)
B2Hist.Draw('E1same')

B3Hist.SetLineColor(3)
B3Hist.SetMarkerColor(3)
B3Hist.SetMarkerStyle(8)
B3Hist.SetMarkerSize(0.5)
B3Hist.Draw('E1same')

B4Hist.SetLineColor(4)
B4Hist.SetMarkerColor(4)
B4Hist.SetMarkerStyle(8)
B4Hist.SetMarkerSize(0.5)
B4Hist.Draw('E1same')

B5Hist.SetLineColor(6)
B5Hist.SetMarkerColor(6)
B5Hist.SetMarkerStyle(8)
B5Hist.SetMarkerSize(0.5)
B5Hist.Draw('E1same')

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
legend.Draw()
