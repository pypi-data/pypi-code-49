# MIT License
#
# Copyright (c) 2018 Jared Gillespie
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__all__ = ['add_resource', 'add_resource_type', 'get_resources', 'get_resource_types', 'ProxyResource', 'RESOURCE_MAP', 'RESOURCE_TYPE_MAP']


from bs4 import BeautifulSoup
from threading import Lock
import time
import json
from .errors import (
    InvalidHTMLError,
    InvalidResourceError,
    InvalidResourceTypeError,
    RequestNotOKError,
    RequestFailedError,
    ResourceAlreadyDefinedError,
    ResourceTypeAlreadyDefinedError
)
from .shared import (
    is_iterable,
    Proxy,
    request_proxy_list
)

_resource_lock = Lock()
_resource_type_lock = Lock()

country_codes = {
    "AF": "Afghanistan", "AX": "Aland Islands", "AL": "Albania", "DZ": "Algeria", "AS": "American Samoa", "AD": "Andorra", "AO": "Angola", "AI": "Anguilla", "AQ": "Antarctica", "AG": "Antigua and Barbuda", "AR": "Argentina", "AM": "Armenia", "AW": "Aruba", "AU": "Australia", "AT": "Austria", "AZ": "Azerbaijan", "BS": "Bahamas", "BH": "Bahrain", "BD": "Bangladesh", "BB": "Barbados", "BY": "Belarus", "BE": "Belgium", "BZ": "Belize", "BJ": "Benin", "BM": "Bermuda", "BT": "Bhutan", "BO": "Bolivia", "BQ": "Bonaire, Saint Eustatius and Saba", "BA": "Bosnia and Herzegovina", "BW": "Botswana", "BV": "Bouvet Island", "BR": "Brazil", "IO": "British Indian Ocean Territory", "VG": "British Virgin Islands", "BN": "Brunei", "BG": "Bulgaria", "BF": "Burkina Faso", "BI": "Burundi", "KH": "Cambodia", "CM": "Cameroon", "CA": "Canada", "CV": "Cape Verde", "KY": "Cayman Islands", "CF": "Central African Republic", "TD": "Chad", "CL": "Chile", "CN": "China", "CX": "Christmas Island", "CC": "Cocos Islands", "CO": "Colombia", "KM": "Comoros", "CK": "Cook Islands", "CR": "Costa Rica", "HR": "Croatia", "CU": "Cuba", "CW": "Curacao", "CY": "Cyprus", "CZ": "Czech Republic", "CD": "Democratic Republic of the Congo", "DK": "Denmark", "DJ": "Djibouti", "DM": "Dominica", "DO": "Dominican Republic", "TL": "East Timor", "EC": "Ecuador", "EG": "Egypt", "SV": "El Salvador", "GQ": "Equatorial Guinea", "ER": "Eritrea", "EE": "Estonia", "ET": "Ethiopia", "FK": "Falkland Islands", "FO": "Faroe Islands", "FJ": "Fiji", "FI": "Finland", "FR": "France", "GF": "French Guiana", "PF": "French Polynesia", "TF": "French Southern Territories", "GA": "Gabon", "GM": "Gambia", "GE": "Georgia", "DE": "Germany", "GH": "Ghana", "GI": "Gibraltar", "GR": "Greece", "GL": "Greenland", "GD": "Grenada", "GP": "Guadeloupe", "GU": "Guam", "GT": "Guatemala", "GG": "Guernsey", "GN": "Guinea", "GW": "Guinea-Bissau", "GY": "Guyana", "HT": "Haiti", "HM": "Heard Island and McDonald Islands", "HN": "Honduras", "HK": "Hong Kong", "HU": "Hungary", "IS": "Iceland", "IN": "India", "ID": "Indonesia", "IR": "Iran", "IQ": "Iraq", "IE": "Ireland", "IM": "Isle of Man", "IL": "Israel", "IT": "Italy", "CI": "Ivory Coast", "JM": "Jamaica", "JP": "Japan", "JE": "Jersey", "JO": "Jordan", "KZ": "Kazakhstan", "KE": "Kenya", "KI": "Kiribati", "XK": "Kosovo", "KW": "Kuwait", "KG": "Kyrgyzstan", "LA": "Laos", "LV": "Latvia", "LB": "Lebanon", "LS": "Lesotho", "LR": "Liberia", "LY": "Libya", "LI": "Liechtenstein", "LT": "Lithuania", "LU": "Luxembourg", "MO": "Macao", "MK": "Macedonia", "MG": "Madagascar", "MW": "Malawi", "MY": "Malaysia", "MV": "Maldives", "ML": "Mali", "MT": "Malta", "MH": "Marshall Islands", "MQ": "Martinique", "MR": "Mauritania", "MU": "Mauritius", "YT": "Mayotte", "MX": "Mexico", "FM": "Micronesia", "MD": "Moldova", "MC": "Monaco", "MN": "Mongolia", "ME": "Montenegro", "MS": "Montserrat", "MA": "Morocco", "MZ": "Mozambique", "MM": "Myanmar", "NA": "Namibia", "NR": "Nauru", "NP": "Nepal", "NL": "Netherlands", "AN": "Netherlands Antilles", "NC": "New Caledonia", "NZ": "New Zealand", "NI": "Nicaragua", "NE": "Niger", "NG": "Nigeria", "NU": "Niue", "NF": "Norfolk Island", "KP": "North Korea", "MP": "Northern Mariana Islands", "NO": "Norway", "OM": "Oman", "PK": "Pakistan", "PW": "Palau", "PS": "Palestinian Territory", "PA": "Panama", "PG": "Papua New Guinea", "PY": "Paraguay", "PE": "Peru", "PH": "Philippines", "PN": "Pitcairn", "PL": "Poland", "PT": "Portugal", "PR": "Puerto Rico", "QA": "Qatar", "CG": "Republic of the Congo", "RE": "Reunion", "RO": "Romania", "RU": "Russia", "RW": "Rwanda", "BL": "Saint Barthelemy", "SH": "Saint Helena", "KN": "Saint Kitts and Nevis", "LC": "Saint Lucia", "MF": "Saint Martin", "PM": "Saint Pierre and Miquelon", "VC": "Saint Vincent and the Grenadines", "WS": "Samoa", "SM": "San Marino", "ST": "Sao Tome and Principe", "SA": "Saudi Arabia", "SN": "Senegal", "RS": "Serbia", "CS": "Serbia and Montenegro", "SC": "Seychelles", "SL": "Sierra Leone", "SG": "Singapore", "SX": "Sint Maarten", "SK": "Slovakia", "SI": "Slovenia", "SB": "Solomon Islands", "SO": "Somalia", "ZA": "South Africa", "GS": "South Georgia and the South Sandwich Islands", "KR": "South Korea", "SS": "South Sudan", "ES": "Spain", "LK": "Sri Lanka", "SD": "Sudan", "SR": "Suriname", "SJ": "Svalbard and Jan Mayen", "SZ": "Swaziland", "SE": "Sweden", "CH": "Switzerland", "SY": "Syria", "TW": "Taiwan", "TJ": "Tajikistan", "TZ": "Tanzania", "TH": "Thailand", "TG": "Togo", "TK": "Tokelau", "TO": "Tonga", "TT": "Trinidad and Tobago", "TN": "Tunisia", "TR": "Turkey", "TM": "Turkmenistan", "TC": "Turks and Caicos Islands", "TV": "Tuvalu", "VI": "U.S. Virgin Islands", "UG": "Uganda", "UA": "Ukraine", "AE": "United Arab Emirates", "GB": "United Kingdom", "US": "United States", "UM": "United States Minor Outlying Islands", "UY": "Uruguay", "UZ": "Uzbekistan", "VU": "Vanuatu", "VA": "Vatican", "VE": "Venezuela", "VN": "Vietnam", "WF": "Wallis and Futuna", "EH": "Western Sahara", "YE": "Yemen", "ZM": "Zambia", "ZW": "Zimbabwe"
}

