import unittest
from template import TemplateEngine

class TestTemplateEngine(unittest.TestCase):
	
	def test_render(self):
		test_text = "x {{ x}}, y {{y }}, z {{ z }}"
		test_obj = TemplateEngine(test_text)
		with self.assertRaises(TypeError):
			test_obj.render(x='jimmy')
		with self.assertRaises(TypeError):
			TemplateEngine('some_string').render(x='1')

		self.assertEqual(test_obj.render(x='1',y='2',z='3'), 'x 1, y 2, z 3')
		self.assertNotEqual(test_obj.render(x='1',y='2',z='3'), 'x 2, y 1, z 3')
		self.assertEqual(TemplateEngine('some_string').render(), 'some_string')
	

	def test_extract_variables(self):
		test_text = 'alabala {{ pesho}}, drun drun {{gosho }}, {{ moni }}'
		test_obj = TemplateEngine(test_text).extract_variables()
		self.assertEqual(test_obj, ['pesho', 'gosho', 'moni'])
		self.assertNotEqual(test_obj, [' pesho', 'gosho ', ' moni ']) # whitespaces
		self.assertEqual(TemplateEngine('').extract_variables(), [])
		self.assertEqual(TemplateEngine('some_string').extract_variables(), [])

if __name__ == '__main__':
	unittest.main()
