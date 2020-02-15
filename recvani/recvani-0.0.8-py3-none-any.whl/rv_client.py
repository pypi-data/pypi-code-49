import requests
import json
import hmac
import hashlib
import base64
from recvani.rv_requests import base_request

class rv_client(object):

    def __init__(self, api_key, model, secret_key, uri = None):
        self.api_key = api_key
        self.model = model
        self.secret_key = secret_key
        self.session = requests.Session()
        self.id = 0 
        if (uri == None):
            self.uri = 'https://api.recvani.com/rpc'
        else:
            self.uri = uri

    def send(self, request):
        assert(issubclass(request.__class__, base_request)), "Request not derived from base_request"
        self.id = self.id + 1
        params = request._get_params()
        params.insert(0, self.model)
        dt = {"method": request.get_method() , "params": params, "id" : self.id}
        raw_data = json.dumps(dt)
        sign = self._get_sign(raw_data)
        headers = self._get_headers(sign)
        res = None
        retries = 0
        success = False
        while (retries <5 and  (success == False)):
            try:
                res = self.session.post(self.uri, raw_data, headers=headers)
                success = True
            except (requests.ConnectionError):
                retries +=1
        if (res.status_code != 200):
            print(res.content)
            raise RuntimeError("Got non 200 response")
        else:
            dt = json.loads(res.content)
            if (dt["error"] == None):
                return  dt['result']
            raise RuntimeError("Got Error in request: " + dt["error"])

    def _get_sign(self, data):
        raw_sign = hmac.new(str.encode(self.secret_key), str.encode(data), hashlib.sha256).digest()
        sign = "RV " + base64.b64encode(raw_sign).decode("utf-8")
        return sign

   
    def _get_headers(self, sign):
        headers = {}
        headers["Content-Type"] = "application/json"
        headers ["Authorization"] = sign
        headers["apikey"] = self.api_key
        return headers
