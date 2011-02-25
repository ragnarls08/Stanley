# -*- coding: utf-8 -*-

from TimeLine import TimeLine

class DataSet(list):
	
	def __init__(self, title, dsId, granularity=""):
		self.dsId = dsId
		self.title = title
		self.granularity = granularity

	def __str__(self):
		return "---DataSet---\n" + "\nTitle: " + self.title \
			+ "\nId: " + self.dsId + "\n" \
			+ "Granularity: " + self.granularity + "\n" \
			+ "\n\t---TimeLines---\n" \
			+ "\n" + "\n\n".join( str(x) for x in self )

	def apend(self, item):
		if not isinstance(item, TimeLine):
			raise TypeError, 'item is not of type %s' % TimeLine
		super(DataSet, self).append(item)
	
