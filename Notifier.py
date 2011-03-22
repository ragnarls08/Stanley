# encoding: utf-8
"""
Notifier.py

Created by Thordur Arnarson on 2011-02-22.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
#import math
from DataSet import DataSet
from TimeLine import TimeLine
from MathMagic import MathMagic #check if this should be module
#from statlib import stats
#from Parser import Parser
#from DmGateway import DmGateway

MULTVALUE_FOR_STDEV = 2

class Notifier:
	
	def __init__(self):
		self.flags = 	[(0,"Smallest value in timeline."),
						(1, "Largest value in timeline"), 
						(2, "Value is more than " + str(MULTVALUE_FOR_STDEV) + " times the standard deviation")]
		self.mathMagic = MathMagic()
	#Applies statistical analysis on a given timeline
	#Loops through a dataSet and applies statistical analysis on the timelines in the dataset
	#param: dataSet
	#return: a list of results from the statistical analyser
	def getReport(self, ds):
		report = []	
		for timeline in ds[1:]: #wouldn't it be better if this was a tuple? name is not a DS and should therefore not be a part of this list of DS
			listOfFlags = self.mathMagic.standardDevAnalysis(timeline, ds[0])
			report.append([ds.dsId, ds.title, timeline.cId, timeline.title, listOfFlags])
				
		return report	
