import ROOT
from array import array
from ROOT import TMath
from ROOT import TH1F, TF1, TLine
import math
import array as arr
import numpy as np
import matplotlib.pyplot as plt


B1File = ROOT.TFile('/hepstore/pmehta/sigbm_test/Sigbm175/Completed_sigbm_test/435.mc.pos5.1.7_0.8_0.5_10.dat_Completed.root')
B1Hist = B1File.Get('QwPosBeam')
B1Hist.SetStats(0)
B1Hist.SetFillStyle(0)
B1Hist.SetMarkerStyle(8)
B1Hist.SetMarkerSize(1)
can = ROOT.TCanvas('can','can',1200,900)
B1Hist.Fit("gaus","","",-1000,0)
B1Hist.Draw('E1')
B1Line = TLine(-676.65,0.0,-676.65,4000000.0)
B1Line.SetLineColor(4)
B1Line.SetLineWidth(3)
B1Line.SetLineStyle(9)
B1Line.Draw()
#Get Guassian Parameters from fit and print sigma
f1 = B1Hist.GetListOfFunctions().FindObject("gaus")
sig = f1.GetParameter(2)
print "Value of sigma"
print sig
print "Value of 3sigma"
num1 = 3
num2 = sig
num3 = sig * num1 
print num3 
num4 = 2
print "Value of 2 times 3sigma"
print num3 * num4
mean = f1.GetParameter(1)
print "Value of mean"
print mean
print "Value of y at mean"
maxy = f1.Eval(mean)
print maxy
print "0.135 times max intensity"
num5 = 0.135
num6 = maxy * 0.135
print num6
print "Value of 1/e^2 radius"
beam_edge = f1.GetX(num6)
print beam_edge
radius = abs(beam_edge-mean)
print "Value of beam radius"
print radius
#Create array of injector and target positions and radius of MC beam spot 
#For B4 Injector
a = arr.array('d', [1490.73, 768.14, -676.65]) #Theroetical Injector positions
b = arr.array('d', [-1459.59, -851.269, -635.7]) #Theoretical Beam spot target
c = arr.array('d', [-1459.59, -851.269, -635.7 + radius]) #Theoretical Beam spot target + radius
#Calculate distance in between injector and target
distance1 = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
distance2 = math.sqrt((a[0]-c[0])**2 + (a[1]-c[1])**2 + (a[2]-c[2])**2)
print "Distance between injector and target"
print distance1
print "Distance between injector and edge of beam spot"
print distance2
#Calculate angle using cosine rule
cosangle = (((distance1)**2 + (distance2)**2) - (radius)**2)/(2*distance1*distance2)
halfangle = np.arccos(cosangle)
angle = halfangle * 2
print "Angle in radians"
print angle
print "Angle in degrees"
print math.degrees(angle) 

