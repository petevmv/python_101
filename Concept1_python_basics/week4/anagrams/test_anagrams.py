import unittest
from anagram import anagrams

class TestAnagram(unittest.TestCase):
	def test_anagrams(self):
		tests_true = [
				(
					"listen",
					"silent"
				),
				(
					"LISTEN",
					"silent"
				),
				(
					"New York Times",
					"monkeys write"
				)
		]


		tests_false = [
				(
					"snake",
					"sssnakee"
				),
				(
					"python",
					"ruby"
				)
		]

		for word1, word2 in tests_true:
			with self.subTest(f'{word1} and {word2} should be anagrams'):
				self.assertTrue(anagrams(word1, word2))
		
		for word1, word2 in tests_false:
			with self.subTest(f'{word1} and {word2} should NOT be anagrams'):
					self.assertFalse(anagrams(word1, word2))

		
if __name__ == '__main__':
	unittest.main()