# encoding: utf-8
"""
StaticGateway.py

Created by Thordur Arnarson on 2011-02-26.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import simplejson

class StaticGateway:
	
	def getDs(self, dsId, maxResults=0):
		return self.call()

	def call(self):
		return simplejson.load(open("staticDataSet.json"))
		