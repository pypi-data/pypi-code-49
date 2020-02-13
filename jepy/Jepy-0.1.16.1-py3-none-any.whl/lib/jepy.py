import json
import datetime
from lib.jepy_exceptions import *
from lib.jepy_client import JepyClient


class Jepy():
    def __init__(self, **kwargs):
        if ('user_id' and 'password') in kwargs:
            self._str_val = self.__repr__()
            user_id, password = kwargs['user_id'], kwargs['password']
            self.client = JepyClient(user_id=user_id, password=password)
            self.jwt_token = self.client.jwt_token
        else:
            self._status()

    def __str__(self):
        return self._str_val
        
    def _status(self):
        result = JepyClient()._call_status()
        self._str_val = self._handle_result(result)[0]

    def _call(self, endpoint):
        headers = {'Authorization': ''.join('JWT ' + self.jwt_token)}
        result = self.client._call_api(endpoint, headers=headers)
        return result

    def _handle_result(self, result):
        if 'results' in result:
            return result['results']
        elif 'message' in result:
            return result['message']
        elif 'error' in result:
            raise ServerError(result['error'])

    def detail_by_claim(self, claim_num):
        call = self._call(''.join(f'/v0/claims/{claim_num}.json'))
        result = self._handle_result(call)
        return result

    def all_claims_detail(self):
        call = self._call('/v0/claims/view_all_detail.json')
        result = self._handle_result(call)
        return result

    def all_claims(self):
        call = self._call('/v0/claims/view_all.json')
        result = self._handle_result(call)
        return result

    def note_by_claim(self, claim_num):
        call = self._call(''.join(f'/v0/notes/{claim_num}.json'))
        result = self._handle_result(call)
        return result

    def check(self, **kwargs):
        claim_num = 'all'
        from_date = False
        to_date = False
        if 'claim_num' in kwargs:
            claim_num = kwargs['claim_num']
        if 'from_date' in kwargs:
            from_date = datetime.datetime.strptime(kwargs['from_date'], '%Y%m%d').date()
        if 'to_date' in kwargs:
            to_date = datetime.datetime.strptime(kwargs['to_date'], '%Y%m%d').date()
        call = self._call(f'/v0/checks/{from_date}/{to_date}/{claim_num}.json')
        result = self._handle_result(call)
        return result
