from TimeLine import TimeLine

class DataSet(list):
	
	def __init__(self, title, dsId, granularity=""):
		self.dsId = dsId
		self.title = title
		self.timelines = []
		self.granularity = granularity
		

	def __len__(self):
		return len(self.timelines)

	def __repr__(self):
		return "Title: " + self.title \
			+ "\nId: " + self.dsId + "\n" \
			+ "Granularity: " + self.granularity + "\n" \
			+ "\n".join( str(x) for x in self.timelines )

	def __str__(self):
		return "Title: " + self.title \
			+ "\nId: " + self.dsId + "\n" \
			+ "Granularity: " + self.granularity + "\n" \
			+ "\n".join( str(x) for x in self.timelines )


	def append(self, title, cId):
		self.timelines.append( TimeLine(title, cId) )

