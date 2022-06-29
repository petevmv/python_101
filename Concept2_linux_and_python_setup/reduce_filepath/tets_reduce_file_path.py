import unittest
from reduce_file_path import *

class TestReduceFilePath(unittest.TestCase):
	def test_reduce_file_path(self):
		cases = [
			(
				"/", 
				"/"
			),
			(
				"/srv/../", 
				"/"
			),
			(
				"/srv/www/htdocs/wtf/", 
				"/srv/www/htdocs/wtf"
			),
			(
				"/srv/www/htdocs/wtf",
				"/srv/www/htdocs/wtf"
			),
			(
				"/srv/./././././", 
				"/srv"
			),
			(
				"/etc//wtf/", 
				"/etc/wtf"
			),
			(
				"/etc/../etc/../etc/../",
				 "/"
			),
			(
				"//////////////", 
				"/"
			),
			(
				"/../",
				 "/"
			),
			(
				'/home//user/courses/./Programming101-Python/week01/../',
				'/home/user/courses/Programming101-Python'
			)
		]

		for actual, expected in cases:
			with self.subTest(f'Expected :{expected}'):
				self.assertEqual(reduce_file_path(actual), expected)

if __name__ == '__main__':
	unittest.main()