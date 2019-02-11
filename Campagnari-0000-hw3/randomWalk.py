#!/usr/bin/env python3
#
# "Animate" a 2D random walk of constant step
#  size 1 in either the x or y direction.
#
# For instructional purpose, it construct
# the random walk with different selectable
# "methods"
#
#                       Claudio 12-12-18
#--------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#-----------------------------------
# Setups
#----------------------------------
n      = 1000       # number of points
method = 2          # method to build random walk
step   = 1          # step size
seed   = 92225      # random number seed
np.random.seed(seed)

#---------------------------------------------
# x and y are coordinates of the random walk.
# Here we get x and y in an ugly brute force way
#---------------------------------------------
if method == 1:
    x = np.array([0])
    y = np.array([0])
    for i in range(n-1):
        # generate random rInteger -2 -1 0 1
        # if -2 --> move back in y
        # if -1 --> move forward in y
        # if 0  --> move back in x
        # if 1  --> move forward in x
        # careful about the range....
        rInteger = np.random.randint(-2,2)
        dx = 0   # step in x
        dy = 0   # step in y
        if rInteger < 0:
            dy = (2*rInteger + 3)*step
        else:
            dx = (2*rInteger - 1)*step
            
        x = np.append(x, x[i]+dx)
        y = np.append(y, y[i]+dy)

#-------------------------------------------------
# This is a much more pythonic way of getting (x,y)
# Elegant, perhaps, but less clear
# It uses the same correspondence between random
# integers (-2, -2, 0, 1) as the previous method
# It uses the trick that multiplying a boolean
# by a number gives 0 or the number (for False vs. True)
# It uses the trick that the position is the
# cumulative sum of all the steps
#-----------------------------------------
if method == 2:
    r  = np.random.randint(-2,2,n) 
    dx = (r>=0) * (2*r-1) * step
    dy = (r<0)  * (2*r+3) * step
    x  = np.cumsum(dx)
    y  = np.cumsum(dy)
       
#--------------------------------------------
# Define the figure and set the axes to be
# such that they fully contain the random walk
# with 10% to spare on all four sides
#---------------------------------------
fig, ax = plt.subplots()
plt.axis([1.1*min(x), 1.1*max(x), 1.1*min(y), 1.1*max(y)])
line, = ax.plot(x[0],y[0])

#-------------------------------------------------
# This is the "animate" function called from 
# by "FuncAnimate".
# Note that line x and y are global variables
#-----------------------------------------
def animate(i):
#    print(i)  # debug statement
    line.set_ydata(y[0:i])
    line.set_xdata(x[0:i])
    return line,

#-----------------------------------------------------------------------
# Finally, this does the actual work. 
#-----------------------------------------------------------------------
ani = animation.FuncAnimation(fig, animate, np.arange(0,n), interval=25, blit=True,
                              repeat=False)
# plt.show()
fig.show()

print("\n \n \n")
input("Enter CR to quit:")


    

    

  
    

