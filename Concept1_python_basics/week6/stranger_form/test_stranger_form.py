import unittest
from stranger_form import *

class TestStrangerForm(unittest.TestCase):
	def test_outside_of_bounds(self):
		tests = [
				[[1, 2, 3], [4, 5, 6]],
				[[1, 2, 3, 4], [5, 6, 7, 8]],
				[[1,2],[3, 4]]
				]		
		with self.subTest('Testing outside_of_bounds'):
			for matrix in tests:
				self.assertFalse(outside_of_bounds((0, 1), matrix))
				self.assertFalse(outside_of_bounds((1, 1), matrix))
				self.assertFalse(outside_of_bounds((1, 0), matrix))
				self.assertFalse(outside_of_bounds((0, 0), matrix))


if __name__ == '__main__':
	unittest.main()