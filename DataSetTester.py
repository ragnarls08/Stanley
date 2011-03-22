import unittest2 as unittest
from DataSet import DataSet
from TimeLine import TimeLine

class DataSetTester(unittest.TestCase):

	def setUp(self):
		self.dataSet = DataSet("Atvinnuleysi", "v28", "Year")
		self.timeline = TimeLine("Title1", "id1")

	def testInsertItem(self):
		self.dataSet.append(self.timeline)
		self.dataSet.append(self.timeline)

		self.assertEqual(len(self.dataSet), 2)

def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(DataSetTester)
	return suite
