import 	ConfigParser, os

config = ConfigParser.RawConfigParser()

config.add_section('API')
config.set('API','key','')
config.set('API','URL','http://www.datamarket.com/api/v1/series.json?callback=')

config.add_section('ReturnValues')	
config.set('ReturnValues','filter','1')
config.set('ReturnValues','consolidateflags','TRUE')
config.set('ReturnValues','latestupdateonly','FALSE')

config.add_section('BollingerVariables')
config.set('BollingerVariables','framesize3','20')
config.set('BollingerVariables','framesize2','13')
config.set('BollingerVariables','framesize1','9')
config.set('BollingerVariables','k','2')

config.add_section('Threads')
config.set('Threads','numberofthreads','6')

config.add_section('ReturnOptions')
config.set('ReturnOptions','topn','20')


with open('config.cfg','wb') as conFile:
	config.write(conFile)
	
