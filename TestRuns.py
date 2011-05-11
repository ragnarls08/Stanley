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

report = rynir.analyze(listOfDataSets[5000:5010])
#report = rynir.analyze("16z9|ibf=1p")
#report = rynir.analyze("12sr")

#report = rynir.analyze("178g|ikm=40")


for ds in report:
  
  	print ds

#for ds in report:
  #for fo in ds:
	#print fo

