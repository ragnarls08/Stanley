import unittest

import DataSetTester
import TimeLineTester

#create suites for the test classes
suite1 = DataSetTester.suite()
suite2 = TimeLineTester.suite()

#initialize suite
suite = unittest.TestSuite()
 
#add tests to suite
suite.addTest(suite1)
suite.addTest(suite2)

unittest.TextTestRunner(verbosity=2).run(suite)
