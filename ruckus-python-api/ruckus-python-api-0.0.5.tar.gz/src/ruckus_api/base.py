import requests
from urllib.parse import urljoin


class BaseAPI(object):
    @property
    def session(self):
        return self._session

    def get(self, *args, **kwargs):
        return self.session.get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self.session.post(*args, **kwargs)

    def put(self, *args, **kwargs):
        return self.session.put(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.session.delete(*args, **kwargs)

    def logout(self):
        if not getattr(self, '_session', None):
            return False
        self._session.close()
        self._session = requests.Session()
        self._session.verify = self.verify_ssl
        return True


class VSpotBase(BaseAPI):
    def __init__(self, base_url, apikey=None, verify_ssl=True):
        self.base_url = base_url
        self.apikey = apikey
        self.verify_ssl = verify_ssl
        self._session = requests.Session()
        self._session.verify = self.verify_ssl
        self._set_auth()

    def endpoint(self, path, *args, version='1'):
        url = urljoin(self.base_url, '/api/v%s/' % version)
        return urljoin(url, path.format(*args))

    def get_file(self, uri):
        '''
            To get files like map images the user must be authenticated
            this function gets the file through the authenticated session
            returns tuple (mime type, file bytes)
            as in ('image/png', b'\\x89PNG\\r\\n\\x...')

            # TODO: iter chunks for big files
        '''
        with self.get(uri, stream=True) as r:
            return r.headers.get('Content-Type'), r.content

    def link_gen(self, response, unwind=True):
        oresp = response

        d = oresp.json()
        if isinstance(d, list) and unwind:
            for x in d:
                yield x
        else:
            yield d
        while 'url' in oresp.links.get('next', ''):
            resp = self.get(oresp.links['next']['url'])
            del oresp
            d = resp.json()
            if isinstance(d, list) and unwind:
                for x in d:
                    yield x
            else:
                yield d
            oresp = resp
            del x, d, resp


    def _set_auth(self):
        if self.apikey is None:
            # TODO: raise error
            return False
        self._session.auth = (self.apikey, 'dummy')
        return True


class SmartZoneBase(BaseAPI):
    def __init__(self, base_url, username, password, verify_ssl=True):
        self.base_url = base_url
        self.username = username
        self.password = password
        self._session = requests.Session()
        self.verify_ssl = verify_ssl
        self._session.verify = verify_ssl
        self.login()

    def logout(self):
        '''
        Use this API command to log off of the controller.
        '''
        r = self.session.delete(self.endpoint('v8_2/session'))
        return super().logout()


    def endpoint(self, path):
        url = urljoin(self.base_url, '/wsg/api/public/')
        return urljoin(url, path)

    def filters_json(self, filter_type, filter_value, start, end, search_type=None, search_value=None, attributes=None):
        if search_type is None:
            search_type = "AND"
        if search_value is None:
            search_value = ""
        if attributes is None:
            attributes = "*"
        json = {
                 "filters": [
                   {
                     "type": filter_type,
                     "value": filter_value
                   }
                 ],
                "extraTimeRange": {
                    "start": start,
                    "end": end,
                    "interval": 0
                    },
                  "fullTextSearch": {
                    "type": search_type,
                    "value": search_value
                 },
                 "attributes": [
                    attributes
                 ]
                }
        return json
