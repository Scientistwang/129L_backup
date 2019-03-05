#!/usr/bin/env python3
#
# Put on the screen a pixel map with
# concentric circles
#
# CC 8-Feb-2019
#-----------------------
import numpy as np
import math
import matplotlib.pyplot as plt

# The color map..pick whatever you like
# More choices here
# https://matplotlib.org/examples/color/colormaps_reference.html
thisMap = "jet"
# thisMap = "brg"
#thisMap = "terrain"
#thisMap = "gnuplot"
#thisMap="ocean"
#thisMap ="brg"

# The boundaries of the plot
xmin = -1.6
ymin = -1.
xmax = 1.6
ymax = 1.

# the size of the figure in pixels
xpix = 640
ypix = 400

# the x and y pixel increments
dx = (xmax - xmin)/xpix
dy = (ymax - ymin)/ypix

# the pixel color map...instantiate a numpy array
# with one entry per pixel and of unsigned integer
# type, one byte (0 to 255)
pixColor = np.zeros( (xpix,ypix), dtype="uint8")
maxPix = 255

# the constant
C = complex(-0.79, 0.156)

# Fill the pixColor array
for ix in range(xpix):
    x = xmin + ix*dx + 0.5*dx
    for iy in range(ypix):
        y = ymin +iy*dy + 0.5*dy
        thisIter = 0
        z = complex(x, y)
        while abs(z) < 2 and thisIter<maxPix:
            z = z*z + C
            thisIter = thisIter+1
        pixColor[ix,iy] = thisIter

# Stupid thing: when putting it on the screen
# the 1st index is the column and the 2nd index is the
# row.  So in order to really have [ix, iy] we need to
# transpose before plotting.
# Even more stupid: the vertical dimension increases
# from the top, not from the bottom.  The "flipud" function
# chnges the order of the rows
newpixColor = np.flipud(pixColor.transpose())

# now the plot
f1, ax1 = plt.subplots()
picture = ax1.imshow(newpixColor, interpolation="none", cmap=thisMap)
ax1.axis("off")   # axis labels off
f1.show()         # show it on the screen
input("Press <Enter> to exit")  # we are done
