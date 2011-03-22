import unittest
import urllib2	
from DmGateway import DmGateway

class DmGatewayTester(unittest.TestCase):
	
	def setUp(self):
		self.gate = DmGateway()


	def testConnection(self):
		self.assertRaises(urllib2.HTTPError, self.gate.getDs, "", 0)
		self.assertRaises(urllib2.HTTPError, self.gate.getDs, None, 0)



# test below were used in unittest lib in python 2.7

#	def testNoneExistingPage(self):		
#
#		with self.assertRaises(urllib2.HTTPError) as cm:
#			self.gate.getDs(None)
#		
#		self.assertEquals(cm.exception.code, 404)

#	def testNoneExistingDataset(self):		
#
#		with self.assertRaises(urllib2.HTTPError) as cm:
#			self.gate.getDs("", 0)
#		
#		self.assertEquals(exc.exception.code, 400)
		
def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(DmGatewayTester)
	return suite



