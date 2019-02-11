#!/usr/bin/env python3
#
# Calculate pi by throwing random numbers (x,y)
# between 0 and 1.
# Then pi = 4 * fraction with (x^2 + y^2) < 1
# Calculate also error due to binomial stats
#
# Do it by throwing sets of 100, 1000 .... 10^6 pairs
#
# Then plot pi as a function of the number of throws
# (with statistical uncertainty of course)
# Also, output values, chisq, and chisq probability
#
#        CC 28 jan 2019
#---------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats

# The random number seed
seed = 1004529

# Empty lists which we will turn into np.array
# It would have been nicer to calculate the error
# later from numpy array, but whatever...this works too.
myPi    = []     # to store results of calculation of pi
myPiErr = []     # to store the error on pi
n       = []     # to store the number of tries

# Loop over sets
for i in np.arange(2,7):         # of pairs in this set will be 10**i
    seed = seed + 10000*i        # new seed for this set 
    np.random.seed(seed)
    x  = np.random.rand(10**i)
    y  = np.random.rand(10**i)
    r2 = x*x + y*y
    # r2<10 is an array of boolean.  Booleans are equivalent to (0,1)
    # Therefore sum over the array gives me the number of True's.
    inCircle = (r2<1.0).sum() 
    frac = inCircle/(10**i)     # this is the fraction with r2<1 
    myPi.append(4.* frac)       
    myPiErr.append(4 * math.sqrt(frac * (1-frac) / (10**i)))
    n.append(10**i)

# turn the lists into arrays
myPi    = np.array(myPi)
myPiErr = np.array(myPiErr)
n       = np.array(n)

# The pulls, the percentage accuraccy, the chisq
dpi     = 100. * np.abs((myPi-math.pi)/math.pi)
pull    = (myPi-math.pi)/myPiErr
chisq   = (pull*pull).sum()
chiprob = 1 - stats.chi2.cdf(chisq, len(n))
    
# Print stuff out
for thisN, thisAcc, thisPull in zip(n, dpi, pull):
    print("N = %.0e   Accuracy = %5.3f%s    pull = %6.2f"
              % (thisN, thisAcc, "%", thisPull))
print('chisquared       = %5.2f per %2d degrees of freedom' % (chisq, len(n)))
print("chisquared prob  = %5.2f" % chiprob)
print("\n \n")
print("Now for a nice plot \n \n")
    

# Plot the measured value of pi
fig, ax = plt.subplots()
ax.errorbar(n, myPi, linestyle='none', yerr=myPiErr, marker=".")
ax.set_xlim(10, 4*n[-1])    # decent lower and upper limits
ax.tick_params("both", direction='in', length=10, right=True)
left, right = ax.get_xlim()  # get the limits that we just put in :)
ax.plot( [left, right], [math.pi, math.pi])  # line at true value of pi
ax.set_xscale('log')   # of course the x axis should be log!
fig.show()



input("enter something to exit")


    
    
