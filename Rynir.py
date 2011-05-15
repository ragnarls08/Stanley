# -*- coding: utf-8 -*-

from QueryStringHandler import QueryStringHandler
import sys
import threading
import thread
import Queue
import ConfigParser
import logging
import heapq
import traceback

class Rynir:
	FORMAT = '%(levelname)s : %(asctime)s, File: %(filename)s Function: %(funcName)s, %(threadName)s %(message)s '
	logging.basicConfig(filename='logfile.log',filemode='w',format=FORMAT,level=logging.DEBUG)
	
	def __init__(self):
		self.config = ConfigParser.RawConfigParser()
		self.config.read('config.cfg')
		try:
			self.numberOfThreads = self.config.getint('Threads','numberofthreads')
			self.topN = self.config.getint('ReturnOptions','topn')
		except ConfigParser.NoSectionError, e:
			logging.error(e)
		except ConfigParser.Error, e:
			logging.error(e)	
		
		self.queue = Queue.Queue()
		self.report = []
		self.lock = thread.allocate_lock()
		
	#param: list of querystrings, ok if single queryString
	#return: returns list of reports, generated by Notifier.getReports
	def analyze(self, queryStringList):
		if type(queryStringList) != list:
			queryStringList = [queryStringList]
		try:
			for item in queryStringList:
				self.queue.put(item)
			
			for i in range(self.numberOfThreads):
				thread = ThreadHelper(self.queue, self.report, self.lock)
				thread.setDaemon(True)
				thread.start()

			self.queue.join()
		except Exception, e:
			logging.error(e)
			
		#if topN is set to 0, a list of all flags is returnd
		
		if self.topN > 0:	
		  self.report = self.getTopResults(self.report)
		
		return self.report

	#param: a report, list of flags that include value of intrest
	#return: a list of the top N most intresting flags
	def getTopResults(self, report):
		results = []
	
		#sort the list of flags for each timeline
		for ds in report:
		  for flagObject in ds:
			#x[1] is the index of the severity in the flag tuple
			flagObject.listOfFlags.sort(key=lambda x: x[1])
			flagObject.listOfFlags.reverse()		
		
		#sort the timelines within a dataset
		for ds in report:
		  ds.sort(key=lambda x: x.listOfFlags[0][1] if x.listOfFlags[0] else 0)
		  ds.reverse()

		#sort the datasets in the report
		report.sort(key=lambda x: x[0].listOfFlags[0][1])
		report.reverse()
	
		#ath format a outputi
		return [item[0] for item in report]
			
	
		
		

class ThreadHelper(threading.Thread):
	def __init__(self, queue, report, lock):
		threading.Thread.__init__(self)
		self.handler = QueryStringHandler()
		self.queue = queue
		self.report = report 
		self.lock = lock
		
	def run(self):
		while True:
			try:
				print "Items left in queue: " + str(self.queue.qsize())
				dataSetReport = self.handler.getReport(self.queue.get())
				if dataSetReport:
				  self.lock.acquire()
				  self.report.append(dataSetReport)
				  self.lock.release()
			except Queue.Empty, e:
				logging.error(e)
			except thread.error, e:
				logging.error(e) 
			except:
				#logging.error('Error in def run() in ThreadHelper')
				logging.error(traceback.format_exc())
				pass
			finally:
				self.queue.task_done()