class ProxyResource:
    """A manager for a single proxy resource.

    :param func:
        The scraping function.
    :param refresh_interval:
        The minimum time (in seconds) between each refresh.
    :type func: function
    :type refresh_interval: int
    """
    def __init__(self, func, refresh_interval, external_url=None):
        self._func = func
        self._refresh_interval = refresh_interval
        self._lock = Lock()
        self._last_refresh_time = 0
        self.external_url = external_url

    def refresh(self, force=False):
        """Refreshes proxies.

        Proxies are refreshed if they haven't been refreshed within the past `refresh_interval`, or if `force` is True.

        :param force:
            Whether to force a refresh. If True, a refresh is always performed; otherwise it is only done if a refresh
            hasn't occurred within the collector's `refresh_interval`. Defaults to False.
        :return:
            A tuple denoting whether proxies were refreshed and the proxies retrieved.
        :rtype: (bool, iterable)
        """
        if not force and self._last_refresh_time + self._refresh_interval > time.time():
            return False, None

        with self._lock:
            # Check if updated before
            if force or self._last_refresh_time + self._refresh_interval <= time.time():

                try:
                    if self.external_url:
                        proxies = self._func(self.external_url)
                    else:
                        proxies = self._func()
                    self._last_refresh_time = time.time()
                    return True, proxies
                except (InvalidHTMLError, RequestNotOKError, RequestFailedError):
                    pass

        return False, None


