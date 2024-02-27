class Polynomial:
    """
    Represents a mathematical expression for a polynomial, along
    with its operations

    coefs: (list) Contains the coefficients of a polynomialas integers numbers.
    Each value matches the exponent of x (the index of each value).
    e.g. [-2, 0, 3] -> 3*x^2 - 2
    """
    def __init__(self, coefs):
        self.coefs = coefs

    def __str__(self):
        result = ""
        index = 0
        for coef in self.coefs:
            if coef == 0:
                index += 1
                continue
            if index == 0:
                x_term = ''
            elif index == 1:
                x_term = '·x'
            else:
                x_term = f'·x^{index}'
            symbol = ''
            if coef > 0:
                symbol = '+'
            result = f'{symbol}{coef}{x_term} ' + result
            index += 1
        result = result.strip()
        if result[0] == '+':
            result = result[1:]
        return result
    
    def __add__(self, otherPolynomial):
        # Hay que hacer una copia para no cambiar el original
        myCoefs = self.coefs.copy()
        coefs2 = otherPolynomial.coefs.copy()

        # Pad with zeros on the right in the lower-degree polynomial
        while len(myCoefs) < len(coefs2):
            myCoefs.append(0)
        while len(coefs2) < len(myCoefs):
            coefs2.append(0)

        # Add coefficients:
        result = []
        i = 0
        for coef in myCoefs:
            result.append(coef + coefs2[i])
            i += 1
        return Polynomial(result)

    def __mul__(self, otherPolynomial):
        result = []
        degree = self.degree() + otherPolynomial.degree()
        for i in range(degree + 1):
            result.append(0)
        for i in range(len(self.coefs)):
            for j in range(len(otherPolynomial.coefs)):
                index = i + j
                result[index] += self.coefs[i] * otherPolynomial.coefs[j]
        return Polynomial(result)


    def degree(self):
        """
        Gets the degree of the polynomial.

        Output: (int) degree
        """
        return len(self.coefs) - 1

myPoly1 = Polynomial([-2, 0, 3, 2])
myPoly2 = Polynomial([-3, 1, -2])

print(myPoly1 * myPoly2)
