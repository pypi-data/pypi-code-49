from abc import abstractmethod
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, tostring

import requests


__title__ = "python-fattura24"
__version__ = "0.0.1"
__author__ = "Federico Torresan"


class BaseAPI(object):
    """
    Main API object for fattura24
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://www.app.fattura24.com/api/v0.3/'
        self.endpoint = ''

    def _do_request(self, data=None):
        if data is None:
            data = {}
        data['apiKey'] = self.api_key
        res = requests.post('%s%s' % (self.base_url, self.endpoint), data=data)
        return ElementTree.fromstring(res.content)

    @abstractmethod
    def send(self):
        """
        Send request to endpoint
        :return:
        """
        raise NotImplementedError()


class Document(BaseAPI):

    DOCUMENT_TYPE_INVOICE = 'I'
    DOCUMENT_TYPE_FE_INVOICE = 'FE'
    
    FIELDS = [
        'document_type',
        'id_numerator',
        'customer_name',
        'customer_address',
        'customer_postcode',
        'customer_city',
        'customer_province',
        'customer_country',
        'customer_fiscal_code',
        'customer_vat_code',
        'customer_cell_phone',
        'customer_email',
        'delivery_name',
        'delivery_address',
        'delivery_postcode',
        'delivery_city',
        'delivery_province',
        'delivery_country',
        'object',
        'total_without_tax',
        'payment_method_name',
        'payment_method_description',
        'vat_amount',
        'total',
        'foot_notes',
        'send_email',
        'update_storage',
        'F24_order_id',
        'id_template',
        'payments',
        'rows'
    ]

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.endpoint = 'SaveDocument'

        # Document fields
        self.document_type = None
        self.id_numerator = None
        self.customer_name = None
        self.customer_address = None
        self.customer_postcode = None
        self.customer_city = None
        self.customer_province = None
        self.customer_country = None
        self.customer_fiscal_code = None
        self.customer_vat_code = None
        self.customer_cell_phone = None
        self.customer_email = None
        self.delivery_name = None
        self.delivery_address = None
        self.delivery_postcode = None
        self.delivery_city = None
        self.delivery_province = None
        self.delivery_country = None
        self.object = None
        self.total_without_tax = None
        self.payment_method_name = None
        self.payment_method_description = None
        self.vat_amount = None
        self.total = None
        self.foot_notes = None
        self.send_email = False
        self.update_storage = None
        self.F24_order_id = None
        self.id_template = None
        self.payments = []
        self.rows = []

    class Payment(object):
        """
        Class for payments
        """
        def __init__(self, *args, **kwargs):
            # Payment fields
            self.date = kwargs.get('date', None)
            self.amount = kwargs.get('amount', None)
            self.paid = kwargs.get('paid', False)

        def xml(self):
            payment = Element('Payment')
            date = SubElement(payment, 'Date')
            date.text = str(self.date.strftime('%Y-%m-%d'))
            amount = SubElement(payment, 'Amount')
            amount.text = str(self.amount)
            paid = SubElement(payment, 'Paid')
            paid.text = self.paid and 'true' or 'false'
            return payment

    class Row(object):
        """
        Class for rows
        """
        def __init__(self, *args, **kwargs):
            # Payment fields
            self.description = kwargs.get('description', None)
            self.qty = kwargs.get('qty', 1)
            self.price = kwargs.get('price', None)
            self.vat_code = kwargs.get('vat_code', None)
            self.vat_description = kwargs.get('vat_description', None)

        def xml(self):
            row = Element('Row')
            description = SubElement(row, 'Description')
            description.text = str(self.description)
            qty = SubElement(row, 'Qty')
            qty.text = str(self.qty)
            price = SubElement(row, 'Price')
            price.text = str(self.price)
            vat_code = SubElement(row, 'VatCode')
            vat_code.text = str(self.vat_code)
            vat_description = SubElement(row, 'VatDescription')
            vat_description.text = str(self.vat_description)
            return row

    def xml(self, output_string=True):
        """
        Generate xml for the document
        :return:
        """
        from fattura24.utils import camelize

        root = Element('Fattura24')
        document = SubElement(root, "Document")
        for field in self.FIELDS:
            if hasattr(self, field) and getattr(self, field, None) is not None:
                el = SubElement(document, camelize(field))
                data = getattr(self, field)
                if type(data) == list:
                    childs = []
                    for c in data:
                        childs.append(c.xml())
                    el.extend(childs)
                elif type(data) == bool:
                    el.text = data and 'true' or 'false'
                else:
                    el.text = str(data)

        if output_string:
            return tostring(root)
        return root

    def send(self):
        """
        Send request to endpoint
        :return:
        """
        return self._do_request(data={'xml': self.xml()})


class FEDocument(Document):
    """
    Document for FE
    """

    PAYMENT_CODE_TYPE_MP01 = 'MP01' # ‘MP01’ per i pagamenti in contanti
    PAYMENT_CODE_TYPE_MP05 = 'MP05' # ‘MP05’ per i pagamenti tramite bonifico
    PAYMENT_CODE_TYPE_MP08 = 'MP08' # ‘MP08’ per i pagamenti tramite carta di credito
    PAYMENT_CODE_TYPE_MP12 = 'MP12' # ‘MP12’ per i pagamenti tramite Riba

    VAT_NATURE_TYPE_N1 = 'N1' # ‘N1’ escluse ex art. 15
    VAT_NATURE_TYPE_N2 = 'N2' # ‘N2’ non soggette
    VAT_NATURE_TYPE_N3 = 'N3' # ‘N3’ non imponibili
    VAT_NATURE_TYPE_N4 = 'N4' # ‘N4’ esenti
    VAT_NATURE_TYPE_N5 = 'N5' # ‘N5’ regime del margine
    VAT_NATURE_TYPE_N6 = 'N6' # ‘N6’ inversione contabile (reverse charge)

    FIELDS = Document.FIELDS + [
        'fe_customer_pec',
        'fe_destination_code',
        'fe_payment_code',
        'fe_vat_nature',
        'vat_type'
    ]

    def __init__(self, *args, **kwargs):
        super(FEDocument, self).__init__(*args, **kwargs)

        # FE Document fields
        self.document_type = Document.DOCUMENT_TYPE_FE_INVOICE
        self.fe_customer_pec = None
        self.fe_destination_code = None
        self.fe_payment_code = None
        self.fe_vat_nature = None
        self.vat_type = None


class GetFile(BaseAPI):
    """
    Retrieve the file about a document
    """
    def __init__(self, *args, **kwargs):
        docId = kwargs.pop('docId', None)

        super(GetFile, self).__init__(*args, **kwargs)
        self.endpoint = 'GetFile'

        # File field
        self.docId = docId

    def send(self):
        """
        Send request to endpoint
        :return:
        """
        return requests.get('%s%s' % (self.base_url, self.endpoint),
                            params={'apiKey': self.api_key, 'docId': self.docId})
