# -*- coding: utf-8 -*-

from TimeLine import TimeLine

class DataSet(list):
	
	def __init__(self, title, dsId, granularity=""):
		self.dsId = dsId
		self.title = title
		self.timelines = []
		self.granularity = granularity
		


#	def __repr__(self):
#		return "Title: " + self.title \
#			+ "\nId: " + self.dsId + "\n" \
#			+ "Granularity: " + self.granularity + "\n" \
#			+ "\n".join( str(x) for x in self.timelines )
#
#	def __str__(self):
#		return "Title: " + self.title \
#			+ "\nId: " + self.dsId + "\n" \
#			+ "Granularity: " + self.granularity + "\n" \
#			+ "\n".join( str(x) for x in self.timelines )


	def apend(self, item):
		if not isinstance(item, TimeLine):
			raise TypeError, 'item is not of type %s' % TimeLine
		super(DataSet, self).append(item)

#	def append(self, title, cId, data=[]):
#		self.timelines.append( TimeLine(title, cId, data) )
