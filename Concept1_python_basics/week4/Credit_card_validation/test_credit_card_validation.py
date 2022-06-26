import unittest
from Credit_card_validation import *

class TestCreaditCardValidation(unittest.TestCase):
	def test_credit_card_validation(self):
		tests_valid = [
							79927398713, 
							31789372997,
							4417123456789113,
							4000002500003155,
						    4000002760003184		
						]	

		tests_invalid = [
							79927398715,
							4000002500003154,
							4000002760003183,
							4000002760003181,
							4000002760003186		
						]
		for valid in tests_valid:
			with self.subTest(f"Tests flaged {valid} as invalid"):
				self.assertTrue(is_credit_card_valid(valid))
		for invalid in tests_invalid:
			with self.subTest(f'Tests flagged {invalid} as valid'):
				self.assertFalse(is_credit_card_valid(invalid))

		
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
		

		for actual, expected in cases:	
			with self.subTest(f"Expected :{expected}"):
				self.assertEqual(sum_of_digits(actual), expected)
		# (79927398715) is False

if __name__ == '__main__':
	unittest.main()