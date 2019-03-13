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
print('Fit number 1:\nExponential')
#background pdf #1: exponential, copying formula from the question 
def B_1(x,alpha):
	pdf = alpha*np.exp(-alpha*x)/(np.exp(-alpha*m1)-np.exp(-alpha*m2))
	return pdf

#define the NLL corresponding to B_1
def NLL_1(S,B,alpha):
	temp = np.log(S*S_pdf(mass)+B*B_1(mass,alpha))
	return S + B -temp.sum() 

#start to fit	
m_fit_1 = Minuit(NLL_1,S=30.,B = 170., alpha = 1., print_level = 1,
			errordef=0.5,error_S=1.0,error_B=1.0,error_alpha = 1.0) 

m_fit_1.migrad()
m_fit_1.minos()
m_fit_1.print_param()

fittedB1 = m_fit_1.values['B']
fittedS1 = m_fit_1.values['S']
fitteda = m_fit_1.values['alpha']
####################################### end of fit 1
print('end of fit 1')

############# FIT num. 2 ##########################<3
print('Fit number 2:\nLinear')
#background pdf #2: linear, y = -kx+b. By normalization, 
#b = 1/(m2-m1)+1/2*k*(m2+m1) 
def B_2(x,k):
	y = -k*x+1/(m2-m1)+1/2*k*(m2+m1)
	return y

#define the NLL corresponding to B_2
def NLL_2(S,B,k):
	temp = np.log(S*S_pdf(mass)+B*B_2(mass,k))
	return S + B -temp.sum()

#start to fit	
m_fit_2 = Minuit(NLL_2,S=5.,B = 195., k = 0.0002, print_level = 1,
			errordef=0.5,error_S=1.0,error_B=1.0,error_k = 0.000001) 

m_fit_2.migrad()
m_fit_2.minos()
m_fit_2.print_param()

fittedB2 = m_fit_2.values['B']
fittedS2 = m_fit_2.values['S']
fittedk = m_fit_2.values['k']
####################################### end of fit 2
print('end of fit 2')

############# FIT num. 3 ##########################<3
print('Fit number 3:\nQuadratic')
#background pdf #2: Quadratic, y = -ax^2+bx+c. By normalization, 
#c = 1/(m2-m1)+1/3*a*(m2^3-m1^3)/(m2-m1)-1/2*b*(m1+m2) 
def B_3(x,a,b):
	c = 1/(m2-m1)+1/3*a*(m2**3-m1**3)/(m2-m1)-1/2*b*(m1+m2)
	y = -a*x**2+b*x+c
	return y

#define the NLL corresponding to B_3
def NLL_3(S,B,a,b):
	temp = np.log(S*S_pdf(mass)+B*B_3(mass,a,b))
	return S + B -temp.sum() + a*a/2+b*b/2

guess_a = 0.6e-6
guess_b = 1e-5
#start to fit	
m_fit_3 = Minuit(NLL_3,S=10.,B = 190., a = guess_a, b = guess_b, print_level = 1,
			errordef=0.5,error_S=1.0,error_B=1.0,error_a = 1e-7,error_b = 0.000001) 

m_fit_3.migrad()
m_fit_3.minos()
m_fit_3.print_param()

fittedB3 = m_fit_3.values['B']
fittedS3 = m_fit_3.values['S']
fittedQa = m_fit_3.values['a']
fittedQb = m_fit_3.values['b']
####################################### end of fit 3
print('end of fit 3')

	
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
a1.plot(plot_x,plot_y*5,label='exponential fit') # have this *5 factor because the 
						 #area of the 
						 # histogram is not 200 but 200*5(bin width)
a1.set_xlabel('mass[GeV]')
a1.set_ylabel('count')
a1.legend(loc = 'upper left')

# plot fitted curve2
f2, a2 = plt.subplots()
c, b, _ = a2.hist(mass, bins, histtype='step')
cc.statBox(a2, mass, b)
a2.set_xlim(b[0], b[-1])
a2.tick_params("both", direction='in', length=10, right=True)
a2.set_xticks(b, minor=True)
a2.tick_params("both", direction='in', length=7, right=True, which='minor')

plot_x = np.linspace(100,200,1001)
plot_y2 = fittedB2*B_2(plot_x,fittedk)+fittedS2*S_pdf(plot_x)
a2.plot(plot_x,plot_y2*5,label='linear fit') # have this *5 factor because the area of the 
						 # histogram is not 200 but 200*5(bin width)

a2.set_xlabel('mass[GeV]')
a2.set_ylabel('count')
a2.legend(loc = 'upper left')

# plot fitted curve3
f3, a3 = plt.subplots()
c, b, _ = a3.hist(mass, bins, histtype='step')
cc.statBox(a3, mass, b)
a3.set_xlim(b[0], b[-1])
a3.tick_params("both", direction='in', length=10, right=True)
a3.set_xticks(b, minor=True)
a3.tick_params("both", direction='in', length=7, right=True, which='minor')

plot_x = np.linspace(100,200,1001)
plot_y3 = fittedB3*B_3(plot_x,fittedQa,fittedQb)+fittedS2*S_pdf(plot_x)
a3.plot(plot_x,plot_y3*5,label='quadratic fit') # have this *5 factor because the area of the 

	
a3.set_xlabel('mass[GeV]')
a3.set_ylabel('count')
a3.legend(loc = 'upper left')

plt.show()


