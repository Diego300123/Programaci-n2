class Line:
    """
    Represents a line in the invoice.
    It has the attributes: Item, quantity (int), Invoice
    Methods: getTotalCost ()
    """
    def __init__(self, myItem, quantity, myInvoice):
        self.item = myItem
        self.quantity = quantity
        self.invoice = myInvoice

    def getTotalCost(self):
        """
        Claculates the total cost of the invoice line (including taxes).

        Output: (float) total cost value of the invoice line.
        """
        return self.quantity * self.item.getTotalCost()