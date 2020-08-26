import ROOT

def getTH1F(name,bins,xlow,xhigh,title,xaxislabel,yaxislabel):
    plot = ROOT.TH1F(name,name,bins,xlow,xhigh)
    plot.SetTitle(title)
    plot.GetXaxis().SetTitle(xaxislabel)
    plot.GetYaxis().SetTitle(yaxislabel)
    plot.SetMarkerStyle(8)
    plot.SetMarkerSize(0.1)
    plot.SetLineColor(1)
    plot.SetMarkerColor(1)
    return plot

def getTH2F(name,bins,xlow,xhigh,ylow,yhigh,title,xaxislabel,yaxislabel):
    plot = ROOT.TH2F(name,name,bins,xlow,xhigh,bins,ylow,yhigh)
    plot.SetTitle(title)
    plot.GetXaxis().SetTitle(xaxislabel)
    plot.GetYaxis().SetTitle(yaxislabel)
    plot.SetMarkerStyle(8)
    plot.SetMarkerSize(0.1)
    return plot

def getTH3F(name,bins,xlow,xhigh,ylow,yhigh,zlow,zhigh,title,xaxislabel,yaxislabel):
    plot = ROOT.TH3F(name,name,bins,xlow,xhigh,bins,ylow,yhigh,bins,zlow,zhigh)
    plot.SetTitle(title)
    plot.GetXaxis().SetTitle(xaxislabel)
    plot.GetYaxis().SetTitle(yaxislabel)
    plot.SetMarkerStyle(8)
    plot.SetMarkerSize(0.1)
    return plot
    
def GetPlots():
    ### TOF from injector
    TOFInjPlot = getTH1F('TOFInjPlot',2000,0,2000,'t-TOF(inj) time','Time (ns)','Hits')

    ### TOF from target
    TOFTarPlot = getTH1F('TOFTarPlot',2000,0,2000,'t-TOF(tar) time','Time (ns)','Hits')

    ### 2D Beam spot plot
    QwBeamSpot = getTH2F('QwBeamSpot',36,-1820.0,1820.0,-1820.0,1820.0,'Beam spot','x position (cm)','y position (cm)')

    ### 1D Beam spot plot
    #QwZPosBeam = getTH1F('QwZPosBeam',18,-1820.0,1820.0,'Charge weighted z position of hits','Hit PMT z position (cm)', 'Qw Hits')
    #QwZPosBeam = getTH1F('QwZPosBeam',100,-1700.0,1700.0,'Charge weighted z position of hits','Hit PMT z position (cm)', 'Qw Hits')
    QwZPosBeam = getTH1F('QwZPosBeam',20,1000,1500,'Charge weighted z position of hits','Hit PMT z position (cm)', 'Qw Hits')
    ### 1D Beam spot plot by angle
    QwAngBeam = getTH1F('QwAngBeam',36,-90,90,'Charge weighted angle of hits','Hit PMT angle from injector (degs)', 'Qw Hits')
    AngBeam = getTH1F('AngBeam',36,-90,90,'Angle of hits','Hit PMT angle from injector (degs)', 'Hits')

    ### TOF from target for selected PMTs
    ZTBAPlot = getTH1F('ZTBAPlot',2000,0,2000,'t-TOF(tar) for hits in z region','t-TOF(target) (ns)','Hits')

    ### 3D beam
    Qw3DBeam = getTH3F('Qw3DBeam',52,-1820.0,1820.0,-1820.0,1820.0,-1820.0,1820.0,'Beam spot','x position (cm)', 'y position (cm)')

    ### Total charge in tank outside 2m exclusion
    QinTank = getTH1F('QinTank',2000,0,2000,'t-TOF(tar) for all hits outside 2m','t-TOF(target) (ns)','Qw Hits')

    ### Total charge outside beam
    QoutBeam = getTH1F('QoutBeam',2000,0,2000,'t-TOF(tar) for all hits outside 2m, outside beam','t-TOF(target) (ns)','Qw Hits')

    ### Total charge inside beam
    QinBeam = getTH1F('QinBeam',2000,0,2000,'t-TOF(tar) for all hits outside 2m, inside beam','t-TOF(target) (ns)','Qw Hits')

    ### Total charge in specific z region
    QinZRegion = getTH1F('QinZRegion',2000,0,2000,'t-TOF(tar) for hits outside 2m in z region','t-TOF(target) (ns)','Qw Hits')

    ### Charge outside beam in z region
    QinZoutBeam = getTH1F('QinZoutBeam',2000,0,2000,'t-TOF(tar) for hits outside 2m, outside beam, in z region','t-TOF(target) (ns)','Qw Hits')

    return TOFInjPlot,TOFTarPlot,QwBeamSpot,QwZPosBeam,QwAngBeam,AngBeam,ZTBAPlot,Qw3DBeam,QinTank,QoutBeam,QinBeam,QinZRegion,QinZoutBeam
