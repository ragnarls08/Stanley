import 	ConfigParser, os

config = ConfigParser.RawConfigParser()

config.add_section('API')
config.set('API','key','')
config.set('API','URL','http://www.datamarket.com/api/v1/series.json?callback=')

config.add_section('ReturnValues')	
config.set('ReturnValues','Filter','1')
config.set('ReturnValues','ConsolidateFlags','TRUE')
config.set('ReturnValues','LatestUpdateOnly','FALSE')

config.add_section('BollingerVariables')
config.set('BollingerVariables','Framesize4','20')
config.set('BollingerVariables','Framesize3','11')
config.set('BollingerVariables','Framesize2','9')
config.set('BollingerVariables','Framesize1','7')
config.set('BollingerVariables','K','2')

config.add_section('Threads')
config.set('Threads','NumberOfThreads','6')


with open('config.cfg','wb') as conFile:
	config.write(conFile)
	
