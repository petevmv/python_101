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

# (79927398715) is False

if __name__ == '__main__':
	unittest.main()