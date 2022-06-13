import unittest
from sum_matrix import sum_matrix

class TestSumMatrix(unittest.TestCase):
	def test_sum_matrix(self):
		
		test_eq = [ 
				  	([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 45),
				  	([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
				  	([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], 55)
				]
		with self.subTest('Testing sum_matrix behaiviour'):
			for actual, expected in test_eq:
				self.assertEqual(sum_matrix(actual), expected)
		with self.subTest('Type Error'):
			with self.assertRaises(TypeError):
				sum_matrix()
			with self.assertRaises(TypeError):
				sum_matrix([1,2,3],[1,2,3])
			with self.assertRaises(TypeError):
				sum_matrix("abc")


if __name__ == "__main__":
	unittest.main()
