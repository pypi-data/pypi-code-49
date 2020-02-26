import requests
import ipfshttpclient
from functools import lru_cache
import functools
from datetime import datetime, timedelta
import magic
from zml.crypt import *
import json


def timed_cache(**timedelta_kwargs):

    def _wrapper(f):
        update_delta = timedelta(**timedelta_kwargs)
        next_update = datetime.utcnow() - update_delta
        # Apply @lru_cache to f with no cache size limit
        f = functools.lru_cache(None)(f)

        @functools.wraps(f)
        def _wrapped(*args, **kwargs):
            nonlocal next_update
            now = datetime.utcnow()
            if now >= next_update:
                f.cache_clear()
                next_update = now + update_delta
            return f(*args, **kwargs)
        return _wrapped
    return _wrapper


class Backend:

    def load(self):
        raise NotImplementedError("Method load not implemented.")

    def save(self):
        raise NotImplementedError("Method save not implemented.")


class FileBackend(Backend):

    def load(self, filename):
        with open(filename) as f:
            raw = f.read()
        mime_type = magic.from_buffer(raw, mime=True)
        return raw, mime_type

    def save(self, filename, code):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(code)


class IpfsBackend(Backend):

    def __init__(self):
        self.client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

    @lru_cache()
    def get_peer_id(self):
        return self.client.key.list()['Keys'][0]['Id']

    @lru_cache()
    def get_peer_cid(self):
        peer_id = self.get_peer_id()
        profile_cid = self.client.name.resolve(peer_id)['Path'].split('/')[-1]
        return profile_cid

    @lru_cache()
    def get_profile(self):
        profile_cid = self.get_peer_cid()
        return self.client.cat(profile_cid).decode('utf-8')

    def cache_clear(self):
        self.get_peer_id.cache_clear()
        self.get_profile.cache_clear()

    def add_str(self, code):
        return self.client.add_str(code)

    def add_bytes(self, code):
        return self.client.add_bytes(code)

    def load(self, address):
        if address.startswith('/ipns/'):
            address = self.client.resolve(address)['Path']
        raw = self.client.cat(address)
        mime_type = magic.from_buffer(raw, mime=True)
        if mime_type in ['image/jpeg', 'image/png', 'image/gif']:
            res = raw
        else:
            try:
                res = raw.decode('utf-8')
                mime_type = 'text/zml'
            except:
                return raw, 'crypt/zml'
        return res, mime_type

    def encrypt(self, raw, key):
        return encrypt(raw, key)

    def decrypt(self, raw, key):
        return decrypt(raw, key)

    def save(self, code):
        if isinstance(code, str):
            return self.add_str(code)
        elif isinstance(code, bytes):
            return self.add_bytes(code)
        else:
            raise "Content must be string or bytes"

    def publish(self, ipfs_path, key=None):
        return self.client.name.publish(ipfs_path, key=key)

    def generate_key(self, name):
        try:
            status = self.client.key.gen(name, type='ed25519')
        except:
            return self.get_key(name)
        return status

    def get_key(self, name):
        status = self.client.key.list()
        if 'Keys' in status:
            for item in status['Keys']:
                if 'Name' in item and item['Name'] == name:
                    return item

    def resolve(self, name, stream=False):
        if stream:
            r = requests.get('http://localhost:5001/api/v0/name/resolve?arg={}&stream=1'.format(name), stream=True)
            for line in r.iter_lines():
                if line:
                    res = json.loads(line)
                    if 'Path' in res:
                        return res['Path']
        else:
            return self.client.name.resolve(name)['Path']


class RestBackend(Backend):

    def load(self, address):
        url = address
        if not url.startswith('https'):
            url = 'https://' + url
            response = requests.get(url)
        root = response.json()
        mime_type = 'text/html'
        return root, mime_type

    def save(self, code):
        pass
