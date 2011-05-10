import unittest2 as unittest
import urllib2	
from DmGateway import *

class DmGatewayTester(unittest.TestCase):
	
	def setUp(self):
		self.gate = DmGateway()


	def testConnection(self):
		#self.assertRaises(urllib2.HTTPError, self.gate.getDs, "", 0)
		#self.assertRaises(urllib2.HTTPError, self.gate.getDs, None, 0)
		self.assertRaises(ConnectionError, self.gate.getDs, "", 0)
		self.assertRaises(ConnectionError, self.gate.getDs, None, 0)
		
def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(DmGatewayTester)
	return suite



