import unittest
from DataSet import DataSet


class DataSetTester(unittest.TestCase):

	def setUp(self):
		self.dataSet = DataSet()

	def testInsertItem(self):
		self.dataSet.timelines.append("bleleafds")

		self.assertEqual(len(self.dataSet), 1)

def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(DataSetTester)
	return suite
