# -*- coding: utf-8 -*-

import sys
import threading
import Queue
from QueryStringHandler import QueryStringHandler
#from DmGateway import DmGateway
#from StaticGateway import StaticGateway
#from Notifier import Notifier
#from MathMagic import MathMagic
#from Parser import Parser


class Rynir:
	def __init__(self):
		self.handler = QueryStringHandler()
		#gate = DmGateway()
		#gate = StaticGateway("staticDataSet.json")
		#self.parser = Parser(gate)
		#self.notifier = Notifier()
		#self.mathMagic = MathMagic()
	
	#param: querystring or list of querystrings
	#return: returns list of reports, generated by Notifier.getReports
	def analyze(self, queryStringList):
		#thread me!
		report = []
		
		if type(queryStringList) != list:
			queryStringList = [queryStringList]
		try:
			for item in queryStringList:
				report.append(self.handler.getReport(item))
			
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
			
		return report
	"""
	def analyze(self, inQueryString):
		if type(inQueryString) == list:
			#thread me!
			ret = []
			for item in inQueryString:
				dset = self.parser.parse( item )
				ret.append( self.notifier.getReport( dset ) )
			return ret	
		else:
			dset = self.parser.parse( inQueryString )
			return [self.notifier.getReport( dset )]
	"""
class Bull(threading.Thread):
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue
		
	def run(self):
		report = handler.getReport(self.queue.get())
		
		self.queue.task_done()
		
		return report