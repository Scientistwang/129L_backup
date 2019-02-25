#!/usr/bin/python3
#Zipeng Wang
#3909934
#hw5 problem 2
#Plot Julia set
import numpy as np
import matplotlib.pyplot as plt
import math
thisMap = 'jet'
xpix = 640
ypix = 400
dx = 3.2/xpix  #step of x in range[-1,6,1.6] 
dy = 2/ypix    #step of y in range[-1,1]

c = complex(-0.79,0.156)
pixColor = np.zeros((xpix,ypix),dtype="uint8")

for ix in range(xpix):
	for iy in range(ypix):
		Loop = True
		# range of x is [-1.6,1.6] 
		x = -1.6+ix*dx #the left edge of the pixel
		y = -1+iy*dy #the bottom edge of the pixel
		xc = x+dx/2 #center of the pixel
		yc = y+dy/2 #center of the pixel
		z = []
		z.append(complex(xc,yc)) #initializing z0
		if abs(z[-1])>2:
			pixColor[ix,iy] = 0
			Loop = False
		if Loop:
			for n in range(1,256):#n is from 1 to 255
				z.append(z[-1]**2+c)
				if abs(z[-1])>2:
					pixColor[ix,iy] = n
					break
#####plotting
newpixColor = np.flipud(pixColor.transpose())
f1,ax1 = plt.subplots()
picture = ax1.imshow(newpixColor,interpolation = 'none',cmap = thisMap)

plt.show()
















