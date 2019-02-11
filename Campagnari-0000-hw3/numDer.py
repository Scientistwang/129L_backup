#!/usr/bin/env python
#
# Two numberical approximations to df/dx
# (Newton's different quotient and symmetric different quotient)
#
#  CC 28 Jan 2019
#----------------------------------

# This is the function to differentiate
def f(x):
    return x**2 * (x - 1.)

# First Approximation
print("Newton's different quotient approximation:")
h = 0.01
x = 1.
while h > 1.e-20:
    dfdx = (f(x+h)-f(x))/h
    print("h = %.0e    f\'(1) =%24.20f" % (h, dfdx) )
    h = h/10.

print(" ")
print(" ")

print("Symmetric different quotient approximation:")
h = 0.01
x = 1.
while h > 1.e-20:
    dfdx = (f(x+h)-f(x-h))/(2 * h)
    print("h = %.0e    f\'(1) =%24.20f" % (h, dfdx) )
    h = h/10.

