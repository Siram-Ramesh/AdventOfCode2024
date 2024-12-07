import unittest
import HistorianHysteria as hh

class TestHistorianHisteriaPart2(unittest.TestCase):

    def test_Basic(self):
        sims = hh.findSimilarity('testcases/basicPart2.txt')
        self.assertEqual(sims[0], 31)
        self.assertEqual(sims[1], 31)

    def test_NoOverlap(self):
        sims = hh.findSimilarity('testcases/noOverlapPart2.txt')
        self.assertEqual(sims[0], 0)
        self.assertEqual(sims[1], 0)

    def test_AbsVal(self):
        sims = hh.findSimilarity('testcases/absValPart2.txt')
        self.assertEqual(sims[0], 4)
        self.assertEqual(sims[1], 4)


if __name__ == '__main__':
    unittest.main()
