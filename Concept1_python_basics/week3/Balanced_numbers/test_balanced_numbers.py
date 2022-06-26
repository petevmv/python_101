import unittest
from Balanced_numbers import is_number_balanced

class TestBalancedNumbers(unittest.TestCase):
	def test_is_number_balanced(self):
		tests_true = [9, 4518, 1238033]

		tests_false = [28471, 1234567, 234563498573]	 
		
		for balanced_num in tests_true:
			with self.subTest(f'test fails with ({balanced_num})'):
				self.assertTrue(is_number_balanced(balanced_num))
		
		for not_balanced_num in tests_false:
			with self.subTest(f'test fails with ({not_balanced_num})'):
				self.assertFalse(is_number_balanced(not_balanced_num))

		
if __name__ == '__main__':
	unittest.main()