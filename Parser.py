# -*- coding: utf-8 -*-
import sys
import urllib2
import simplejson as json
from DataSet import DataSet
from TimeLine import TimeLine
from DmGateway import DmGateway

class Parser:
	
	def __init__(self):
		self.gate = DmGateway()

	#Parses an url into a DataSet:list of timelines
	#Return: DataSet
	def parse(self, dsId, maxResults=0):
		job = self.gate.getDs(dsId, maxResults)

		#TODO REFACTOR W/THROW EXCEPTION
		if not job:
			print "ble"
			return None 
		
		#json object is within a list unwrap it
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
			
