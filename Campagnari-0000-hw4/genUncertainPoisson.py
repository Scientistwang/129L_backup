#!/usr/bin/env python3
#
# Generate and plot Poisson numbers
# including uncertanty (either Gaussian or logNormal)
# 
# CC 29 Jan 2019
#     5 Feb 2019  also return pvalue
#     6 Feb 201   added uncertainty
#----------------------------------------
import argparse
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import ccHistStuff as cc

# Define the arguments
parser =  argparse.ArgumentParser(description="Generate and plot Poisson variable. Calculate pvalue of observed")
parser.add_argument('-m','--mean', help='Mean of the Poisson', required=True, type=float)
parser.add_argument('-n', '--nev', help='No. to generate. Default=10K', required=False, type=int, default=10000)
parser.add_argument('-L', '--Low', help='Minimum for plot', required=False, type=int)
parser.add_argument('-H', '--High', help='Maximum for plot', required=False, type=int)
parser.add_argument('-s', '--seed', help='Random seed. Default=10', required=False, type=int, default=1)
parser.add_argument('-o', '--obs',  help='Number of observed events', required=True, type=int)
parser.add_argument('-u', '--unc',  help='Uncertanty on the mean', required=True, type=float)
# If you add "-g" to the command line, it will be True
parser.add_argument('-g', '--gaus', help='Gaussian uncertainties Default=False',
                    action='store_true')


# This is a dictionary containing the arguments
args = vars(parser.parse_args())

# Extract the arguments
mean   = args['mean']  # mean
nev    = args['nev']   # number of events to generate
seed   = args['seed']
obs    = args['obs']
unc    = args['unc']
gaus   = args['gaus']
nsigma = 5.             # plot to \pm 5 sigma if not specified 
if args['Low'] == None:
    nMin = int(max(0., mean-nsigma*math.sqrt(mean)))
else:
    nMin = args['Low']
if args['High'] == None:
    nMax = int(max(0., mean+nsigma*math.sqrt(mean)))
else:
    nMax = args['High']

# Make sure we dont have too low a maximum
if nMax < 6: nMax=6
if nMax < 1.2*obs: nMax=int(1.2*obs)+1

 
# Initialize the random seed
np.random.seed(seed)

# Generate a bunch of means
if gaus:
    print('-------------------------------------------')
    print("Using Gaussian uncertainties")
    thisMean = np.random.normal(mean, unc, nev)
else:
    print('-------------------------------------------')
    print("Using LogNormal uncertainties")
    thisMean = np.random.lognormal(math.log(mean), math.log(1+unc/mean) , nev)

# If we picked from a Gaussian, let's truncate it and replace the negative ones
thisMean = thisMean[ thisMean>0 ]
if not gaus:
    if len(thisMean) != nev:
        print("Very weird....some lognormal means are <  0  ?????")
while len(thisMean) != nev:
    moreMeans = np.random.normal(mean, unc, nev-len(thisMean))
    moreMeans = moreMeans[ moreMeans>0 ]
    thisMean = np.append(thisMean, moreMeans)

# Generate a bunch of poisson
entries = np.random.poisson(thisMean)

# Calculate the pvalue
boolArray = entries >= obs   # an array of True/False
nTail = boolArray.sum()      # the number of trues in the array
print("-------------------------------")
if nTail == 0:
    print("Not a single try with at least %d entries" %obs)
    print("Cannot calculate very small pvalue")
else:
    pvalue = nTail/nev
    nsigma = stats.norm.ppf(1-pvalue)
    print("pvalue        = ", pvalue)
    print("which corresponds to")
    print("No. of sigmas = ", nsigma)
    print("This number of sigma (n) is from the tail integral of a gaussian distribution.")
    print("In other words, for a gaussian of mean=0 and sigma=1, the integral from")
    print("n to infinity would be equal to ", pvalue)
print("-------------------------------")
    
# Define 1x1 figure
fig, ax = plt.subplots(1,1)

# the histogram
contents, binEdges, _ = ax.hist(entries, np.linspace(nMin-0.5, nMax+0.5, nMax-nMin+2), histtype='step', log=False, color='black')
cc.statBox(ax, entries, binEdges)
ax.set_xlim(binEdges[0], binEdges[-1])
ax.tick_params("both", direction='in', length=10, right=True)

# show the figure
fig.show()
# plt.show()  (this would pause automatically)
input("Press any key to continue")

