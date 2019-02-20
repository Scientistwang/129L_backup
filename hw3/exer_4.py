#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
N = 101
x = np.linspace(0,1,N) #L=1
y = np.linspace(0,1,N)
phi = np.zeros([N,N])
print(phi.shape)
#calculating phi
for i in range(N):
	for j in range(N):
		phi[i][j] = np.sin(2*np.pi*x[i])*np.sin(5*np.pi*y[j])
phi = phi.transpose()

fig,ax = plt.subplots()
image = ax.imshow(phi,cmap = 'jet',origin = 'lower',aspect = 'auto')
fig.colorbar(image)
plt.show()
		
