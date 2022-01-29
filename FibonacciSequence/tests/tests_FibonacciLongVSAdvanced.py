import unittest
from fibonacciVariations import fibLong, fibAdvanced


class FibonacciLongVSAdvancedTests(unittest.TestCase):
    def test_Fibs1_000(self):
        self.assertEqual(fibAdvanced(1_000), fibLong(1_000))

    def test_Fibs10_000(self):
        self.assertEqual(fibAdvanced(10_000), fibLong(10_000))

    def test_Fibs100_000(self):
        self.assertEqual(fibAdvanced(100_000), fibLong(100_000))

    def test_Fibs1_000_000(self):
        self.assertEqual(fibAdvanced(1_000_000), fibLong(1_000_000))

    def test_Fibs10_000_000(self):
        self.assertEqual(fibAdvanced(10_000_000), fibLong(10_000_000))

    def test_Fibs100_000_000(self):
        self.assertEqual(fibAdvanced(100_000_000), fibLong(100_000_000))

    def test_Fibs1_000_000_000(self):
        self.assertEqual(fibAdvanced(100_000_000), fibLong(100_000_000))

    def test_Fibs1_000_000_000_000_000(self):
        self.assertEqual(fibAdvanced(1_000_000_000_000_000), fibLong(1_000_000_000_000_000))

    def test_Fibs1_000_000_000_000_000_000_000(self):
        self.assertEqual(fibAdvanced(1_000_000_000_000_000_000_000), fibLong(1_000_000_000_000_000_000_000))

    def test_Fibs1_000_000_000_000_000_000_000_000_000(self):
        self.assertEqual(fibAdvanced(1_000_000_000_000_000_000_000_000_000), fibLong(1_000_000_000_000_000_000_000_000_000))


if __name__ == '__main__':
    unittest.main()
