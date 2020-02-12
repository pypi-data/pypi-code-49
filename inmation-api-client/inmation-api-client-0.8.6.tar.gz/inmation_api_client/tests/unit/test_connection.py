import unittest
import getpass
import json

from base64 import b64encode
from urllib import request, parse

from .base import OPTIONS, AUTH, ENV
from inmation_api_client.inclient import Client
from inmation_api_client.model import WSConnectionInfo
from inmation_api_client.options import Options


class TestConnection(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_can_open_connection(self):
        self.client.Connect(host=ENV.host, port=ENV.port, options=OPTIONS)
        self.assertEqual(self.client.GetConnectionInfo.state, WSConnectionInfo.CONNECTED)

    def test_can_close_connection(self):
        self.client.Disconnect()
        self.assertEqual(self.client.GetConnectionInfo.state, WSConnectionInfo.DISCONNECTED)

    def test_can_connect_with_bearer_token(self):
        body = {
            'grant_type': 'password',
            'authority': 'inmation',
            'username': AUTH['auth']['username'],
            'password': AUTH['auth']['password']
        }
        body = parse.urlencode(body)

        req = request.Request('http://{}:{}/api/oauth2/token'.format(ENV.host, str(ENV.port)), data=body.encode())
        req.add_header('Content-Type', 'application/json')
        resp = request.urlopen(req)
        resp = json.loads(resp.read().decode())
        token = resp['access_token']

        opt = Options()
        opt.authorization = "Bearer {}".format(token)

        self.client.Connect(host=ENV.host, port=ENV.port, options=opt)
        self.assertEqual(self.client.GetConnectionInfo.state, WSConnectionInfo.CONNECTED)

    def test_can_connect_with_basic_token(self):
        auth_data = '{}:{}'.format(AUTH['auth']['username'], AUTH['auth']['password'])
        token = b64encode(auth_data.encode()).decode()
        opt = Options()
        opt.authorization = "Basic {}".format(token)

        self.client.Connect(host=ENV.host, port=ENV.port, options=opt)
        self.assertEqual(self.client.GetConnectionInfo.state, WSConnectionInfo.CONNECTED)
        self.client.Disconnect()

    @unittest.skip
    def test_can_connect_using_active_directory(self):
        con = input('Do you want to test the AD connection y/n?')

        if str(con) == 'y':
            name = input('Username:')
            pwd = getpass.getpass('Password:')

            opt = Options({
                'auth': {
                    'username': name,
                    'password': pwd,
                    'authority': 'ad',
                    'grant_type': 'password'
                }
            })

            self.client.Connect(host=ENV.host, port=ENV.port, options=opt)
            self.assertEqual(self.client.GetConnectionInfo.state, WSConnectionInfo.CONNECTED)
            self.client.Disconnect()
