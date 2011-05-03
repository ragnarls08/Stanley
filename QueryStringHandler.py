# encoding: utf-8

from Parser import Parser
from MathMagic import MathMagic
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