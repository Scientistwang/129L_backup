#!/usr/bin/python3

import csv
#import locale
#locale.setlocale( locale.LC_ALL, 'en_US.UTF-8')
import numpy as np
import matplotlib.pyplot as plt

with open('CensusTownAndCityPopulation.csv' , 'r') as f:
	data = csv.reader(f)
	numbers = []
	next(data,None)
	for row in data:
		numbers.append(int(row[2][0]))
	#print(numbers)

####plot
bins = np.linspace(0.5,9.5,10)
fig,ax = plt.subplots()
contents, binEdges, _ = ax.hist(numbers,bins,histtype = 'stepfilled',color = 'r', label = 'first signifcant digit from census data',alpha = 0.5)
ax.legend(loc='upper right')
ax.set_xlabel('digit')
ax.set_ylabel('count')
ax.set_xlim(binEdges[0],binEdges[-1])
ax.tick_params("both",direction = 'in', length = 10, right = True)
plt.xticks(np.linspace(1,9,9))
plt.show()



