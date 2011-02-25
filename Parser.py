# -*- coding: utf-8 -*-
import sys
import urllib2
import simplejson as json
from DataSet import DataSet
from TimeLine import TimeLine

class Parser:

	def __init__(self, urlBase="http://www.datamarket.com/api/v1/series.json?callback=", 
			urlQuery="&ds=v28&maxresults=5" ):
		self.urlBase = urlBase
		self.urlQuery = urlQuery


	#Gets a json object from the url
	#Return: Json object
	def getJsonFromUrl(self):
		try:
			request = urllib2.Request( self.urlBase + self.urlQuery )
			response = urllib2.urlopen( request )
			results = json.load( response )

			return results
		except:
			return None 
	

	#Parses an url into a DataSet:list of timelines
	#Return: DataSet
	def parse(self):
		job = self.getJsonFromUrl()

		#REFACTOR W/THROW EXCEPTION
		if not job:
			print "ble"
			return None 
		job = job[0]
	
		#get data as a list of rows instead of columns	
		colData = map(None, *job["data"] )
		
		dataset = DataSet( job["title"].encode('utf-8'), job["id"].encode('utf-8'), 
									job["columns"][0]["time_granularity"].encode('utf-8'))
		
		

		for col in range(0, len(colData ) ):
			tl = TimeLine( job["columns"][col]["title"].encode('utf-8'),
							job["columns"][col]["cid"].encode('utf-8'),
							colData[col] )
			dataset.append(tl)
		
		return dataset				 
			
