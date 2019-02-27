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

S_set = np.linspace(0,15,300) #resonable values of S
num_events = 300  #the "a bunch of numbers" from Possionan mean of S+B
fraction_set = [] #the fraction of n s.t. n<N associated with each S in S_set 
for S in S_set:
	n_set = []
	for i in range(num_events):
		success = False     #pick a B from truncated gaussian
		while not success:
			B_try = np.random.normal(mu,sigma)
			if B_try > 0:
				success = True
		n_set.append(np.random.poisson(B_try+S)) #from a Poissonian of mean s+b
	n_set = np.array(n_set)
	boolArray = n_set < N     #boolArray technique to calculate number of n s.t. n<N
	fraction_set.append(sum(boolArray)/num_events)

#print(fraction_set) # a good visualization of the decreasing fractions
exclu_S = [] #select those with a fraction < 0.05
for i in range(len(fraction_set)):
	if fraction_set[i]<0.05:
		exclu_S.append(S_set[i])
print(min(exclu_S))
#for N = 5, this value is about 5.6 
#for N = 1, this value is about 0.1 to 0.5
