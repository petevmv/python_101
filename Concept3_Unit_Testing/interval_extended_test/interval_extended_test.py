from unittest import TestCase
from interval import Interval

class IntervalTest(TestCase):
	def test_is_inside_produce_correct_results(self):
		closed_interval = Interval(1, 10)
		open_interval = Interval(1, 10, start_opened=True, end_opened=True)
		half_closed_interval_start = Interval(1, 10, start_opened=False, end_opened=True)
		half_closed_interval_end = Interval(1, 10, start_opened=True, end_opened=False)

		self.assertTrue(closed_interval.is_inside(1))
		self.assertTrue(closed_interval.is_inside(5))
		self.assertTrue(closed_interval.is_inside(10))

		self.assertFalse(open_interval.is_inside(1))
		self.assertTrue(open_interval.is_inside(5))
		self.assertFalse(open_interval.is_inside(10))

		self.assertTrue(half_closed_interval_start.is_inside(1))
		self.assertTrue(half_closed_interval_start.is_inside(5))
		self.assertFalse(half_closed_interval_start.is_inside(10))

		self.assertFalse(half_closed_interval_end.is_inside(1))
		self.assertTrue(half_closed_interval_end.is_inside(5))
		self.assertTrue(half_closed_interval_end.is_inside(10))


	def test_stringify_produce_correct_result(self):
		closed_interval = Interval(1, 10)
		open_interval = Interval(1, 10, start_opened=True, end_opened=True)
		half_closed_interval_start = Interval(1, 10, start_opened=False, end_opened=True)
		half_closed_interval_end = Interval(1, 10, start_opened=True, end_opened=False)

		expected = {
			closed_interval.stringify() : '[1, 10]',
			open_interval.stringify() : '(1, 10)', 
			half_closed_interval_start.stringify(): '[1, 10)',
			half_closed_interval_end.stringify(): '(1, 10]'
		}

		for k, v in expected.items():
			self.assertEqual(v, k)







