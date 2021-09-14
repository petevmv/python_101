import unittest
from template import TemplateEngine

class TestTemplateEngine(unittest.TestCase):
	
	def test_render(self):
		test_text = "x {{ x}}, y {{y }}, z {{ z }}"
		test_obj = TemplateEngine(test_text)
		
		same_multy_vars = "x {{x}}, y {{x}}, z {{x}}"
		same_vars_test_obj = TemplateEngine(same_multy_vars)
		
		random_whitespaces = 'py {{   x}}, md {{  x   }}, ka {{ x  }}, bl{{x      }}'
		random_ws_test_obj = TemplateEngine(random_whitespaces)

		with self.subTest('Type Error'):
			with self.assertRaises(TypeError):
				test_obj.render(x='jimmy')
			with self.assertRaises(TypeError):
				TemplateEngine('some_string').render(x=1)


		with self.subTest('render test method equal results'):
			self.assertEqual(test_obj.render(x='1',y='2',z='3'), 'x 1, y 2, z 3')
			self.assertEqual(test_obj.render(x='2',y='3',z='1'), 'x 2, y 3, z 1')
			self.assertEqual(test_obj.render(x='3',y='1',z='2'), 'x 3, y 1, z 2')
			self.assertEqual(TemplateEngine('some_string').render(), 'some_string')
			self.assertEqual(same_vars_test_obj.render(x='1',y='2',z='3'), 'x 1, y 1, z 1')
			self.assertEqual(random_ws_test_obj.render(
														x='~',
														y='3',
														z='5',
														g='k'),
														'py ~, md ~, ka ~, bl~')
		
		with self.subTest('render test method NOT equal results'):
			self.assertNotEqual(test_obj.render(x='1',y='2',z='3'), 'x 2, y 1, z 3')
			self.assertNotEqual(test_obj.render(x='1',y='2',z='3'), 'x1, y2, z3')
			self.assertNotEqual(test_obj.render(x='1',y='2',z='3'), '')
			self.assertNotEqual(test_obj.render(x='1',y='2',z='3'), test_text)
			self.assertNotEqual(random_ws_test_obj.render(
														x='~',
														y='3',
														z='5',
														g='k'),
														'py ~, md 3, ka 5, blk')

	def test_extract_variables(self):
		test_text = 'alabala {{ pesho}}, drun drun {{gosho }}, {{ moni }}'
		test_obj = TemplateEngine(test_text).extract_variables()
		same_multy_vars = 'alabala {{ pesho}}, drun drun {{pesho }}, {{ pesho }}'
		same_multy_vars_test_obj = TemplateEngine(same_multy_vars).extract_variables()
		with self.subTest('extract_variables method equal results'):
			self.assertEqual(test_obj, ['pesho', 'gosho', 'moni'])
			self.assertEqual(TemplateEngine('').extract_variables(), [])
			self.assertEqual(TemplateEngine('some_string').extract_variables(), [])
			self.assertEqual(same_multy_vars_test_obj, ['pesho']*3)

		with self.subTest('extract_variables method NOT equal results'):
			self.assertNotEqual(test_obj, [' pesho', 'gosho ', ' moni ']) # whitespaces
			self.assertNotEqual(test_obj, ['gosho', 'pesho', 'moni'])
			self.assertNotEqual(test_obj, ['moni', 'gosho', 'pesho'])
			self.assertNotEqual(test_obj, [])

if __name__ == '__main__':
	unittest.main()
