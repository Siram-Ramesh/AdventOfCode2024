import unittest
import numpy
import pandas as pd
import HistorianHysteria as hh

class TestHistorianHisteriaPart1(unittest.TestCase):

    def test_LengthOfOne(self):
        dist = hh.findTotalDistance('testcases/lengthOfOne.txt')
        self.assertEqual(dist, 7)

    def test_NoDiff(self):
        dist = hh.findTotalDistance('testcases/noDiff.txt')
        self.assertEqual(dist, 0)

    def test_AbsVal(self):
        dist = hh.findTotalDistance('testcases/absVal.txt')
        self.assertEqual(dist, 9)

if __name__ == '__main__':
    unittest.main()
