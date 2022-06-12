import unittest
from fact_digit import fact_digits

class TestFactorialDigit(unittest.TestCase):
	def test_fact_digit(self):
		with self.subTest('Value Error'):
			with self.assertRaises(ValueError):
				fact_digits('abc')
			with self.assertRaises(ValueError):
				fact_digits([])
			with self.assertRaises(ValueError):
				fact_digits({})
			with self.assertRaises(ValueError):
				fact_digits((1, 2))
		with self.subTest('Type Error'):
			with self.assertRaises(TypeError):
				fact_digits(1,2,3,4,5)
			
		with self.subTest('Testing fact_digit() behave as expected'):
			self.assertEqual(fact_digits(1),1)
			self.assertEqual(fact_digits(101), 3)
			self.assertEqual(fact_digits(111), 3)
			self.assertEqual(fact_digits(145), 145)
			self.assertEqual(fact_digits(999), 1088640)
			self.assertNotEqual(fact_digits(101), 2)
			self.assertNotEqual(fact_digits(111), 1)
			self.assertNotEqual(fact_digits(145), 144)
			self.assertNotEqual(fact_digits(999), 999)

if __name__ == '__main__':
	unittest.main()


