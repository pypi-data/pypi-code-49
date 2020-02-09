class LabeledPrice:
    """This class represents a portion of the price for goods or services

    :param label: Portion label
    :type label: str
    :param amount: Price of the product in the smallest units of the currency (int not float/double)
    :type amount: int
    """
    def __init__(self, *, label, amount):
        self.label = label
        self.amount = amount
