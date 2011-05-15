import numpy as np
import matplotlib.pyplot as plot
import scikits.timeseries as ts
import scikits.timeseries.lib.plotlib as tplot
from scikits.timeseries.lib.moving_funcs import *
import scipy as sp
from StaticGateway import StaticGateway
import traceback
from Rynir import Rynir
from DmGateway import DmGateway
from Parser import Parser

rynir = Rynir()


#time_series = ["gunni_Awesom","leh3", "yef","1eh3"] # 1. er ologlegur, 2. ekki til, 3. of stor, 4 ok
#time_series = "yef"
#time_series = 'yfu|6zj=1'
#time_series = '16z3|ib9=3b'
time_series = 'xja|67k=3'
#time_series = 'x7p|61x=2'
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

#report = rynir.analyze(time_series)
#report = rynir.analyze(queryStringList)

try:
	for x in report:
		for i in x:
			print i
except:
	pass

#debugging plot below, make sure parameters match the ones actually used
gate = DmGateway()
#gate = StaticGateway("staticDataSet.json")
ps = Parser()

dset = ps.parse(time_series)

series = ts.time_series(dset[1].getMaskedArray(),
						start_date=ts.Date(freq='year', year=1, month=1))
#print series.count

fig = tplot.tsfigure()
# 111 = width, height, subplots
fsp = fig.add_tsplot(111)
fsp.tsplot(series, '-')
np.seterr(invalid='raise')
try:
	avg = mov_average(series, 20)
	std = mov_std(series, 20)
except Exception as error:
	print error
	traceback.print_exc()
print series
print avg
print std
lowerlim = avg+std*2
upperlim = avg-std*2
print lowerlim
print upperlim

fsp.tsplot(lowerlim, '-r')
fsp.tsplot(upperlim, '-r')
#for item in report[0]:
    #for x in item.listOfFlags:
        ##print "-----Flag: " + str(x[0])
        ##print "--index: " + str(x[2])
        ##print "place flag at : " + str(x[2]) + ", " + str(series[x[2]])


        #fsp.annotate(x[1], xy=(x[2], dset[1][x[2]]),
                    #xytext=(x[2]+5, dset[1][x[2]]+5), arrowprops=dict(facecolor='black', shrink=0.05),)

#fsp.annotate('raggi', xy=(50,20), xytext=(60, 20), arrowprops=dict(facecolor='black', shrink=0.05),)

#fsp.plot(dset[1].getMaskedArray())
#fsp.tsplot(series, '-')


plot.show()
#plot.savefig('Kaup i kaupthing - timalina og bond')











#draw the series from the parser, solid line
#fsp.tsplot(series, '-')


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


"""

from scipy import linspace, polyval, polyfit, sqrt, stats, randn
from pylab import plot, title, show , legend


print dset


n=50
t=linspace(-5,5,n)

a=0.8
b=-4

x=polyval([a,b],dset[1]4)
xn=x+randn(n)

(ar,br)=polyfit(t,xn,1)
xr=polyval([ar,br],t)

err=sqrt(sum((xr-xn)**2)/n)



print('Linear regression using polyfit')
print('parameters: a=%.2f b=%.2f \nregression: a=%.2f b=%.2f, ms error= %.3f' % (a,b,ar,br,err))

#matplotlib ploting
title('Linear Regression Example')
plot(t,x,'g.--')
plot(t,xn,'k.')
plot(t,xr,'r.-')
legend(['original','plus noise', 'regression'])

show()


#Linear regression using stats.linregress
(a_s,b_s,r,tt,stderr)=stats.linregress(t,xn)
print('Linear regression using stats.linregress')
print('parameters: a=%.2f b=%.2f \nregression: a=%.2f b=%.2f, std error= %.3f' % (a,b,a_s,b_s,stderr))





"""




