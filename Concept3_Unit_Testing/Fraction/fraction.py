class Fraction:
    def __init__(self, numerator, denominator):
        """
        Construct a new Fraction.

        If denominator = 0, raise ValueError.
        """
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator < 0:
            self.numerator = 0 - self.numerator
            self.denominator = abs(self.denominator)
        if self.denominator == 0:
            raise ValueError('Cannot divide by zero')
        
        # elif type(self.numerator) != int or type(self.denominator) != int:
        #     raise TypeError

        else:
            self.value = self.numerator/self.denominator
        

    def __str__(self):
        """
        Returns the string representation of self.
        """
        if self.numerator == 0:
            return '0'

        return f"{self.numerator}/{self.denominator}"


    def __repr__(self):
        """
        Returns the REPL representation of self.
        """
        if self.numerator == 0:
            return '0'
        
        return f"{self.__class__.__name__}{self.numerator, self.denominator}"


    def __eq__(self, other):    
        """
        Returns True/False, if self is equal to other.
        """
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        
        return False
          

    def __add__(self, other):
        """
        Returns new Fraction, that's the sum of self and other.
        """
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        
        nok = Fraction.get_nok(abs(self.denominator), abs(other.denominator))
        new_numerator = (nok // self.denominator) * self.numerator 
        other_new_numerator = (nok // other.denominator) * other.numerator
        return Fraction(new_numerator + other_new_numerator, nok) 
            

    def __sub__(self, other):
        """
        Returns new Fraction, that's the substraction of self and other.
        """
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)
        
        nok = Fraction.get_nok(abs(self.denominator), abs(other.denominator))
        new_numerator = (nok // self.denominator) * self.numerator 
        other_new_numerator = (nok // other.denominator) * other.numerator
        return Fraction(new_numerator - other_new_numerator, nok) 

    
    def __mul__(self, other):
        """
        Returns new Fraction, that's the product of self and other.
        """
        return Fraction(self.numerator * other.numerator, 
                        self.denominator * other.denominator)


    def __lt__(self, other):
        return self.value < other.value 

    
    def get_nok(a, b):
        if a % b == 0 or b % a == 0:
            return max(a, b)

        counter = max(a, b) + 1
        while (counter % max(a, b) != 0):
            counter += 1
        
        if counter % min(a, b) == 0:
            return counter
        else:
            return a * b

    
    def get_divider(a, b):
        num_list = []
        for num in range(2, min(abs(a), abs(b)) + 1):
            if a % num == 0 and b % num == 0:
                num_list.append(num)
        if num_list:
            return max(num_list)
        else:
            return 1


    def simplify(self):
        """
        Returns new Fraction, that's the simplification of self
        """
        divider = Fraction.get_divider(self.numerator, self.denominator)
        return Fraction(self.numerator // divider, self.denominator// divider)


    def is_simplified(self):
        """
        Returns True/False, if self cannot be simplified further
        """
        result = Fraction(self.numerator, self.denominator).simplify()
        if result == Fraction(self.numerator, self.denominator):
            return True
        else:
            return False

a = Fraction(1, 2)
b = Fraction(1, 2)

print(a == b)  # True

print(a)  # 1/2
print(b)  # 1/2

c = a + b

print(a)  # 1/2
print(b)  # 1/2
print(c)  # 2/2

print(c.simplify())  # 1/1
print(c)  # 2/2

print(c.is_simplified())  # False
print(c.simplify().is_simplified())  # True

d = a - b
print(d)  # 0
print(d.simplify())  # 0
print(d.is_simplified())  # True

e = a * b
print(e)  # 1/4
print(e.simplify())  # 1/4
print(e.is_simplified())  # True
print(sorted([Fraction(5,6),Fraction(3,4), Fraction(1,2)]))

print(Fraction(1, -2))