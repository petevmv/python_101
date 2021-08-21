class Interval:
    def __init__(self, start, end, start_opened=False, end_opened=False):
        # This is the constructor
        self.start = start
        self.end = end
        self.start_opened = start_opened
        self.end_opened = end_opened


       
        

    def is_inside(self, value):
        if self.start_opened == False and self.end_opened == False:
            return self.start <= value <= self.end
        
        elif self.start_opened == False and self.end_opened == True:
            return self.start <= value < self.end

        elif self.start_opened == True and self.end_opened == False:
            return self.start < value <= self.end

        elif self.start_opened == True and self.end_opened == True:
            return self.start < value < self.end

    def stringify(self):
        start_symbol_closed = '['
        end_symbol_closed = ']'
        start_symbol_open = '('
        end_symbol_open = ')'
        
        if self.start_opened == False and self.end_opened == False:
            print(f"{start_symbol_closed}{self.start}, {self.end}{end_symbol_closed}")
            return f"{start_symbol_closed}{self.start}, {self.end}{end_symbol_closed}"
        
        elif self.start_opened == False and self.end_opened == True:
            print(f'{start_symbol_closed}{self.start}, {self.end}{end_symbol_open}')
            return f'{start_symbol_closed}{self.start}, {self.end}{end_symbol_open}'
        
        elif self.start_opened == True and self.end_opened == False:
            print(f'{start_symbol_open}{self.start}, {self.end}{end_symbol_closed}')
            return f'{start_symbol_open}{self.start}, {self.end}{end_symbol_closed}'

        elif self.start_opened == True and self.end_opened == True:
            print(f'{start_symbol_open}{self.start}, {self.end}{end_symbol_open}')
            return f'{start_symbol_open}{self.start}, {self.end}{end_symbol_open}'


closed_interval = Interval(1, 10)

print(closed_interval.is_inside(1) is True)
print(closed_interval.is_inside(5) is True)
print(closed_interval.is_inside(10) is True)

print(closed_interval.stringify() == "[1, 10]") 


opened_interval = Interval(1, 10, start_opened=True, end_opened=True)

print(opened_interval.is_inside(1) is False)
print(opened_interval.is_inside(5) is True)
print(opened_interval.is_inside(10) is False)

print(opened_interval.stringify() == "(1, 10)")


half_opened_interval = Interval(1, 10, start_opened=False, end_opened=True)

print(half_opened_interval.is_inside(1) is True)
print(half_opened_interval.is_inside(5) is True)
print(half_opened_interval.is_inside(10) is False)

print(half_opened_interval.stringify() == "[1, 10)")



half_opened_interval = Interval(1, 10, start_opened=True, end_opened=False)

print(half_opened_interval.is_inside(1) is False)
print(half_opened_interval.is_inside(5) is True)
print(half_opened_interval.is_inside(10) is True)

print(half_opened_interval.stringify() == "(1, 10]")
