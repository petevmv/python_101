import unittest
from exception_silencer import ExceptionSilencer

class ExceptionSilencerTests(unittest.TestCase):

	def test_correct_exception_silencer(self):
		with ExceptionSilencer(ValueError):
			int('some string')

		with ExceptionSilencer(IndexError):
			'some string'[100]
		
		with ExceptionSilencer(ModuleNotFoundError):
			import python101.forever

		with ExceptionSilencer(NameError):
			value

		with ExceptionSilencer(KeyError):
			{"key":"value"}['yek']

	def test_incorect_exception_silencer(self):
		with self.assertRaises(ValueError):
			with ExceptionSilencer(KeyError):
				int('some string')

		with self.assertRaises(IndexError):
			with ExceptionSilencer(ValueError):
				'some string'[100] 
				

		with self.assertRaises(ModuleNotFoundError):
			with ExceptionSilencer(ValueError):
				import python101.forever
		

		with self.assertRaises(NameError):
			with ExceptionSilencer(ImportError):
				value

		with self.assertRaises(KeyError):
			with ExceptionSilencer(IndexError):
				{"key":"value"}['yek']


if __name__ == "__main__":
	unittest.main()


		
		
		
