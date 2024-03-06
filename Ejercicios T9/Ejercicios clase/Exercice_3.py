from math import sqrt

class Point:
    """
    Represents points in a bidimensional point.
    Each point have two coordinates (X, Y).
    """
    def __init__(self, coord_x = 0, coord_y = 0):
        self.x = coord_x
        self.y = coord_y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def get_quadrant(self):
        """
        Indicates which quadrant the point belongs to.
        The posibilities are: First , second, third or fourth quadrant, on the x/y axis, origin
        """
        if (self.x > 0 and self.y > 0):
            print("1st quadrant")
        elif (self.x < 0 and self.y > 0):
            print("2nd quadrant")
        elif (self.x < 0 and self.y < 0):
            print("3rd quadrant")
        elif (self.x > 0 and self.y < 0):
            print("4th quadrant")
        elif (self.x == 0 and self.y == 0):
            print("Origin")
        elif (self.x == 0 and self.y != 0):
            print("Y axis")
        elif (self.x != 0 and self.y == 0):
            print("X axis")
        else:
            print("Wrong values")

    def get_distance(self, anothePoint):
        """
        Calculates the distance between two points.
        
        AnotherPoint (Point): Point to calculate the distance from self.
        Output (float): Distance as a numeric value.
        """
        diff1 = anothePoint.x - self.x
        diif2 = anothePoint.y - self.y
        return sqrt(diff1**2 + diif2**2)


Punto1 = Point(3,2)
Punto2 = Point()
Punto3 = Point(1)
Punto4 = Point(coord_y=3)
Punto5 = Point(-3, -5)
Punto6 = Point(1,1)
Punto7 = Point(-2, 1)
Punto8 = Point(-3, -1)

print(Punto3.get_distance(Punto2))