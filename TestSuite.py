import unittest2 as unittest

import DataSetTester
import TimeLineTester
import MathMagicTester
import DmGatewayTester
import QueryStringHandlerTester


#create suites for the test classes
suite1 = DataSetTester.suite()
suite2 = TimeLineTester.suite()
suite3 = MathMagicTester.suite()
#suite4 = DmGatewayTester.suite()
suite5 = QueryStringHandlerTester.suite()

#initialize suite
suite = unittest.TestSuite()
 
#add tests to suite
suite.addTest(suite1)
suite.addTest(suite2)
suite.addTest(suite3)
#suite.addTest(suite4)
suite.addTest(suite5)

unittest.TextTestRunner(verbosity=2).run(suite)
