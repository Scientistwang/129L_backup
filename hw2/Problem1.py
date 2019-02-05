#!/usr/bin/python3
while True:
    try:
        x = int(input("Please enter an integer: "))
        y = x**2
        print("the number squared is", y )
        break
    except ValueError:
        print("That is not an integer. Try again.")





