import unittest
from word_counter import *

class TestWordCounter(unittest.TestCase):
	def test_word_counter(self):
		cases = [
		(
			"actually",
			[
		    ["i", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z", "o", "y", "m"],
		    ["e", "v", "n", "h", "t", "r", "x", "e", "k", "y", "d", "a", "i", "l", "c"],
		    ["i", "a", "c", "t", "u", "a", "l", "l", "y", "m", "c", "x", "r", "l", "e"],
		    ["m", "v", "c", "n", "p", "u", "a", "m", "n", "t", "l", "u", "e", "a", "a"],
		    ["q", "r", "i", "t", "w", "e", "a", "q", "u", "p", "r", "x", "t", "u", "z"],
		    ["p", "e", "a", "c", "t", "u", "a", "l", "l", "y", "w", "p", "y", "t", "m"],
		    ["o", "y", "h", "t", "r", "e", "l", "u", "f", "p", "q", "n", "z", "c", "s"],
		    ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e", "q", "a", "r"]
			],
			4
		),
		(
			"ivan",
			[
		    ["i", "v", "a", "n"],
		    ["e", "v", "n", "h"],
		    ["i", "n", "a", "v"],
		    ["m", "v", "v", "n"],
		    ["q", "r", "i", "t"]
			],
			3
		),
		(
 			"madam",
		 	[
		    ["z", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z"],
		    ["e", "v", "m", "h", "t", "r", "x", "e", "k", "y", "m", "a"],
		    ["i", "a", "c", "a", "u", "a", "l", "l", "y", "a", "c", "x"],
		    ["m", "v", "c", "n", "d", "u", "a", "m", "d", "t", "l", "u"],
		    ["q", "t", "i", "t", "w", "a", "a", "a", "u", "p", "r", "x"],
		    ["p", "e", "m", "a", "d", "a", "m", "l", "l", "y", "w", "p"],
		    ["o", "y", "h", "t", "e", "e", "l", "u", "f", "p", "q", "n"],
		    ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e"]
			],
			3
		),
		(
	 		"python",
		 	[
		    ["r", "u", "b", "y"],
		    ["r", "u", "b", "y"],
		    ["r", "u", "b", "y"],
		    ["r", "u", "b", "y"],
			],
			0
		)
		]

		for word, matrix, expected in cases:
			with self.subTest(f'Expected: {expected}'):
				self.assertEqual(word_counter(matrix, word), expected)

if __name__ == '__main__':
	unittest.main()