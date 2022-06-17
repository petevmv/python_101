import unittest
from prime_factorization import *

class TestPrimeFactorization(unittest.TestCase):
	def test_prime_factorization(self):
		cases = [
			(10, [(2, 1), (5, 1)]), # This is 2^1 * 5^1
			(14, [(2, 1), (7, 1)]),
			(356, [(2, 2), (89, 1)]),
			(89, [(89, 1)]), # 89 is a prime number
			(1000, [(2, 3), (5, 3)])
		]

		with self.subTest("Testing proper behaiviour of prime_factorization"):
			for actual, expected in cases:
				self.assertEqual(prime_factorization(actual), expected)
	def test_is_it_prime(self):
		cases_true = [2, 3, 5, 7, 13, 11, 13, 17, 19, 23, 29]
		cases_false = [6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28]

		with self.subTest('Testing proper behaiviour of test_is_it_prime'):
			for actual in cases_true:
				self.assertTrue(is_it_prime(actual))
			for actual in cases_false:
				self.assertFalse(is_it_prime(actual))


if __name__ == '__main__':
	unittest.main()