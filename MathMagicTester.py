# -*- coding: utf-8 -*-
import unittest2 as unittest
from MathMagic import MathMagic

class MathMagicTester(unittest.TestCase):
	
	def setUp(self):
		self.testList = [1,2,3,4,5]
		self.mathMagic = MathMagic()
		
	#sends a timeline to assert the standard deviation
	def testStandardDev(self):
		self.assertEqual(self.mathMagic.standardDev(self.testList),1.5811388300841898)
		self.assertEqual(self.mathMagic.standardDev([]),None)
	#sends a timeline to assrert the mean of that timeline	
	def testMean(self):
		self.assertEqual(self.mathMagic.mean(self.testList),3)
		self.assertEqual(self.mathMagic.mean([]),None)
		
		
def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(MathMagicTester)
	return suite
