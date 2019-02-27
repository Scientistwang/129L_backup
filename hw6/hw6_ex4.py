#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
N = 101
x = np.linspace(0,1,N) #L=1
y = np.linspace(0,1,N)
phi = np.zeros([N,N])

#calculating phi
for i in range(N):
	for j in range(N):
		phi[i][j] = (np.sin(2*np.pi*x[i])*np.sin(5*np.pi*y[j]))**2
phi = phi.transpose()

fig,ax = plt.subplots()
levels = [0.1,0.25,0.5,0.8,]
strs = [str(i) for i in levels]
image = ax.contour(x,y,phi,levels)
fmt = {}
for l,s in zip(levels,strs):
	fmt[l]=s
ax.clabel(image,inline = True, fmt=fmt, fontsize = 9)
plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.title('pdf of a particle in 2D box')
plt.show()
		
