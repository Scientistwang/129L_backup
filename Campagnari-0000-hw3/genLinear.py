#!/usr/bin/env python3
#
# Pick n random variables between 0 and 1
# with pdf f(x) = (1 + 4x)/3
# Plot the distribution in a histogram with nbins.
#
# This can be done in two ways, with a boolean
#
# In this case the acceptance/rejection 
# method is not needed  
# 
# CC  29-Jan-2019
#-----------------------------------
import numpy as np
import matplotlib.pyplot as plt
import ccHistStuff as cc

# Hardwired parameters
n           = 10000
nbins       = 10
firstMethod = True

# Initialize the seed
np.random.seed(123455)

if (firstMethod):
    #-----------------------------------------------------
    # First method: invert the cumulative distr of f(x)
    #-----------------------------------------------------
    # f(x) = (1+4x)/3
    # The cumulative distribution is F(x) = (x+2x^2)/3
    # The (positive) inverse of F is
    # invF(x) = 0.25 * ( -1 + sqrt(1 - 24x) )
    r = np.random.rand(n)
    x = 0.25 * ( -1. + np.sqrt(1 + 24*r) )

else:
    
    #-------------------------------------
    # Second method.
    #------------------------------------
    # f(x) = (1+4x)/3
    # Can think of two components
    # (a) a "flat" component with probability 1/3
    # (b) a (more) simple linear component with
    #      probability 2/3 pdf g(x) = 2*x
    #      Cumulative is G(x) = x^2
    #      invG(x) = sqrt(x)
    #
    # Draw from either (a) or (b) in the ratio 1:3
    nflat = n//3    # not exactly 1/3 if n not divisible by 3 (ignore)
    nlin  = n - nflat
    xflat = np.random.rand(nflat)
    xlin  = np.sqrt(np.random.rand(nlin))
    x = np.concatenate( (xflat, xlin) )
    # Note: at this point the order in x is not random!!!
    # Since we are just making a plot it does not matter.
    # If we were to use x for some real work we would
    # reshuffle the elements with np.random.shuffle

#------------------------------------------------
# Plot the histogram and the line
#------------------------------------------------
fig, ax, = plt.subplots()

# the histogram
contents, binEdges, _ = ax.hist(x, np.linspace(0., 1., nbins+1),
                                histtype='step', log=False, color='blue') 
cc.statBox(ax, x, binEdges, x=0.3)
# cc.plotErr(ax, contents, binEdges, color='blue')

# the line  (mind the normalization!!!!)
xl = np.array( [0., 1.] )    # straight line, 2 points are enough!!! 
yl = (1./3) * (1. + 4*xl) * (n/nbins)
ax.plot(xl, yl, color='orange', linestyle='dashed')

# make it prettier
ax.set_xlim(binEdges[0], binEdges[-1])
ax.tick_params("both", direction='in', length=10, right=True)
ax.set_xticks(binEdges, minor=True)
ax.tick_params("both", direction='in', length=7, right=True, which='minor')
ax.set_xlabel("Linear random variable")
ax.set_ylabel("Number of entries")

fig.show()
input("Press any key to continue")
