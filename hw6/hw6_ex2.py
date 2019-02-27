#!/usr/bin/python3
#Zipeng Wang
#3909934
#hw6 problem2
import argparse
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

#input
# Define the arguments
parser =  argparse.ArgumentParser(description="plot Bayesean posterior pdf")
parser.add_argument('-N','--N', help='Observed value', required=True, type=int)
parser.add_argument('-m', '--mu', help='Background mean', required=True, type=float)
parser.add_argument('-s', '--sigma', help='Uncertainty of background', required=True,type = float)

# This is a dictionary containing the arguments
args = vars(parser.parse_args())

# Extract the arguments
N    = args['N']  
mu    = args['mu']  
sigma   = args['sigma']

xlim = 15
Nx = 300
x = np.linspace(0,xlim,Nx+1) # pts on x-axis # limited to x>0
x = np.delete(x,-1) #leave only 100 pts, on the left of each interval
dx = xlim/Nx
def g(x,y):
	'''function being integrated'''
	return np.exp(-(x+y))*(x+y)**N

f_x = []# will contain pts in y-axis
for x_i in x:
	Ny = 300
	lower, upper = 0, np.inf
        #Generate truncated Gaussian fron 0 to +inf
	X = stats.truncnorm(
    (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
	y = X.rvs(Ny)
	sum_gy = 0
	for y_i in y:
		sum_gy+=g(x_i,y_i)
	f_x.append(sum_gy/Ny)

#Normalize f_x 
#assume that f(x) value after x=15 are negligible
sum_f_x = sum(f_x)*dx # area of the original integral
for i in range(len(f_x)):
	f_x[i] = f_x[i]/sum_f_x

#print(sum(f_x)*dx)	 #check if properly normalized

#count 95% value of x(which is just S)
area = 0
for i in range(len(f_x)):
	if area > 0.95:
		break
	area += f_x[i]*dx
print(area)
print('95% Bayesean Cl is',x[i])
#about 3.7 for N = 1, mu = 3, sigma = 0.5
#about 7.75 for N = 5, mu = 3, sigma = 0.5
#Plot config stuffs
plt.plot(x,f_x,'b')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Approximation of f(x) between [0,{}]".format(xlim))
plt.xlim([0,xlim])
plt.show()
	


