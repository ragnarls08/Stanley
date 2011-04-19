# encoding: utf-8

import numpy as np
import matplotlib.pyplot as plot
import scikits.timeseries as ts
import scikits.timeseries.lib.plotlib as tplot
from scikits.timeseries.lib.moving_funcs import *
import scipy as sp

class MathMagic:
  def standardDevAnalysis(self, timeline, timeAxis, frameSize = 5):
    
    #draw moving average, framesize 5, dotted green line
    timeline = timeline.getMaskedArray()
    
    avg = mov_average(timeline, frameSize)
    std = mov_std(timeline, frameSize)
    flags = []
    
    lowerlim = avg+std*2
    upperlim = avg-std*2
    
    for i in range(len(timeline)):
      if (timeline[i] < lowerlim[i] or timeline[i] > upperlim[i]):
	flags.append((timeAxis[i],50)) #index of flag + severity of flag
	
    return flags
    
"""
series = ts.time_series(dset[5].getMaskedArray(),
						start_date=ts.Date(freq=dset.granularity, year=int(dset[0][0][0:4]), month=1))
print series.count

fig = tplot.tsfigure()
# 111 = width, height, subplots
fsp = fig.add_tsplot(111)

#draw the series from the parser, solid line
fsp.tsplot(series, '-')

#draw moving average, framesize 5, dotted green line
avg = mov_average(series, 6)
std = mov_std(series, 6)

lowerlim = avg+std*1.5
upperlim = avg-std*1.5

fsp.tsplot(lowerlim, '--r')
fsp.tsplot(upperlim, '--r')
fsp.tsplot(avg, '--g')

#t = sp.fft(dset[1].getMaskedArray())
#fftSer = ts.time_series(sp.fft(dset[1].getMaskedArray()),
#						start_date=ts.Date(freq=dset.granularity, year=int(dset[0][0][0:4]), month=1))

#fsp.tsplot(fftSer, '--y')
#print t

plot.show()
"""
