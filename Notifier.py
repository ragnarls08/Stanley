# encoding: utf-8
"""
Notifier.py

Created by Thordur Arnarson on 2011-02-22.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
from MathMagic import MathMagic
from DataSet import DataSet
from TimeLine import TimeLine
from statlib import stats
from Parser import Parser

class Notifier:
		
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
		
		for timeline in ds[1:-1]:
	
			newest = timeline.pop()			
			standarddev = stats.lstdev(timeline.getListNoNoneType())
#			for x in timeline[0:]:
#				print type(x)
			print standarddev	
		return report
	

def main():
	
	p = Parser()
	ds = p.parse()
	n = Notifier()
	results = n.isIntresting(ds)
	print results

#	Noti = Notifier()
#	Noti.isIntresting(Noti.fakeDataSet())
		
if __name__ == '__main__':
	main()