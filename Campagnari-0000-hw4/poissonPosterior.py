#!/usr/bin/env python3
#
# This is a plot of the function
# f(x) = Integral [exp(-x-y) * (x+y)^N G(y | mu sigma) dy]
# where G is a Gaussian for y of mean=mu and std dev=sigma
# with y>0
#
# It is plotted betwee x1 and x2
#
# CC 6 Feb 2019
#--------------------------------
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import ccHistStuff as cc

# The function that multiplies the Gaussian
def ff(x,y,N):
    return np.exp(-x-y) * (x+y)**N

# parameters from problem
N       = 5
mu      = 3
sigma   = 0.5
x1      = -3.
x2      = 15.
npoints = 100            # number of points in x to plot
ntoy    = 1000           # for MC integration of y
dx      = (x2-x1)/100
xar     = np.linspace(x1, x2, npoints) # the points in x to plot

# init random number
np.random.seed(1234567)

# an array for f(x) initialized to zero
far = np.zeros(npoints)
i = 0
for x in xar:
    y      = np.random.normal(mu, sigma, ntoy)  # pick y
    y      = y[ y> 0 ]      # require y>0
    thisN  = len(y)         # how many "usable" y's do we really have?       
    ftoy   = ff(x, y, N)    
    far[i] = (1./thisN) * ftoy.sum()
    i      = i + 1

# now the plot
fig, ax = plt.subplots()
ax.plot(xar, far)
ax.set_xlim(x1,x2)
ax.set_ylim(0)
ax.grid(True, which='both')
fig.show()
input("blah to continue")
