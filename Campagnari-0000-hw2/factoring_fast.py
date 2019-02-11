#!/usr/bin/env python3
#
# Get an integer and find its prime factors
# (faster version)
#
# CC 26-Apr-2018
#     1-May-2018  Use integer division!!
#----------------------------
import math

# Get the number from the user
while True:
    try:
        inString = input("Enter an integer: ")
        thisNumber = int(inString)
        break
    except:
        print("Not a number, try again")

# list to keep the factors
factors = []

# treat 2 in a "special" way
if thisNumber % 2 == 0: factors.append(2)
N = thisNumber
while N % 2 == 0:
    N = N // 2

keepLooping = True
while keepLooping and N>1 :
    # Loop over all possible factors (the "+3" may be excessive)
    # The business with the isUniqueFactor is probably also not
    # needed.  In any case, it does not hurt.
    foundFactor = False
    for i in range(3, int(math.sqrt(N))+3, 2):
        if (N % i) == 0:
            foundFactor = True
            isUniqueFactor = True
            for j in factors:
                if (i % j) == 0: isUniqueFactor = False
            if isUniqueFactor: factors.append(i)
            while N % i == 0:
                N = N // i
            break
        
    # We found the last factor.
    # No more trying to break it down
    # Add it to the list unless it is a repeat
    if not foundFactor:
        keepLooping = False
        isAlreadyThere = N in factors
        if (not isAlreadyThere): factors.append(int(N)) 

# if we found no factors we are done
if len(factors)==0:
    print(thisNumber," is prime")
    exit()
        
# We now have all the prime factors.
# Now find the power of each factor, store in a parallel list
powers=[0]*len(factors)
index = -1
for i in factors:
    index = index + 1
    p = 1
    while thisNumber % (i**p) == 0:  #keep dividing
        p = p+1
    powers[index] = p - 1

# and now output
for index in range(0,len(factors)):
    print(factors[index], " to the power ", powers[index])
