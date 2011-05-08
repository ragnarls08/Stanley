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


rynir = Rynir()
report = rynir.analyze(listOfDataSets[0:100])

for ds in report:
  for fo in ds:
  	print fo