def get_didsoft_proxies(url):
    response = request_proxy_list(url)

    try:
        proxies = set()
        data = response.content.decode('utf-8')
        data = json.loads(data)
        lproxy = data['result']
        for proxy in lproxy:
            xproxy = proxy.split('#')
            if len(xproxy) == 2:
                code = xproxy[1]
                yproxy = xproxy[0].split(':')
                if len(yproxy) == 2:
                    host = yproxy[0]                
                    port = yproxy[1]                
                    country = country_codes[code] if code in country_codes else 'United States'
                    anonymous = 'anonymous'
                    version = 'http'
                    proxies.add(Proxy(host, port, code, country, anonymous, version, 'didsoft-proxy-list'))
        return proxies

    except (AttributeError, KeyError):
        raise InvalidHTMLError()


def get_anonymous_proxies():
    url = 'https://free-proxy-list.net/anonymous-proxy.html'
    response = request_proxy_list(url)

    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'id': 'proxylisttable'})
        proxies = set()

        for row in table.find('tbody').find_all('tr'):
            data = list(map(lambda x: x.text, row.find_all('td')))
            host = data[0]
            port = data[1]
            code = data[2].lower()
            country = data[3].lower()
            anonymous = data[4].lower() in ('anonymous', 'elite proxy')
            version = 'https' if data[6].lower() == 'yes' else 'http'

            proxies.add(Proxy(host, port, code, country, anonymous, version, 'anonymous-proxy'))

        return proxies
    except (AttributeError, KeyError):
        raise InvalidHTMLError()


def get_free_proxy_list_proxies():
    url = 'http://www.free-proxy-list.net'
    response = request_proxy_list(url)
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'id': 'proxylisttable'})
        proxies = set()

        for row in table.find('tbody').find_all('tr'):
            data = list(map(lambda x: x.text, row.find_all('td')))
            host = data[0]
            port = data[1]
            code = data[2].lower()
            country = data[3].lower()
            anonymous = data[4].lower() in ('anonymous', 'elite proxy')
            version = 'https' if data[6].lower() == 'yes' else 'http'

            proxies.add(Proxy(host, port, code, country, anonymous, version, 'free-proxy-list'))

        return proxies

    except (AttributeError, KeyError):
        raise InvalidHTMLError()
    

def _get_proxy_daily_proxies_parse_inner(element, type, source):
    content = element.contents[0]
    rows = content.replace('"', '').replace("'", '').split('\n')

    proxies = set()
    for row in rows:
        row = row.strip()
        if len(row) == 0:
            continue

        params = str(row).split(':')
        params.extend([None, None, None, type, source])
        proxies.add(Proxy(*params))
    return proxies


