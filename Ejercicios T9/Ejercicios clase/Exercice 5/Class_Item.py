class Item:
    """
    Represents an item.
    It has the attributes: code (str), name (str), cost before taxes (float), tax percentage (float).
    Methods: getTotalCost ()
    """
    def __init__(self, code, name, cost, taxPercent):
        self.code = code
        self.name = name
        self.cost = cost
        self.taxPercent = taxPercent
    
    def getTotalCost (self):
        """
        Calculates the total cost of the item by adding taxes
        
        Output: (float) Value of the item with added taxes
        """
        return self.cost + self.cost * self.taxPercent