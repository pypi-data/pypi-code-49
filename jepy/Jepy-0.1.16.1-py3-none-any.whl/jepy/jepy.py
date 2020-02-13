import json
import datetime
from jepy.jepy_exceptions import *
from jepy.jepy_client import JepyClient


class Jepy():
    def __init__(self, **kwargs):
        self.prefix = 'v0'
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

    def _call_safely(self, remaining_uri):
        call = self._call(''.join(f'/{self.prefix}/{remaining_uri}'))
        result = self._handle_result(call)
        return result

    def claims(self, **kwargs):
        if len(kwargs) > 1:
            raise ArgumentError('Too many keyword arguments, use only one.')
        else:
            if 'detailed_list' in kwargs:
                if kwargs['detailed_list'] == True:
                    return self._call_safely(f'claims/view_all_detail.json')
            elif 'claim_num' in kwargs:
                return self._call_safely(f"claims/{kwargs['claim_num']}.json")
            else:
                return self._call_safely(f'claims/view_all.json')

    def notes(self, claim_num):
        return self._call_safely(f'notes/{claim_num}.json')

    def checks(self, endpoint='checks', **kwargs):
        claim_num = 'all'
        from_date = False
        to_date = False
        if 'claim_num' in kwargs:
            claim_num = kwargs['claim_num']
        if 'from_date' in kwargs:
            from_date = datetime.datetime.strptime(kwargs['from_date'], '%Y%m%d').date()
        if 'to_date' in kwargs:
            to_date = datetime.datetime.strptime(kwargs['to_date'], '%Y%m%d').date()
        return self._call_safely(f'{endpoint}/{from_date}/{to_date}/{claim_num}.json')

    def reserves(self, **kwargs):
        return self.checks(endpoint='reserves', **kwargs)

    def additional(self, claim_num):
        return self._call_safely(f'additional/{claim_num}.json')
