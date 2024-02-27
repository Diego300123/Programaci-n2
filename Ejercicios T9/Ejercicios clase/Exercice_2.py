class Matrix:
    """
    Represents a mathematical matrix, i.e. a "box" of numbers disposed in rows and columns. 

    values: (List) a 2 dimensional list of numbers, organised in rows.
    """

    def __init__(self, values):
        self.values = values
    
    def __add__(self, otherMatrix):
        rows = len(self.values)
        for my_row in rows:
            for n in my_row:
            

    def __mul__(self, otherValue):
        pass

    def dimension(self):
        """
        Calulates a matrix dimension.

        Output: (int, int)
        """
        pass

    def transposed(self):
        """
        Calculates the transpose of a matrix.

        Output: (Matrix)
        """
        pass

    def save(self, fname):
        """
        Stores the matrix in text file.

        filename: (str) name of the file that will contain the data.
        """
        pass




