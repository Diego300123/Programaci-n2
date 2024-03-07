class Customer:
    """
    Represents the information of the customer.
    Has the attributes: id (int), First name (str), Last name (str).
    Other methods
    """
    def __init__(self, customerId, firstName, lastName):
        self.customerId = customerId
        self.firstName = firstName
        self.lastName = lastName