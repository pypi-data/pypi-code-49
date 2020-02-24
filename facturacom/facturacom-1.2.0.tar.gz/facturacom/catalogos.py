import logging
from facturacom.api_wrapper import ApiWrapper

LOG = logging.getLogger(__name__)

class Catalogos(object):
    """
    Manage catalogs from endpoints
    """
    def __init__(self):
        pass

    @staticmethod
    def list_aduanas():
        """
        Get all aduanas
        """
        return ApiWrapper.api_call('/v3/catalogo/Aduana', dict())

    @staticmethod
    def list_units():
        """
        Get all units of measurment
        """
        return ApiWrapper.api_call('/v3/catalogo/ClaveUnidad', dict())

    @staticmethod
    def list_payment_methods():
        """
        Get all payment methods
        """
        return ApiWrapper.api_call('/v3/catalogo/FormaPago', dict())

    @staticmethod
    def list_taxes():
        """
        Get all tax
        """
        return ApiWrapper.api_call('/v3/catalogo/Impuesto', dict())

    @staticmethod
    def list_currencies():
        """
        Get all currencies
        """
        return ApiWrapper.api_call('/v3/catalogo/Moneda', dict())

    @staticmethod
    def list_countries():
        """
        Get all countries
        """
        return ApiWrapper.api_call('/v3/catalogo/Pais', dict())

    @staticmethod
    def list_tax_configurations():
        """
        Get all Tax Configurations (Regimen Fiscal)
        """
        return ApiWrapper.api_call('/v3/catalogo/RegimenFiscal', dict())

    @staticmethod
    def list_relation_types():
        """
        Get all Relation types
        """
        return ApiWrapper.api_call('/v3/catalogo/Relacion', dict())

    @staticmethod
    def list_cfdi_uses():
        """
        Get all CFDI use
        """
        return ApiWrapper.api_call('/v3/catalogo/UsoCfdi', dict())
