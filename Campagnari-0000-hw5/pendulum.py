#!/usr/bin/env python3
#
# Plot the correction to the small angle approximation
# to the period of the pendulum as a function of the
# amplitude of oscillation in degrees.
#
# Integral will be done with the simple MC method
#
# CC 7 Feb 2019
#---------------------------------
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import special
import ccHistStuff as cc

# Complete elliptic integral of the 1st kind I(k)
# I(K) = Integral [f(beta,k) dbeta]
# The interval of integration is 0->pi/2
def f(beta, k):
    s2 = np.sin(beta)*np.sin(beta)
    return 1./ np.sqrt(1-k*k*s2)

# Angles from 0 to 90 in degrees (amplitude)
angleDegree = np.linspace(0.,90.,91)
k = np.sin(math.pi * angleDegree / 360.)

# We will store the results here
result   = []
error    = []   # needed for the "bonus" plot at the end
scResult = []   # result from scipy integration (as a "bonus")

# Initialize seed
np.random.seed(1284567)

# Nimber of MC points
N = 5000

# Loop over amplitudes (ie: loop over k)
# There are somehat wasteful multiplications by pi/2
# to get the integral, immediately followed by 
# multiplications by 2/pi to get the correction to
# the actual period (but OK, never mind, CPU is cheap)
for thisK in k:
    beta       = 0.5 * math.pi * np.random.rand(N)
    fbeta      = f(beta, thisK)
    integral   =  (math.pi/(2*N)) * fbeta.sum()
    correction = (2./math.pi) * integral
    result.append( correction )

    # needed for the "bonus" at the end
    # https://en.wikipedia.org/wiki/Monte_Carlo_integration
    mean       = fbeta.mean()
    temp       = (fbeta-mean)*(fbeta-mean)
    fVar       = temp.sum()/(N-1)                     # variance of f
    iVar       = (math.pi/2)*(math.pi/2) * fVar / N   # variance of the integral
    eCorr      = (2./math.pi) * np.sqrt(iVar)         # error on correction
    error.append( eCorr )
    scIntegral = special.ellipk(thisK*thisK)
    scCorr     = (2./math.pi) * scIntegral
    scResult.append( scCorr)


# Plot the correction
fig, ax = plt.subplots()
ax.plot(angleDegree, result)
ax.set_xlim(angleDegree[0], angleDegree[-1])
ax.grid(True, which='both')
ax.set_ylim(0.9, 1.3)
fig.show()
input("Carriage return to continue....")

# A bonus (see message below)
print(' ')
print('As a bonus, we compare with the result from the scipy function')
print('For each angle, we calculate the stat. uncertainty (\"u\") on')
print('the correction factor that we compute (\"c\").')
print('We then compare from what scipy claims it should be (\"s\").')
print('We calculate a pull for each angle as pull=(c-s)/u.')
print('Assuming that \"s\" is MUCH more precise than \"c\", the')
print('pull distribution should have mean=0 and sigma=1')

num     = ( np.array(result) - np.array(scResult) )  
den     = np.array(error)
den[0]  = 1.      # this is a zero pull (perfect)
pull    = num/den
f2, a2  = plt.subplots()
c, b, _ = a2.hist(pull, np.linspace(-3,3,20), histtype='step')
cc.statBox(a2, pull, b)
a2.set_xlim(-3,3)
f2.show()

input("Carriage return to continue....")







    
    
