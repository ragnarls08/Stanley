# encoding: utf-8

import numpy as np
import matplotlib.pyplot as plot
import scikits.timeseries as ts
import scikits.timeseries.lib.plotlib as tplot
from scikits.timeseries.lib.moving_funcs import *
import scipy as sp
import operator

emptySet = ['--', 'nan', 'inf']

class MathMagic:	

	def analyze(self, timeline, timeAxis, frameSize = None):
		dictionary = {}
		
		for item in timeAxis:
			dictionary[item] = (None, None, 1)
		
		if frameSize:
			print "received frameSize"
			dictionary = bollingerAnalysis(timeline, dictionary, frameSize, timeAxis)
		else:	
			print "no framesize, iterating"
			#kalla í fourier, ef það kemur rammastærð úr því þá kalla í BollingerFourier, annars iterativeBollinger
			dictionary = self.iterativeBollinger(timeline, timeAxis, dictionary)
			
			
		listi = self.consolidateFlags(dictionary)
			
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


	def consolidateFlags(self, listi):

		retDict = {}
		listi = sorted(listi.iteritems(), key=operator.itemgetter(1))	
		
		removeList = []
		last = None
		
		for item in listi:
			curr = item[1]
	
			if last == None:
				last = curr
				lastDate = item[0]
			#if the items are next to each other with the same sign
			elif curr[0] - last[0] == 1 and last[1] == curr[1] and curr[2] > last[2]:
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
				lastDate = item[0]
				last = curr
		
		
		retList = []
		
		for item in listi:
			if item[0] not in removeList:
				retList.append( (item[0], item[1][2], item[1][0]) )
				
		return retList

	#bollinger analysis function
	def bollingerAnalysis(self, timeline, dictionary, frameSize, timeAxis):
		timeline = timeline.getMaskedArray()
		
		try:
			#avg = mov_average_expw(timeline, frameSize) # ! this function returns value for first n-1 iterations of the frame, std does not !
			#for x in range(0, frameSize-1):
				#avg[x] = None
			#avg = np.ma.masked_array([ np.NaN if type(item) == type(None) else item for item in self ])
			#print avg
			avg = mov_average(timeline, frameSize)
			std = mov_std(timeline,frameSize)
		except NotImplementedError:
			print '*********************************ERROR*************************'
			return dictionary

		print "\n\nstd"
		print std
		print "avg\n\n"
		print avg

		#set the upper and lower bands for the bollinger analysis at K = 2
		lowerlim = avg-std*2
		upperlim = avg+std*2
		count = 0

#ATH NOTA STAERRI TOLUR TIL AÐ PROFA OVERFLOW

#		print "framesize: " + str(frameSize)
#		print timeline		
#		print '*******************'
#		print upperlim
#		print avg
#		print lowerlim
#		print '*******************'
		
		bandwidth_avg = (upperlim-lowerlim).mean()
		
		#for index, item in enumerate(timeline[:frameSize-1]):
#		for index, item in enumerate(timeline[1:]):
		for index, item in enumerate(timeline):
			bandwidth = (upperlim[index-1] - lowerlim[index-1])
			denominator = (upperlim[index] - avg[index])
			
#			print str(item) + " - " + str(avg[index]) + " / " + str(upperlim[index]) + " - " + str(avg[index])
			
			if str(item) in emptySet or str(upperlim[index]) in emptySet or str(lowerlim[index]) in emptySet or str(avg[index]) in emptySet or denominator == 0:
				percentb = 0
			else:
				percentb = abs((item - avg[index])/denominator)
				
			"""
			if denominator == 0:
				percentb = 0
			else:	
				percentb = abs((item - avg[index])/denominator)
			
			if (str(percentb) in emptySet):
				percentb = 0
			"""

			if (bandwidth <= bandwidth_avg*0.25):
				#could use some more logic: if item is higher than some % of timeline's average
				pass#percentb = percentb*0.6
			#print str(timeAxis[index]) + " : " + str(percentb)

			#dictionary[timeAxis[index]] = percentb * dictionary[timeAxis[index]]
			
			#print "---------------" + str(percentb)
			if item > avg[index]:
				dictionary[timeAxis[index]] = (index, '+', percentb * dictionary[timeAxis[index]][2])
			else:
				dictionary[timeAxis[index]] = (index, '-', percentb * dictionary[timeAxis[index]][2])
										

		return dictionary

	#fourier analysis function
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
