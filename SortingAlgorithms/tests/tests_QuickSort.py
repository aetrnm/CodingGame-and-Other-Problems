import unittest

from SortingAlgorithms import SortingAlgorithms

SA = SortingAlgorithms()


class QuickSortTestCases(unittest.TestCase):

    def test_evenAmountOfElements(self):
        self.assertEqual(SA.quickSort([3, 1, 4, 2]), [1, 2, 3, 4])

    def test_oddAmountOfElements(self):
        self.assertEqual(SA.quickSort([1, 3, 4, 2, -1]), [-1, 1, 2, 3, 4])

    def test_zeros(self):
        self.assertEqual(SA.quickSort([0]), [0])

    def test_allValuesDifferent(self):
        self.assertEqual(SA.quickSort([7, 3, 4, 1, 2, 5, -1]), [-1, 1, 2, 3, 4, 5, 7])

    def test_elementEqualToBarrier(self):
        self.assertEqual(SA.quickSort([3, 1, 2, 4, 16, 9, 2, 10, 9, 23]), [1, 2, 2, 3, 4, 9, 9, 10, 16, 23])


if __name__ == '__main__':
    unittest.main()
