#!/usr/bin/env python3
#
# MC integration of 2D function thisF over
# interval [xmin xmax] [ymin ymax]
#  (analytic answer is 47)
#
#   CC 26 Jan 2019
#----------------------------------------
import numpy as np

def thisF(x,y):
    return (x+2*y)*(x+y)

# intervals
xrng = [0., 1.]
yrng = [2., 4.]

# 2D-"Volume" (really an area in this case
V = (xrng[1] - xrng[0]) * (yrng[1] - yrng[0])

# number of MC points
n = 100000

# initialize random number
np.random.seed(129871)

# get random numbers in range
xr = np.random.uniform(xrng[0], xrng[1], n)
yr = np.random.uniform(yrng[0], yrng[1], n)

# get function
fr = thisF(xr, yr)

# estimated integral
integral = (V/n) * fr.sum()

# calculate the uncertainty
fMean = fr.mean()
fVar  = (1/(n-1)) * ((fr-fMean)*(fr-fMean)).sum()
delta = V * np.sqrt(fVar/n)

# print it out
print("Integral = ", integral, "+-", delta)
    
