import unittest
from nan_expand import nan_expand

class TestNaNExpand(unittest.TestCase):
	def test_nan_expand(self):
		tests = [
				(nan_expand(0) , ""),
				(nan_expand(1) , "Not a NaN"),
				(nan_expand(2) , "Not a Not a NaN"),
				(nan_expand(3) , "Not a Not a Not a NaN")
				]
		with self.subTest("Test NaN_expand behaive as expected"):
			for actual, expected in tests:
				self.assertEqual(actual, expected)

		with self.subTest('Type Error'):
			with self.assertRaises(TypeError):
				nan_expand('abc')
			with self.assertRaises(TypeError):
				nan_expand([])
			with self.assertRaises(TypeError):
				nan_expand({})
			with self.assertRaises(TypeError):
				nan_expand((1,2))
			with self.assertRaises(TypeError):
				nan_expand('123')
			with self.assertRaises(TypeError):
				nan_expand(0.5)

if __name__ == "__main__":
	unittest.main()

