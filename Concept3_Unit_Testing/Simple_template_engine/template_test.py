import unittest
from template import TemplateEngine

class TestTemplateEngine(unittest.TestCase):
	
	def test_render(self):
		test_text = "x {{ x}}, y {{y }}, z {{ z }}"
		test_obj = TemplateEngine(test_text)
		with self.subTest('Type Error'):
			with self.assertRaises(TypeError):
				test_obj.render(x='jimmy')
			with self.assertRaises(TypeError):
				TemplateEngine('some_string').render(x='1')
			with self.assertRaises(TypeError):
				TemplateEngine('some_string').render(x=1)


		with self.subTest('render test method equal results'):
			self.assertEqual(test_obj.render(x='1',y='2',z='3'), 'x 1, y 2, z 3')
			self.assertEqual(test_obj.render(x='2',y='3',z='1'), 'x 2, y 3, z 1')
			self.assertEqual(test_obj.render(x='3',y='1',z='2'), 'x 3, y 1, z 2')
			self.assertEqual(TemplateEngine('some_string').render(), 'some_string')

		
		with self.subTest('render test method NOT equal results'):
			self.assertNotEqual(test_obj.render(x='1',y='2',z='3'), 'x 2, y 1, z 3')
			self.assertNotEqual(test_obj.render(x='1',y='2',z='3'), 'x1, y2, z3')
			self.assertNotEqual(test_obj.render(x='1',y='2',z='3'), '')
			self.assertNotEqual(test_obj.render(x='1',y='2',z='3'), test_text)

	def test_extract_variables(self):
		test_text = 'alabala {{ pesho}}, drun drun {{gosho }}, {{ moni }}'
		test_obj = TemplateEngine(test_text).extract_variables()
		
		with self.subTest('extract_variables method equal results'):
			self.assertEqual(test_obj, ['pesho', 'gosho', 'moni'])
			self.assertEqual(TemplateEngine('').extract_variables(), [])
			self.assertEqual(TemplateEngine('some_string').extract_variables(), [])
		
		with self.subTest('extract_variables method NOT equal results'):
			self.assertNotEqual(test_obj, [' pesho', 'gosho ', ' moni ']) # whitespaces
			self.assertNotEqual(test_obj, ['gosho', 'pesho', 'moni'])
			self.assertNotEqual(test_obj, ['moni', 'gosho', 'pesho'])
			self.assertNotEqual(test_obj, [])

if __name__ == '__main__':
	unittest.main()
