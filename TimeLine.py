# -*- coding: utf-8 -*-
import numpy

class TimeLine(list):
	def __init__(self, title, cId, data=[]):
		self.title = title
		self.cId = cId
		super(TimeLine, self).extend( data )
	
	def __str__(self):
		return "\tTitle: " + self.title \
				+ "\n\tcId: " + self.cId \
				+ "\n\t[" + ", ".join( str(x) for x in self ) + "]" 

	def append(self, item):
		super(TimeLine, self).append( item )			

	def extend(self, ls):
		super(TimeLine, self).extend( ls )

	def getListNoNoneType(self):
		return [item for item in self if type(item) != type(None)]	

	def getMaskedArray(self):
		return numpy.ma.masked_array([ numpy.NaN if type(item) == type(None) else item for item in self ])	
