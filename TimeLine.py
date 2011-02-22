# -*- coding: utf-8 -*-

class TimeLine(list):
	def __init__(self, title, cId, data=[]):
		self.title = title
		self.cId = cId

	def append(self, item):
		super(TimeLine, self).append( item )			

	def extend(self, ls):
		super(TimeLine, self).extend( ls )
	
#	def __repr__(self):
#		return "\tTitle: " + self.title \
#			+ "\n\tId: " + self.cId
#	def __str__(self):
#		return "\tTitle: " + self.title \
#			+ "\n\tId: " + self.cId


