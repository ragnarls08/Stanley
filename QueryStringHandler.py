# encoding: utf-8

from Parser import Parser
from MathMagic import MathMagic
from FlagObj import FlagObj
import logging

class QueryStringHandler:
	def __init__(self):
		self.parser = Parser()
		self.mathMagic = MathMagic()
	
	#Param: a queryString
	#Return: datasetReport, list of timelines with flags
	def getReport(self, queryString):
		try:
			dset = self.parser.parse(queryString)
			datasetReport = []
			
			timeAxis = dset[0]
			
			for timeline in dset[1:]:
				listOfFlags = self.mathMagic.analyze(timeline, timeAxis)
				timelineFlagList = FlagObj(dset.dsId, dset.title, timeline.cId, timeline.title, listOfFlags)
				datasetReport.append(timelineFlagList)
			
			return datasetReport
			#TODO Specify exceptions
		except Exception, e:
			#logging.error(e)
			return []