def get_proxy_daily_data_elements():
    url = 'http://www.proxy-daily.com'
    response = request_proxy_list(url)

    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find('div', {'id': 'free-proxy-list'})
        return content.find_all(class_="freeProxyStyle")
    except (AttributeError, KeyError):
        raise InvalidHTMLError()


def get_proxy_daily_http_proxies():
    http_data_element = get_proxy_daily_data_elements()[0]
    return _get_proxy_daily_proxies_parse_inner(http_data_element, 'http', 'proxy-daily-http')


def get_proxy_daily_socks4_proxies():
    socks4_data_element = get_proxy_daily_data_elements()[1]
    return _get_proxy_daily_proxies_parse_inner(socks4_data_element, 'socks4', 'proxy-daily-socks4')


def get_proxy_daily_socks5_proxies():
    socks5_data_element = get_proxy_daily_data_elements()[2]
    return _get_proxy_daily_proxies_parse_inner(socks5_data_element, 'socks5', 'proxy-daily-socks5')


def get_socks_proxies():
    url = 'https://www.socks-proxy.net'
    response = request_proxy_list(url)

    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'id': 'proxylisttable'})
        proxies = set()

        for row in table.find('tbody').find_all('tr'):
            data = list(map(lambda x: x.text, row.find_all('td')))
            host = data[0]
            port = data[1]
            code = data[2].lower()
            country = data[3].lower()
            version = data[4].lower()
            anonymous = data[5].lower() in ('anonymous', 'elite proxy')

            proxies.add(Proxy(host, port, code, country, anonymous, version, 'socks-proxy'))

        return proxies
    except (AttributeError, KeyError):
        raise InvalidHTMLError()


def get_ssl_proxies():
    url = 'https://www.sslproxies.org/'
    response = request_proxy_list(url)

    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'id': 'proxylisttable'})
        proxies = set()

        for row in table.find('tbody').find_all('tr'):
            data = list(map(lambda x: x.text, row.find_all('td')))
            host = data[0]
            port = data[1]
            code = data[2].lower()
            country = data[3].lower()
            anonymous = data[4].lower() in ('anonymous', 'elite proxy')

            proxies.add(Proxy(host, port, code, country, anonymous, 'https', 'ssl-proxy'))

        return proxies
    except (AttributeError, KeyError):
        raise InvalidHTMLError()


def get_uk_proxies():
    url = 'https://free-proxy-list.net/uk-proxy.html'
    response = request_proxy_list(url)

    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'id': 'proxylisttable'})
        proxies = set()

        for row in table.find('tbody').find_all('tr'):
            data = list(map(lambda x: x.text, row.find_all('td')))
            host = data[0]
            port = data[1]
            code = data[2].lower()
            country = data[3].lower()
            anonymous = data[4].lower() in ('anonymous', 'elite proxy')
            version = 'https' if data[6].lower() == 'yes' else 'http'

            proxies.add(Proxy(host, port, code, country, anonymous, version, 'uk-proxy'))

        return proxies
    except (AttributeError, KeyError):
        raise InvalidHTMLError()


def get_us_proxies():
    url = 'https://www.us-proxy.org'
    response = request_proxy_list(url)

    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'id': 'proxylisttable'})
        proxies = set()

        for row in table.find('tbody').find_all('tr'):
            data = list(map(lambda x: x.text, row.find_all('td')))
            host = data[0]
            port = data[1]
            code = data[2].lower()
            country = data[3].lower()
            anonymous = data[4].lower() in ('anonymous', 'elite proxy')
            version = 'https' if data[6].lower() == 'yes' else 'http'

            proxies.add(Proxy(host, port, code, country, anonymous, version, 'us-proxy'))

        return proxies
    except (AttributeError, KeyError):
        raise InvalidHTMLError()


