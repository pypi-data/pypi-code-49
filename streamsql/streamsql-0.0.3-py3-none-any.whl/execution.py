import re
import requests
import json
from collections import namedtuple
from urllib.parse import parse_qs, urlsplit, urlunsplit, urlencode
from .const import *


class Execution:
    """
    The Execution object provides an interface to connect to the StreamSQL Execution environment.
    This enables the creation, deletion, and introspection of stream, tables, and transforms.
    """
    def __init__(self, apikey, host):
        self.apikey = apikey
        self.host = host

    def register_stream(self, name):
        """

        :param name:
        :return:
        """
        return Stream(self.apikey, self.host, name)

    def deregister_stream(self, name):
        """

        :param name:
        :return:
        """
        return Stream(self.apikey, self.host, name).delete()

    def register_lookup(self, name):
        """

        :param name:
        :return:
        """
        return Lookup(self.apikey, self.host, name)

    def deregister_lookup(self, name):
        """

        :param name:
        :return:
        """
        return Lookup(self.apikey, self.host, name).delete()

    def register_transformation(self, name):
        """

        :param name:
        :return:
        """
        return Transformation(self.apikey, self.host, name)

    def deregister_transformation(self, name):
        """

        :param name:
        :return:
        """
        return Transformation(self.apikey, self.host, name).delete()

    def get_resources(self):
        """

        :return:
        """
        headers = dict()
        headers[APIKEY_HEADER] = self.apikey

        url = "{host}{path}".format(host=self.host, path=RESOURCE_PATH)
        r = requests.get(url=url,  headers=headers)

        if r.status_code >= 400:
            raise ValueError(r.text)

        return json.loads(r.text)

    def get_transformations(self):
        """

        :return:
        """
        headers = dict()
        headers[APIKEY_HEADER] = self.apikey

        url = "{host}{path}".format(host=self.host, path=TRANSFORM_PATH)
        r = requests.get(url=url, headers=headers)

        if r.status_code >= 400:
            raise ValueError(r.text)

        return json.loads(r.text)

    def describe_transformation(self, name):
        """

        :param name:
        :return:
        """
        pass

    def get_transformation_status(self, name):
        """

        :param name:
        :return:
        """

        url = "{host}{path}".format(host=self.host, path=STATUS_PATH)
        headers = {'X-StreamSQL-Key': self.apikey}

        scheme, netloc, path, query_string, fragment = urlsplit(url)
        query_params = parse_qs(query_string)

        query_params['name'] = [name]


        new_query_string = urlencode(query_params, doseq=True)
        url = urlunsplit((scheme, netloc, path, new_query_string, fragment))

        r = requests.get(url=url, headers=headers)
        print(r.text)
        return r.text

class Resource:
    data_format = JSON

    def __init__(self, apikey, host, name, resource):
        self.apikey = apikey
        self.name = name
        self.host = host
        self.resource = resource

    def format(self, data_format):
        self.data_format = data_format
        return self

    def commit(self):
        self._validate()
        self._create()

    def _validate(self):
        # Check that apikey UUID is correct format
        if not re.match(RE_API_KEY, self.apikey):
            raise ValueError("Invalid Apikey")

        if self.data_format not in FORMAT_TYPES:
            raise ValueError("Invalid Format. Not one of {fmt}".format(fmt=FORMAT_TYPES))

        if not re.match(RE_RESOURCE_NAME, self.name):
            raise ValueError("Invalid Name. Uppercase, Lowercase, and Numeric characters only")

    def _create(self):
        payload = dict()
        payload['name'] = self.name
        payload['type'] = self.resource

        headers = dict()
        headers[APIKEY_HEADER] = self.apikey

        url = "{host}{path}".format(host=self.host, path=RESOURCE_PATH)
        r = requests.post(url=url, data=json.dumps(payload), headers=headers)

        if r.status_code >= 400:
            raise ValueError(r.text)

    def delete(self):
        self._validate()
        payload = dict()
        payload['name'] = self.name
        payload['type'] = self.resource

        headers = dict()
        headers[APIKEY_HEADER] = self.apikey

        url = "{host}{path}".format(host=self.host, path=RESOURCE_PATH)
        r = requests.delete(url=url, data=json.dumps(payload), headers=headers)

        if r.status_code >= 400:
            raise ValueError(r.text)


