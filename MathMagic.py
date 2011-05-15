# encoding: utf-8

import traceback
import numpy as np
import matplotlib.pyplot as plot
import scikits.timeseries as ts
import scikits.timeseries.lib.plotlib as tplot
from scikits.timeseries.lib.moving_funcs import *
import scipy as sp
import operator
import ConfigParser
import logging

emptySet = ['--', 'nan', 'inf']

class MathMagic:

	def __init__ (self):
		self.config = ConfigParser.RawConfigParser()
		self.config.read('config.cfg')
		try:
			self.K = self.config.getfloat('BollingerVariables','k')
		except ConfigParser.NoSectionError, e:
			logging.error(e)
		except ConfigParser.Error, e:
			logging.error(e)	
		
		self.frame1 = self.config.getint('BollingerVariables','framesize1')
		self.frame2 = self.config.getint('BollingerVariables','framesize2')
		self.frame3 = self.config.getint('BollingerVariables','framesize3')

		#TODO: Eftir ad setja inn consolidate flags breytu
		#TODO: filter breyta
		
		
	def analyze(self, timeline, timeAxis, frameSize = None):
	
		
		#if timeline is too short or too long, return no flags
		if len(timeline) < 7: 
			return []
		if len(timeline) > 50000:
			return []
		
		#frameSize = self.fourierAnalysis(timeline, timeAxis)
		
		dictionary = {}
		
		#create an empty tuple to multiply the flag values with
		for item in timeAxis:
			dictionary[item] = (None, None, 0,len(timeline), 0)
		
		#if a specific framesize was requested use that, otherwise use itarative bollinger
		if frameSize:
			dictionary = bollingerAnalysis(timeline, dictionary, frameSize, timeAxis)
		else:	
			#kalla í fourier, ef það kemur rammastærð úr því þá kalla í BollingerFourier, annars iterativeBollinger
			dictionary = self.iterativeBollinger(timeline, timeAxis, dictionary)

		#TODO config variable for consolidate flags
		#consolidates flags that are adjecent, picks the highest severity in each adjecent sequence
		if True:#flag missing
		  listi = self.consolidateFlags(dictionary)
		else:
		  tempList = sorted(dictionary.iteritems(), key=operator.itemgetter(1))
		  for item in tempList:
			listi.append( (item[0], item[1][2], item[1][0]) )

		return listi

	def iterativeBollinger(self, timeline, timeAxis, dictionary):
		self.bollingerAnalysis(timeline,dictionary,self.frame1, timeAxis)
		self.bollingerAnalysis(timeline,dictionary,self.frame2, timeAxis)
		self.bollingerAnalysis(timeline,dictionary,self.frame3, timeAxis)

		retDict = {}
		
		#TODO config variable for filter
		#filter out all flags with severity lower than filter.
		for key in dictionary:
			if dictionary[key][4] == 0:
				denominator = 1
			else:
				denominator = dictionary[key][4]
			
			if dictionary[key][2]/denominator > 1:
				retDict[key] = dictionary[key]

		return retDict

	def consolidateFlags(self, listi):
		retList = []
					
		#sort items on severity 
		listi = sorted(listi.iteritems(), key=operator.itemgetter(1))
			
		groups = []
		currList = []
		
		for item in listi:
		  #if list is not empty
		  if currList:
			#if current item is adjecent to the last item in the listi
			if item[1][0] - currList[-1][1][0] == 1 and item[1][1] == currList[-1][1][1]:
			  currList.append(item)
			#else put the current list into the group lists and apend the current item to and empty list
			else:
			  groups.append(currList)
			  currList = []
			  currList.append(item)
		  #if the list was not empty, append an item to it
		  else:
			currList.append(item)
			
		#if there is anything remaining append it to the groups list
		if currList:
		  groups.append(currList)
			
		#loop through groups, get the max item out of each grouping
		for item in groups:
			maxItem = max(item, key=lambda x: (x[1][2])/(x[1][4]))
			date = maxItem[0]
			severity = maxItem[1][2]/maxItem[1][4]
			index = maxItem[1][0]
			timelineLen = maxItem[1][3]
			retList.append( (date, severity, index, timelineLen) )
		
		return retList
		
		
	#bollinger analysis function
	def bollingerAnalysis(self, timeline, dictionary, frameSize, timeAxis):
		np.seterr(invalid='raise')
		timeline = timeline.getMaskedArray()
		
		try:
			avg = mov_average(timeline, frameSize)
			std = mov_std(timeline,frameSize)		
			
		except NotImplementedError as error:
			logging.error('From bollingerAnalysis in MathMagic : %s', str(error))
			return dictionary
		except ValueError as error:
			logging.error('From bollingerAnalysis in MathMagic : %s', str(error))
			return dictionary
		except FloatingPointError as error:
			raise
			#logging.error('From bollingerAnalysis in MathMagic : %s', str(error))
			#return dictionary
		#set the upper and lower bands for the bollinger analysis at K = 2
		lowerlim = avg-std*self.K
		upperlim = avg+std*self.K
		
		bandwidth_avg = (upperlim-lowerlim).mean()
		
		for index, item in enumerate(timeline):
			prevUpperlim = upperlim[index-1]
			prevLowerlim = lowerlim[index-1]
				
			if str(prevUpperlim) in emptySet or str(prevLowerlim) in emptySet:
				bandwidth = 0
			else:
				bandwidth = (prevUpperlim - prevLowerlim)
				
			denominator = (upperlim[index] - avg[index])
			
			if str(item) in emptySet or str(upperlim[index]) in emptySet or str(lowerlim[index]) in emptySet or str(avg[index]) in emptySet or denominator == 0:
				percentb = 0
			else:
				percentb = abs((item - avg[index])/denominator)

			if (bandwidth <= bandwidth_avg*0.25):
				#could use some more logic: if item is higher than some % of timeline's average
				percentb = percentb*0.6
			
			severity = percentb + dictionary[timeAxis[index]][2]
			try:
				if percentb > 0:
					#print dictionary[timeAxis[index]][4]
					flaggedCounter = dictionary[timeAxis[index]][4] + 1
				else:
					#print dictionary[timeAxis[index]][4]
					flaggedCounter = dictionary[timeAxis[index]][4]
				
				if item > avg[index]:
					dictionary[timeAxis[index]] = (index, '+', severity, len(timeline), flaggedCounter)
				else:
					dictionary[timeAxis[index]] = (index, '-', severity, len(timeline), flaggedCounter)
			except Exception:
				traceback.print_exc()
			if False:
				print 'FrameSize: ' + str(frameSize)
				print timeline
				print 'Denominator: ' + str(denominator)
				print 'Avg: ' + str(avg[index])
				print 'Std: ' + str(std[index])
				print 'Upperlim: ' + str(upperlim[index])
				print 'Lowerlim: ' + str(lowerlim[index])
				print 'Severity: ' + str(severity)
				
		return dictionary

	#fourier analysis function
	def fourierAnalysis(self, timeline, timeAxis):
		try:
			periodSize = None
			Y=sp.fft(timeline)
			n=len(Y)
			power = abs(Y[1:(n/2)])**2
			nyquist=1./2
			freq=sp.array(range(n/2))/(n/2.0)*nyquist
			period=1./freq
			
			end = len(power)
			
			avg = np.mean(power[1:end])
			#avg = np.mean(power)
			print 'avg: ' + str(avg)
			std = np.std(power[1:end])
			#std = np.std(power)
			print 'std: ' + str(std)
			maxItem = max(power[1:end]-avg)
			print maxItem
			
			index = np.where(power==maxItem)
			
			if (maxItem-avg)/std > 2:
					periodSize = period[index[0][0]+1]
		
		except Exception, e:
			loggeing.error(e)
			
		finally:
			print 'fourier says: '
			print 'returning: ' + str(periodSize)
			print 'fourier done'
			plot.plot(period[1:len(period)], power)
			plot.show()
			return periodSize