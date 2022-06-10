import unittest
from iban_formater import iban_formater

class TestIbanFormater(unittest.TestCase):
	def test_iban_foramter(self):
		with self.subTest('Attribute Error'):
			with self.assertRaises(AttributeError):
				iban_formater([]) 
			with self.assertRaises(AttributeError):
				iban_formater({})
			with self.assertRaises(AttributeError):
				iban_formater(2)
			with self.assertRaises(AttributeError):
				iban_formater(('abc','def'))
		with self.assertRaises(TypeError):
			iban_formater()


		test_input1 = "BG80BNBG96611020345678"
		test_input_whitespaces = "BG80 BNBG 9661 1020 3456 78"
		test_input2 = "BG14TTBB94005362446381"
		test_input3 = "BG91UNCR70001864961754"
		test_random_whitespace = "B G1 4TTBB 9400 536 24 46 381"
		with self.subTest('Testing the iban_formater function behave as expected'):
			self.assertEqual(iban_formater(test_input1), "BG80 BNBG 9661 1020 3456 78")
			self.assertEqual(iban_formater(test_input_whitespaces), "BG80 BNBG 9661 1020 3456 78")
			self.assertEqual(iban_formater(test_input2), "BG14 TTBB 9400 5362 4463 81")
			self.assertEqual(iban_formater(test_input3), "BG91 UNCR 7000 1864 9617 54")
			self.assertEqual(iban_formater(test_random_whitespace), "BG14 TTBB 9400 5362 4463 81")
			self.assertNotEqual(iban_formater(test_input1), "BG14 TTBB 9400 5362 4463 81")
			self.assertNotEqual(iban_formater(test_input1), test_input1)
			self.assertNotEqual(iban_formater(test_random_whitespace), "B G1 4TTBB 9400 536 24 46 381")




if __name__ == '__main__':
	unittest.main()