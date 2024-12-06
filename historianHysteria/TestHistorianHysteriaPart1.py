import unittest
import numpy
import pandas as pd
import HistorianHysteria as hh

class TestHistorianHisteriaPart1(unittest.TestCase):

    def test_LengthOfOne(self):
        df = pd.read_csv('testcases/lengthOfOne.txt', header=None, delimiter='   ')
        arr1 = df.iloc[:,0].to_numpy()
        arr2 = df.iloc[:,1].to_numpy()
        
        dist = hh.findTotalDistance(arr1, arr2)
        self.assertEqual(dist, 7)

    def test_NoDiff(self):
        df = pd.read_csv('testcases/noDiff.txt', header=None, delimiter='   ')
        arr1 = df.iloc[:,0].to_numpy()
        arr2 = df.iloc[:,1].to_numpy()
        
        dist = hh.findTotalDistance(arr1, arr2)
        self.assertEqual(dist, 0)

if __name__ == '__main__':
    unittest.main()
