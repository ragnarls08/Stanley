# encoding: utf-8
"""
Notifier.py

Created by Thordur Arnarson on 2011-02-22.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
import math
from DataSet import DataSet
from TimeLine import TimeLine
from statlib import stats
from Parser import Parser
from DmGateway import DmGateway

MULTVALUE_FOR_STDEV = 2

class Notifier:
	
	def __init__(self):
		self.flags = 	[(0,"Smallest value in timeline."),
						(1, "Largest value in timeline"), 
						(2, "Value is more than " + str(MULTVALUE_FOR_STDEV) + " times the standard deviation")]
		
	#Applies statistical analysis on a given timeline
	#Loops through a dataSet and applies statistical analysis on the timelines in the dataset
	#param: dataSet
	#return: a list of results from the statistical analyser
	def isIntresting(self, ds):
		report = []	
		for timeline in ds[1:]:	
			newest = timeline.pop()		#the latest value in the timeline						
			param = timeline.getListNoNoneType()	#holds the value to compair

			if param != []:
				standarddev = stats.lstdev(param)	
				mean = stats.mean(param)					
				diff = (math.sqrt(math.pow((mean - newest), 2)))				
				
				listOfFlags = []
				#flags if newest is the lowest value in the timeline
				if newest < min(param):	
					listOfFlags.append(self.flags[0])				
				#flags if newest is the highest value in the timeline	
				if newest > max(param):
					listOfFlags.append(self.flags[1])
				#flaogs if the diffrence between the newest value and the 
				#mean of all the other values in the timeline are greater then x standarddev
				if diff > standarddev*MULTVALUE_FOR_STDEV:
					listOfFlags.append(self.flags[2])
					
				if len(listOfFlags) > 0:
					report.append([ds.dsId, ds.title, timeline.cId, timeline.title, listOfFlags])
				
		return report	
