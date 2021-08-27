import unittest
from fraction import Fraction

class FractionTest(unittest.TestCase):

	def test_string_repr_and_zero(self):
		test = Fraction(1, 2)
		zero = Fraction(0, 1)

		self.assertEqual(test.__str__(), str(test))
		self.assertEqual(test.__repr__(), repr(test))
		
		self.assertEqual(zero.__str__(), str(zero))
		self.assertEqual(zero.__repr__(), repr(zero))




	def test_simplyfy_produce_correct_result(self):
		test1 = Fraction(10, 20)
		test2 = Fraction(4, 4)

		self.assertEqual(test1.simplify(), Fraction(1, 2))
		self.assertEqual(test2.simplify(), Fraction(1, 1))

	def test_is_simplyfied_produce_correct_result(self):
		test1 = Fraction(10, 20)
		test2 = Fraction(1 , 2)
		
		self.assertFalse(test1.is_simplified())
		self.assertTrue(test2.is_simplified())
		self.assertTrue(test1.simplify().is_simplified())



if __name__ == "__main__":
	unittest.main()			


	
