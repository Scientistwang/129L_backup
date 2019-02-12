#!/usr/bin/python3
# Zipeng Wang
# 3909934

import numpy as np

#g(x,y) = (x+y)/7

def g(x,y): 
	if x>0 and x<1 and y>2 and y<4:
		return (x+y)/7
	else:
		return 0

def prop(x,y): #uniform at a square around (x,y)
	x_out = 1*(np.random.random()-0.5)+x #betwen x-0.5 and x+0.5
	y_out = 2*(np.random.random()-0.5)+y #betwen y-1 and y+1
	return x_out,y_out
###initialize the chain in the middle
mark_x = [0.5]
mark_y = [3]
###create markov chain
N = 100000
burnn = N//10 #create N//10 more pts for burning in
for i in range(N+burnn-1):
	x_prop,y_prop = prop(mark_x[-1],mark_y[-1])
	a = g(x_prop,y_prop)/g(mark_x[-1],mark_y[-1])
	a = min([1,a])  #probably no use
	trial = np.random.random()
	if trial<a:
		mark_x.append(x_prop)
		mark_y.append(y_prop)
	else:
		mark_x.append(mark_x[-1])
		mark_y.append(mark_y[-1])

#discard the first 10% of the chain
del mark_x[0:burnn]
del mark_y[0:burnn]

print(len(mark_x),len(mark_y))

#####Monte Carlo########
###f = (x+y)*(x+2y)in x:[0,1], y:[2,4]
###since we already extracts g(x,y),only
###need to approximate (x+2y)/7
sum_f = 0
for i in range(len(mark_x)):
	sum_f+= (mark_x[i]+2*mark_y[i])*7

I = 1./len(mark_x)*sum_f
print(I)








