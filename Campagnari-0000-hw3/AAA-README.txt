Some solutions make use of the utility functions in ccHist.py.
This file is therefore included in the tgz file.


Exercise 1
--------
To run the program that solves this problem
linux> ./calculatePi.py
Note: as a bonus, this also produces a graph of the calculated
pi as afunction of N

Exercise 2
---------
To run the program that solves this problem
linux> ./numDer.py

Exercise 3
---------
To run the program that solves this problem
linux> ./testBenfordLaw.py
Note: the csv file must be in the working directory,  It
is included in the tgz file

Exercise 4 
---------
To run the program that solves this problem 
linux> ./ParticleInA2DBox.py

Exercise 5
---------
To run the program that solves this problem 
linux> ./genLinear.py
I have coded this in two ways
(a) by inverting the cumulative distribution of f(x)
(b) by exploiting the fact that f(x) is the sum of a flat
     pdf with prob 1/3 and of f(x)=2x with probability 2/3.
     Thus, 1/3 of the times I pick from a flat distribution.
     The remaining 2/3 of the times I pick from f(x)=2x which is super-trivial
     to integrate and take the inverse, ie, x = sqrt(R),
Can choose between the two methods by changing a boolean at the
beginning of the code.
At the end of the day, I am not sure which one is more efficient.
Acceptance/Rejection would be a third option, but for sure more
inefficient.

Exercise 6
---------
To run the program that solves this problem 
linux> ./randomWalk.py
