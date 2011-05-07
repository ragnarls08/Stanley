# -*- coding: utf-8 -*-

import urllib2
import simplejson as json
from DataSet import DataSet
from TimeLine import TimeLine
import ConfigParser
import logging,sys,traceback

class DmGateway():
	
	def __init__(self):
		
		self.config = ConfigParser.RawConfigParser()
		self.config.read('config.cfg')
		
		self.callUrl = ""
			
		#BaseURL read from config
		#TODO:	Still have to add key to URL
		try:
			self.baseUrl = self.config.get('API','URL') #baseUrl
			self.DMkey = self.config.get('API','key')
		except ConfigParser.NoSectionError, e:
			logging.error(e)
		except ConfigParser.Error, e:
			logging.error(e)	

	#Constructs the URI for the dataset
	#param: datasetId and maxResults, initalized as 0
	#return: calls self.call()
	def getDs(self, dsId, maxResults=0):
		self.callUrl = self.baseUrl + "&ds=" + str(dsId)

		if maxResults > 0:
			self.callUrl += "&maxresults=" + str(maxResults)
		
		if len(self.DMkey) > 0:
			self.callUrl += '&api_key=' + self.DMkey

		return self.call()

	#Gets a json object from the url
	#Return: Json object
	def call(self):
		try:
			request = urllib2.Request( self.callUrl )
			response = urllib2.urlopen( request )
			results = json.load( response )
			return results
		except 	urllib2.HTTPError, e:
			logging.warning(' %s,  when trying to open %s', e , self.callUrl	)	
		except 	urllib2.URLError, e:
			logging.error(' %s,  when trying to open %s', e , self.callUrl	)			
		#except 	Exception, e: 
		#	logging.error('===UNKNOWN EXCEPTION=== : %s,  when trying to open %s', e , self.callUrl	)

		

