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


time_series = ["gunni_Awesom","leh3", "yef","1eh3"] # 1. er ologlegur, 2. ekki til, 3. of stor, 4 ok
#time_series = "yef"

#time_series = "1eh3" #british fatalities in afghanistan
#time_series = "1d8b|wzl=6" #crude oil
#time_series = "18ax|l2g=1w:l2h=2:l2i=12" #avocado
#time_series = "1ctt|wtr=3t:wts=f:wtt=1" #age population brazil
#time_series = "1bdn|twc=6:twe=k" #elecricity generation
#time_series = "w3x|6bx=3"
#time_series = "17tl|kqb=3" #rising slope, not interesting
#time_series = "1bcz|tuh=1o:tui=b:tuj=k" #oil import from iraq
#time_series = "yef" #?

#queryStringList = ["1eh3", "1d8b|wzl=6", "18ax|l2g=1w:l2h=2:l2i=12", "1ctt|wtr=3t:wts=f:wtt=1", "1bdn|twc=6:twe=k", "17tl|kqb=3", "1bcz|tuh=1o:tui=b:tuj=k", "1968"]

report = rynir.analyze(time_series)
#report = rynir.analyze(queryStringList)

try:
	for x in report:
		for i in x:
			print i
except:
	print 'wrong'
"""	
#debugging plot below, make sure parameters match the ones actually used
gate = DmGateway()
#gate = StaticGateway("staticDataSet.json")
ps = Parser()

dset = ps.parse(time_series)
#series = ts.time_series(dset[1].getMaskedArray(),
#						start_date=ts.Date(freq=dset.granularity, year=int(dset[0][0][0:4]), month=1))
#print series.count

fig = tplot.tsfigure()
# 111 = width, height, subplots
fsp = fig.add_tsplot(111)

for item in report[0]:
    for x in item.listOfFlags:
        #print "-----Flag: " + str(x[0])
        #print "--index: " + str(x[2])
        #print "place flag at : " + str(x[2]) + ", " + str(series[x[2]])


        fsp.annotate(x[1], xy=(x[2], dset[1][x[2]]),
                    xytext=(x[2]+5, dset[1][x[2]]+5), arrowprops=dict(facecolor='black', shrink=0.05),)

#fsp.annotate('raggi', xy=(50,20), xytext=(60, 20), arrowprops=dict(facecolor='black', shrink=0.05),)

fsp.plot(dset[1].getMaskedArray())
#fsp.tsplot(series, '-')


plot.show()
#plot.savefig('gunniAwesome')











#draw the series from the parser, solid line
#fsp.tsplot(series, '-')

"""
"""
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
"""

#fig = plot.figure(1, figsize=(8,5))
#ax = fig.add_subplot(111, autoscale_on=True)#, xlim=(-1,5), ylim=(-4,3))

#print series




