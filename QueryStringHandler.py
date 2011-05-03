# encoding: utf-8

from Parser import Parser
from DataSet import DataSet
from TimeLine import TimeLine
from MathMagic import MathMagic #check if this should be module
from FlagObj import FlagObj

class QueryStringHandler:
	
	def __init__(self):
		self.parser = Parser()
		self.mathMagic = MathMagic()

	def getReport(self, queryString):
		dset = self.parser.parse(queryString)
		datasetReport = []
		
		timeAxis = dset[0]
		
		for timeline in dset[1:]:
			listOfFlags = self.mathMagic.analyze(timeline, timeAxis)
			timelineFlagList = FlagObj(dset.dsId, dset.title, timeline.cId, timeline.title, listOfFlags)
			datasetReport.append(timelineFlagList)
		
		return datasetReport
	#Applies statistical analysis on a given timeline
	#Loops through a dataSet and applies statistical analysis on the timelines in the dataset
	#param: dataSet
	#return: a list of results from the statistical analyser
	"""
	def getReport(self, ds):
		report = []	
		for timeline in ds[1:]: #wouldn't it be better if this was a tuple? name is not a DS and should therefore not be a part of this list of DS
			listOfFlags = self.mathMagic.analyze(timeline, ds[0])
			#self.mathMagic.fourierAnalysis(timeline, ds[0])
			flag = FlagObj(ds.dsId, ds.title, timeline.cId, timeline.title, listOfFlags)
			report.append(flag)
				
		return report	
	"""