#!/usr/bin/python3
#Zipeng Wang
#3909934
#hw7 exercise2
#Start from CC solutions plotDataset.py

import numpy as np
import matplotlib.pyplot as plt
import ccHistStuff as cc

# read the data set
X = np.load("dataSet.npy")

# the bin edges (nbins + 1 because of lower and upper edge)
nbins = 40
bins  = np.linspace(0, 20, nbins+1)

# the histogram
fig, ax = plt.subplots()
contents, binEdges, _ = ax.hist(X, bins, histtype='step', log=True, color='black')
#contests contains N values
#construct x values, which are at the center of each bin
x_long = []
for i in range(len(binEdges)-1):
    center = (binEdges[i]+binEdges[i+1])/2
    x_long.append(center)
x_long = np.array(x_long)
#fit only first 25 bins
x = x_long[:25]
N = contents[:25]
#print(len(x),len(N)) #test


#fit function
def f(x,p0,p1):
    return p0*np.exp((-p1)*x)

# Initial Guess 
p = np.array([10000,0.3])
y0 = f(x,p[0],p[1])

#inverse convariance matrix
#sigma_i = sqrt(Ni)
W = np.diag(1/N)
#print(W) #test

#iteration time
niter = 10
#derivative of p[0] is np.exp(-p[1]*x)
#derivative of p[1] is -x*p[0]*e^(-p[1]*x)
for iteration in range(niter):
    At = np.array([np.exp(-p[1]*x),-x*f(x,p[0],p[1]) ]) # 2xN 
    A = (At.T).copy()    #Nx2
    dy = np.array([(N-y0),]).T        #1xN
    
    #print(At.shape,A.shape,dy.shape) #test
    #first calculated (At*W*A)^-1
    temp1 = np.matmul(At,W)
    temp2 = np.matmul(temp1,A)
    inver = np.linalg.inv(temp2)
    
    #Calculate C
    temp3 = np.matmul(inver,At)
    C = np.matmul(temp3,W)
        
    #update p[0],p[1]
    diff = np.matmul(C,dy)
    p[0] = p[0]+diff[0][0]
    p[1] = p[1]+diff[1][0]

    #update y0,chisq
    y0 = f(x,p[0],p[1])
    chisq = ((N-y0)**2/N).sum()
    
    print(' ')
    print('interation No.',iteration)
    print('Chisq is',chisq)
    print('p0=',p[0])
    print('p1=',p[1])
#print final parameters and chisq
print('')
print('final values')
print('Chisq is',chisq)
print('p0=',p[0])
print('p1=',p[1])

#plot fitted functions (extend to the full range of graph)
y_long = f(x_long,p[0],p[1])
ax.plot(x_long,y_long,'--r')

# We were asked to add labels and stat box
ax.set_xlabel('X')
ax.set_ylabel('Entries per 0.5')
cc.statBox(ax, X, binEdges)

# This is purely esthetics (personal preference)
ax.tick_params("both", direction='in', length=10, right=True)
ax.set_xticks(binEdges, minor=True)
ax.tick_params("both", direction='in', length=7, right=True, which='minor')
ax.set_xlim(0, 20)

plt.show()

