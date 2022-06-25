import unittest
from fact_digit import fact_digits

class TestFactorialDigit(unittest.TestCase):
	def test_fact_digit(self):
		cases_equal = [
					  (1, 1),
					  (101, 3),
					  (111, 3),
					  (145, 145),
					  (999, 1088640)
			    	  ]
		for fact_input, expected in cases_equal:
			with self.subTest(f'Expected: {expected}'):
				self.assertEqual(fact_digits(fact_input), expected)
			
			# self.assertNotEqual(fact_digits(101), 2)
			# self.assertNotEqual(fact_digits(111), 1)
			# self.assertNotEqual(fact_digits(145), 144)
			# self.assertNotEqual(fact_digits(999), 999)

if __name__ == '__main__':
	unittest.main()


