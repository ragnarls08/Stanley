class FlagObj:

	def __init__ (self,dsID,dsTitle,tlID,tlTitle,listOfFlags):
		self.dsID = dsID
		self.dsTitle = dsTitle
		self.tlID = tlID
		self.tlTitle = tlTitle
		self.listOfFlags = listOfFlags

	def __str__(self):
		return 	'DataSet ID: ' + self.dsID + '\n' \
				'DataSet Title: ' + self.dsTitle +'\n' \
				'TimeLine ID: ' + self.tlID +'\n'  \
				'TimeLine title: ' + self.tlTitle +'\n' \
				'ListOfFlags: ' + '\n'.join( str(x) for x in self.listOfFlags ) +'\n' 
				
