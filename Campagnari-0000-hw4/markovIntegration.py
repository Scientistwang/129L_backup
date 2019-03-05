#!/usr/bin/env python3
#
# Markov chain integration of 2D function
# x^2 + 2y^2 +3xy over the interval
# [xmin=0 xmax=1] [ymin=2 ymax=4]
#
# The function can be re-written as
#  f(x,y) = (x+2y)*(x+y) = g(x,y)*p(x,y)
# where
# p(x,y) = (x+y)/7
# g(x,y) = 7(x+2y)
# Then
# p(x,y) is a properly normalized pdf over the interval.
#
# We will proceed as follows:
# (a) Generate a Markov Chain according to p(x,y).
#     The "proposal" function will be of symmetric Metropolis-Hastings type
#     Will use 10% of the chain as "burn in"
# (b) The expectation values of g(x,y) will be used to approximate the integral
#
# (analytic answer is 47)
#
#   CC 26 Jan 2019
#----------------------------------------
import numpy as np

# True if (x,y) is out of range
def outOfrange(x, y, dx, dy):
    out = False
    out = out or x<dx[0]
    out = out or x>dx[1]
    out = out or y<dy[0]
    out = out or y>dy[1]
    return out

# The pdf (note: to generate the chain the normalization is not needed
def thisPdf(x,y):
    return (x+y)

# The function
def thisG(x,y):
    return 7*(x+2*y)

# A proposal: 2D gaussian of sigma=step
def proposal(x,y,step):
    xpr = x + step*np.random.randn()
    ypr = y + step*np.random.randn()
# The one below is an alternative proposal: uniform +/- step
#    xpr = x - step/2. + step*np.random.rand()
#    ypr = y - step/2. + step*np.random.rand()
    return xpr, ypr
    
# intervals
xrng = [0., 1.]
yrng = [2., 4.]

# step for the propsal
step = 0.5

# number of MC points
n = 100000

# initialize random number
np.random.seed(1629871)

# start in the middle (makes sense, I guess)
xstart = 0.5 * (xrng[1] + xrng[0])
ystart = 0.5 * (yrng[1] + yrng[0])
xlist  = [xstart]
ylist  = [ystart]

# do n-1 steps (we already have 1 step...)
for i in range(n-1):
    xp, yp = proposal(xlist[-1], ylist[-1], step)
    if outOfrange(xp, yp, xrng, yrng):
        xlist.append(xlist[-1])
        ylist.append(ylist[-1])
    else:
        fnow  = thisPdf(xlist[-1], ylist[-1])
        fnext = thisPdf(xp,    yp)
        a = fnext/fnow
        if np.random.rand() < a:
            xlist.append(xp)
            ylist.append(yp)
        else:
            xlist.append(xlist[-1])
            ylist.append(ylist[-1])

# put in an array removing a 10% burn out
xr = np.array(xlist[int(0.1*n) : ])
yr = np.array(ylist[int(0.1*n) : ])

# This is the actual number of samples we will be using
n = len(xr)

# get function
fr = thisG(xr, yr)

# estimated integral
integral = (1./n) * fr.sum()

# print it out
print("Integral = ", integral)
