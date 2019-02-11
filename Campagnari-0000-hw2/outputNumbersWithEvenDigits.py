#!/usr/bin/env python3
#
# Output all numbers between 100 and 400 (included)
# whose digits are all even
#
# CC 22 Jan 2019
#----------------------------------------

# Although the first and last are already specified
# in the question, it is often a good idea to define
# them at the beginning instead of harwiring them
# throughout the code.  This way if you are asked to
# hange them, you know exactly where to go to make the change.
first = 100
last  = 400

# Loop over numbers from first to last
for i in range(first, last+1):    # last+1 is skipped!!!
    s = str(i)              # turn number into string
    good = True             # assume the number i is "good"
    for k in list(s):       # list(s) is list of individual characters
        if int(k)%2 != 0:   # k is a string, int(k) is an integer
            good = False    # this number is no good
            break           # found odd character, no point in looking further

    if good: print(i)
