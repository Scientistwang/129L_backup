#!/usr/bin/env python3
#
# Prompt the user for a sentence, count the
# number of words and the number of non blank
# characters (whitespaces)
#
# CC 22 Jan 2019
#----------------------------------------

# Prompt the user for input
inp = input("Enter a sentence: ")

# We need to count words...words can be separated by
# blank spaces, but also various punctuations.
# Save the original entry, then substitutes blank
# spaces for commas etc. 
original = inp 
inp = inp.replace("," , " ")
inp = inp.replace("." , " ")
inp = inp.replace(";" , " ")
inp = inp.replace(":" , " ")
inp = inp.replace("!" , " ")
inp = inp.replace("?" , " ")

# This is most likely not necessary, but just in case
# remove leading and trailing whitespaces
inp = inp.strip()

# Split the strings into pieces, using whitespaces
# The output is a list.  Each item is a list is a
# word.  The number of items in the list is then the
# number of words
w = inp.split()
print("The number of words in the sentence is ", len(w))

# To count the number of non blank characters we will take
# the original input string and remove all whitespaces.
# The length of the string will then be the number of characters.
inpNoBlank = original.replace(" ","")
print("The number of non blank characters in the sentence is ", len(inpNoBlank))
