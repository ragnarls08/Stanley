import string
from Rynir import Rynir


f = open('published_dataset_ids.txt','r')
listOfDataSets = []

for x in f:
	listOfDataSets.append(x.strip())
	
#print listOfDataSets[:10]
#print listOfDataSets[:2]
rynir = Rynir()
report = rynir.analyze(listOfDataSets[:10])

#for x in report:
#	for i in x:
#		print i


for item in report:
  if item is None:
	pass
  else:
	print type(item)
	for sub in item:
	  print sub