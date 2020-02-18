import os
import requests

auth_server = 'https://auth.pravah.io:5000'

class Auth:
    def __init__(self, auth_token, client_id=''):
        self.auth_token = self.get_access_token(auth_token)

    def get_access_token(self, auth_token, client_id=''):
        real_path = os.path.join(os.path.dirname(__file__), 'chain.pravah.io.crt')
        res = requests.post(auth_server + '/token', json={
            'authentication_token': auth_token
        }, verify=real_path)

        return res.content
    
    def get_token(self):
        return self.auth_token