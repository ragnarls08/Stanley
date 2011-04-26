# encoding: utf-8

import numpy as np
import matplotlib.pyplot as plot
import scikits.timeseries as ts
import scikits.timeseries.lib.plotlib as tplot
from scikits.timeseries.lib.moving_funcs import *
import scipy as sp
import operator

class MathMagic:

	def standardDevAnalysis(self, timeline, timeAxis, frameSize = 60):
		return self.iterationTest(timeline, timeAxis)
	
	def iterationTest(self, timeline, timeAxis):
		listi = {} 

		listi = self.iterate(timeline,listi,5, timeAxis, 0.05)
		listi = self.iterate(timeline,listi,9, timeAxis, 0.12)
		listi = self.iterate(timeline,listi,13, timeAxis, 0.17)
		listi = self.iterate(timeline,listi,20, timeAxis, 0.26)
		listi = self.iterate(timeline,listi,30, timeAxis, 0.40)	
		
		return sorted(listi.iteritems(), key=operator.itemgetter(1))
		"""
		listinnokkar = []
        
		for key in listi:
			listinnokkar.append( (key, listi[key]) )
		
		return listinnokkar
		"""

	def iterate(self, timeline, dictionary, frameSize, timeAxis, weight):
        
		timeline = timeline.getMaskedArray()

		#avg = mov_average_expw(timeline, frameSize) # ! this function returns value for first n-1 iterations of the frame, std does not !
		avg = mov_average(timeline, frameSize)
		std = mov_std(timeline,frameSize)

		lowerlim = avg-std*2
		upperlim = avg+std*2
		count = 0
		
		for index, item in enumerate(timeline):
			#print "std: " + str(std[index]) + " type is " + str(type(std[index]))
			#print "avg: " + str(avg[index]) + " type is " + str(type(avg[index]))
			
			"""if (timeAxis[index] == '2005-10'):
				print timeAxis[index]
				print item
				print '\t' + str(upperlim[index])
				print '\t' + str(avg[index])
				print '\t' + str(lowerlim[index])
				print '\t' + str(std[index])
				print '\n'"""
			
			#try:
				#if (std[index] - avg[index] < -0,2 or std[index] - avg[index] > 0,2):
			#if(upperlim[index] != avg[index]):
			if (item < lowerlim[index]):
				count+=1
				severity = (item - lowerlim[index]) / (item - avg[index])*weight
				print "Framesize " + str(frameSize) + " flagged with weighted severity " + str(severity)
				if timeAxis[index] in dictionary:
					dictionary[timeAxis[index]] = severity + dictionary[timeAxis[index]] 
				else:
					dictionary[timeAxis[index]] = severity
			elif (item > upperlim[index]):
				count+=1
				severity = (item - upperlim[index]) / (item - avg[index])*weight
				print "Framesize " + str(frameSize) + " flagged " + timeAxis[index] + " with weighted severity " + str(severity)
				if timeAxis[index] in dictionary:
					dictionary[timeAxis[index]] = severity + dictionary[timeAxis[index]] 
				else:
					dictionary[timeAxis[index]] = severity
			#except:
			#	print 'error'
			#	pass
		print "Framesize " + str(frameSize) + " flagged " + str(count) + " instances"
		return dictionary
"""
    #draw moving average, framesize 5, dotted green line
    timeline = timeline.getMaskedArray()
    
#    avg = mov_average(timeline, frameSize)
    avg = mov_average_expw(timeline, frameSize)
#    std = mov_std(timeline, frameSize)
    std = mov_std(timeline, frameSize)
    flags = []
    
    lowerlim = avg-std*2
    upperlim = avg+std*2

    for index, item in enumerate(timeline):
        if (item < lowerlim[index]):
            severity = (item - lowerlim[index]) / (item - avg[index])
            flags.append((timeAxis[index], severity))
        elif (item > upperlim[index]):
            severity = (item - upperlim[index]) / (item - avg[index])
            flags.append((timeAxis[index], severity))

    


    #for i in range(len(timeline)):
    #  if (timeline[i] < lowerlim[i] or timeline[i] > upperlim[i]):
#	flags.append((timeAxis[i],50)) #index of flag + severity of flag

    return flags

"""
