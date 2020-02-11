class TicketException(Exception):
    def __init__(self, message):
        super(Exception, self).__init__(message)
        self.message = message


class CustomerIDMissing(TicketException):
    def __init__(self, econtract_id):
        super(TicketException, self).__init__(
            "The customer id is missing fot the EticomContract({})".format(econtract_id))


class CustomerUserMissing(TicketException):
    def __init__(self, econtract_id):
        super(TicketException, self).__init__(
            "The customer user is missing fot the EticomContract({})".format(econtract_id))


class CustomerVatNumberMissing(TicketException):
    def __init__(self, econtract_id):
        super(TicketException, self).__init__(
            "The customer vat number is missing fot the EticomContract({})".format(econtract_id))


class CustomerMailMissing(TicketException):
    def __init__(self, econtract_id):
        super(TicketException, self).__init__(
            "The customer mail is missing fot the EticomContract({})".format(econtract_id))


class ServiceTypeNotAllowedError(TicketException):
    def __init__(self, service_type):
        super(TicketException, self).__init__("Contract Type not allowed: {}".format(service_type))
