import unittest
from Balanced_numbers import is_number_balanced

class TestBalancedNumbers(unittest.TestCase):
	def test_is_number_balanced(self):
		tests_true = [
				is_number_balanced(9),
				is_number_balanced(4518),
				is_number_balanced(1238033) 
				]

		tests_false = [
				is_number_balanced(28471),
				is_number_balanced(1234567),
				is_number_balanced(234563498573)				
				]	 
		
		with self.subTest('Testing proper function behaivour'):
			for i in tests_true:
				self.assertTrue(i)
			for i in tests_false:
				self.assertFalse(i)
		
		with self.subTest("Value Error"):
			with self.assertRaises(ValueError):
				is_number_balanced([])
			with self.assertRaises(ValueError):
				is_number_balanced({})
			with self.assertRaises(ValueError):
				is_number_balanced((1, 2))
			with self.assertRaises(ValueError):
				is_number_balanced('abc')
			with self.assertRaises(ValueError):
				is_number_balanced(1231.3)
if __name__ == '__main__':
	unittest.main()