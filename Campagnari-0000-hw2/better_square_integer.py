#!/usr/bin/env python3
#
# Prompt the user for an integer number, print out the square
#
# This uses the python facilities to gracefully handle
# errors and exceptions. To learn more about this, see
# https://docs.python.org/3/tutorial/errors.html
#
# CC 22 Jan 2019
#----------------------------------------
import sys   # this is the "package" for exception handling

while True:
    try:
        inp = int(input("Please enter an integer: "))
        break                # get out of the while loop
    except ValueError:
        print("You did not enter an integer, try again")
        
# We get here when the while loop has terminated
print(inp," squared is ",inp*inp)




    
