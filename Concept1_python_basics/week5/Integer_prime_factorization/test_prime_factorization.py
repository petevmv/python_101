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

if __name__ == '__main__':
	unittest.main()