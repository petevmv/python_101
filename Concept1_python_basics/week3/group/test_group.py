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
		for actual, expected in test_cases:
			with self.subTest(f'Expected: {expected}'):
				self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()






