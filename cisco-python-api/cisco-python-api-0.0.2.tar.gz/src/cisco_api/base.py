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

class CMXBase(BaseAPI):
   def __init__(self, url, username, password, verify_ssl=True):
      self.base_url = base_url #this is tenant-id
      self.apikey = apikey
      self.verify_ssl = verify_ssl
      self._session = requests.Session()
      self._session.verify = self.verify_ssl
      self._set_auth()

   def _endpoint(self, path):
       url = urljoin(self.base_url, '.cmxcisco.com/')
       return urljoin(url, path)

   def _formatdate(self, date_range):
       '''
       Format for CMX: YYYY-MM-DD
       '''
       return date_range

    def _requestRange(self, url, siteId, date_range):
        date_range = self._formatdate(date_range)
        if date_range[1] == date_range[0]:
            data = {
                    'siteId': siteId,
                    'startDate': date_range[0],
                    'endDate': date_range[1]
                    }
            r = self.session.get(url, data=data)
            return r.json()
        else:
            #Falta implementar requisição varrendo datas
            #for data in data x = x+1
            data = {
                    'siteId': siteId,
                    'startDate': date_range[0],
                    'endDate': date_range[1]
                    }
            r = self.session.get(url, data=data)
            return r.json()
