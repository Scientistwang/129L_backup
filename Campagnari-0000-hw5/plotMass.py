#!/usr/bin/env python3
#
# Read the file mass.txt and plot inot
# a reasonably defined histogram
# 
# CC 8 Feb 2019
#---------------------------------
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import special
import ccHistStuff as cc

# Read the masses into an array 
mass = np.loadtxt("mass.txt")

# How many do we have, what is the max and min
#    print( len(mass) )
#    m1 = np.amax(mass)
#    m2 = np.amin(mass)
#    print(m1,m2)
# From te tests above, looks like 200 entries
# between 100 and 200?
# A reasonable binning may be 20 bisn
x1 = 100.
x2 = 200.
nb = 20
bins = np.linspace(x1, x2, nb+1)

# plot now
f, a = plt.subplots()
c, b, _ = a.hist(mass, bins, histtype='step')
cc.statBox(a, mass, b)
a.set_xlim(b[0], b[-1])
a.tick_params("both", direction='in', length=10, right=True)
a.set_xticks(b, minor=True)
a.tick_params("both", direction='in', length=7, right=True, which='minor')
f.show()

input("Carriage return to continue....")


