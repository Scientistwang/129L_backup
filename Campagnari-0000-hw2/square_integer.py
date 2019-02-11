#!/usr/bin/env python3
#
# Prompt the user for an integer number, print out the square
#
# CC 22 Jan 2019
#----------------------------------------

# Good inputs are entries like 156 +457 -876
haveGoodInput = False

# Prompt for input, repeat until we get something we like
while not haveGoodInput:
    inp = input("Please enter an integer: ")  # this will return a string

    inp = inp.strip()        # remove leading and trailing whitespace
    if inp.isnumeric():      # is the string made up of all numbers?
        haveGoodInput = True
    elif inp[0]=="+" or inp[0]=="-":   # string starts with a + or a -?
        if inp[1:].isnumeric():        # are all other characters numbers?
            haveGoodInput = True

    if not haveGoodInput:             # tell user to try again
        print(inp, " is not a number")

# We get here when the while loop has terminated
print(inp," squared is ",int(inp)*int(inp))
    
