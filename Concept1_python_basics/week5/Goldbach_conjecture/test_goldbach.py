import unittest
from Goldbach import goldbach

class TestGoldbach(unittest.TestCase):
	def test_goldbach(self):
		test_cases = [
				(4, [(2,2)]),
				(6, [(3,3)]),
				(8, [(3,5)]),
				(10, [(3,7), (5,5)]),
				(100, [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]),
				(5, None)
				]

		with self.subTest('Testing proper behaiviour of goldbach function'):
			for actual, expected in test_cases:
				self.assertEqual(goldbach(actual), expected)


if __name__ == '__main__':
	unittest.main()