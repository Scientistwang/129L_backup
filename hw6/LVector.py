#!/usr/bin/python3
#Zipeng Wang
#3909934
#hw6 problem1

#########
# a class of 4-vectors

import numpy as np

class LVector:
	'''Lorentz vectors'''

	def __init__(self,Vector):
		self.x = np.array([0.,0.,0.,0.])
		self.x[0] = Vector[0]
		self.x[1] = Vector[1]
		self.x[2] = Vector[2]
		self.x[3] = Vector[3]
	def copy(self):
		return LVector(self.x)
	def __str__(self):
		return ' x0 = {0:.3f} \n x1 = {1:.3f} \n x2 = {2:.3f} \n x3 = {3:.3f}\n'.format(self.x[0],self.x[1],self.x[2],self.x[3]) 

	def __add__(self,other):
		new = self.copy()
		for i in range(len(self.x)):
			new.x[i] = self.x[i] + other.x[i]
		return new
	
	def __sub__(self,other):
		new = self.copy()
		for i in range(len(self.x)):
			new.x[i] = self.x[i] - other.x[i]
		return new

	def __mul__(self,other):
		new = self.copy()
		if type(other) == int or type(other)== float:
			new.x = new.x * other
			return new
		if type(other) == LVector:
			return self.x[0]*other.x[0]-self.x[1]*other.x[1]-self.x[2]*other.x[2]-self.x[3]*other.x[3]

	def __rmul__(self,other):
		return (self*other)

	def square(self):
		return (self*self)
	
	def set_x0(self,x0):
		self.x[0] = x0
	def set_x1(self,x1):
		self.x[1] = x1
	def set_x2(self,x2):
		self.x[2] = x2
	def set_x3(self,x3):
		self.x[3] = x3

	def get_rlength(self):
		count = 0
		for i in range(1,4):
			count += self.x[i]**2
		return count
	
	def get_rtlength(self):
		return np.sqrt(self.x[1]**2+self.x[2]**2)

	def get_r(self):
		Vector = np.zeros(3)
		for i in range(3):
			Vector[i] = self.x[i+1]
		return Vector
	def get_rt(self):
		Vector = self.get_r()
		Vector[2] = 0
		return Vector

	def phi(self):
		return np.arctan(self.x[2]/self.x[1])	
	def theta(self):
		length_2D = np.sqrt(self.x[1]**2+self.x[2]**2)
		return np.arctan(length_2D/self.x[3])		

	def eta(self):
		theta = self.theta()
		out = -np.log(np.tan(theta/2))
		return out
	
	def Y(self):
		ratio = (self.x[0]+self.x[3])/(self.x[0]-self.x[3])
		return 0.5*np.log(ratio)

	def boost(self,beta):
		beta = np.array(beta)
		gamma = 1/np.sqrt(1-np.dot(beta,beta))
		temp = np.zeros(4)
		temp[0] = gamma*(self.x[0]-np.dot(beta,self.x[1:]))
		temp[1:] = self.x[1:]+(-gamma*self.x[0]+(gamma**2)/(1+gamma)*np.dot(beta,self.x[1:]))*beta
		for i in range(4):
			self.x[i] = temp[i]




 


