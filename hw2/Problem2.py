#!/usr/bin/python3

string = input("Please enter a sentence: ")
sepra = []  # will be a list containing positions of separations
for i in range(len(string)):
    if string[i]==',' or string[i]==' ':
        sepra.append(i) 
#print(sepra)  # for testing purposes
count = 0
for j in range(len(sepra)):
    if j==0:   
        if sepra[j]>0: #adding the first word
            count+=1
    if j==len(sepra)-1:
        if sepra[j]<len(string)-1:
            count+=1  #adding the last word
    if j>0:
        if sepra[j]-sepra[j-1]>1:
            count+=1
print(count)
print(len(string))

