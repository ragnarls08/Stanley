# -*- coding: utf-8 -*-

from DmGateway import DmGateway
from Notifier import Notifier
from Parser import Parser


class Rynir:
	def __init__(self):
		gate = DmGateway()
		self.parser = Parser(gate)
		self.notifier = Notifier()

	def analyze(self, inStr):
		if type(inStr) == list:
			ret = []
			for item in inStr:
				dset = self.parser.parse( item )
				ret.append( self.notifier.isIntresting( dset ) )
			return ret	
		else:
			dset = self.parser.parse( inStr )
			return self.notifier.isIntresting( dset )
		
