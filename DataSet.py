from TimeLine import TimeLine

class DataSet(list):
	
	def __init__(self, title, dsId):
		self.dsId = dsId
		self.title = title
		self.timelines = []

	def __len__(self):
		return len(self.timelines)

	#error in join part
	def __repr__(self):
			return "Title: " + self.title \
				+ "\nId: " + self.dsId \
				+ "\n".join( self.timelines )


	def append(self, title, cId):
		self.timelines.append( TimeLine(title, cId) )

