import unittest

from SortingAlgorithms import SortingAlgorithms

SA = SortingAlgorithms()


class CountingSortTestCases(unittest.TestCase):

    def test_evenAmountOfElements(self):
        self.assertEqual(SA.countingSort([3, 1, 4, 2], 1, 4), [1, 2, 3, 4])

    def test_oddAmountOfElements(self):
        self.assertEqual(SA.countingSort([1, 3, 4, 2, -1], -1, 4), [-1, 1, 2, 3, 4])

    def test_zeros(self):
        self.assertEqual(SA.countingSort([0], 0, 0), [0])


if __name__ == '__main__':
    unittest.main()
