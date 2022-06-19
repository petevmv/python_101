import unittest
from matrix_bomber import matrix_bombing_plan

class TestMatrixBomber(unittest.TestCase):
	def test_matrix_bomber(self):
		test_cases  = {(0, 0): 42,
					   (0, 1): 36,
					   (0, 2): 37,
					   (1, 0): 30,
					   (1, 1): 15,
					   (1, 2): 23,
					   (2, 0): 29,
					   (2, 1): 15,
					   (2, 2): 26}
					 
	with self.subTest("Testing matrix_bomber function behaiviour"):
		self.assertEqual(matrix_bombing_plan([[1,2,3], [4,5,6], [7,8,9]]), test_cases)

	with self.subTest('Value Error'):
		with self.assertRaises(ValueError):
			matrix_bombing_plan([1,2,3])
		with self.assertRaises(ValueError):
			matrix_bombing_plan([1,2,3], [1,2,3])
		with self.assertRaises(ValueError):
			matrix_bombing_plan('abc')

if __name__ == '__main__':
	unittest.main()