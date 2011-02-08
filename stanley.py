import urllib2
import simplejson as json


urlBase = "http://www.datamarket.com/"
urlTail = "/api/v1/series.json?callback=&ds=v28&maxresults=10"

fullUrl = urlBase + urlTail 


#gets a json timeline from the url given
#returns a json object
def getTimeLine( url ):
	try:
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		results = json.load( response )
		return results[0]
	except:
		return -1


#prints out the data portion of a timeline as a table
def displayData( timeLine ):
	str = ''
	i = 1 
	for entry in timeLine["columns"]:
		str += `i`
		str += "\t"
		str += entry["title"].encode('utf-8')
		str += "\n"
		i = i+1

	print str	
	str = ''
	for x in range(1, i):
		str += `x`
		str += "\t" 	
	print str
	print 
	for row in timeLine["data"]:
		str = ''
		for item in row:
			str += `item`
			str += "\t" 
		print str	

	
displayData( getTimeLine( fullUrl ) )


	
