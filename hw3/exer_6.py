#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#generate numbers
x = [0]
y = [0]
fig,ax = plt.subplots()
line, = ax.plot(x,y)

def animate(i):
	ran = np.random.random()
	if ran < 0.25:
		x.append(x[-1]+1)
		y.append(y[-1])
	elif ran <0.5:
		x.append(x[-1]-1)
		y.append(y[-1])
	elif ran<0.75:
		x.append(x[-1])
		y.append(y[-1]+1)
	else:
		x.append(x[-1])
		y.append(y[-1]-1)
	line.set_xdata(x)
	line.set_ydata(y)
	print(len(x))
	return line ,

plt.axis([-50,50,-50,50])
ani = animation.FuncAnimation(fig,animate,frames = 998,interval =1,repeat = False)
fig.show()
input("Press Enter to quit:")






