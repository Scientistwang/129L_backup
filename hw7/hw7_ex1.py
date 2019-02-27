#!/usr/bin/python3
#Zipeng Wang
#perm: 3909934
#Physics 129L hw 6 problem 1

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import ccHistStuff as cc

#data is stored in straightTracks.txt
filename = 'straightTracks.txt'
X0,Y0 = [],[]
y00,y01,y02,y03 = [],[],[],[]
y10,y11,y12,y13 = [],[],[],[]
variable_list = [X0,Y0,y00,y01,y02,y03,y10,y11,y12,y13]

with open(filename) as f:
	for line in f:
		split_line = line.split()
		for i in range(len(split_line)):
			variable_list[i].append(float(split_line[i]))	
		
 
#for var in variable_list:
#	print(var[-1],end = ' ')      #for test purposes

def straight_fit(x,slope,offset):
	'''function used to fit data to straight line'''     
	return slope*x+offset    

myGuess = [0.,1.]
x = [2.,3.,5.,7.] # x coords of measurements
error = 50*10**(-4)/np.sqrt(12) #error in cm
err = [error,error,error,error]	#error of the measurements is 50micrometer/sqrt(12), uniform
X1,X2 = [],[]
for i in range(len(X0)):
	track0 = [y00[i],y01[i],y02[i],y03[i]]
	p0,cov0 = curve_fit(straight_fit,x,track0,p0=myGuess,sigma=err,absolute_sigma=True)
	X1.append(-p0[1]/p0[0]) #x intersection = -offset/slope. Here use fitted values
		
	track1 = [y10[i],y11[i],y12[i],y13[i]]
	p1,cov1 = curve_fit(straight_fit,x,track1,p0=myGuess,sigma=err,absolute_sigma=True)
	X2.append(-p1[1]/p1[0])

#make histograms
X0 = np.array(X0)
X1 = np.array(X1)
X2 = np.array(X2)

low = -500*10**(-4)
high = -low
nbins = 100
bins = np.linspace(low,high,nbins+1)

fig1,ax1 = plt.subplots()
c1,b1,_, = ax1.hist((X1-X0),bins, histtype = 'step',color= 'b',label = 'X1-X0')
c2,b2,_, = ax1.hist((X2-X0),bins,histtype = 'step',color = 'r',label = 'X2-X0')

#cc.statBox(ax1,(X1-X0),b1) #ccStatBoxes will stack together if multiples are in the 
							#graph. Only show (X2-X0) since they are more or less the same
cc.statBox(ax1,(X2-X0),b1)
ax1.set_xlim(b1[0],b1[-1])
ax1.legend(loc = 'upper left')
ax1.set_xlabel('X_fitted - X0[cm]')
ax1.set_ylabel('count')



fig2,ax2 = plt.subplots()
Xav = (X1+X2)/2
c3,b3,_, = ax2.hist((Xav-X0),bins,histtype = 'step',color = 'k',label = 'Xav-X0')
cc.statBox(ax2,(Xav-X0),b1)
ax2.set_xlim(b1[0],b1[-1])
ax2.legend(loc = 'upper left')
ax1.set_xlabel('X_fitted - X0[cm]')
ax1.set_ylabel('count')

plt.show()




