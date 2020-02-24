import binascii

import urllib3
from requests import Session
import pickle, json, codecs, zlib
from enum import IntEnum, unique

DOMAIN = 'https://westd.dev'
DEMO_TOKEN = 'b79F256208DdD39f88EE5bAEccE01831'


class Filters:
    # THIS FILTER CLASS USES PICKLE WITH NO SAFEGUARDS USE AT OWN RISK
    class Pickle:

        @staticmethod
        def stringify(obj):
            return codecs.encode(pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL), "base64").decode()

        @staticmethod
        def objectify(string):
            try:
                return pickle.loads(codecs.decode(string.encode(), "base64"))
            except Exception as e:
                return string

    # THIS FILTER CLASS LITERALLY EXECUTES CODE INDISCRIMINATELY FROM THE SERVICE USE AT OWN RISK
    class Repr:

        @staticmethod
        def stringify(obj):
            return repr(obj)

        @staticmethod
        def objectify(string):
            try:
                return eval(string)
            except Exception as e:
                return string

    class StringOnly:

        @staticmethod
        def stringify(obj):
            return str(obj)

        @staticmethod
        def objectify(string):
            return string


class Client:
    @unique
    class Status(IntEnum):
        ALIVE = 1
        DEAD = 0

    class NameSpace:

        def __init__(self, client):
            self.client = client

        @property
        def map_names(self):
            return self.client.session.get(f'{self.client.url}/name_space/maps').json()

        @property
        def maps(self):
            return [self.Mapping(self.client, map_name) for map_name in self.map_names]

        @property
        def locked_map_names(self):
            return self.client.session.get(f'{self.client.url}/name_space/locks').json()

        @property
        def locked_maps(self):
            return [self.Mapping(self.client, map_name) for map_name in self.locked_map_names]

        @property
        def name(self):
            return self.client.name_space_name

        def __getitem__(self, map_name: str):
            return Client.NameSpace.Mapping(self.client, map_name)

        def __setitem__(self, map_name: str, items: dict):
            items = {self.client.filter_class.stringify(k): self.client.filter_class.stringify(v) for k, v in
                     items.items()}
            resp = self.client.session.put(self[map_name].url, json=items)
            if resp.status_code == 404:
                self.client.session.post(self[map_name].url, json=items)

        class Mapping:

            NAME_MAX_LENGTH = 128
            KEY_MAX_LENGTH = 128
            VALUE_MAX_LENGTH = 2048

            def __init__(self, client, name, auto_create=True):
                self.client = client
                if len(name) > self.NAME_MAX_LENGTH:
                    ValueError('Map name too long')
                self.url = f'{client.url}/map/{name}'
                if name not in client.name_space.map_names:
                    if auto_create:
                        client.session.post(self.url).json()
                    else:
                        raise ValueError(
                            f'A map with the name "{name}" does not exist in the name_space ("{client.name_space.name}").'
                        )
                self.name = name

            def as_dict(self):
                return {self.client.filter_class.objectify(k): self.client.filter_class.objectify(v) for k, v in
                        self.client.session.get(self.url).json().items()}

            def items(self):
                return self.as_dict().items()

            @property
            def locked_keys(self):
                return list([self.client.filter_class.objectify(key) for key in
                             self.client.session.get(self.url + '/locks').json()])

            @property
            def keys(self):
                return list([self.client.filter_class.objectify(key) for key in
                             self.client.session.get(self.url + '/keys').json()])

            @property
            def values(self):
                return list([self.client.filter_class.objectify(key) for key in
                             self.client.session.get(self.url + '/values').json()])

            def delete(self):
                return self.client.session.delete(self.url).json()

            def __iter__(self):
                return iter(self.keys)

            def __getitem__(self, key):
                key = self.client.filter_class.stringify(key)
                if len(json.dumps(key)) > self.KEY_MAX_LENGTH:
                    raise ValueError('Pickled Item key is too long.')
                return self.client.filter_class.objectify(self.client.session.get(self.url + f'/item/{key}').json())

            def __setitem__(self, key, value):
                key = self.client.filter_class.stringify(key)
                value = self.client.filter_class.stringify(value)
                if len(json.dumps(key)) > self.KEY_MAX_LENGTH:
                    raise ValueError('Pickled Item key is too long.')
                if len(json.dumps(value)) > self.VALUE_MAX_LENGTH:
                    raise ValueError('Pickled Item value is too long.')
                resp = self.client.session.put(self.url + f'/item/{key}', json={key: value})
                if resp.status_code == 404:
                    self.client.session.post(self.url + f'/item/{key}', json={key: value})

            def __len__(self):
                return int(self.client.session.get(self.url + '/length').json())

            def delete_item(self, key):
                key = self.client.filter_class.stringify(key)
                resp = self.client.session.delete(self.url + f'/item/{key}')
                return resp.status_code == 200

            def lock_item(self, key):
                key = self.client.filter_class.stringify(key)
                resp = self.client.session.patch(self.url + f'/item/{key}/lock')
                return resp.status_code == 200

            def unlock_item(self, key):
                key = self.client.filter_class.stringify(key)
                resp = self.client.session.patch(self.url + f'/item/{key}/unlock')
                return resp.status_code == 200

            def transfer_item(self, key, client_id: int):
                key = self.client.filter_class.stringify(key)
                resp = self.client.session.patch(self.url + f'/item/{key}/transfer', json=client_id)
                return resp.status_code == 200

    class Token:

        def __init__(self, client):
            self.client = client

        @property
        def client_ids(self):
            return self.client.session.get(f'{self.client.url}/token/clients').json()

        @property
        def authed_name_spaces(self):
            return self.client.session.get(f'{self.client.url}/token/name_spaces').json()

        @property
        def value(self):
            return self.client.token_value

    def __init__(self, token, name_space='shared',
                 server_url=f'{DOMAIN}/services/wmsb/api', filter_class=Filters.StringOnly):
        self.filter_class = filter_class
        self.status = Client.Status.DEAD
        self._on_the_fly = True
        self.session = Session()
        self.session.headers = {'user-agent': 'west-message-service-bus-python-api/0.0.0'}
        self.url = f'{server_url}'
        self.token_value = token
        self.token = self.Token(self)
        self.name_space_name = name_space
        self.name_space = self.NameSpace(self)
        self.id = None
        self.get_new_client()

    def get_new_client(self, token=None, name_space=None):
        if self.id is not None:
            self.kill()
        resp = self.session.post(f'{self.url}/client',
                                 auth=(token or self.token.value, name_space or self.name_space.name))
        self.id = int(resp.json())
        self.status = self.Status.DEAD

    # opt 1 static DEMO_TOKEN
    # opt 2 static id, DEMO_TOKEN
    # opt 3 non-static
    def kill(*args, **kwargs):
        def token_static(token: str, name_space='', server_url=f'{DOMAIN}/services/wmsb/api'):
            temp_session = Session()
            temp_session.delete(f'{server_url}/kill', auth=(token, name_space))

        def id_static(id: int, token: str, name_space='', server_url=f'{DOMAIN}/services/wmsb/api'):
            temp_session = Session()
            temp_session.delete(f'{server_url}/client/{id}', auth=(token, name_space))

        if type(args[0]) == str:
            return token_static(*args, **kwargs)
        elif type(args[0]) == int:
            return id_static(*args, **kwargs)
        args[0].raise_status()
        args[0].session.delete(f'{args[0].url}/client')
        args[0].status = Client.Status.DEAD

    def raise_status(self):
        pass
        # if self.status == 0:
        #     raise ValueError(f'Client Status is {self.status.name.capitalize()}')

    @property
    def ns(self):
        return self.name_space


if __name__ == "__main__":

    class Bar:
        def __init__(self, bar: int = 1):
            self.bar = bar

        def __repr__(self):
            return f'Bar({self.bar})'


    class Foo:
        def __init__(self, foo: int = 1):
            self.foo = foo

        def __repr__(self):
            return f'Foo({self.foo})'


    # Client.kill(DEMO_TOKEN)

    c = Client(DEMO_TOKEN)
    ns = c.ns

    m = ns['shared']

    ns['shared'][Foo()] = Bar()

    m['hell'] = 1134

    print(m.as_dict())

    m.delete_item('hell')

    print(m.as_dict())

    m.delete()

    print(f'Name Space: {repr(ns.name)}')
    for map in c.name_space.maps:
        print('\t' + repr(map.name))
        for key, value in map.items():
            print('\t\t' + f'{key}: {value}')

    c.kill()
