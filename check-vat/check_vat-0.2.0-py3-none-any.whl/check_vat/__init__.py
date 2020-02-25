"""Check VAT main"""
__all__ = ['is_valid_vat']

from zeep import Client

VIES_URL = "http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl"


def is_valid_vat(vat_id: str):
    """
    Check given string against EU VAT library
    :param vat_id:
    :return: {'valid': boolean,  # check this first, if false other fields might not in the dict
         'countryCode': 'DE',
         'vatNumber': '308316836',
         'requestDate': datetime.date(2019, 9, 11),
         'name': '---',
         'address': '---'
    }
    """
    result = {'valid': False}
    vat = vat_id.replace(" ", "").strip()
    client = Client(VIES_URL)
    try:
        result = client.service.checkVat(countryCode=vat[:2], vatNumber=vat[2:])
    except zeep.exceptions.Fault as fault:
        print('CheckVAT Error: %s' % fault)
    return result['valid']
