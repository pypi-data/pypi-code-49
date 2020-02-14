import pytest

from unittest.mock import MagicMock
from dli.client.dli_client import DliClient
from dli.client.exceptions import CatalogueEntityNotFoundException


class Client(DliClient):
    def __init__(self):
        self._session = MagicMock()
        self._environment = MagicMock()
        self._environment.accounts = 'https://local.test/'

    @property
    def session(self):
        return self._session


@pytest.fixture
def client():
    yield Client()


class TestAccounts:
    def test_get_account(self, client):
        client.session.get().json.return_value = {
          'data': [
            {
              'attributes': {
                'tenant_id': '9516c0ba-ba7e-11e9-8b34-000c6c0a981f',
                'organisation_id': '9516c0ba-ba7e-11e9-8b34-000c6c0a981f',
                'data': {
                  'contacts': [
                    {
                      'name': 'Michael Salerno',
                      'role': 'Global Head of Rights Management',
                      'type': 'Business',
                      'email': 'CARMDataLakeChecks@ihsmarkit.com'
                    }
                  ],
                  'division': 'Other',
                  'cost_code': 'N/A',
                  'description': 'Content acquisition and rights management team',
                  'is_internal': True
                },
                'name': 'CARM'
              },
              'id': 'test'
            }
          ],
        }

        account = client.get_account_by_name('CARM')
        assert account.id == 'test'

    def test_get_account_no_results(self, client):
        client.session.get().json.return_value = {'data': []}
        with pytest.raises(CatalogueEntityNotFoundException):
            client.get_account_by_name('CARM')
