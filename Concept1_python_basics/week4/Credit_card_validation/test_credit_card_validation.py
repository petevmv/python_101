import unittest
from Credit_card_validation import *

class TestCreaditCardValidation(unittest.TestCase):
	def test_credit_card_validation(self):
		tests_valid = [
			(79927398713, True),
			(31789372997, True),
			(4417123456789113, True),  
			(4000002500003155, True),
			(4000002760003184, True)
		]

		tests_invalid = [
			(79927398715, False),
			(4000002500003154, False),
			(4000002760003183, False),
			(4000002760003181, False),
			(4000002760003186, False)
		]

		with self.subTest("Testing proper behaviour of credit_card_validation"):
			for actual, expected in tests_valid:
				self.assertTrue(is_credit_card_valid(actual))
			for actual, expected in tests_invalid:
				self.assertFalse(is_credit_card_valid(actual))

		with self.subTest("Value Error"):
			with self.assertRaises(ValueError):
				is_credit_card_valid([])
			with self.assertRaises(ValueError):
				is_credit_card_valid({})
			with self.assertRaises(ValueError):
				is_credit_card_valid((1,2))
			with self.assertRaises(ValueError):
				is_credit_card_valid('abc')

	def test_sum_of_digits(self):
		cases = [
					(1, 2),
					(2, 4),
					(3, 6),
					(4, 8),
					(5, 1),
					(6, 3),
					(7, 5),
					(8, 7),
					(9, 9)
				]
		with self.subTest("Test proper behaviour of sum_of_digits"):
			for actual, expected in cases:
				self.assertEqual(sum_of_digits(actual), expected)
	# (79927398715) is False

if __name__ == '__main__':
	unittest.main()