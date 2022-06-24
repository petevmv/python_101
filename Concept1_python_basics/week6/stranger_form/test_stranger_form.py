import unittest
from stranger_form import *

class TestStrangerForm(unittest.TestCase):
	def test_outside_of_bounds(self):
		tests = [
				[[1, 2, 3], [4, 5, 6]],
				[[1, 2, 3, 4], [5, 6, 7, 8]],
				[[1, 2], [3, 4]]
				]		
		
		with self.subTest('Testing outside_of_bounds'):
			for matrix in tests:
				self.assertFalse(outside_of_bounds((0, 1), matrix))
				self.assertFalse(outside_of_bounds((1, 1), matrix))
				self.assertFalse(outside_of_bounds((1, 0), matrix))
				self.assertFalse(outside_of_bounds((0, 0), matrix))
				self.assertTrue(outside_of_bounds((0, 4), matrix))
				self.assertTrue(outside_of_bounds((2, 0), matrix))
				self.assertTrue(outside_of_bounds((2, 4), matrix))

	def test_build_friends_relative_position(self):
		test = [(
				["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"],
				{'A':(0, 0), 
				 'B':(-1, 0), 
				 'C':(-2, 0), 
				 'D':(-2, 1),
				 'E':(-3, 1), 
				 "F":(0, 1),
				 "G":(-3,0)}
			),
			(
				['A', 'BBA', "FLA", "CBB",'DLC', 'EBD','GRE'],
				{'A': (0, 0),
				 'B': (1, 0),
				 'C': (2, 0),
				 'D': (2, -1),
				 'E': (3, -1),
				 'F': (0, -1),
				 'G': (3, 0)}
			)
		]
		

		with self.subTest('Testing build_friends_relative_position()'):
			for configuration, expected in test:
				self.assertEqual(build_friends_relative_position(configuration), expected)

	
	def test_in_cinema(self):
		points_in = [(0, 0),
				 	 (0, 1),
				 	 (0, 3),
					 (0, 4),
					 (0, 5),
					 (0, 7),
					 (4, 0),
					 (9, 3)]
	 	
		
		points_out = [(0, 2),
 					  (0, 6),
					  (0, 8),
					  (0, 9),
					  (2, 0),
					  (2, 9),
					  (2, 11),
					  (3, 10),
					  (9, 0)]

		
		cinema_layout = [
						'..*...*.**',
						'.....**...',
						'*.*...*..*',
						'.**....*.*',
						'...*..*.*.',
						'.***...*..',
						'*......*.*',
						'.....**..*',
						'..*.*.*..*',
						'***.*.**..'
						]
    	

		with self.subTest('Testing in_cinema'):
			for point in points_in:
				self.assertTrue(in_cinema(point, cinema_layout))
			for point in points_out:
				self.assertFalse(in_cinema(point, cinema_layout))


	def test_add_point(self):
		tests = [((0, 0), (0, 1), (0, 1)),
				((1, 1), (0, 0), (1, 1)),
				((1, 1), (1, 1), (2, 2)),
				((1, 5), (3, 8), (4, 13)),
				((-1, 3), (1, -3), (0, 0)),
				((-1, -3), (-1, -3),(-2, -6))]
		

		with self.subTest('Testing add_point'):
			for point1, point2, expected in tests:
				self.assertEqual(add_point(point1, point2), expected)

if __name__ == '__main__':
	unittest.main()