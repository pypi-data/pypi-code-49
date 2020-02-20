import requests
import urllib
import json
import os

API_URL = 'https://www.tronalddump.io/'
WORK_DIR = os.path.dirname(os.path.abspath(__file__))

class TronaldDumpException(Exception):
    pass


class TronaldDumpResponse:
    '''Response class '''

    def __init__(self, response):
        self.response = response

    def __repr__(self):
        return "<{}: '{}'>".format(self.__class__.__name__, self.response.url)

    @property
    def data(self):
        '''Parse response JSON and store it'''
        if not hasattr(self, '_data'):
            try:
                self._data = json.loads(self.response.content)
            except:
                raise TronaldDumpException('No JSON data could be parsed from the response.')
        return self._data

    @property
    def url(self):
        '''Return URL adress for the given response'''
        return self.response.url
    


class TronaldDumpAPI:
    '''TronaldDump API class'''

    def _build_url(self, *args, **kwargs):
        '''Build the API URL to request. *args build the URL path, **kwargs build the GET params.'''
        args = [x.replace(' ', '%20') for x in args if x]
        path = '/'.join([str(x) for x in args if x])
        url = urllib.parse.urljoin(API_URL, path)
        url += '?{}'.format(urllib.parse.urlencode(kwargs) if kwargs else '')
        return url

    def _send_request(self, *args, **kwargs):
        '''Send a request to the API'''
        api_url = self._build_url(*args, **kwargs)
        resp = requests.get(api_url)
        if resp.status_code != 200:
            raise TronaldDumpException(f'The API endpoint returned error code <{resp.status_code}>\n{resp.url}')
        return TronaldDumpResponse(resp)

    # TAG

    def find_tag(self, value):
        '''Find a tag by its value. Given parameters will be capitalized'''
        value = [elem.capitalize() for elem in value.split(' ')]
        return self._send_request("tag", ' '.join(value))

    def all_tags(self):
        '''Retrieve all existing tags'''
        return self._send_request("tag")

    # QUOTE

    def random_quote(self):
        '''Retrieve a random quote'''
        return self._send_request("/random/quote")

    def random_meme(self, output_dir, filename="randommeme.png", force_write=True):
        '''Retrieve a random meme and store it in the given path and filename.'''
        file = os.path.join(output_dir, filename)
        if not os.path.exists(output_dir):
            raise FileNotFoundError('The given directory does not exist.')
        elif os.path.exists(file) and force_write == False:
            raise FileExistsError('The given path already contains file with such name.')
        respclass = self._send_request("/random/meme")
        with open(file, "wb") as image:
            image.write(respclass.response.content)
        return respclass

    def search_quote(self, query=None, tag=None, page=0):
        '''Search for a quote by the query or tag. Returns one-page answer where page number is determined by page param.'''
        # for now returns only the first page for a query
        # SEARCH IS CASE-SENSETIVE

        if not query and not tag:
            raise TronaldDumpException("Function 'search_quote' takes at least one argument but none was given.")
        elif query and tag:
            raise TronaldDumpException("Function 'search_quote' takes only one of the arguments but two were given.")
        elif tag:
            return self._send_request("search/quote",tag=tag, page=page)
        return self._send_request("search/quote", query=query, page=page)

    def find_quote(self, id: str):
        '''Find a quote by its ID'''
        return self._send_request("quote", id)

    # QUOTE-SOURCE

    def quote_source(self, id: str):
        '''Retrive the source of a quote by its ID'''
        return self._send_request("quote-source", id)

    # AUTHOR

    def find_author(self, id: str):
        '''Find an author by their ID'''
        return self._send_request("author", id)