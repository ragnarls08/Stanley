import string
from Rynir import Rynir


f = open('published_dataset_ids.txt','r')
listOfDataSets = []

for x in f:
	listOfDataSets.append(x.strip())
	
#print listOfDataSets[:10]
#print listOfDataSets[:2]
rynir = Rynir()
report = rynir.analyze(listOfDataSets[:100])

#for x in report:
#	for i in x:
#		print i

"""
for item in report:
	for sub in item:
	  print sub
	  """