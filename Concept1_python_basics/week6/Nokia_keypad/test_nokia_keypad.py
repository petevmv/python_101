import unittest
from Nokia_keypad import *

class TestNokiaKeypad(unittest.TestCase):
	def test_numbers_to_message(self):
		tests_for_numbers_to_msg = [
		(
			[0,0,0,0],
			'    '
		),
		(	
			[2, -1, 2, 2, -1, 2, 2, 2],
			'abc'
		),
		(
			[2, 2, 2, 2, 2, 2, 2],
			'a'
		),
		(
			[2, 3, 4, 5, 6, 7, 8, 9],
			'adgjmptw'
		),
		(
			[1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2],
			'Ivo e Panda'
		)
		]	

		for pressed_input, expected in tests_for_numbers_to_msg:
			self.assertEqual(numbers_to_message(pressed_input), expected)



	def test_message_to_number(self):
		test_for_msg_to_numbers = [	
		(
			'abc',
			[2,-1,2,2,-1,2,2,2]
		),
		(
			'aabbcc',
			[2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2]
		),
		(
			'Ivo e Panda',
			[1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]
		),
		(
			'a',
			[2]
		)
		]

		for message, expected in test_for_msg_to_numbers:
			self.assertEqual(message_to_numbers(message), expected)



if __name__ == '__main__':
	unittest.main()


