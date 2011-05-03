import string
from Rynir import Rynir


f = open('published_dataset_ids.txt','r')
listOfDataSets = []

for x in f:
	listOfDataSets.append(x.strip())
	
#print listOfDataSets[:10]

rynir = Rynir()
report = rynir.analyze('1968')

print report
