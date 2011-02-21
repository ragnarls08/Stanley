import unittest
from DataSet import DataSet


class DataSetTester(unittest.TestCase):

	def setUp(self):
		self.dataSet = DataSet("Atvinnuleysi", "v28")

	def testInsertItem(self):
		self.dataSet.append("Karlar 28", "1ke")

		self.assertEqual(len(self.dataSet), 1)

def suite():
	suite = unittest.TestLoader().loadTestsFromTestCase(DataSetTester)
	return suite
