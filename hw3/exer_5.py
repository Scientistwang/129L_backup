#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

N = 10000
r = np.random.random(N)
x = np.sqrt(3*r/2+1/16)-1/4 #calculated according to notes
curve_x = np.linspace(0,1,1000)
g = N/10*(1+4*curve_x)/3

#plot stuffs
fig,ax = plt.subplots()
bins = np.linspace(0,1,11)
ax.plot(curve_x,g,'b')
contents,edges,_ = ax.hist(x,bins,histtype = 'stepfilled',color ='r')
ax.set_xlim(edges[0],edges[1])
ax.set_xticks(edges,minor = True)
ax.tick_params("both",direction ='in', length = 10, right = True)
plt.show()

