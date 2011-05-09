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

t=['12sr']
rynir = Rynir()
report = rynir.analyze(t)

for ds in report:
  for fo in ds:
  	print fo

