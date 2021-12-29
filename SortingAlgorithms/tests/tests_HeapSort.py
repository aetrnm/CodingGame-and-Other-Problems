import unittest

from SortingAlgorithms import SortingAlgorithms

SA = SortingAlgorithms()


class HeapSortTestCases(unittest.TestCase):

    def test_evenAmountOfElements(self):
        self.assertEqual(SA.heapSort([3, 1, 4, 2]), [1, 2, 3, 4])

    def test_oddAmountOfElements(self):
        self.assertEqual(SA.heapSort([1, 3, 4, 2, -1]), [-1, 1, 2, 3, 4])

    def test_zeros(self):
        self.assertEqual(SA.heapSort([0]), [0])


if __name__ == '__main__':
    unittest.main()
