import unittest
from fraction import Fraction

class FractionTest(unittest.TestCase):

	def test_init(self):
		with self.assertRaises(ValueError):
			Fraction(1, 0)

		with self.assertRaises(TypeError):
			Fraction('str', 1)

		with self.assertRaises(TypeError):
			Fraction(1, 'str')

		with self.assertRaises(TypeError):
			Fraction()


	def test_string_repr_and_zero(self):
		self.assertEqual(str(Fraction(1, 2)), '1/2')
		self.assertEqual(repr(Fraction(1, 2)), 'Fraction(1, 2)')
		
		self.assertEqual(str(Fraction(0, 1)), '0')
		self.assertEqual(repr(Fraction(0, 1)), '0')

		

	def test_add_sub_and_mul(self):
		a = Fraction(1, 2)
		b = Fraction(1, 2)
		a_neg = Fraction(-1, 2)
		b_neg = Fraction(-1, 2)
		neg_denom = Fraction(1, -2)

		self.assertEqual(neg_denom + neg_denom, Fraction(-2, 2))
		self.assertEqual(neg_denom - neg_denom, Fraction(0, 2))
		self.assertEqual(neg_denom * neg_denom, Fraction(1, 4))
		
		self.assertEqual(a + neg_denom, Fraction(0, 2))
		self.assertEqual(a - neg_denom, Fraction(2, 2))
		self.assertEqual(a * neg_denom, Fraction(-1, 4))
		
		self.assertEqual(a + b, Fraction(2, 2))	
		self.assertEqual(a - b, Fraction(0, 2))
		self.assertEqual(a * b, Fraction(1, 4))
		
		self.assertEqual(a_neg + b_neg, Fraction(-2, 2))
		self.assertEqual(a_neg - b_neg, Fraction(0, 2))
		self.assertEqual(a_neg * b_neg, Fraction(1, 4))
	
	def test_eq(self):
		self.assertEqual(Fraction(1, 2), Fraction(1, 2))
		self.assertNotEqual(Fraction(1, 2), Fraction(1, 61))
		self.assertEqual(Fraction(1, 2), Fraction(1, 2).simplify())

	def test_lt(self):
		self.assertTrue(Fraction(1, 2) < Fraction(3, 4))
		self.assertEqual(sorted([Fraction(3, 4), Fraction(1, 2)]), 
						[Fraction(1, 2), Fraction(3, 4)])


	def test_simplyfy_produce_correct_result(self):
		self.assertEqual(Fraction(10, 20).simplify(), Fraction(1, 2))
		self.assertEqual(Fraction(4, 4).simplify(), Fraction(1, 1))
		self.assertEqual(Fraction(1, 3).simplify(), Fraction(1, 3))

	def test_is_simplyfied_produce_correct_result(self):
		self.assertFalse(Fraction(10, 20).is_simplified())
		self.assertTrue(Fraction(1, 2).is_simplified())
		self.assertTrue(Fraction(1, 2).simplify().is_simplified())

	def test_get_divider(self):
		self.assertEqual(Fraction.get_divider(2, 4), 2)
		self.assertEqual(Fraction.get_divider(3, 5), 1)

	def test_get_nok(self):
		self.assertEqual(Fraction.get_nok(12, 18), 36)
		self.assertEqual(Fraction.get_nok(6, 6), 6)
		self.assertEqual(Fraction.get_nok(7, 8), 56)
		self.assertEqual(Fraction.get_nok(6, 12), 12)


if __name__ == "__main__":
	unittest.main()			


	
