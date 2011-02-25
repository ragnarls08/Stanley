import unittest

from TimeLine import TimeLine

class TimeLineTester(unittest.TestCase):
	
	def setUp(self):
		self.timeLine = TimeLine("Karlar 18-35", 5)

	def testSetTitle(self):
		self.assertEqual(self.timeLine.title, "Karlar 18-35")

	def testSetId(self):
		self.assertEqual(self.timeLine.cId, 5)


def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(TimeLineTester)
	return suite

