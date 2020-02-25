import unittest
from datetime import datetime
from pprint import pprint

from aistac.handlers.abstract_handlers import ConnectorContract


class ConnectorContractTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_runs(self):
        """Basic smoke test"""
        ConnectorContract('uri', 'module_name', 'handler', kwarg1='One')

    def test_immutable(self):
        sc = ConnectorContract('uri', 'module_name', 'handler', kwarg1='One')
        control = {'uri_raw': 'uri', 'uri_parsed': {'address': 'uri','schema': '', 'netloc': '', 'path': 'uri', 'params': [], 'query': {}, 'fragment': ''},
                   'module_name': 'module_name',
                   'handler': 'handler',
                   'version': "v00",
                   'kwargs': {'kwarg1': 'One'}}
        self.assertDictEqual(control, sc.to_dict())
        with self.assertRaises(AttributeError) as context:
            sc.uri_raw = "new"
        self.assertTrue("The attribute 'uri_raw' is immutable once set and can not be changed" in str(context.exception))

    def test_empty_uri(self):
        with self.assertRaises(ValueError) as context:
            ConnectorContract(None, None, None)
        self.assertTrue("The uri must be a valid string" in str(context.exception))
        with self.assertRaises(ValueError) as context:
            ConnectorContract("", None, None)
        self.assertTrue("The uri must be a valid string" in str(context.exception))
        sc = ConnectorContract('a', None, None)
        result = sc.to_dict()
        control = {'uri_raw': 'a', 'uri_parsed': {'address': 'a', 'schema': '', 'netloc': '', 'path': 'a', 'params': [],
                                               'query': {}, 'fragment': ''},
                   'module_name': None,
                   'handler': None,
                   'version': "v00",
                   'kwargs': {}}
        self.assertDictEqual(control, result)

    def test_min_uri(self):
        uri = "file.csv"
        sc = ConnectorContract(uri, 'base.module_name', 'Handler')
        result = sc.to_dict()
        control = {'uri_raw': 'file.csv', 'uri_parsed': {'address': 'file.csv', 'schema': '', 'netloc': '',
                                                     'path': 'file.csv', 'params': [], 'query': {}, 'fragment': ''},
                   'module_name': 'base.module_name',
                   'handler': 'Handler',
                   'version': "v00",
                   'kwargs': {}}
        self.assertDictEqual(control, result)

    def test_full_uri(self):
        uri = "http://user:pass@NetLoc:80/path/file.csv;parameters2;param3?query=argument&query2=attr#fragment"
        sc = ConnectorContract(uri, 'base.module_name', 'Handler', kwarg1='One')
        result = sc.to_dict()
        control = {'uri_raw': 'http://user:pass@NetLoc:80/path/file.csv;parameters2;param3?query=argument&query2=attr#fragment',
                   'uri_parsed': {'address': 'http://user:pass@netloc:80/path/file.csv', 'schema': 'http',
                                  'netloc': 'user:pass@NetLoc:80', 'path': '/path/file.csv',
                                  'params': ['parameters2', 'param3'], 'query': {'query': 'argument', 'query2': 'attr'},
                                  'fragment': 'fragment', 'username': 'user', 'password': 'pass', 'hostname': 'netloc',
                                  'port': 80},
                   'module_name': 'base.module_name',
                   'handler': 'Handler',
                   'version': "v00",
                   'kwargs': {'kwarg1': 'One'}}
        self.assertDictEqual(control, result)

    def test_get(self):
        uri = "http://user:pass@NetLoc:80/path/file.csv;parameters2;param3?query1=value1&query2=value2#fragment"
        cc = ConnectorContract(uri, 'base.module_name', 'Handler', kwarg1='kwOne', kwarg2='kwTwo')
        self.assertEqual('value1', cc.get_key_value('query1'))
        self.assertEqual('kwTwo', cc.get_key_value('kwarg2'))
        self.assertEqual('NoValue', cc.get_key_value('kwarg3', 'NoValue'))
        self.assertEqual({'query1': 'value1', 'query2': 'value2'}, cc.query)
        self.assertEqual({'kwarg1': 'kwOne', 'kwarg2': 'kwTwo'}, cc.kwargs)

    def test_parse_address(self):
        uri = "http://user:pass@NetLoc:80/path/file.csv;parameters2;param3?query1=value1&query2=value2#fragment"
        result = ConnectorContract.parse_address(uri=uri)
        self.assertEqual('http://user:pass@netloc:80/path/file.csv', result)
        result = ConnectorContract.parse_address(uri=uri, with_credentials=True)
        self.assertEqual('http://user:pass@netloc:80/path/file.csv', result)
        result = ConnectorContract.parse_address(uri=uri, with_port=True)
        self.assertEqual('http://user:pass@netloc:80/path/file.csv', result)
        # False
        result = ConnectorContract.parse_address(uri=uri, with_credentials=False)
        self.assertEqual('http://netloc:80/path/file.csv', result)
        result = ConnectorContract.parse_address(uri=uri, with_port=False)
        self.assertEqual('http://user:pass@netloc/path/file.csv', result)
        result = ConnectorContract.parse_address(uri=uri, with_credentials=False, with_port=False)
        self.assertEqual('http://netloc/path/file.csv', result)
        # minimal
        uri = "file.csv"
        result = ConnectorContract.parse_address(uri=uri)
        self.assertEqual('file.csv', result)
        result = ConnectorContract.parse_address(uri=uri, with_credentials=True, with_port=True)
        self.assertEqual('file.csv', result)
        result = ConnectorContract.parse_address(uri=uri, with_credentials=False, with_port=False)
        self.assertEqual('file.csv', result)

    def test_parse_elemets(self):
        uri = "http://user:pass@NetLoc:80/path/file.csv;parameters2;param3?query1=value1&query2=value2#fragment"
        schema, netloc, path = ConnectorContract.parse_address_elements(uri=uri)
        self.assertEqual('http', schema)
        self.assertEqual('user:pass@netloc:80', netloc)
        self.assertEqual('/path/file.csv', path)
        # False
        schema, netloc, path = ConnectorContract.parse_address_elements(uri=uri, with_credentials=False, with_port=False)
        self.assertEqual('http', schema)
        self.assertEqual('netloc', netloc)
        self.assertEqual('/path/file.csv', path)

    def test_parse_query(self):
        uri = "file.csv"
        query = ConnectorContract.parse_query(uri)
        self.assertEqual({}, query)
        uri = "http://user:pass@NetLoc:80/path/file.csv;parameters2;param3?query1=value1&query2=value2#fragment"
        query = ConnectorContract.parse_query(uri)
        self.assertEqual({'query1': 'value1', 'query2': 'value2'}, query)

    def test_uri(self):
        uri = "s3://bucket/path/aistac_manager_task_connector.pickle"
        cc = ConnectorContract(uri, 'module.name', 'Handler')
        self.assertEqual(uri, cc.uri)
        # VERSION
        uri = "s3://bucket/path/aistac_manager_task_connector${VERSION}.pickle"
        cc = ConnectorContract(uri, 'module.name', 'Handler')
        self.assertEqual("s3://bucket/path/aistac_manager_task_connector_v00.pickle", cc.uri)
        cc = ConnectorContract(uri, 'module.name', 'Handler', version="v1.01")
        self.assertEqual("s3://bucket/path/aistac_manager_task_connector_v1.01.pickle", cc.uri)
        # DATETIME
        uri = "s3://bucket/path/aistac_manager_task_connector${TO_DAYS}.pickle"
        cc = ConnectorContract(uri, 'module.name', 'Handler')
        control = f"s3://bucket/path/aistac_manager_task_connector{datetime.now().strftime('_%Y%m%d')}.pickle"
        self.assertEqual(control, cc.uri)
        # VERSION & DATETIME
        uri = "s3://bucket/path/aistac_manager_task_connector${VERSION}${TO_DAYS}.pickle"
        cc = ConnectorContract(uri, 'module.name', 'Handler', version="v1.01")
        control = f"s3://bucket/path/aistac_manager_task_connector_v1.01{datetime.now().strftime('_%Y%m%d')}.pickle"
        self.assertEqual(control, cc.uri)

    def test_version(self):
        uri = "s3://bucket/path/aistac_manager_task_connector.pickle"
        cc = ConnectorContract(uri, 'module.name', 'Handler')
        self.assertEqual("v00", cc.version)
        cc = ConnectorContract(uri, 'module.name', 'Handler', version='v1.00')
        self.assertEqual("v1.00", cc.version)


if __name__ == '__main__':
    unittest.main()
