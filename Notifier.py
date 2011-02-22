#!/usr/bin/env python
# encoding: utf-8
"""
Notifier.py

Created by Thordur Arnarson on 2011-02-22.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
#from MathMagic import MathMagic
from DataSet import DataSet

class Notifier:
		
	def multi(self, number):
		return number*number
		
	#Applies statistical analysis on a given timeline
	#param: list
	#return: 1 if intresting and 0 if not	
	def isIntresting(self):
		return 1