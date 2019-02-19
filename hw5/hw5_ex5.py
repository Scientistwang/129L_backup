#!/usr/bin/python3
#Zipeng Wang
#3909934
#bisection method
#calculate x*cos(x)- 1/2 = 0 near x = 0.7
import numpy as np
##define the function that is being calculated
def f(x):
	out = x*np.cos(x)-1/2
	return out


pt = 0.7    #the pt of interest
#first find the opposite signs
rangelist = [0.05,0.1,0.15,0.2]
for i in rangelist:
	x_1 = pt-i
	x_2 = pt+i 
	if f(x_1)*f(x_2)<0:
		minrange=(pt-i)
		maxrange=(pt+i) #the starting range
		break	
#print(minrange,maxrange)

#starting the bisection method
sRange = minrange #initializing small range
lRange = maxrange #initializing large range
while (lRange-sRange)>0.0001:    #0.0001 is the required precision
	tryRange = (lRange+sRange)/2
	if f(tryRange)*f(lRange)>0:  #if try and large are the same sign:
		lRange= tryRange  #it is the new large
	else:      #if opposite sign
		sRange= tryRange
	#repeat as necessary

root = (sRange+lRange)/2
error = (lRange-sRange)/2
print("The root is {0:.4f}, with uncertainty (plus or minus) {1:.5f}".format(root,error))









