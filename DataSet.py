from TimeLine import TimeLine

class DataSet(list):
	
	def __init__(self, title, dsId):
		self.dsId = dsId
		self.title = title
		self.timelines = []

	def __len__(self):
		return len(self.timelines)

	def __repr__(self):
		return "Title: " + self.title \
			+ "\nId: " + self.dsId + "\n" \
			+ "\n".join( str(x) for x in self.timelines )

	def __str__(self):
		return "Title: " + self.title \
			+ "\nId: " + self.dsId + "\n" \
			+ "\n".join( str(x) for x in self.timelines )

	def append(self, title, cId):
		self.timelines.append( TimeLine(title, cId) )

