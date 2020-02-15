import base64

from Crypto import Random
from Crypto.Cipher import AES
import zeep
from zeep import Client

from citram_api.utils.custom_exceptions import NotEnoughParametersException


class CitramApi:
    def __init__(self):
        # This is for the SOAP service only
        self.client = Client('http://www.citram.es:8080/WSMultimodalInformation/MultimodalInformation.svc?wsdl')
        self.public_key = self._get_public_key()
        self.auth_key = self._authenticate()

    # SOAP endpoints
    def get_trips(self, cod_modo, cod_linea):
        if cod_modo is None and cod_linea is None:
            raise NotEnoughParametersException('One of cod_modo or cod_linea must be different than None.')

        try:
            return self.client.service.GetTrips(authentication=self._auth_dict(),
                                                  codModo=cod_modo,
                                                  codLinea=cod_linea)
        except zeep.exceptions.Fault as e:
            if str(e) == 'Authentication Exception. Valid time has expired ':
                self.public_key = self._get_public_key()
                self.auth_key = self._authenticate()
                return self.client.service.GetTrips(authentication=self._auth_dict(),
                                                      codModo=cod_modo,
                                                      codLinea=cod_linea)

    def get_companies(self):
        # o.client.service.GetCompanies(authentication={'connectionKey': '4dYaOO1ChV/34WZ/xYftszYSNqC7je/msvq6EHorMa8='}, codCompany=[])
        try:
            return self.client.service.GetCompanies(authentication=self._auth_dict(),
                                                    codCompany=[])
        except zeep.exceptions.Fault as e:
            if str(e) == 'Authentication Exception. Valid time has expired ':
                self.public_key = self._get_public_key()
                self.auth_key = self._authenticate()
                return self.client.service.GetCompanies(authentication=self._auth_dict(),
                                                        codCompany=[])

    def get_calendars(self, cod_modo, cod_linea, cod_itinerario, cod_expedicion):
        if cod_modo is None:
            raise NotEnoughParametersException('Provide at least a transport mode code.')

        try:
            return self.client.service.GetCalendars(authentication=self._auth_dict(),
                                                      codModo=cod_modo,
                                                      codLinea=cod_linea,
                                                      codItinerario=cod_itinerario,
                                                      codExpedicion=cod_expedicion)
        except zeep.exceptions.Fault as e:
            if str(e) == 'Authentication Exception. Valid time has expired ':
                self.public_key = self._get_public_key()
                self.auth_key = self._authenticate()
                return self.client.service.GetCalendars(authentication=self._auth_dict(),
                                                          codModo=cod_modo,
                                                          codLinea=cod_linea,
                                                          codItinerario=cod_itinerario,
                                                          codExpedicion=cod_expedicion)

    def _auth_dict(self):
        return {'connectionKey': self.auth_key}

    def _get_public_key(self):
        return self.client.service.GetPublicKey()

    def _authenticate(self):
        private_key = 'pruebapruebapruebapruebaprueba12'.encode('US-ASCII')
        plain = self.public_key
        plain = self._pad(plain)

        iv = Random.new().read(AES.block_size)
        cipher = AES.new(private_key, AES.MODE_CBC, iv)

        return base64.b64encode(cipher.encrypt(plain.encode('US-ASCII'))).decode('UTF-8')

    def _pad(self, plain_text):

        """
        https://gist.github.com/komuw/70211c54358d1eca45f2

        func to pad cleartext to be multiples of 8-byte blocks.
        If you want to encrypt a text message that is not multiples of 8-byte blocks,
        the text message must be padded with additional bytes to make the text message to be multiples of 8-byte blocks.
        """

        block_size = AES.block_size

        number_of_bytes_to_pad = block_size - len(plain_text) % block_size

        ascii_string = chr(number_of_bytes_to_pad)

        padding_str = number_of_bytes_to_pad * ascii_string

        padded_plain_text = plain_text + padding_str

        return padded_plain_text

