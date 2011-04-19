# encoding: utf-8

from DataSet import DataSet
from TimeLine import TimeLine
from MathMagic import MathMagic #check if this should be module

class Notifier:
	
	def __init__(self):
		self.mathMagic = MathMagic()

	#Applies statistical analysis on a given timeline
	#Loops through a dataSet and applies statistical analysis on the timelines in the dataset
	#param: dataSet
	#return: a list of results from the statistical analyser
	def getReport(self, ds):
		report = []	
		for timeline in ds[1:]: #wouldn't it be better if this was a tuple? name is not a DS and should therefore not be a part of this list of DS
			listOfFlags = self.mathMagic.standardDevAnalysis(timeline, ds[0], 20)
			report.append([ds.dsId, ds.title, timeline.cId, timeline.title, listOfFlags])
				
		return report	
