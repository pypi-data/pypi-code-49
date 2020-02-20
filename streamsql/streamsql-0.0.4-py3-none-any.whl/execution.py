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
        Registers a stream
        :param name:
        Name of the stream to register
        :return:
        Instance of Stream
        """
        return Stream(self.apikey, self.host, name)

    def deregister_stream(self, name):
        """
        Deregisters a stream
        :param name:
        Name of stream to deregister
        :return:
        None
        """
        return Stream(self.apikey, self.host, name).delete()

    def register_lookup(self, name):
        """
        Registers a lookup
        :param name:
        Name of register to lookup
        :return:
        Instance of Lookup
        """
        return Lookup(self.apikey, self.host, name)

    def deregister_lookup(self, name):
        """
        Deregisters a lookup
        :param name:
        Name of register to deregister
        :return:
        None
        """
        return Lookup(self.apikey, self.host, name).delete()

    def register_transformation(self, name):
        """
        Registers a transformation
        :param name:
        Name of transformation to register
        :return:
        Instance of Transformation
        """
        return Transformation(self.apikey, self.host, name)

    def deregister_transformation(self, name):
        """
        Deregisters a transformation
        :param name:
        Name of transformation to deregister
        :return:
        None
        """
        return Transformation(self.apikey, self.host, name).delete()

    def get_resources(self):
        """
        Returns all table resources for the given API key
        :return:
        dict() of resources
        """
        headers = dict()
        headers[APIKEY_HEADER] = self.apikey

        url = "{host}{path}".format(host=self.host, path=RESOURCE_PATH)
        r = requests.get(url=url, headers=headers)

        if r.status_code >= 400:
            raise ValueError(r.text)

        return json.loads(r.text)

    def get_transformations(self):
        """
        Returns all transformation for a given API key
        :return:
        dict() of transformations
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
        Description of a given transformation
        :param name:
        Name of a transformation
        :return:
        dict() of transformation Attributes
        """
        pass

    def get_transformation_status(self, name):
        """
        Status of a transformation
        :param name:
        Name of the transformation
        :return:
        dict() containing the status: {"status": <status_value>}
        """

        url = "{host}{path}".format(host=self.host, path=STATUS_PATH)
        headers = {'X-StreamSQL-Key': self.apikey}

        # Adds args to uri
        scheme, netloc, path, query_string, fragment = urlsplit(url)
        query_params = parse_qs(query_string)

        query_params['name'] = [name]

        new_query_string = urlencode(query_params, doseq=True)
        url = urlunsplit((scheme, netloc, path, new_query_string, fragment))

        r = requests.get(url=url, headers=headers)
        if r.status_code >= 400:
            raise ValueError(r.text)
        return json.loads(r.text)


class Resource:
    """
    A generic resource type that provides functions to create configurations, commit, and delete
    """
    data_format = JSON

    def __init__(self, apikey, host, name, resource):
        self.apikey = apikey
        self.name = name
        self.host = host
        self.resource = resource

    def format(self, data_format):
        """
        Sets format options
        :param data_format:
        Format of data
        :return:
        Self
        """
        self.data_format = data_format
        return self

    def commit(self):
        """
        Validates configurations then creates and sends
        :return:
        None
        """
        self._validate()
        self._create()

    def _validate(self):
        """
        Checks that apikey, data format, and name are all valid formats
        :return:
        None
        """
        # Check that apikey UUID is correct format
        if not re.match(RE_API_KEY, self.apikey):
            raise ValueError("Invalid Apikey")

        if self.data_format not in FORMAT_TYPES:
            raise ValueError("Invalid Format. Not one of {fmt}".format(fmt=FORMAT_TYPES))

        if not re.match(RE_RESOURCE_NAME, self.name):
            raise ValueError("Invalid Name. Uppercase, Lowercase, and Numeric characters only")

    def _create(self):
        """
        Creates the payload for the resource and sends
        :return:
        None
        """
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
        """
        Deletes the given resource
        :return:
        None
        """
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
    """
    Creates a Stream Resource using the Resource base class
    """
    def __init__(self, apikey, host, name):
        super().__init__(apikey, host, name, STREAM_RESOURCE)


class Lookup(Resource):
    """
    Creates a Lookup Resource using the Resource base class
    """
    def __init__(self, apikey, host, name):
        super().__init__(apikey, host, name, LOOKUP_RESOURCE)


class Transformation:
    """
    Allows the ability to interact with transformations.
    """
    fields = []
    field = namedtuple('field', 'raw, alias, type')

    def __init__(self, apikey, host, name):
        self.apikey = apikey
        self.host = host
        self.name = name

    def source(self, name, type):
        """
        Sets the source resource for the transformation
        :param name:
        Name of the source resource
        :param type:
        Type of resource
        :return:
        Self
        """
        tbl = Table(name, type)

        # Validates resouce
        tbl.validate()
        self.source_tbl = tbl
        return self

    def sink(self, name, type):
        """
        Sets the sink resource for the transformation
        :param name:
        Name of the sink resource
        :param type:
        Type of resource
        :return:
        Self
        """
        tbl = Table(name, type)

        # Validates resource
        tbl.validate()
        self.sink_tbl = tbl
        return self

    def query(self, query):
        """
        Sets the query for the transformation
        :param query:
        SQL Query string
        :return:
        Self
        """
        self.q = query
        return self

    def extract(self, raw, alias, type):
        """
        Extracts field from JSON data and provides a type and alias
        :param raw:
        The raw field in the JSON object where the path consists of period join keys to the value
        Ex.
        {
            "key1":{
                "key2": "value"
            }
        }
        The raw value would be: "key1.key2"
        :param alias:
        The alias for the path to a given field in the JSON object
        :param type:
        Type of the field
        :return:
        Self
        """
        self.fields.append(self.field(raw, alias, type))
        return self

    def commit(self):
        """
        Validates configuration then builds and sends
        :return:
        None
        """
        self._validate()
        self._send(self._build())

    def _validate(self):
        """
        Validates names and fields
        :return:
        None
        """
        self._validate_name()
        self._validate_fields()

    def _validate_name(self):
        """
        Validates transform name matches regex
        :return:
        None
        """
        if not re.match(RE_TRANSFORM_NAME, self.name):
            raise ValueError("Invalid Transform Name. Uppercase, Lowercase, and Numeric characters only")

    def _validate_fields(self):
        """
        Validates that field names and aliases match regex
        :return:
        None
        """
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
        """
        Builds transform payload
        :return:
        dict() of transformation attributes
        """
        payload = dict()
        payload['name'] = self.name
        payload['source'] = self.source_tbl.build()
        payload['sink'] = self.sink_tbl.build()
        payload['query'] = self._build_query()

        return payload

    def _build_query(self):
        """
        Builds query information including appending fields, aliases, and options together
        for backend usage
        :return:
        dict() of query attributes
        """
        query = dict()
        query['sql'] = self.q
        query['rawFields'] = ""
        query['fieldTypes'] = ""
        query['fields'] = ""

        # Joins fields. Required for backend
        for idx, field in enumerate(self.fields):
            sep = "," if idx is not 0 else ""

            query['rawFields'] = "{fields}{sep}{field}".format(fields=query['rawFields'], sep=sep, field=field[0])
            query['fields'] = "{fields}{sep}{field}".format(fields=query['fields'], sep=sep, field=field[1])
            query['fieldTypes'] = "{fields}{sep}{field}".format(fields=query['fieldTypes'], sep=sep, field=field[2])

        return query

    def _send(self, payload):
        """
        Posts transform attributes to API for creation
        :param payload:
        dict() of transformation attributes
        :return:
        None
        """
        headers = dict()
        headers[APIKEY_HEADER] = self.apikey

        url = "{host}{path}".format(host=self.host, path=TRANSFORM_PATH)
        r = requests.post(url=url, data=json.dumps(payload), headers=headers)

        if r.status_code >= 400:
            raise ValueError(r.text)

    def delete(self):
        """
        Deletes transformation
        :return:
        None
        """
        payload = dict()
        payload['name'] = self.name

        headers = dict()
        headers[APIKEY_HEADER] = self.apikey

        url = "{host}{path}".format(host=self.host, path=TRANSFORM_PATH)
        r = requests.delete(url=url, data=json.dumps(payload), headers=headers)

        if r.status_code >= 400:
            raise ValueError(r.text)


class Table:
    """
    Contains the values that transformations need to treat resources like tables
    """
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def validate(self):
        """
        Validates the name and type of table
        :return:
        None
        """
        self._validate_name()
        self._validate_type()

    def build(self):
        """
        Builds the table
        :return:
        dict() with table attributes
        """
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
