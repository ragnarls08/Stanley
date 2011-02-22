import unittest

import DataSetTester
import TimeLineTester
import NotifierTester

#create suites for the test classes
suite1 = DataSetTester.suite()
suite2 = TimeLineTester.suite()

suite4 = NotifierTester.suite()

#initialize suite
suite = unittest.TestSuite()
 
#add tests to suite
suite.addTest(suite1)
suite.addTest(suite2)

suite.addTest(suite4)

unittest.TextTestRunner(verbosity=2).run(suite)
