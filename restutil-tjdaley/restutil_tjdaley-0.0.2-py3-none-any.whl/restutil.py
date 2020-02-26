import re
import requests
import time

from .urlmaker import UrlMaker


class RestUtil(object):
    def __init__(self, api_key: str):
        self.urlmaker = UrlMaker(api_key, host='localhost')
        self.auth = (api_key, None)

    def average_mortage_rate(self, year: int, month: int = 6, term: int = 30) -> dict:
        """
        Return average mortgage interest rate per Federal Reserve
        of St. Louis.

        Args:
          year (int): Year, e.g. 1999 [Required]
          month (int): Month where 1=January, 12=December, etc. [Default=6]
          term (int): Term of the loan in years. Must be one of 5, 15, or 30. [Default=30]
        Returns:
          (dict): Result Set the interest rate
        """
        url = self.urlmaker.url_for('fred', 'historical_rate', year=year, month=month, term=term)
        response = self.__get_response(url)
        return response.json()['data']['response']

    def __get_response(self, url: str):
        """
        Retrieve response from server, with retry logic.

        Args:
            url (str): URL to retrieve.
        Returns:
            requests.response if OK otherwise an exception.
        """
        rate_limit_retries_remaining = 5
        while rate_limit_retries_remaining > 0:
            response = requests.get(url, auth=self.auth)
            if response.status_code == 401:
                raise Exception(response.text)
            response_json = response.json()
            if response_json['success'] is True:
                return response
            if response_json['code'] == 'ERR_RATE_LIMIT' and rate_limit_retries_remaining > 0:
                time.sleep(1)
                rate_limit_retries_remaining -= 1
        message = f"{response_json['message']} ({response_json['code']})"
        raise Exception(message)


def main():
    ru = RestUtil('my_access_key')
    for i in range(5):
        print(ru.average_mortage_rate(2010, i+1, 15))


if __name__ == '__main__':
    main()
