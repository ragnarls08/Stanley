# -*- coding: utf-8 -*-

import sys
import threading
import thread
import Queue
from QueryStringHandler import QueryStringHandler
import ConfigParser
import logging

import heapq

class Rynir:
	logging.basicConfig(filename='logfile.log', format='%(levelname)s : %(asctime)s, File: %(filename)s Function: %(funcName)s, %(threadName)s %(message)s ', level=logging.WARNING)
	
	def __init__(self):
		self.config = ConfigParser.RawConfigParser()
		self.config.read('config.cfg')
		try:
			self.numberOfThreads = self.config.getint('Threads','numberofthreads')
		except ConfigParser.NoSectionError, e:
			logging.error(e)
		except ConfigParser.Error, e:
			logging.error(e)	
	
		
		#self.handler = QueryStringHandler()
		self.queue = Queue.Queue()
		self.report = []
		self.lock = thread.allocate_lock()
		
	#param: list of querystrings, ok if single queryString
	#return: returns list of reports, generated by Notifier.getReports
	def analyze(self, queryStringList):
		#thread me!		
		if type(queryStringList) != list:
			queryStringList = [queryStringList]
		try:
			for item in queryStringList:
				self.queue.put(item)
				#report.append(self.handler.getReport(item))
			
			for i in range(self.numberOfThreads):
				thread = ThreadHelper(self.queue, self.report, self.lock)
				thread.setDaemon(True)
				thread.start()

			self.queue.join()
		except Exception, e:
			logging.error(e)
			
			
		#TODO: config variable for top N
		if True:	
		  self.report = self.getTopResults(self.report, 100)
		
			
		return self.report
  
	def getTopResults(self, report, N):
		results = []
		
		for ds in report:
		  for tl in ds:
			for flag in tl.listOfFlags:
			  print (tl.dsID, tl.tlID, flag)
			  item = wrapFlag( (tl.dsID, tl.tlID, flag) )
			  
			  heapq.heappush(results, item )
			  #heapq.heappush(results, (tl.dsID, tl.tlID, flag))
	"""
		print "\n\n"
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		print heapq.heappop(results).value
		
	"""	
def wrapFlag(value):
    class Wrapper(object):
        def __init__(self, value): self.value = value
        def __cmp__(self, obj): 
			return cmp(obj.value[2][1], self.value[2][1])
        
    return Wrapper(value)
		

class ThreadHelper(threading.Thread):
	def __init__(self, queue, report, lock):
		threading.Thread.__init__(self)
		self.handler = QueryStringHandler()
		self.queue = queue
		self.report = report 
		self.lock = lock
		
	def run(self):
		while True:
			print self
			try:
				dataSetReport = self.handler.getReport(self.queue.get())
				
				if dataSetReport:
				  self.lock.acquire()
				  self.report.append(dataSetReport)
				  self.lock.release()
			except:
				logging.error('Error in def run() in ThreadHelper')
				pass
			finally:
				self.queue.task_done()
