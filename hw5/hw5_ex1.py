#!/usr/bin/python3
#Zipeng Wang
#perm: 3909934
#hw5 exercise 1 
import numpy as np
import scipy.special as sci
import matplotlib.pyplot as plt

#goal: integrate 2/pi*1/sqrt[1-k^2*(sin(b))^2] in the interval
# [0,pi/2], and k := sin(a/2). a goes from pi/180 to pi/4.
upper = np.pi/2 #upper bound of integration
lower = 0  #lower bound of integration
def f(beta,k):
	''' returns the integrand'''
	out = 2/np.pi/np.sqrt(1-(k**2)*(np.sin(beta)**2))
	return out


def ellip(alpha):
	'''
	Gives one MC approx of the integral with one given 
	alpha value
	'''
	N = 10000
	k = np.sin(alpha/2)
	#using simple Monte Carlo method to do this integral
	trial = np.random.random(N)*(upper-lower)
	fsum = 0
	for i in trial:
		fsum+=f(i,k)
	I = (upper-lower)/N*fsum
	return I

def sci_check(alpha):
	'''
	return same integral as ellip but uses scipy module
	'''
	k = np.sin(alpha/2)
	return 2/np.pi*sci.ellipk(k**2)

angles = np.linspace(1,90,90)
alphas = np.pi/180*angles
T_ratio_MC = ellip(alphas)###calculated by MC
T_ratio_sci = sci_check(alphas)###calculated by scipy
######plotting#############3
fig,ax = plt.subplots()
plt.plot(angles,T_ratio_MC,'b',label = "MC")
plt.plot(angles,T_ratio_sci,'--r',label = 'scipy')
plt.xlabel("angle in degree")
plt.ylabel(r'$T/T_0$')
plt.legend()
plt.show()








 




