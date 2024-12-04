import unittest
import numpy
import pandas as pd

class TestHistorianHisteriaPart1(unittest.TestCase):

    def test_LengthOfOne(self):
        df = pd.read_csv('lengthOfOne.txt', header=None, delimiter='\t')
        self.arr1 = df[[0]].to_numpy()
        self.arr2 = df[[1]].to_numpy()
        
        dist = findTotalDistance(arr1, arr2)
        unittest.assertEqual(dist, 7)

    def test_NoDiff(self):
        df = pd.read_csv('noDiff.txt', header=None, delimiter='\t')
        self.arr1 = df[[0]].to_numpy()
        self.arr2 = df[[1]].to_numpy()
        
        dist = findTotalDistance(arr1, arr2)
        unittest.assertEqual(dist, 0)

if __name__ == '__main__':
    unittest.main()
