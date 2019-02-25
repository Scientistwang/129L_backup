#!/usr/bin/python3
#Zipeng Wang
#perm: 3909934
#Physics 129L hw 6 problem 1

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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

#error of the measurements is 50micrometer/sqrt(12)



def straight_fit(x,slope,offset):
	'''function used to fit data to straight line'''     
	return slope*x+offset    










