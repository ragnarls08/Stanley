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


#report = rynir.analyze('c|1tt=1c8b:1tu=1c8i')
#report = rynir.analyze('16w5|i8b=w')
report = rynir.analyze(listOfDataSets[5000:6000])


#report = rynir.analyze("16z9|ibf=1p")
#report = rynir.analyze("12sr|e7l=3p")
#report = rynir.analyze("12sr")
#report = rynir.analyze("178g|ikm=40")
#report = rynir.analyze('y6d|6f2=3:6f3=9.5:6f4=2:6f5=1:6f6=1')
#report = rynir.analyze('yfu|6zj=1')
#report = rynir.analyze('xja|67k=3') #flagg i endann
#report = rynir.analyze('16z3|ib9=3b')

#for ds in report:
  	#print ds


for ds in report:
  for fo in ds:
	print fo