class Stream(Resource):
    def __init__(self, apikey, host, name):
        super().__init__(apikey, host, name, STREAM_RESOURCE)


class Lookup(Resource):
    def __init__(self, apikey, host, name):
        super().__init__(apikey, host, name, LOOKUP_RESOURCE)


class Transformation:
    fields = []
    field = namedtuple('field', 'raw, alias, type')

    def __init__(self, apikey, host, name):
        self.apikey = apikey
        self.host = host
        self.name = name

    def source(self, name, type):
        tbl = Table(name, type)
        tbl.validate()
        self.source_tbl = tbl
        return self

    def sink(self, name, type):
        tbl = Table(name, type)
        tbl.validate()
        self.sink_tbl = tbl
        return self

    def query(self, query):
        self.q = query
        return self

    def extract(self, raw, alias, type):
        self.fields.append(self.field(raw, alias, type))
        return self

    def commit(self):
        self._validate()
        return self._send(self._build())

    def _validate(self):
        self._validate_fields()

    def _validate_name(self):
        if not re.match(RE_TRANSFORM_NAME, self.name):
            raise ValueError("Invalid Transform Name. Uppercase, Lowercase, and Numeric characters only")

    def _validate_fields(self):
        for field in self.fields:
            self._validate_alias(field[1])
            self._validate_type(field[2])

    def _validate_alias(self, alias):
        if not re.match(RE_ALIAS_NAME, alias):
            raise ValueError(
                "Invalid Alias: '{alias}'. Uppercase, Lowercase, and Numeric characters only".format(alias=alias))

    def _validate_type(self, type):
        if type not in SQL_TYPES:
            raise ValueError(
                "Invalid Type: '{type}'. Valid Types: {valid}".format(type=type, valid=SQL_TYPES))

    def _build(self):
        payload = dict()
        payload['name'] = self.name
        payload['source'] = self.source_tbl.build()
        payload['sink'] = self.sink_tbl.build()
        payload['query'] = self._build_query()

        return payload

    def _build_query(self):
        query = dict()
        query['sql'] = self.q
        query['rawFields'] = ""
        query['fieldTypes'] = ""
        query['fields'] = ""

        for idx, field in enumerate(self.fields):
            sep = "," if idx is not 0 else ""

            query['rawFields'] = "{fields}{sep}{field}".format(fields=query['rawFields'], sep=sep, field=field[0])
            query['fields'] = "{fields}{sep}{field}".format(fields=query['fields'], sep=sep, field=field[1])
            query['fieldTypes'] = "{fields}{sep}{field}".format(fields=query['fieldTypes'], sep=sep, field=field[2])

        return query

    def _send(self, payload):
        print(json.dumps(payload, indent=2))

        headers = dict()
        headers[APIKEY_HEADER] = self.apikey

        url = "{host}{path}".format(host=self.host, path=TRANSFORM_PATH)
        r = requests.post(url=url, data=json.dumps(payload), headers=headers)

        if r.status_code >= 400:
            raise ValueError(r.text)

    def delete(self):
        payload = dict()
        payload['name'] = self.name

        headers = dict()
        headers[APIKEY_HEADER] = self.apikey

        url = "{host}{path}".format(host=self.host, path=TRANSFORM_PATH)
        r = requests.delete(url=url, data=json.dumps(payload), headers=headers)

        if r.status_code >= 400:
            raise ValueError(r.text)


class Table:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def validate(self):
        self._validate_name()
        self._validate_type()

    def build(self):
        payload = dict()
        payload['name'] = self.name
        payload['type'] = self.type
        return payload

    def _validate_name(self):
        if not re.match(RE_TABLE_NAME, self.name):
            raise ValueError("Invalid Name. Uppercase, Lowercase, and Numeric characters only")

    def _validate_type(self):
        if self.type not in RESOURCE_TYPES:
            raise ValueError("Invalid Type. Use one of: {type}".format(type=RESOURCE_TYPES))
