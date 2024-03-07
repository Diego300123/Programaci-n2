class Invoice:
    """
    Represents an invoice.
    It has the attributes: number (int), Customer and Line.
    Methods: addLine (Line), calculateTotal ()
    """
    def __init__(self, number, myCustomer):
        self.number = number
        self.customer = myCustomer
        self.lines = []


    def addLine(self, myLine):
        """
        Add a line to the invoice

        myLine: (Line) an invoice line
        """
        self.lines.append(myLine)


    def deleteLine(self, n):
        """
        Deletes a choosen line from the invoice.

        n: (int) number of the line
        """
        self.lines.pop(n) # del self.lines[n]

    def calculateTotal(self):
        """
        Calculate the total cost of the invoice.

        Output: (float) Value of the invoice cost
        """
        totalCost = 0
        for myLine in self.lines:
            totalCost += myLine.getTotalCost()
        return totalCost

