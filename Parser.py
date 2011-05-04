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
			raise TypeError('Parser received illegal dataset ID')

		job = job[0]
	
		#get data as a list of rows instead of columns	
		colData = map(None, *job["data"] )
		
		dataset = DataSet( job["title"].encode('utf-8'), job["id"].encode('utf-8'), 
					job["columns"][0]["time_granularity"].encode('utf-8'))
		

		for col, item in enumerate(colData):
			
			#if type(colData[0]) != tuple:
			 # raise TypeError('Data is not of type: Tuple')
			  
			#else:
			  tl = TimeLine( job["columns"][col]["title"].encode('utf-8'),
					  job["columns"][col]["cid"].encode('utf-8'),
					  colData[col] )
			  dataset.append(tl)
		
		return dataset				 
			
