#!/usr/bin/env python3
#Zipeng Wang
#3909934
#hw7 exercise3

import numpy as np
import matplotlib.pyplot as plt
import ccHistStuff as cc
x = [2.,3.,5.,7.]
#data is stored in straightTracks.txt
filename = 'straightTracks.txt'
X0,Y0 = [],[]
y00,y01,y02,y03 = [],[],[],[]
y10,y11,y12,y13 = [],[],[],[]
variable_list = [X0,Y0,y00,y01,y02,y03,y10,y11,y12,y13]
width = 50*10**(-4) # in cm
with open(filename) as f:
    for line in f:
        split_line = line.split()
        for i in range(len(split_line)):
            variable_list[i].append(float(split_line[i]))

num_y = 8
y_err = np.full(num_y,width)/np.sqrt(12)

xf_list = []
xf_var = []
for i in range(len(X0)):
    y_1 = [item[i] for item in variable_list[2:6]]
    y_2 = [item[i] for item in variable_list[6:]]
    y_all = y_1+y_2
    #print(y_all)
    #print(y_1,y_2) #test
    # We have two lines to fit with three parameters
    # y1 = k1(x-xf), and y2 = k2(x-xf), both lines intercept
    # x axis at xf.

    W = np.diag(1/y_err**2) #8x8 weight matrix

    #initial guess
    k1,k2,xf = -1,1,0
    yFit0_1 = [k1*(x_i-xf) for x_i in x]
    yFit0_2 = [k2*(x_i-xf) for x_i in x]
    yFit0 = yFit0_1 + yFit0_2
    #print(yFit0)
    #Only interate once since the problem is linear
    #contruct At
    #derivative of k1 is (x-xf), deri of k2 is (x-xf)
    #derivative of xf is -k1 or -k2
    deri_k1 = np.append(np.array(x)-xf,np.zeros(4))
    deri_k2 = np.append(np.zeros(4),np.array(x))
    deri_xf = np.array([-k1,-k1,-k1,-k1,-k2,-k2,-k2,-k2])

    At = np.array([deri_k1,deri_k2,deri_xf])
    A  = (At.T).copy()
    dy = (np.array( [(np.array(y_all)-np.array(yFit0)),] )).T
    
    #print(At)
    #print(A)
    #print(W)
    #print(dy)
    #matrix multiplitcation
    temp  = np.matmul(At, W)
    temp2 = np.matmul(temp, A)
    cov = np.linalg.inv(temp2)
    
    temp4 = np.matmul(cov, At)
    temp5 = np.matmul(temp4, W)
    dpar  = np.matmul(temp5, dy)
    #print(dpar)
    k1 = k1 + dpar[0][0]
    k2 = k2 + dpar[1][0]
    xf = xf + dpar[2][0]
    plot_sample = False
    if i == 10 and plot_sample:
        #a nice graph showing the fitting curve
        fig0,ax0 = plt.subplots()
        plt.errorbar(x+x,y_all,yerr = y_err,fmt = 'o')
        plt.plot(x,k1*(np.array(x)-xf))
        plt.plot(x,k2*(np.array(x)-xf))
    xf_list.append(xf)
    xf_var.append(cov[2][2])

#plot the histogram
low = -500*10**(-4)
high = -low
nbins = 100
bins = np.linspace(low,high,nbins+1)

#calculate pull
delta_x = np.array(xf_list)-np.array(X0)
xf_err = np.sqrt(np.array(xf_var))
pull = delta_x / xf_err

fig1,ax1 = plt.subplots()
c1,b1,_, = ax1.hist(delta_x,bins, histtype = 'step',
                    color= 'b',label = 'Xf-X0')
cc.statBox(ax1,delta_x,b1)
plt.legend(loc = 'upper left')
plt.xlabel('xf-x0')
plt.ylabel('count')
#plot pull
fig2,ax2 = plt.subplots()
low2,high2 = -40,40
nbins2 = 100
bins2 = np.linspace(low2,high2,nbins2+1)
c2,b2,_, = ax2.hist(pull,bins2, histtype = 'step',
                    color= 'r',label = 'pull')
cc.statBox(ax2,pull,b2)
plt.legend(loc='upper left')
plt.xlabel('pull')
plt.ylabel('count')

plt.show()




