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
		with self.subTest('Testing proper behaivior of sum_digits()'):
			for actual, expected in test_eq:
				self.assertEqual(actual, expected)
			self.assertNotEqual(sum_digits(1325132435356), 44)
			self.assertNotEqual(sum_digits(123), 5)
		
		with self.subTest('Type Error'):
			with self.assertRaises(TypeError):
				sum_digits(1,2,3,4,5,6)
			with self.assertRaises(TypeError):
				sum_digits([1,2,3,4,5,6])
			with self.assertRaises(TypeError):
				sum_digits({})
			with self.assertRaises(TypeError):
				sum_digits((1,2))
			with self.assertRaises(TypeError):
				sum_digits()
			with self.assertRaises(TypeError):
				sum_digits('abc')


if __name__ == "__main__":
	unittest.main()