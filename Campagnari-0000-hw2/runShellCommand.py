#!/usr/bin/env python3
#
# Run the command /bin/ls /etc from python and
# output the result to the screen
#
import os
import subprocess

command = '/bin/ls /etc/'

# First we do it through the os modules (which still
# works but is "deprecated".
print("We first do this through the deprecated os module")
input("Enter carriage return to continue ")

blah   = os.popen(command)   # issue the command into a pipe
result = blah.read()         # result is now a string
lis    = result.split('\n')  # split into a list based on newline delimiter
for l in lis:
    print(l)                 # print it line by line
# Note:
# We could have just done
# print(result)
# and gotten the exact same output :)
# Also:
# this is not protected against errors


# Next, we do the same thing using the more modern subprocess pachage
print(" ")
print(" ")
print("---------------------------")
print("Now we do the same thing through the process module")
input("Enter carriage return to continue ")

# Note: the first parameter of subprocess.run should be a list,
# something like ['/bin/ls', '/etc/']
# We make a list by splitting the command string defined above
result = subprocess.run(command.split(), stdout=subprocess.PIPE)

# result.stdout is a byte stream, decode into an ascii string
string = result.stdout.decode('ascii')

# Now we send the output to the screen
print(string)
# Note: we could have broken the string into a list
# just like we did in the first example solutions
#
# A different way of doing the same thing is shown below
# Note: result.communicate is a tuple of byte streams, we take
# the first entry of the tuple and decode it
#
#result = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
#print( (result.communicate()[0]).decode('ascii') )


