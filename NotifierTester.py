# encoding: utf-8
"""
NotifierTester.py

Created by Thordur Arnarson on 2011-02-22.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import unittest
from Notifier import Notifier
from DataSet import DataSet
from TimeLine import TimeLine
from StaticGateway import StaticGateway
from Parser import Parser

class NotifierTester(unittest.TestCase):

	def setUp(self):
		self.notifier = Notifier()				
		self.gate = StaticGateway("staticDataSet.json")
		p = Parser(self.gate)
		self.dsObj = p.parse("")						
					
	def testIsIntresting(self):
		testResult = self.notifier.getReport(self.dsObj)		
		self.assertEqual(testResult[0][4][0][0], 1)
		self.assertEqual(testResult[0][4][1][0], 2)
		self.assertEqual(testResult[1][4][0][0], 1)
		self.assertEqual(testResult[1][4][1][0], 2)
		self.assertEqual(testResult[2][4][0][0], 2)
		self.assertEqual(testResult[3][4][0][0], 1)
		self.assertEqual(testResult[3][4][1][0], 2)			
		self.assertEqual(testResult[4][4][0][0], 0)
		
def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(NotifierTester)
	return suite