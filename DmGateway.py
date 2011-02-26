# -*- coding: utf-8 -*-

import urllib2
import simplejson as json
from DataSet import DataSet
from TimeLine import TimeLine



class DmGateway():

	def __init__(self, baseUrl="http://www.datamarket.com/api/v1/series.json?callback=" ):
		self.baseUrl = baseUrl
		self.callUrl = ""		

	def getDs(self, dsId, maxResults=0):
		self.callUrl = self.baseUrl + "&ds=" + str(dsId)

		if maxResults > 0:
			self.callUrl += "&maxresults=" + str(maxResults)

		return self.call()

	#Gets a json object from the url
	#Return: Json object
	def call(self):
		try:
			request = urllib2.Request( self.callUrl )
			response = urllib2.urlopen( request )
			results = json.load( response )

			return results
		except urllib2.HTTPError, urllib2.URLError:
			raise 
	
