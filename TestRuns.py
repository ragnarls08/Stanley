import string
from Rynir import Rynir


f = open('published_dataset_ids.txt','r')
listOfDataSets = []

for x in f:
	listOfDataSets.append(x.strip())
	
#print listOfDataSets[:10]

rynir = Rynir()
report = rynir.analyze(listOfDataSets[22])

for x in report:
	for i in x:
		print i
