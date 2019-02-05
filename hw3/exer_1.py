#!/usr/bin/python3
import numpy as np
import math
exactPi = math.pi

from scipy import stats
#prob = 1 - stats.chi2.cdf(chisquared,5) # chisqaured will be calculated
										 # below
pull = np.zeros(5)
for i in range(5):  #5 different trials
	N = 100*10**i
	x = np.random.rand(N)
	y = np.random.rand(N)
	count = 0    # counts # of pairs inside the circle
	for j in range(N):
		if x[j]**2+y[j]**2<1:
			count += 1
	approxPi = count/N*4
	closeness = abs(approxPi-exactPi)/exactPi *100
	f = count/N 
	sigmaPi= 4*np.sqrt(f*(1-f)/N) # times 4 because the estimate is on 1/4Pi.
	pull[i] = (approxPi-exactPi)/sigmaPi
	print("N ={:d}. Percent error is {:f}%. Pull = {:f}".format(N,closeness,pull[i]))

chisquared = 0
for i in range(5):
	chisquared += pull[i]**2
print("Chi sqaured value is {:f}".format(chisquared))
prob = 1 - stats.chi2.cdf(chisquared,5)
print("Probability of finding a larger chi sqaured is {:f}".format(prob))


