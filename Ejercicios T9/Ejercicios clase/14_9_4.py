class Fraction:
    """
    Represents a mathematical fraction X/Y.
    Includes operations to add and multiply other fractions

    dividend: (int) Dividend of the fraction.
    divisor: (int) Divisor of the fraction.
    """
    def __init__(self, dividend, divisor):
        if not isinstance(dividend, int):
            raise TypeError("Wrong Dividend: Only integers numbers are allowed")
        if not isinstance(divisor, int):
            raise TypeError("Wrong Divisor: Only integers numbers are allowed")
        self.dividend = dividend
        self.divisor = divisor
    
    def __str__(self):
        return f"{self.dividend}/{self.divisor}"
    
    def __add__(self, anotherFraction):
        if not isinstance(anotherFraction, Fraction):
            raise TypeError("Wrong type: Only Fraction objects are allowed")
        divisor = self.divisor * anotherFraction.divisor
        dividend = (self.dividend * anotherFraction.divisor) + (anotherFraction.dividend * self.divisor)
        result = Fraction(dividend, divisor)
        return result

    def __mul__(self, anotherFraction):
        if not isinstance(anotherFraction, Fraction):
            raise TypeError("Wrong type: Only Fraction objects are allowed")
        divisor = self.divisor * anotherFraction.divisor
        dividend = self.dividend * anotherFraction.dividend
        result = Fraction(dividend, divisor)
        return result   

    def simplify(self):
        """Reduce the dividend and the divisor of the fraction 
        so that they represent the same value.
        Both values are therefore modified.
        """
        greater_value = max(self.dividend, self.divisor)
        lower_value = min(self.dividend, self.divisor)
        while True:
            reaminder = greater_value % lower_value
            if reaminder == 0:
                gcd = lower_value
                break
            greater_value = lower_value
            lower_value = reaminder
        self.dividend = int(self.dividend // gcd)
        self.divisor = int(self.divisor // gcd)


myFraction = Fraction(3, 4)
otherFraction = Fraction(2, 4)

# print("Sum of the fractions is:", myFraction + otherFraction)
# print("Multiplication of the fractions is:", myFraction * otherFraction)

otherFraction.simplify()
print(otherFraction)