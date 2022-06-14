import unittest
from anagram import anagrams

class TestAnagram(unittest.TestCase):
	def test_anagrams(self):
		tests_true = [
					("listen", "silent"),
					("LISTEN", "silent"),
					("New York Times", "monkeys write")
					]


		tests_false = [
					("snake", "sssnakee"),
					("python", "ruby")
					]
		
		with self.subTest('Test anagram function behaive as expected'):
			for word1, word2 in tests_true:
				self.assertTrue(anagrams(word1, word2))
			for word1, word2 in tests_false:
				self.assertFalse(anagrams(word1, word2))

		with self.subTest('Attribute Error'):
			with self.assertRaises(AttributeError):
				anagrams(1,2)
			with self.assertRaises(AttributeError):
				anagrams([],1)
		with self.subTest('Type Error'):		
			with self.assertRaises(TypeError):
				anagrams('alabala')

if __name__ == '__main__':
	unittest.main()