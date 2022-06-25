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

		cases_not_equal = [ 
					      (111, 2),
					      (111, 1),
					      (145, 144),
					      (999, 999)
				       	  ]	    	  

		for fact_input, expected in cases_equal:
			with self.subTest(f'Expected: {expected}'):
				self.assertEqual(fact_digits(fact_input), expected)
			
		for fact_input, expected in cases_not_equal:
			with self.subTest(f'Expected not equal:{expected}'):
				self.assertNotEqual(fact_digits(fact_input), expected)

if __name__ == '__main__':
	unittest.main()


