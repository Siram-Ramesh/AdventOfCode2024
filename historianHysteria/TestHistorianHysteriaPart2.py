import unittest
import HistorianHysteria as hh

class TestHistorianHisteriaPart2(unittest.TestCase):

    def test_Basic(self):
        sims = hh.findSimilarity('testcases/part2/basic.txt')
        self.assertEqual(sims, 31)

    def test_NoOverlap(self):
        sims = hh.findSimilarity('testcases/part2/noOverlap.txt')
        self.assertEqual(sims, 0)

    def test_AbsVal(self):
        sims = hh.findSimilarity('testcases/part2/absVal.txt')
        self.assertEqual(sims, 4)


if __name__ == '__main__':
    unittest.main()
