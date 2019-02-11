#!/usr/bin/python3
import ccHistStuff as cc
import numpy as np
import matplotlib.pyplot as plt


data = np.load('dataSet.npy')#import data
print(min(data),max(data)) #for test purposes

#histogram
nbins = 13
bins = np.linspace(-5,+1.5,nbins+1)#get these numbers from trial
fig,ax = plt.subplots()
contents,binEdges,_, = ax.hist(np.log10(data),bins,histtype = 'stepfilled',log = True,color = 'b')

cc.statBox(ax,np.log10(data),binEdges)

ax.set_xlim(binEdges[0],binEdges[-1])
ax.set_xticks(binEdges,minor = True)
ax.tick_params("both",direction = 'in')
ax.set_xlabel(r'$log_{10}x$')
ax.set_ylabel('count')
plt.show()

