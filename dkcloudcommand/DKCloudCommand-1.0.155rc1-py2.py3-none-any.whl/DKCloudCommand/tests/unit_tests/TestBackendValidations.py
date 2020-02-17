import os
import requests

from mock import patch
from click.testing import CliRunner

from DKCommon.api_utils.api_utils import validate_and_get_response

from DKCloudCommand.cli.__main__ import dk
from DKCloudCommand.cli.__main__ import Backend
from DKCloudCommand.modules.DKCloudAPI import DKCloudAPI
from DKCloudCommand.modules.DKCloudCommandRunner import DKCloudCommandRunner
from DKCloudCommand.tests.DKCommonUnitTestSettings import (
    DKCommonUnitTestSettings,
    HEADERS,
    MockBackendResponse,
)


class TestBackendValidations(DKCommonUnitTestSettings):

    @patch.object(DKCloudAPI, 'login', return_value='FAKE_TOKEN')
    @patch.object(DKCloudAPI, '_get_common_headers', return_value=HEADERS)
    @patch.object(Backend, 'check_version', return_value=True)
    def test_variation_does_not_exist_status_412(self, backend, _, dkcloudapi_login):
        # Config
        runner = CliRunner()
        mock_command = 'put'
        mock_status = 412
        mock_response = {
            'message': {
                'status': 'failed',
                'error': {
                    'message':
                        'kitchen (alex-cli-vault-child-default),recipe (sr),variation (VAriation1)',
                    'detail':
                        'unable to find the variation named VAriation1 in the recipe sr variations.json'
                }
            }
        }

        # Test
        with patch.object(requests, mock_command,
                          return_value=MockBackendResponse(status_code=mock_status,
                                                           response_dict=mock_response)):
            result = runner.invoke(
                dk, ["or", "-k", "my-kitchen", "-r", "my-recipe", "-y", "VAriation1"]
            )

        wrong_string = os.linesep.join(['u', 'n', 'a', 'b', 'l', 'e'])
        self.assertTrue(wrong_string not in result.output)

    @patch.object(Backend, 'check_version', return_value=True)
    def test_variation_does_not_exist_status_412_list(self, _):
        # Config
        mock_status = 412
        mock_response = {
            'message': {
                'status': 'failed',
                'error': {
                    'message':
                        'kitchen (alex-cli-vault-child-default),recipe (sr),variation (VAriation1)',
                    'detail': [{
                        'severity': 'error',
                        'file': None,
                        'description': 'Error Number 1'
                    }, {
                        'severity': 'error',
                        'file': None,
                        'description': 'Error Number 2'
                    }, {
                        'severity': 'error',
                        'file': None,
                        'description': 'Error Number 3'
                    }]
                }
            }
        }

        # Test
        return_value = MockBackendResponse(status_code=mock_status, response_dict=mock_response)
        try:
            validate_and_get_response(return_value)
            self.assertFalse(True, 'An exception expected in here')
        except Exception as e:
            error_message = str(e)

            self.assertTrue('Error Number 1' in error_message)
            self.assertTrue('Error Number 2' in error_message)
            self.assertTrue('Error Number 3' in error_message)

    def test_format_issues(self):
        # config
        issues = [{
            'severity': 'warning',
            'file': None,
            'description': 'Vault entry vault://alex/fake1 does not exist'
        }, {
            'severity': 'warning',
            'file': None,
            'description': 'Vault entry vault://alex/fake2 does not exist'
        }]

        # test
        output = DKCloudCommandRunner.format_issues(issues)

        # assertions
        self.assertTrue(issues[0]['description'] in output)
        self.assertTrue(issues[1]['description'] in output)
