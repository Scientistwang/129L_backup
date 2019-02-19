#!/usr/bin/python3
#Zipeng Wang
#3909934
#hw5 problem 6
#circuit plot

import matplotlib.pyplot as plt
import numpy as np

def Vin(t):  #a sqaure wave function
	n = 0
	while n < t:
		n += 1
	if n%2 == 0:
		return -1
	else:
		return 1
#print(Vin(0.8),Vin(4.5),Vin(3.2)) #test

#define the differential equation
#dVout/dt = 1/tao*(Vin(t)-Vout)
def f(t,Vout,tau):
	out = 1/tau*(Vin(t)-Vout)
	return out

def RK_method(t,Vout,tau,h):
	k1 = h*f(t,Vout,tau)
	k2 = h*f(t+h/2,Vout+k1/2,tau)
	k3 = h*f(t+h/2,Vout+k2/2,tau)
	k4 = h*f(t+h,Vout+k3,tau)
	y_out = Vout + 1/6*(k1+2*k2+2*k3+k4)
	t_out = t+h
	return t_out,y_out

t_max = 100
N = 10000
dt = t_max/N

####input part
while True:
	instring = input("Please enter a number for time constant tau: ")
	try: 
		tau = float(instring)
		if tau >0:
			break
		else:
			print('a negative time constant is unphysical. Try again.')
	except ValueError:
		print("That is not a float number. Try again.")

#initiallizing t and Vout (initial condition)
Vout = [0]
t = [0]
for i in range(N):
	t_new,Vout_new = RK_method(t[-1],Vout[-1],tau,dt)
	Vout.append(Vout_new)
	t.append(t_new)

#####plot this
N_t10 = int(10/dt)
N_t90 = int(90/dt)
plt.figure(1)
plt.plot(t[:N_t10],Vout[:N_t10])
plt.xlabel('t')
plt.ylabel(r'$V_{out}$')
plt.title('First 10 seconds')

plt.figure(2)
plt.plot(t[N_t90:],Vout[N_t90:])
plt.xlabel('t')
plt.ylabel(r'$V_{out}$')
plt.title('last 10 seconds')

plt.show()


















