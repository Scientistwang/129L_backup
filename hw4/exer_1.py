#!/usr/bin/python3
#Zipeng Wang
#3909934
#read data from .npy file and plot a semilog histogram
import ccHistStuff as cc
import numpy as np
import matplotlib.pyplot as plt


data = np.load('dataSet.npy')#import data
print(min(data),max(data)) #for test purposes

#histogram
nbins = 24
bins = np.linspace(0,24,nbins+1)#get these numbers from trial
fig,ax = plt.subplots()
contents,binEdges,_, = ax.hist(data,bins,log = True,color = 'b',rwidth = 0.85)

cc.statBox(ax,data,binEdges)

ax.set_xlim(binEdges[0],binEdges[-1])
ax.set_xticks(binEdges,minor = True)
ax.tick_params("both",direction = 'in')
ax.set_xlabel('x')
ax.set_ylabel('count')
plt.show()

