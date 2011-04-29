import numpy as np
import matplotlib.pyplot as plot
import scikits.timeseries as ts
import scikits.timeseries.lib.plotlib as tplot
from scikits.timeseries.lib.moving_funcs import *
import scipy as sp
from StaticGateway import StaticGateway

from Rynir import Rynir
from DmGateway import DmGateway
from Parser import Parser

rynir = Rynir()
time_series = "1eh3" #british fatalities in afghanistan
#time_series = "1d8b|wzl=6" #crude oil
#time_series = "18ax|l2g=1w:l2h=2:l2i=12" #avocado
#time_series = "1ctt|wtr=3t:wts=f:wtt=1" #age population brazil
#time_series = "1bdn|twc=6:twe=k" #elecricity generation
#time_series = "17tl|kqb=3" #rising slope, not interesting
#time_series = "1bcz|tuh=1o:tui=b:tuj=k" #oil import from iraq

report = rynir.analyze(time_series)

for x in report[0]:
	pass#print x

#debugging plot below, make sure parameters match the ones actually used
gate = DmGateway()
#gate = StaticGateway("staticDataSet.json")
ps = Parser(gate)

dset = ps.parse(time_series)
series = ts.time_series(dset[1].getMaskedArray(),
						start_date=ts.Date(freq=dset.granularity, year=int(dset[0][0][0:4]), month=1))
#print series.count

fig = tplot.tsfigure()
# 111 = width, height, subplots
fsp = fig.add_tsplot(111)

#draw the series from the parser, solid line
fsp.tsplot(series, '-')

#draw moving average, framesize 5, dotted green line
avg = mov_average(series, 13)
#avg9 = mov_average(series, 9)
#avg13 = mov_average(series, 13)
avgexp = mov_average_expw(series, 13)
std = mov_std(series, 13)
#std9 = mov_std(series, 9)
#std13 = mov_std(series, 13)

lowerlim = avg+std*2
upperlim = avg-std*2

#lowerlim9 = avg9+std9*2
#upperlim9 = avg9-std9*2

#lowerlim13 = avg13+std13*2
#upperlim13 = avg13-std13*2

fsp.tsplot(lowerlim, '--r')
fsp.tsplot(upperlim, '--r')

#fsp.tsplot(lowerlim9, '--y')
#fsp.tsplot(upperlim9, '--y')

#fsp.tsplot(lowerlim13, '--g')
#fsp.tsplot(upperlim13, '--g')

fsp.tsplot(avg, '--r')
fsp.tsplot(avgexp, '--y')
#fsp.tsplot(avg9, '--y')
#fsp.tsplot(avg13, '--g')

#t = sp.fft(dset[1].getMaskedArray())
#fftSer = ts.time_series(sp.fft(dset[1].getMaskedArray()),
#						start_date=ts.Date(freq=dset.granularity, year=int(dset[0][0][0:4]), month=1))

#fsp.tsplot(fftSer, '--y')
#print t

plot.show()















