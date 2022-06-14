import unittest
from Group import group

class TestGroup(unittest.TestCase):
	def test_group(self):
		test_cases = [
						(group([1, 1, 1, 2, 3, 1, 1]), [[1, 1, 1], [2], [3], [1, 1]]),
						(group([]), []),
						(group([1]), [[1]]),
						(group([1, 1, 1, 1]), [[1, 1, 1, 1]])	
					]
		with self.subTest('Test Group behaivior'):
			for actual, expected in test_cases:
				self.assertEqual(actual, expected)
		
		with self.subTest('Type Error'):
			with self.assertRaises(TypeError):
				group(1,2,3,4,5)
			


if __name__ == '__main__':
	unittest.main()






