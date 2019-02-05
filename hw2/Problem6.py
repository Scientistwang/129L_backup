#!/usr/bin/python3

while True:
    try:
        num = int(input("Please enter an integer: "))
        if num>0:
            break
        else:
            print("That number is negative. Try again.")
    except ValueError:
        print("That is not an integer. Try again.")

#Trival case
if num ==1:
    print("Your number is 1, which doesn't have prime factors.")
else:
    temp = num
    primes = []
    while True:
        div = [i for i in range(2,temp)]
        finish = False
        for i in div:
            if temp%i==0:
                primes.append(i)
                temp = temp//i
                break
            if i == temp-1 :
                finish = True
        if finish or div == []:
            primes.append(temp)
            break
   # print(primes) #for test purposes
    #calculate the frequency of elements
    re_prime = [] #reduced prime list
    freq = []     #frequency of a number
    for i in range(len(primes)):
        if i == 0:
            re_prime.append(primes[i])
            k0 = i
        else:
            if primes[i] != primes[i-1]:
                re_prime.append(primes[i])
                freq.append(i-k0)
                k0 = i
            if i == len(primes)-1:
                freq.append(i-k0+1)
    print(re_prime) # for test purposes
    print(freq)  # for test purposes
    
    for i in range(len(re_prime)):
        print(re_prime[i], "to the power", freq[i])


