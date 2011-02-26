#!/usr/bin/env python
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

class NotifierTester(unittest.TestCase):

	def setUp(self):
		self.notifier = Notifier()
		self.testList = [1,2,3,4,5]
		self.ds = DataSet("Atvinnuleysi", "v28", "Year")
		self.ls = TimeLine("1st", "1ke", [1,2,3])
		
		self.ds.append(self.ls)
		

					
	def testMultiply(self):
		self.assertEqual(self.notifier.multi(2), 4)
		
#	def testIsIntresting(self):
#		self.assertEqual(self.notifier.isIntresting(self.ds), 1)
		
	
def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(NotifierTester)
	return suite

if __name__ == '__main__':
	unittest.main()