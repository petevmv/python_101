import unittest
from Increasing_and_decreasing import *

class TestIncreasingAndDecreasing(unittest.TestCase):
	def test_increasing_or_decresing(self):
		tests = [
			(
				[1, 2, 3, 4, 5], 
				Monotonicity.INCREASING
			),
			(
				[5, 6, -10], 
				Monotonicity.NONE
			),
			(
				[1, 1, 1, 1], 
				Monotonicity.NONE
			),
			(
				[9, 8, 7, 6],
				Monotonicity.DECREASING
		 	),
			(
				[],
				Monotonicity.NONE
			),
			(
				[1], 
				Monotonicity.NONE
			),
			(
				[1, 100],
				Monotonicity.INCREASING
			),
			(
				[1, 100, 100], 
				Monotonicity.NONE
			),
			(
				[100, 1], 
				Monotonicity.DECREASING
			),
			(
				[100, 1, 1], 
				Monotonicity.NONE
			),
			(
				[100, 1, 2], 
				Monotonicity.NONE
			)
		]

		for actual, expected in tests:
			with self.subTest(f'Expected: {expected}'):
				self.assertEqual(increasing_or_decreasing(actual), expected)

if __name__ == '__main__':
	unittest.main()