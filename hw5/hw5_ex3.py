#!/usr/bin/python3
#Zipeng Wang
#3909934
#hw5 problem3
#Read and plot a dataset from mass.txt

import numpy as np
import matplotlib.pyplot as plt
import ccHistStuff as cc

data = np.loadtxt('mass.txt')
print(min(data),max(data))
#ranges between about 100 and 200
####histogram
nbins = 20
bins = np.linspace(100,200,nbins+1)
fig,ax = plt.subplots()
contents,binEdges,_,=ax.hist(data,bins,color = 'b')
cc.statBox(ax,data,binEdges)
######figure configs
ax.set_xlim(binEdges[0],binEdges[-1])
ax.set_xticks(binEdges,minor = True)
ax.tick_params("both",direction = 'in')
ax.set_xlabel('data')
ax.set_ylabel('count')

plt.show()




