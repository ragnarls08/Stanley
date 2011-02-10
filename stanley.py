import sys
import getopt
import urllib2
import simplejson as json

#def main():
try:
	opts, args = getopt.getopt(sys.argv[1:], "i:" )
except getopt.GetoptError, err:
	print str(err)
	sys.exit(2)

id = 28 #def value

for o,v in opts:
	if o == "-i":
		id = v

#if __name__ == "__main__":
#	main()

 
urlBase = "http://www.datamarket.com/api/v1/series.json?callback="

fullUrl = urlBase + "&ds=" + str(id)


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


	
