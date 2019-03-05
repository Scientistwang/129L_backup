#!/usr/bin/env python3
#
# Solve x*cosx=0.5 near x=1
# Uses bisection method
#
# CC 9 feb 2019
#-------------------------
import math

# Will solve for f(x)=0
def f(x):
    return x*math.cos(x)-0.5

# Note f(0.5) = -0.50
#      f(1)   =  0.04
xneg        = 0.5
xpos        = 1.0
dx          = xpos-xneg
tollerance  = 0.0001
while dx/2 > tollerance:
    x = 0.5*(xpos+xneg)
    if f(x) < 0:
        xneg = x
    else:
        xpos = x
    dx = xpos-xneg

result = 0.5*(xpos+xneg)
print("Answer is x = ", result)
print("f(x)        = ", f(x))
