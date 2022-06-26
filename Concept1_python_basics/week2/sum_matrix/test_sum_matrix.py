import unittest
from sum_matrix import sum_matrix

class TestSumMatrix(unittest.TestCase):
	def test_sum_matrix(self):
		
		test_eq = [ 
				  	([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 45),
				  	([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
				  	([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], 55)
				]
		for actual, expected in test_eq:
			with self.subTest('Expected: {expected}'):
				self.assertEqual(sum_matrix(actual), expected)

if __name__ == "__main__":
	unittest.main()
