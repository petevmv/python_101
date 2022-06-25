import unittest
from iban_formater import iban_formater

class TestIbanFormater(unittest.TestCase):
	def test_iban_foramter(self):
		cases = [
		 	(
			 	"BG80BNBG96611020345678",
			 	"BG80 BNBG 9661 1020 3456 78"
		 	),
		 	(
			 	"BG80 BNBG 9661 1020 3456 78",
			 	"BG80 BNBG 9661 1020 3456 78"
			),
			( 	
				"BG14TTBB94005362446381",
				"BG14 TTBB 9400 5362 4463 81"
			),
			(
			 	"BG91UNCR70001864961754",
			 	"BG91 UNCR 7000 1864 9617 54"
		 	),
		 	(
			 	"B G1 4TTBB 9400 536 24 46 381",
			 	"BG14 TTBB 9400 5362 4463 81"
			)
		]
		
		for actual, expected in cases:
			with self.subTest(f'Expected: {expected}'):
				self.assertEqual(iban_formater(actual), expected)
			



if __name__ == '__main__':
	unittest.main()