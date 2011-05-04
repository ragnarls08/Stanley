import unittest2 as unittest
from QueryStringHandler import QueryStringHandler

class QueryStringHandlerTester(unittest.TestCase):
	
	def setUp(self):
		self.handler = QueryStringHandler()

	def testInvalidQueryString(self):
		self.assertEqual(self.handler.getReport('gunniAwesome'), None)
	
	def testLegalQueryString(self):
		self.assertNotEqual(self.handler.getReport('1eh3'), None)
	
	def testNoneQueryString(self):
		self.assertEqual(self.handler.getReport(None), None)

		
def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(QueryStringHandlerTester)
	return suite



