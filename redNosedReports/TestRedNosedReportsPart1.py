import unittest
import RedNosedReports as rnr

class TestRedNosedReportsPart1(unittest.TestCase):

    def test_singleRowAscValid(self):
        numValid = rnr.countValidReports('testcases/part1/singleRowAscValid.txt')
        self.assertEqual(numValid, 1)

    def test_basic(self):
        numValid = rnr.countValidReports('testcases/part1/basic.txt')
        self.assertEqual(numValid, 2)


if __name__ == '__main__':
    unittest.main()
