# encoding: utf-8

import numpy as np
import matplotlib.pyplot as plot
import scikits.timeseries as ts
import scikits.timeseries.lib.plotlib as tplot
from scikits.timeseries.lib.moving_funcs import *
import scipy as sp

class MathMagic:
  def standardDevAnalysis(self, timeline, timeAxis, frameSize = 60):
    
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


