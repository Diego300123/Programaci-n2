class Customer:
    """
    Represents the information of the customer.
    Has the attributes: id (int), First name (str), Last name (str).
    Other methods
    """


class Item:
    """
    Represents an item.
    It has the attributes: code (str), name (str), cost before taxes (float), tax percentage (float).
    Methods: getTotalCost ()
    """


class Line:
    """
    Represents a line in the invoice.
    It has the attributes: Item, quantity (int), Invoice
    Methods: getTotalCost ()
    """


class Invoice:
    """
    Represents an incoice.
    It has the attributes: number (int), Customer and Line.
    Methods: addLine (Line), calculateTotal ()
    """