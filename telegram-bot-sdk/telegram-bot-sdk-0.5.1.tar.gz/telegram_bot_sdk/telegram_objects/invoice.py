class Invoice:
    """This class contains basic information about an invoice

    :param title: Product name
    :type title: str
    :param description: Product description
    :type description: str
    :param start_parameter: Unique bot deep.linking parameter that can be used to generate this invoice
    :type start_parameter: str
    :param currency: Three letter ISO 4217 currency code
    :type currency: str
    :param total_amount: Total amount in the smallest units of the currency (int, not float/double)
    :type total_amount: int
    """
    def __init__(self, *, title, description, start_parameter, currency, total_amount):
        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = total_amount
