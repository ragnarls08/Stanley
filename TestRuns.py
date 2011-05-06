import string
import random
from Rynir import Rynir


f = open('published_dataset_ids.txt','r')
listOfDataSets = []

for x in f:
	listOfDataSets.append(x.strip())
	
#randList = []
#for x in range(100):
#	randList.append(listOfDataSets[0:100])#random.randint(0,11780)
#print listOfDataSets[:10]
#print listOfDataSets[:2]
rynir = Rynir()
report = rynir.analyze(listOfDataSets[:50])

#for x in report:
#	for i in x:
#		print i

"""
for ds in report:
  for tl in ds:
	if tl is None:
	  pass
	else:
	  pass #print tl
"""
