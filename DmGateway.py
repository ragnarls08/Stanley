# -*- coding: utf-8 -*-

import urllib2
import simplejson as json
from DataSet import DataSet
from TimeLine import TimeLine
import ConfigParser

class DmGateway():
	def __init__(self):
		self.config = ConfigParser.RawConfigParser()
		self.config.read('config.cfg')
		
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
		except urllib2.URLError:
			raise ConnectionError('No connection')
		except urllib2.HTTPError:
			raise ConnectionError('404 : Not found')
		#except urllib2.HTTPError, urllib2.URLError:
			#raise ConnectionError(message)
	
class ConnectionError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
