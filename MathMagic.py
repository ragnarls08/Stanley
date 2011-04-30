# encoding: utf-8

import numpy as np
import matplotlib.pyplot as plot
import scikits.timeseries as ts
import scikits.timeseries.lib.plotlib as tplot
from scikits.timeseries.lib.moving_funcs import *
import scipy as sp
import operator

emptySet = ['--', 'nan']

class MathMagic:	

	def analyze(self, timeline, timeAxis, frameSize = None):
		dictionary = {}
		
		for item in timeAxis:
			dictionary[item] = (None, None, 1)
		
		if frameSize:
			print "received frameSize"
			dictionary = bollingerAnalysis(timeline, dictionary, frameSize, timeAxis, 1)
		else:	
			print "no framesize, iterating"
			#kalla í fourier, ef það kemur rammastærð úr því þá kalla í BollingerFourier, annars iterativeBollinger
			dictionary = self.iterativeBollinger(timeline, timeAxis, dictionary)
			
			
		listi = self.removeConsolidatingFlags(dictionary)
			
		#return listi
		#return sorted(listi.iteritems(), key=operator.itemgetter(1))
		return listi
	
	def iterativeBollinger(self, timeline, timeAxis, dictionary):
		self.bollingerAnalysis(timeline,dictionary,9, timeAxis)
		self.bollingerAnalysis(timeline,dictionary,13, timeAxis)
		self.bollingerAnalysis(timeline,dictionary,20, timeAxis)
		
		retDict = {}
		
		for key in dictionary:
			if dictionary[key][2] > 1:
				retDict[key] = dictionary[key]

		return retDict


	def removeConsolidatingFlags(self, listi):
		print "removing conso flags"

		retDict = {}

		
		print "semisort-----------------"
		listi = sorted(listi.iteritems(), key=operator.itemgetter(1))
		
		for key in listi:
			print key

		print "endisort-----------------"
		
		print "removing items..."
		
		removeList = []
		last = None
		
		for item in listi:
			curr = item[1]
	
			#index = item[1][0]
			#sing = item[1][1]	
				
			#print "index: " + str(item[1][0])
			#print "last: " + str(lastIndex)
			#print "sign: " + str(item[1][1])
			print "---"
			print last
			print curr
			
	
			if last == None:
			#	print "if..."
				last = curr
				lastDate = item[0]
			#if the items are next to each other with the same sign
			elif curr[0] - last[0] == 1 and last[1] == curr[1] and curr[2] > last[2]:
			#	print "elif..."
				#dostuff
				
				#curr Serverity is higher, throw out last
				if curr[2] > last[2]:
					print "the following item should be remoevd: " + str(lastDate)
					removeList.append(lastDate)
					
					last = curr
					lastDate = item[0]
				else:
					print "the following item should be remoevd: " + str(item[0])
					removeList.append(item[0])
					
					last = (curr[0], last[1], last[2])
					curr = last

			else:
			#	print "else..."
				lastDate = item[0]
				last = curr
		
		
		retList = []
		
		for item in listi:
			if item[0] not in removeList:
				retList.append( (item[0], item[1][2]) )
				
		return retList
#		return sorted(listi.iteritems(), key=operator.itemgetter(1))	


	
	def bollingerAnalysis(self, timeline, dictionary, frameSize, timeAxis):
		timeline = timeline.getMaskedArray()

		#avg = mov_average_expw(timeline, frameSize) # ! this function returns value for first n-1 iterations of the frame, std does not !
		avg = mov_average(timeline, frameSize)
		std = mov_std(timeline,frameSize)

		print "std"
		print std

		lowerlim = avg-std*2
		upperlim = avg+std*2
		count = 0

#ATH NOTA STAERRI TOLUR

		print "framesize: " + str(frameSize)
		print timeline		
		
		print upperlim
		print avg
		print lowerlim
		
		bandwidth_avg = (upperlim-lowerlim).mean()
		
		for index, item in enumerate(timeline):
			bandwidth = (upperlim[index-1] - lowerlim[index-1])
			
#			print str(item) + " - " + str(avg[index]) + " / " + str(upperlim[index]) + " - " + str(avg[index])
			percentb = abs((item - avg[index])/(upperlim[index] - avg[index]))
			if (str(percentb) in emptySet):
				percentb = 0
				
			if (bandwidth <= bandwidth_avg*0.25):
				percentb = percentb*0.6
			#print str(timeAxis[index]) + " : " + str(percentb)

			#dictionary[timeAxis[index]] = percentb * dictionary[timeAxis[index]]
			
			print "---------------" + str(percentb)
			if item > avg[index]:
				dictionary[timeAxis[index]] = (index, '+', percentb * dictionary[timeAxis[index]][2])
			else:
				dictionary[timeAxis[index]] = (index, '-', percentb * dictionary[timeAxis[index]][2])
										
		return dictionary


	def fourierAnalysis(self, timeline, timeAxis):
		Y=sp.fft(timeline)
		n=len(Y)
		power = abs(Y[1:(n/2)])**2
		nyquist=1./2
		freq=sp.array(range(n/2))/(n/2.0)*nyquist
		period=1./freq
		
		plot.plot(period[1:len(period)], power)
		#plot.plot(Y)
		plot.show()
