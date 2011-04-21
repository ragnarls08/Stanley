# -*- coding: utf-8 -*-
import unittest2 as unittest
from MathMagic import MathMagic

class MathMagicTester(unittest.TestCase):
	
	def setUp(self):
		self.testList = [1,2,3,4,5]
		self.mathMagic = MathMagic()
		
		
def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(MathMagicTester)
	return suite
