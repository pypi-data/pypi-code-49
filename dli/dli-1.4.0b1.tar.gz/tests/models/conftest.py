import pytest

from dli.client.dli_client import DliClient
from unittest.mock import MagicMock


class TestClientMock(DliClient):

    def __init__(self, args, kwargs):
        self._session = MagicMock()
        self._environment = MagicMock()
        self._environment.consumption = ''
        self._analytics_handler = MagicMock()
        self.packages = self._packages()
        self.datasets = self._datasets()

    @property
    def session(self):
        return self._session


@pytest.fixture
def test_client():
    yield TestClientMock('abc', '123')


@pytest.fixture
def client():
    yield TestClientMock('abc', '123')


@pytest.fixture
def package_request():
    return {
            'class': ['Access Requests', 'collection'],
            'properties': {'page': 1, 'pages_count': 1},
            'entities': [{
                'properties': {
                    'packageId': '8137dec0-8569-11e9-8727-f64112f300c3',
                    'name': 'Test Package',
                    'data': {
                        'name': 'Test Package',
                        'topic': 'Test Topic',
                        'keywords': ['test'],
                        'hasAccess': True,
                        'description': 'DESC',
                        'documentation': 'href',
                        'dataSensitivity': 'Private',
                    },
                    'total_records': 1,
                }
            }]
           }


@pytest.fixture
def dataset_request():
    return {
            'data': [
                {'type': 'dataset',
                 'attributes': {
                     'package_id': '59e6a698-975d-11e9-84cc-7e5ef76d533f',
                     'updated_by': 'update@ihsmarkit.com',
                     'keywords': [],
                     'location': {},
                     'has_access': False,
                     'first_datafile_at': '2019-05-06',
                     'short_code': 'TestDataset',
                     'absolute_taxonomy': 'Data-Test',
                     'publishing_frequency': 'Monthly',
                     'name': 'Test DataSet',
                     'last_datafile_at': '2020-01-01',
                     'data_format': 'PARQUET',
                     'created_at': '2019-06-25',
                     'description': 'description',
                     'organisation_name': 'IHS Markit',
                     'created_by': 'creator@ihsmarkit.com',
                     'taxonomy': []
                 },
                 'id': '5b01376e-975d-11e9-8832-7e5ef76d533f'
                 }],
            'meta': {'total_count': 1, 'page': 1,
                     'total_pages': 1}
          }


@pytest.fixture
def dataset_request_v1():
    return {
        'data': [{
            'class': None,
            'title': None,
            'properties': {
                'name': None,
                'keywords': None,
                'loadType': None,
                'location': None,
                'taxonomy': None,
                'createdAt': None,
                'createdBy': None,
                'datasetId': None,
                'packageId': None,
                'updatedAt': None,
                'updatedBy': None,
                'dataFormat': None,
                'contentType': None,
                'description': None,
                'documentation': None,
                'lastDatafileAt': None,
                'firstDatafileAt': None,
                'namingConvention': None,
                'publishingFrequency': None,
                'hasDatafileMonitoring': None,
                'shortCode': None,
                'managerId': None,
                'techDataOpsId': None,
                'accessManagerId': None,
                'tenantId': None,
                'tenantName': None,
                'isInternalWithinOrganisation': None,
                'type': None,
                'tags': None,
                'index_join_field': None,
                'packageName': None,
                'hasAccess': None
                },
            'package_id': '59e6a698-975d-11e9-84cc-7e5ef76d533f',
            'updated_by': 'update@ihsmarkit.com',
            'keywords': [],
            'location': None,
            'links': None,
            'actions': None,
            'rel': None
        }],
        'meta': {
            'total_count': 1, 'page': 1,
            'total_pages': 1}
                   }


@pytest.fixture
def instance_request():
    return {
        'properties': {'pages_count': 1},
        'entities': [{
            'properties': {'datafileId': 1}
        }]
    }
