#!/usr/bin/python3

string = input("Please enter a sentence: ")
sepra = []  # will be a list containing positions of separations
for i in range(len(string)):
    if string[i]==',' or string[i]==' ':
        sepra.append(i) 
#print(sepra)  # for testing purposes
words = []
for j in range(len(sepra)):
    if j==0:   
        if sepra[j]>0: #adding the first word
            words.append(string[0:sepra[j]]) 
    if j>0:     
        if sepra[j]-sepra[j-1]>1: #if ther is a word between
            if string[sepra[j-1]+1:sepra[j]] not in words:
                words.append(string[sepra[j-1]+1:sepra[j]])
    if j==len(sepra)-1: #adding the last word
        if sepra[j]<len(string)-1:
            if string[sepra[j]+1:len(string)] not in words:
                words.append(string[sepra[j]+1:len(string)])
#print(words) #test purposes

out = ''
for l in range(len(words)):
    out += words[l]+' '
print(out)

