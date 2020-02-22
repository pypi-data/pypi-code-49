import attr


def str_corrector(value):
    return value.rstrip().replace('"', "'").replace('\n', '')


def date_corrector(value):
    # return common_corrector(value).split('+')[0]
    return value.split('+')[0]


@attr.s
class PaymentData:
    """ Wrap dict and validate/convert values of each field"""
    bin = attr.ib(default='')
    taxorgcode = attr.ib(converter=str_corrector, default='')
    nametaxru = attr.ib(converter=str_corrector, default='')
    nametaxkz = attr.ib(converter=str_corrector, default='')
    kbk = attr.ib(converter=str_corrector, default='')
    kbknameru = attr.ib(converter=str_corrector, default='')
    kbknamekz = attr.ib(converter=str_corrector, default='')
    paynum = attr.ib(converter=str_corrector, default='')
    paytype = attr.ib(converter=str_corrector, default='')
    entrytype = attr.ib(converter=str_corrector, default='')
    receiptdate = attr.ib(converter=date_corrector, default='')
    writeoffdate = attr.ib(converter=date_corrector, default='')
    summa = attr.ib(converter=str_corrector, default='')


def prepare(row, struct):
    """ Convert dict into tuple by casting to certain structure.
        For correct type casting we wrap
        dict in attr class. So we can apply convert/corrector
        function for every field.
        For example: attr.ib(converter=common_corrector, default='')
        """

    # cast all fields name of struct in lowercase
    _p_dict = {k.lower(): v for k, v in row.items() if k.lower()}

    # wrap in struct
    # so we can convert values and correct them
    # data = JuridicalInfo(**_p_dict)
    data = struct(**_p_dict)

    # return only values
    return attr.astuple(data)


class KgdTaxPaymentParser:
    pass


