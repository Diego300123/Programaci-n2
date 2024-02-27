from math import radians, tan
from turtle import Turtle, title, Screen

class RegularPolygon():
    """Represents regular polygons of a given number of sides,
    and with a side length.

    Attributes: numberOfSides (int), sideLength (float), colour (str)
    Methods: getPerimeter (), getArea ()
    """
    pass

    def __init__(self, numberOfSides, length, colour): #Init es el método constructor.
        self.numberOfSides = numberOfSides
        self.length = length
        self.colour = colour
    
    def __str__(self): #Devuelve una descripción del objeto
        return f"""Regular polygon of {self.numberOfSides} sides, \
        with side length {self.length} and colour {self.colour}"""

    def __eq__(self, anotherPolygon): #Vamos a decir que dos polígonos son iguales si, en este caso, tienen el nº de lados y la longitud iguales.
        return self.numberOfSides == anotherPolygon.numberOfSides \
        and self.length == anotherPolygon.length

    def __lt__(self, anotherPolygon): #Vamos a decir que un polígono es menor que otro si su área es más pequeña.
        return self.get_area() < anotherPolygon.get_area()

    def __ge__(self, anotherPolygon): #Vamos a decir que un polígono es mayor o igual que otro.
        return self.get_area() >= anotherPolygon.get_area()

    def __gt__(self, anotherPolygon): #Vamos a decir que un polígono es mayor.
        return self.get_area() > anotherPolygon.get_area()
    
    def __le__(self, anotherPolygon): #Vamos a decir que un polígono es menor o igual que otro.
        return self.get_area() <= anotherPolygon.get_area()

    def get_apothema(self):
        """Calulates the value of the apothema of the polygon

        Output: (float) Value of the apothema
        """
        angle = 360 / self.numberOfSides # grados
        angle = radians(angle)      # radiales
        return self.length / (2 * tan(angle/2))
    
    def get_perimeter(self):
        """Calculates the perimeter of a regular polygon.

        Output: (float)  Value of the perimeter
        """
        return self.numberOfSides * self.length

    def get_area(self):
        """Calculates the area of a regular polygon.
        
        Output: (float) Value of the area
        """
        return (self.get_perimeter() * self.apothema()) / 2

    def draw_poly(self):
        """
        Draws a polygon object using turtle module.
        """
        angle = 360 / self.numberOfSides
        sides = self.numberOfSides
        myPoly = Turtle()
        myPoly.speed(2)
        myPoly.color(self.colour)
        myScreen = Screen()
        myDict = {
            3:"Triangle",
            4:"Square",
            5:"Pentagon",
            6:"Hexagon",
            7:"Heptagon",
            8:"Octogon",
            9:"Eneagono",
            10:"Decagono"
        }
        if sides > 10:
            myScreen.title(f"Polygon of {sides} number of sides.")
        else:
            for key in myDict:
                if key == sides:
                    myScreen.title(myDict[key])
        for i in range(sides):
            myPoly.forward(self.length)
            myPoly.left(angle)

# print(RegularPolygon.__doc__)

mySquare = RegularPolygon(4, 100, "Green")
mySquare2 = RegularPolygon(4, 10, "Red")
mySquare3 = RegularPolygon(4, 3, "White")
myTriangle = RegularPolygon(3, 40, "Black")
bigPoly = RegularPolygon(17, 40, "Black")

# print("The perimeter of the square is:", mySquare.get_perimeter())
# print("The apothema of the square is:", mySquare.get_apothema())
# print("The area of the square is:", mySquare.get_area())

# print(mySquare == mySquare2)

# print("The perimeter of the triangle is:", myTriangle.get_perimeter())
# print("The apothema of the triangle is:", myTriangle.get_apothema())
# print("The area of the triangle is:", myTriangle.get_area())

myTriangle.draw_poly()