# -*- coding: utf-8 -*-
import unittest2 as unittest
from MathMagic import MathMagic
from TimeLine import TimeLine

class MathMagicTester(unittest.TestCase):
	
	def setUp(self):
		self.legalTimeline = TimeLine('Legal', 'MyID', [0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 3, 3, 8, 19, 1, 0, 3, 2, 2, 4, 1, 5, 4, 6, 100, 7, 1, 2, 2, 1, 2, 2, 3, 3, 13, 4, 2, 4, 1, 7, 9, 6, 6, 3, 1, 12, 4, 22, 19, 8, 6, 12, 9, 6, 15, 12, 3, 8, 20, 16, 7, 6, 4, 100, 3, 2, 7, 1])
		self.emptyTimeline = TimeLine('Title', 'ID', [])
		self.charTimeline = TimeLine('Title', 'ID', ['a', 'b', 'c', 'd', 'e'])
		self.emptyValuesTimeline = TimeLine('Title', 'ID', [None, 1, 2, 1, 4, None, 6, 7, 8, 9, 100, 1])
		self.illegalValuesTimeline = TimeLine('Title', 'ID', ['inf', 1, 2, 1, 4, '--', 6, 7, 8, 9, 100, 1])
		self.mathMagic = MathMagic()

	def testLegalTimeline(self):
		timeAxis = []
		for index, item in enumerate(self.legalTimeline):
			timeAxis.append(index)
		
		dictionary = {}
		for item in timeAxis:
			dictionary[item] = (None, None, 1)

		testResult = self.mathMagic.bollingerAnalysis(self.legalTimeline, dictionary, 20, timeAxis)
		
		#for key in testResult:
		#	if testResult[key][2] > 1:
		#		print 'flag at ' + str(testResult[key][0]) + ' with value of ' + str(self.legalTimeline[testResult[key][0]])
		#		print testResult[key][2]
		
		self.assertGreater(testResult[67][2], 1)
		self.assertGreater(testResult[106][2], 1)
		self.assertGreater(testResult[67][2], testResult[106][2])
		
	def testEmptyTimeline(self):
		timeAxis = []
		
		#check if dictionary is empty for empty timeline
		testResult = self.mathMagic.bollingerAnalysis(self.emptyTimeline, {}, 2, timeAxis)
		self.assertEqual(testResult, {})
		
		#check if dictionary is the same after call with an empty timeline
		testResult = self.mathMagic.bollingerAnalysis(self.emptyTimeline, {1:'2'}, 2, timeAxis)
		self.assertEqual(testResult, {1:'2'})
		
	def testIllegalTimeline(self):
		#check if dictionary is empty after call with timeline with illegal values
		timeAxis = [1, 2, 3, 4, 5]
		testResult = self.mathMagic.bollingerAnalysis(self.charTimeline, {}, 2, timeAxis)
		self.assertEqual(testResult, {})
		
	def testEmptyValues(self):
		timeAxis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
		dictionary = {}
		for item in timeAxis:
			dictionary[item] = (None, None, 1)
			
		#check if flag has higher than one severity. severity should be calculated even though timeline has some empty values
		testResult = self.mathMagic.bollingerAnalysis(self.emptyValuesTimeline, dictionary, 2, timeAxis)
		self.assertGreater(testResult[11], 1)		
		
	def testIllegalValues(self):
		timeAxis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
		dictionary = {}
		for item in timeAxis:
			dictionary[item] = (None, None, 1)
			
		#check if flag has higher than one severity. severity should be calculated even though timeline has some illegal values
		testResult = self.mathMagic.bollingerAnalysis(self.illegalValuesTimeline, dictionary, 2, timeAxis)
		self.assertGreater(testResult[11], 1)
		
	def testRisingConsecutiveFlags(self):
		dictionary = {0:(0, '+', 1.5), 1:(1, '+', 1.9), 2:(2, '+', 3), 3:(3, '+', 2.5), 4:(4, '+', 2), 5:(5, '+', 2)}
		flags = self.mathMagic.consolidateFlags(dictionary)
		self.assertEqual(flags, [(2, 3, 2)])
		
	def testRisingNonConsecutiveFlags(self):
		dictionary = {0:(0, '+', 1.5), 1:(1, '+', 1.9), 2:(2, '+', 3), 3:(4, '+', 2.5), 4:(5, '+', 2), 5:(6, '+', 2)}
		flags = self.mathMagic.consolidateFlags(dictionary)
		self.assertEqual(flags, [(2, 3, 2), (3, 2.5, 4)])
	
def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(MathMagicTester)
	return suite
