#!/usr/bin/env python3
#
# Runge-Kutta solution to low pass
# RC filter with RC=tau (1 musec)
# Input voltage is square wave btw +/- 1 V
# V=1  for t=0-1 musec
# V=-1 for t=1-2 musec
# etc etc
#
# Result is plotted for 0-10 and 90-100 musec
# 
# CC 9 Feb 2019
#-------------------------
import math
import numpy as np
import matplotlib.pyplot as plt

# The derivative y' = f(x,y)
def f(Vin, Vout, tau):
    return (Vin - Vout)/tau
    
# The Runge Kutta function
def rKutta(VoutNow, VinNow, VinHalfStep, VinNext, step, tau):
    k1 = step * f(VinNow,      VoutNow,       tau)
    k2 = step * f(VinHalfStep, VoutNow+k1/2., tau)
    k3 = step * f(VinHalfStep, VoutNow+k2/2., tau)
    k4 = step * f(VinNext,     VoutNow+k3,   tau)
    d  = (k1 + 2*k2 + 2*k3 +k4)/6.
    return VoutNow+d 

# Get input from keyboard
while True:
    try:
        tau = float(input("Please enter tau in microseconds "))
        break                # get out of the while loop
    except ValueError:
        print("You did not enter a valid float, try again")

# minimum and maximum for the calculation
tmin =  0.
tmax = 100.

# Seems sensible that the time steps
# be smaller than tau.
# step = tau/50 seems reasonable
# Then again, CPU is cheap, so we can
# probably easily afford 10K steps.
step  = tau/50.
nstep = int( (tmax-tmin)/step )
if nstep < 100000:
    nstep = 100000
step = (tmax-tmin)/nstep
print("We will use nstep = ", nstep)

# For Runge Kutta I need Vin specified
# with twice the granularity as Vout
# Twice the granularity:
t2    = np.linspace(tmin, tmax, 2*nstep)
temp2 = np.floor(t2)   # truncate the floats
Vin2  = 1 - 2*np.mod(temp2, 2)
# Granularity for Vout
t    = np.linspace(tmin, tmax, nstep)
temp = np.floor(t)   # truncate the floats
Vin  = 1 - 2*np.mod(temp, 2)
Vout = np.zeros( nstep )

# Solve for Vout
for i in range(nstep-1):
    j = 2*i
    Vout[i+1] = rKutta(Vout[i], Vin2[j], Vin2[j+1], Vin2[j+2], step, tau)
    
# Plot Vout and Vin for 0-10 and 90-100
fig, ax = plt.subplots(2,1)

ax[0].plot(t, Vout)
ax[0].plot(t, Vin)
ax[0].set_xlim(0, 10)
ax[0].grid(True, which='both')

ax[1].plot(t, Vout)
ax[1].plot(t, Vin)
ax[1].set_xlim(90, 100)
ax[1].grid(True, which='both')

fig.show()
input("Carriage return to continue....")
