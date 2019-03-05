#!/usr/bin/env python3
#
# Decode integer where
# bits 0- 3 = channel
# bits 4- 7 = time
# bits 8-15 = pulseheight
#
# CC 9 Feb 2019
#
def decodeWord(word):
    channelMask = 0b0000000000001111
    timeMask    = 0b0000000011110000
    pulseMask   = 0b1111111100000000
    ch    =  word & channelMask
    time  = (word & timeMask) >> 4
    pulse = (word & pulseMask) >> 8
    return ch, time, pulse

# get input from keyboard
while True:
    try:
        word = int(input("Please enter integer to decode "))
        break                # get out of the while loop
    except ValueError:
        print("You did not enter a valid integer, try again")

c,t,p = decodeWord(word)

print("channel = ", c)
print("time    = ", t)
print("pHeight = ", p)
