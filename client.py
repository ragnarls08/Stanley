import numpy as np
import matplotlib.pyplot as plot
import scikits.timeseries as ts
import scikits.timeseries.lib.plotlib as tplot
from scikits.timeseries.lib.moving_funcs import *
import scipy as sp

from Rynir import Rynir
from DmGateway import DmGateway
from Parser import Parser

rynir = Rynir()
time_series = "1eh3" #british fatalities in afghanistan
#time_series = "1d8b|wzl=6" #crude oil
#time_series = "18ax|l2g=1w:l2h=2:l2i=12" #avocado
#time_series = "1ctt|wtr=3t:wts=f:wtt=1" #age population brazil
report = rynir.analyze(time_series)

for x in report[0]:
	print x

#debugging plot below, make sure parameters match the ones actually used
gate = DmGateway()
ps = Parser(gate)

dset = ps.parse(time_series)
series = ts.time_series(dset[1].getMaskedArray(),
						start_date=ts.Date(freq=dset.granularity, year=int(dset[0][0][0:4]), month=1))
print series.count

fig = tplot.tsfigure()
# 111 = width, height, subplots
fsp = fig.add_tsplot(111)

#draw the series from the parser, solid line
fsp.tsplot(series, '-')

#draw moving average, framesize 5, dotted green line
avg = mov_average(series, 5)
#avg = mov_average_expw(series, 15)
std = mov_std(series, 5)

lowerlim = avg+std*2
upperlim = avg-std*2

fsp.tsplot(lowerlim, '--r')
fsp.tsplot(upperlim, '--r')
fsp.tsplot(avg, '--g')

#t = sp.fft(dset[1].getMaskedArray())
#fftSer = ts.time_series(sp.fft(dset[1].getMaskedArray()),
#						start_date=ts.Date(freq=dset.granularity, year=int(dset[0][0][0:4]), month=1))

#fsp.tsplot(fftSer, '--y')
#print t

plot.show()















