class Fraction:
    def __init__(self, numerator, denominator):
        """
        Construct a new Fraction.

        If denominator = 0, raise ValueError.
        """
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator == 0:
            raise ValueError
        else:
            self.value = self.numerator/self.denominator
        


    def __str__(self):
        """
        Returns the string representation of self.
        """
        if self.numerator == 0:
            return '0'

        return f"{self.numerator}{'/'}{self.denominator}"

    def __repr__(self):
        """
        Returns the REPL representation of self.
        """
        return f"{self.__class__.__name__}{self.numerator, self.denominator}"

    def __eq__(self, other):
        """
        Returns True/False, if self is equal to other.
        """
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        else:
            return False
          
    def __add__(self, other):
        """
        Returns new Fraction, that's the sum of self and other.
        """
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        else:
            nok = self.denominator * other.denominator
            self.new_numerator = (nok // self.denominator) * self.numerator 
            other.new_numerator = (nok // other.denominator) * other.numerator
            return Fraction(self.new_numerator + other.new_numerator, nok) 
                





    def __sub__(self, other):
        """
        Returns new Fraction, that's the substraction of self and other.
        """
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)
        else:
            nok = self.denominator * other.denominator
            self.new_numerator = (nok // self.denominator) * self.numerator 
            other.new_numerator = (nok // other.denominator) * other.numerator
            return Fraction(self.new_numerator - other.new_numerator, nok) 

    def __mul__(self, other):
        """
        Returns new Fraction, that's the product of self and other.
        """
        return Fraction(self.numerator * other.numerator, 
                        self.denominator * other.denominator)
        
        
    def simplify(self):
        """
        Returns new Fraction, that's the simplification of self
        """
        if self.numerator % self.denominator == 0 or self.denominator % self.numerator == 0:
            divider = min(self.numerator, self.denominator)
            return Fraction(self.numerator // divider, self.denominator // divider)
        

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
# print(a)
# print('repr', repr(a))
print(a == b)
c = a + b

# print(c.simplify())
# print(c)
# print(c.is_simplified()) 
# print(c.simplify().is_simplified())

d = a - b
print(d)  # 0
print(d.simplify())  # 0
print(d.is_simplified())  # True

