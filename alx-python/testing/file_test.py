import doctest
import unittest
import doc1

suite = unittest.TestSuite()

suite.addTest(doctest.DocTestSuite(doc1))
suite.addTest(doctest.DocFileSuite('doc1.txt'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
