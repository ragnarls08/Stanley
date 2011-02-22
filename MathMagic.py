# -*- coding: utf-8 -*-

from DataSet import DataSet
import math

class MathMagic:
	
	#Add function, used by the reduce func to sum up lists
	def add(self,x,y): return x+y
	
	#Calcutates standard deviation of a list of numbers (not population standard deviation)
	#param: list
	#return: real number
	def standardDev(self,ds):
		if len(ds) > 0:
			mean = self.mean(ds)	
			distList = []
			for val in ds:
				distList.append(pow( (val-mean) , 2))
	
			stdPow2 = reduce(self.add,distList)/(len(ds)-1.0)
			return math.sqrt(stdPow2)
		else:
			return

	#Calcutates the mean of a list of numbers
	#param: list
	#return: real number or None if list is empty		
	def mean(self,ds):
		if len(ds) > 0:
			sum = reduce(self.add,ds)
			return sum/len(ds)
		else:
			return	