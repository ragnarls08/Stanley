

class TimeLine:
	def __init__(self, title, cId):
		self.title = title
		self.cId = cId
	
	def __repr__(self):
		return "\tTitle: " + self.title \
			+ "\n\tId: " + self.cId
	def __str__(self):
		return "\tTitle: " + self.title \
			+ "\n\tId: " + self.cId
