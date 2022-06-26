import unittest
from sum_digits import sum_digits

class TestSumDigits(unittest.TestCase):
	def test_sum_digits(self):
		test_eq = [
					(sum_digits(1325132435356), 43),
					(sum_digits(123), 6),
					(sum_digits(6), 6),
					(sum_digits(-1), 1)
				]
		for actual, expected in test_eq:
			with self.subTest(f'Expected: {expected}'):
				self.assertEqual(actual, expected)
	

if __name__ == "__main__":
	unittest.main()