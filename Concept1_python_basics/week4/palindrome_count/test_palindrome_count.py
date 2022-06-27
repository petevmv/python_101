import unittest
from palindromes_count import palindromes_count

class TestPalindromeCount(unittest.TestCase):
	def test_palindrome_count(self):
		tests = [
				(10, 0),
				(20, 1),  # only 11
				(101, 10),  # 11, 22, 33, 44, 55, 66, 77, 88, 99, 101
				(92009, 1009),
				(99999, 1089)
				]

		for actual, expected in tests:
			with self.subTest(f"Expected: {expected}"):
				self.assertEqual(palindromes_count(actual), expected)


if __name__ == '__main__':
	unittest.main()