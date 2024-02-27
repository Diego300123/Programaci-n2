class Vector:
    """
    Represents a list of elements [x, y, z] as coordinates.

    x: (int) A coordinate.
    y: (int) Other coordinate.
    z: (int) Other coordinate.
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"
    
    def __add__(self, otherVector):
        try:
            new_x = self.x + otherVector.x
            new_y = self.y + otherVector.y
            new_z = self.z + otherVector.z
            result = Vector(new_x, new_y, new_z)
        except ...:
            result = "Vectors must have 3 parameters, [x, y, z]" 
        return result

Coord1 = Vector(1, 2, 3)
Coord2 = Vector(4, 1)

print("The sum of the two coordinates is:", Coord1 + Coord2)