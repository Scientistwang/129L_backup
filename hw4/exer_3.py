#!/usr/bin/python3
#integral [2,4]dy[0,1]dx(x+2y)(x+y) using MC
# Correct Value: 47
import numpy as np
N = 100000
x = np.random.random(N)
y = 2*np.random.random(N)+2 #uniform in (2,4)
sum_f = 0
for i in range(N):
	sum_f += (x[i]+2*y[i])*(x[i]+y[i])

I = (4-2)*(1-0)/N*sum_f
print(I)




