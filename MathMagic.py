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
		listi = {}
		
		for item in timeAxis:
			listi[item] = 1
		
		if frameSize:
			bollingerAnalysis(timeline, listi, frameSize, timeAxis, 1)
		else:	
			#kalla í fourier, ef það kemur rammastærð úr því þá kalla í BollingerFourier, annars iterativeBollinger
			self.iterativeBollinger(timeline, timeAxis, listi)
			
		#return listi
		return sorted(listi.iteritems(), key=operator.itemgetter(1))
	
	def iterativeBollinger(self, timeline, timeAxis, dictionary):
		self.bollingerAnalysis(timeline,dictionary,9, timeAxis, 0.8)#0.45)#0.30)
		self.bollingerAnalysis(timeline,dictionary,13, timeAxis, 0.5)#0.30)#0.15)
		self.bollingerAnalysis(timeline,dictionary,20, timeAxis, 0.3)#0.15)#0.10)
		
		return dictionary
	
	def bollingerAnalysis(self, timeline, dictionary, frameSize, timeAxis, weight):
		timeline = timeline.getMaskedArray()

		#avg = mov_average_expw(timeline, frameSize) # ! this function returns value for first n-1 iterations of the frame, std does not !
		avg = mov_average(timeline, frameSize)
		std = mov_std(timeline,frameSize)

		lowerlim = avg-std*2
		upperlim = avg+std*2
		count = 0
		
		bandwidth_avg = (upperlim-lowerlim).mean()
		
		for index, item in enumerate(timeline):
			bandwidth = (upperlim[index-1] - lowerlim[index-1])
			
			percentb = abs((item - avg[index])/(upperlim[index] - avg[index]))
			if (str(percentb) in emptySet):
				percentb = 0
				
			if (bandwidth <= bandwidth_avg*0.2):
				percentb = percentb*0.8
			#print str(timeAxis[index]) + " : " + str(percentb)
			dictionary[timeAxis[index]] = percentb * dictionary[timeAxis[index]]
		return dictionary
		"""
			try:
				#bandwidth = (upperlim[index-1] - lowerlim[index-1])
				
				if (item < lowerlim[index]):
					count+=1
					severity = (item - lowerlim[index]) / (item - avg[index])*weight
					print "Framesize " + str(frameSize) + " flagged with weighted severity " + str(severity)
					if (bandwidth <= bandwidth_avg*0.5):
						severity = severity*0.1
						print "Bandwidth to low: severity bumped down to " + str(severity)
					if timeAxis[index] in dictionary:
						dictionary[timeAxis[index]] = severity + dictionary[timeAxis[index]] 
					else:
						dictionary[timeAxis[index]] = severity
						
				elif (item > upperlim[index]):
					count+=1
					severity = (item - upperlim[index]) / (item - avg[index])*weight
					print "Framesize " + str(frameSize) + " flagged " + timeAxis[index] + " with weighted severity " + str(severity)
					if (bandwidth <= bandwidth_avg*0.2):
						severity = severity*0.1 #******************************************must check how severe this item is from the timeline's mean
						print "Bandwidth to low: severity bumped down to " + str(severity)
					if timeAxis[index] in dictionary:
						print "Item found, adding severity"
						dictionary[timeAxis[index]] = severity + dictionary[timeAxis[index]] 
					else:
						print "Item not found, new key created"
						dictionary[timeAxis[index]] = severity
			except Exception as inst:
				print type(inst)     # the exception instance
				print inst.args      # arguments stored in .args
				print inst           # __str__ allows args to printed directly
				
		print "Framesize " + str(frameSize) + " flagged " + str(count) + " instances"
		return dictionary
	"""
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
