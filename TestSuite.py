import unittest

import DataSetTester

#create suites for the test classes
suite1 = DataSetTester.suite()

#initialize suite
suite = unittest.TestSuite()
 
#add tests to suite
suite.addTest(suite1)


unittest.TextTestRunner(verbosity=2).run(suite)
