class Interval:
	def __init__(self, start, end, start_opened=False, end_opened=False):
		# This is the constructor
		self.start = start
		self.end = end
		self.start_opened = start_opened
		self.end_opened = end_opened


	def is_inside(self, value):
		
		if not self.start_opened and not self.end_opened:
			return self.start <= value <= self.end

		elif not self.start_opened and self.end_opened:
			return self.start <= value < self.end

		elif self.start_opened and not self.end_opened:
			return self.start < value <= self.end

		elif self.start_opened and self.end_opened:
			return self.start < value < self.end


	def stringify(self):
		start_symbol_closed = '['
		end_symbol_closed = ']'
		start_symbol_open = '('
		end_symbol_open = ')'

		if not self.start_opened and not self.end_opened:
			return "{}{}, {}{}".format(start_symbol_closed, self.start, self.end, end_symbol_closed)

		elif not self.start_opened and self.end_opened:
			return "{}{}, {}{}".format(start_symbol_closed, self.start, self.end, end_symbol_open)

		elif self.start_opened and not self.end_opened:
			return "{}{}, {}{}".format(start_symbol_open,self.start, self.end, end_symbol_closed)

		elif self.start_opened and self.end_opened:
			return "{}{}, {}{}".format(start_symbol_open, self.start, self.end, end_symbol_open)



closed_interval = Interval(1, 10)

print(closed_interval.is_inside(1) is True)
print(closed_interval.is_inside(5) is True)
print(closed_interval.is_inside(10) is True)

print(closed_interval.stringify() == '[1, 10]')
















