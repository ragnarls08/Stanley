# -*- coding: utf-8 -*-

import urllib2
import simplejson as json
from DataSet import DataSet
from TimeLine import TimeLine
import ConfigParser
import logging,sys,traceback

class DmGateway():
	
	def __init__(self):
		try:
			self.config = ConfigParser.RawConfigParser()
			self.config.read('config.cfg')
		except IOError as error:
			logging.error(str(error))
			raise IOError
			
		#BaseURL read from config
		#TODO:	Still have to add key to URL
		self.baseUrl = self.config.get('API','URL') #baseUrl
		self.DMkey = self.config.get('API','key')
		self.callUrl = ""		

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
			
		except 	urllib2.URLError as error:	
			logging.error(': %s,  when trying to open %s', str(error),self.callUrl	)
			#logging.exeption('EXE : when trying to open %s',self.callUrl	)
			#traceback.print_exc(limit=5,file=None)
			#raise URLError	
		
		#except urllib2.HTTPError, urllib2.URLError:
			#raise ConnectionError(message)
		

