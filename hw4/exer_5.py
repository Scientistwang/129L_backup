#!/usr/bin/python3

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

#x is from -3 to 15
Nx = 100
x = np.linspace(-3,15,Nx)

N = 5
def g(x,y):
	return np.exp(-(x+y))*(x+y)**N

f_x = []
for x_i in x:
	Ny = 1000
	lower, upper = 0, np.inf
	mu, sigma = 3, 0.5
	X = stats.truncnorm(
    (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
	y = X.rvs(Ny)
	sum_gy = 0
	for y_i in y:
		sum_gy+=g(x_i,y_i)
	f_x.append(sum_gy/Ny)

plt.plot(x,f_x,'b')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
	

