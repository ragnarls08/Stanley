# encoding: utf-8
"""
Notifier.py

Created by Thordur Arnarson on 2011-02-22.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
from MathMagic import MathMagic
import math
from DataSet import DataSet
from TimeLine import TimeLine
from statlib import stats
from Parser import Parser
from DmGateway import DmGateway
from StaticGateway import StaticGateway

MULTVALUE_FOR_STDEV = 2

class Notifier:
	
	def __init__(self):
		self.flags = 	[(0,"Smallest value in timeline."),
						(1, "Largest value in timeline"), 
						(2, "Value is more than " + str(MULTVALUE_FOR_STDEV) + " times the standard deviation")]
		
	def multi(self, number):
		return number*number

	def fakeDataSet(self):
		ds = DataSet("Verdbolga", "v28", "Month")
		tl = TimeLine("titill", "cId bla", [1,2,3,4,5])	
		ds.append(tl)
		return ds
		
	def idList(id):
		timelineIds = []
		
	#Applies statistical analysis on a given timeline
	#Loops through a dataSet and applies statistical analysis on the timelines in the dataset
	#param: dataSet
	#return: the timeline id if it is intresting else none
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
				
				#flags if newest is the lowest in the timeline
				if newest < min(param):	
					listOfFlags.append(self.flags[0])				

				if newest > max(param):
					listOfFlags.append(self.flags[1])
					
				if diff > standarddev*MULTVALUE_FOR_STDEV:
					listOfFlags.append(self.flags[2])
					
				if len(listOfFlags) > 0:
					report.append([ds.dsId, ds.title, timeline.cId, timeline.title, listOfFlags])
				
		return report
	

def main():
	gateway = StaticGateway()
	
	p = Parser(gateway)
	ds = p.parse("V28", 0)
	n = Notifier()
	results = n.isIntresting(ds)

	for x in results:
		print x
		
if __name__ == '__main__':
	main()