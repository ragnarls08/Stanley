# encoding: utf-8

import numpy as np
import matplotlib.pyplot as plot
import scikits.timeseries as ts
import scikits.timeseries.lib.plotlib as tplot
from scikits.timeseries.lib.moving_funcs import *
import scipy as sp


from DmGateway import DmGateway
from StaticGateway import StaticGateway
from Parser import Parser


#gate = StaticGateway("staticDataSet.json")
gate = DmGateway()
ps = Parser(gate)

dset = ps.parse("wf5")
series = ts.time_series(dset[1].getMaskedArray(),
						start_date=ts.Date(freq=dset.granularity, year=int(dset[0][0][0:4]), month=1))

fig = tplot.tsfigure()
# 111 = width, height, subplots
fsp = fig.add_tsplot(111)

#draw the series from the parser, solid line
fsp.tsplot(series, '-')

#draw moving average, framesize 5, dotted green line
avg = mov_average(series, 5)
std = mov_std(series, 5)

lowerlim = avg+std*1.5
upperlim = avg-std*1.5

fsp.tsplot(lowerlim, '--r')
fsp.tsplot(upperlim, '--r')
fsp.tsplot(mov_average(series, 5), '--g')

#t = sp.fft(dset[1].getMaskedArray())
#fftSer = ts.time_series(sp.fft(dset[1].getMaskedArray()),
#						start_date=ts.Date(freq=dset.granularity, year=int(dset[0][0][0:4]), month=1))

#fsp.tsplot(fftSer, '--y')
#print t

plot.show()