def add_resource(name, func, resource_types=None):
    """Adds a new resource, which is representative of a function that scrapes a particular set of proxies.

    :param name:
        An identifier for the resource.
    :param func:
        The scraping function.
    :param resource_types:
        (optional) The resource types to add the resource to. Can either be a single or sequence of resource types.
    :type name: string
    :type func: function
    :type resource_types: iterable or string or None
    :raises InvalidResourceTypeError:
        If 'resource_types' is defined are does not represent defined resource types.
    :raises ResourceAlreadyDefinedError:
        If 'name' is already a defined resource.
    """
    if name in RESOURCE_MAP:
        raise ResourceAlreadyDefinedError('{} is already defined as a resource'.format(name))

    if resource_types is not None:
        if not is_iterable(resource_types):
            resource_types = {resource_types, }

        for resource_type in resource_types:
            if resource_type not in RESOURCE_TYPE_MAP:
                raise InvalidResourceTypeError(
                    '{} is not a defined resource type'.format(resource_type))

    with _resource_lock:
        # Ensure not added by the time entered lock
        if name in RESOURCE_MAP:
            raise ResourceAlreadyDefinedError('{} is already defined as a resource'.format(name))

        RESOURCE_MAP[name] = func

        if resource_types is not None:
            for resource_type in resource_types:
                RESOURCE_TYPE_MAP[resource_type].add(name)


def add_resource_type(name, resources=None):
    """Adds a new resource type, which is a representative of a group of resources.

    :param name:
        An identifier for the resource type.
    :param resources:
        (optional) The resources to add to the resource type. Can either be a single or sequence of resources.
    :type name: string
    :type resources: string or iterable
    :raises InvalidResourceError:
        If any of the resources are invalid.
    :raises ResourceTypeAlreadyDefinedError:
        If 'name' is already a defined resource type.
    """
    if name in RESOURCE_TYPE_MAP:
        raise ResourceTypeAlreadyDefinedError(
            '{} is already defined as a resource type'.format(name))

    with _resource_type_lock:
        # Ensure not added by the time entered lock
        if name in RESOURCE_TYPE_MAP:
            raise ResourceTypeAlreadyDefinedError(
                '{} is already defined as a resource type'.format(name))

        if resources is not None:
            if not is_iterable(resources):
                resources = {resources, }
            resources = set(resources)

            for resource in resources:
                if resource not in RESOURCE_MAP:
                    raise InvalidResourceError('{} is an invalid resource'.format(resource))
        else:
            resources = set()

        RESOURCE_TYPE_MAP[name] = resources


def get_resource_types():
    """Returns a set of the resource types.

    :return:
        The defined resource types.
    :rtype: set
    """
    return set(RESOURCE_TYPE_MAP.keys())


def get_resources():
    """Returns a set of the resources.

    :return:
        The defined resources.
    :rtype: set
    """
    return set(RESOURCE_MAP.keys())


RESOURCE_MAP = {
    'anonymous-proxy': get_anonymous_proxies,
    'free-proxy-list': get_free_proxy_list_proxies,
    'proxy-daily-http': get_proxy_daily_http_proxies,
    'proxy-daily-socks4': get_proxy_daily_socks4_proxies,
    'proxy-daily-socks5': get_proxy_daily_socks5_proxies,
    'socks-proxy': get_socks_proxies,
    'ssl-proxy': get_ssl_proxies,
    'uk-proxy': get_uk_proxies,
    'us-proxy': get_us_proxies
}

RESOURCE_TYPE_MAP = {
    'http': {
        'us-proxy',
        'uk-proxy',
        'free-proxy-list',
        'proxy-daily-http',
        'anonymous-proxy'
    },
    'https': {
        'us-proxy',
        'uk-proxy',
        'free-proxy-list',
        'ssl-proxy',
        'anonymous-proxy'
    },
    'socks4': {
        'socks-proxy',
        'proxy-daily-socks4'
    },
    'socks5': {
        'socks-proxy',
        'proxy-daily-socks5'
    }
}
