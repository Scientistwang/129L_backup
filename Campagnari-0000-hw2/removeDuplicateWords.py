#!/usr/bin/env python3
#
# Prompt the user for a sentence
# Output the sentence removing duplicate words.
# All punctuations are dropped.
#
# CC 22 Jan 2019
#----------------------------------------

# Prompt the user for input
inp = input("Enter a sentence: ")

# Replace punctuations with bank spaces.
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
# The output is a list.  Each item in the list is a word
words = inp.split()

# a new empty list to hold all the words with no duplicates
wordsNoDup = []      # an empty list

# Loop over words from the original list.
# If the word is not in the new list, add it to it
for w in words:
    if w not in wordsNoDup:
        wordsNoDup.append(w)

# Build the output string and send it to the screen
output = " "     # an empty string
for w in wordsNoDup:
    output = output + w + " "
print(output.strip())




