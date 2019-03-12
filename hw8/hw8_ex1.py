#!/usr/bin/python3
#Zipeng Wang
#3909934
#hw8 problem 1
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import special
import ccHistStuff as cc
from iminuit import Minuit 

# Read the masses into an array 
mass = np.loadtxt("mass.txt")

#define the singal pdf, which is a Gaussian of mean 155 and sigma 5
def S_pdf(x):
	mean = 155
	sigma= 5
	A = 1/np.sqrt(2*np.pi*sigma**2)
	exp_part = -(x-mean)**2/(2*sigma**2)
	return A*np.exp(exp_part) 

#define pdf boundary m1 and m2:
m1,m2 = 100,200

############# FIT num. 1 ##########################<3
#background pdf #1: exponential, copying formula from the question 
def B_1(x,alpha):
	pdf = alpha*np.exp(-alpha*x)/(np.exp(-alpha*m1)-np.exp(-alpha*m2))
	return pdf

#define the NLL corresponding to B_1
def NLL_1(S,B,alpha):
	temp = np.log(S*S_pdf(mass)+B*B_1(mass,alpha))
	return S + B -temp.sum() + alpha*alpha/2

#start to fit	
m_fit_1 = Minuit(NLL_1,S=10.,B = 150., alpha = 1., print_level = 1,
			errordef=0.5,error_S=1.0,error_B=1.0,error_alpha = 1.0) 

m_fit_1.migrad()
m_fit_1.minos()
m_fit_1.print_param()

fittedB1 = m_fit_1.values['B']
fittedS1 = m_fit_1.values['S']
fitteda = m_fit_1.values['alpha']
####################################### end of fit 1

############# FIT num. 2 ##########################<3
#background pdf #2: linear, y = -kx+b 
def B_1(x,alpha):
	pdf = alpha*np.exp(-alpha*x)/(np.exp(-alpha*m1)-np.exp(-alpha*m2))
	return pdf

#define the NLL corresponding to B_1
def NLL_1(S,B,alpha):
	temp = np.log(S*S_pdf(mass)+B*B_1(mass,alpha))
	return S + B -temp.sum() + alpha*alpha/2

#start to fit	
m_fit_1 = Minuit(NLL_1,S=10.,B = 150., alpha = 1., print_level = 1,
			errordef=0.5,error_S=1.0,error_B=1.0,error_alpha = 1.0) 

m_fit_1.migrad()
m_fit_1.minos()
m_fit_1.print_param()

fittedB1 = m_fit_1.values['B']
fittedS1 = m_fit_1.values['S']
fitteda = m_fit_1.values['alpha']
####################################### end of fit 1


	
# Histogram configuration
x1 = 100.
x2 = 200.
nb = 20
bins = np.linspace(x1, x2, nb+1)

# plot the histogram
# plot fitted curve1
f1, a1 = plt.subplots()
c, b, _ = a1.hist(mass, bins, histtype='step')
cc.statBox(a1, mass, b)
a1.set_xlim(b[0], b[-1])
a1.tick_params("both", direction='in', length=10, right=True)
a1.set_xticks(b, minor=True)
a1.tick_params("both", direction='in', length=7, right=True, which='minor')

plot_x = np.linspace(100,200,1001)
plot_y = fittedB1*B_1(plot_x,fitteda)+fittedS1*S_pdf(plot_x)
print('sum is ',sum(plot_y)*0.1)
a1.plot(plot_x,plot_y*5) # have this *5 factor because the area of the 
						 # histogram is not 200 but 200*5(bin width)


plt.show()


