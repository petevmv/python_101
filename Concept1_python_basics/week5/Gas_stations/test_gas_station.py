import unittest
from Gas_Station import gas_stations

class TestGasStation(unittest.TestCase):
	def test_gas_stations(self):
		test_cases = [
			(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]), [80, 140, 220, 290]),
			(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]), [70, 140, 210, 280, 350]),
			(gas_stations(100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150]), [40, 80]),
			(gas_stations(100, 50, [10, 90]), []),
			(gas_stations(150, 40, [30, 40, 80, 90, 130]), [])
		]

		for actual, expected in test_cases:
			with self.subTest(f"Expected : {expected}"):	
				self.assertEqual(actual, expected)


if __name__ == '__main__':
	unittest.main()