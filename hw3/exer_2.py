#!/usr/bin/python3

def f(x):
	return (x**2)*(1-x)

#def deri_f_1(x,h):
#	return (f(x+h)-f(x))/h

#def deri_f_2(x,h):
#	return (f(x+h)-f(x-h))/2h   don't actually need them, but are good refs 
#                               be put here.

time = 18
deri_1 = []
deri_2 = []
for i in range(time):
	h = 10**(-2)*10**(-i)
	deri_1.append((f(1+h)-f(1))/h)
	deri_2.append((f(1+h)-f(1-h))/(2*h))
	print("h =", h)
	print("method1: %.20f" % deri_1[-1])
	print("method2: %.20f" % deri_2[-1])

