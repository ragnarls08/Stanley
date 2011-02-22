import unittest

import DataSetTester
import TimeLineTester
import MathMagicTester

#create suites for the test classes
suite1 = DataSetTester.suite()
suite2 = TimeLineTester.suite()
suite3 = MathMagicTester.suite()

#initialize suite
suite = unittest.TestSuite()
 
#add tests to suite
suite.addTest(suite1)
suite.addTest(suite2)
suite.addTest(suite3)

unittest.TextTestRunner(verbosity=2).run(suite)
