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
		
		for actual, expected in tests:
			with self.subTest(f"Expected: {expected}"):
				self.assertEqual(actual, expected)


if __name__ == "__main__":
	unittest.main()

