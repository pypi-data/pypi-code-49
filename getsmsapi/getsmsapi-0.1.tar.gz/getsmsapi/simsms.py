import requests
import logging
import pydash
from json.decoder import JSONDecodeError
from time import sleep


class Simsms(object):
    """Class to use sim-sms api to receive virtual numbers"""

    __slots__ = ('api_key', 'country', 'service')

    available_services = (
        'opt29',
        'opt41',
    )
    available_countries = (
        'RU',
        'UA'
    )

    def __init__(self, api_key: str, service: str, country: str = 'ru') -> None:
        """Init
        :param api_key: Your api key in sim-sms service
        :param service: service which number you will request
        :param country: country of number
        """
        self.api_key = api_key

        if country in self.available_countries:
            self.country = country
        else:
            raise ValueError("No such service")

        if service in self.available_services:
            self.service = service
        else:
            raise ValueError("No such service")

    def get_number(self) -> tuple:
        """Get virtual number
        :return: tuple - number and order id
        """
        status = '0'
        url = f"http://simsms.org/priemnik.php?metod=get_number&" \
            f"country=RU&service={self.service}&apikey={self.api_key}"
        while status != '1':
            response = requests.get(url)
            logging.warning(f'Url {response.url}')

            try:
                response_text = response.json()
            except JSONDecodeError:
                logging.warning(f'Json decode error')
                sleep(30)
                continue

            status = pydash.get(response_text, 'response')
            logging.warning(f'{status}')
            if status == '2':
                sleep(30)
            elif status == '1':
                return pydash.get(response_text, 'number'), pydash.get(response_text, 'id')
            else:
                sleep(30)

    def get_code(self, id_: str):
        """Get sms code
        :param id_: if from number order
        :return: tuple - number, sms
        """
        url = f'http://simsms.org/priemnik.php?metod=get_sms&country=ru&' \
            f'service={self.service}&id={id_}&apikey={self.api_key}'
        status = '0'
        logging.warning(f'Url {url}')
        while status != '1':
            response = requests.get(url)
            response_text = response.json()

            status = pydash.get(response_text, 'response')
            if status == '2':
                sleep(30)
            elif status == '1':
                return pydash.get(response_text, 'number'), pydash.get(response_text, 'sms')
            else:
                logging.warning(response_text)
                sleep(10)

    def mark_as_used(self, id_):
        url = f'http://simsms.org/priemnik.php?metod=ban&service={self.service}' \
            f'&apikey={self.api_key}&id={id_}'
        requests.get(url)
