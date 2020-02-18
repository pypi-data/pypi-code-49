from tests.base_test import BaseTest
from disco.core.exceptions import RequestException, BucketPathsException, \
    DiscoErrorCodes
from disco.core.exception_factory import ExceptionFactory


class TestUtils(BaseTest):

    def test_from_response_no_message_with_http_status_code(self):
        http_status_code = 404
        json_response = {'code': http_status_code}

        result = ExceptionFactory.from_response(json_response)

        assert isinstance(result, RequestException)
        assert str(result) == f'{RequestException.DEFAULT_MESSAGE} ({json_response.get("code")})'
        assert result.additional_info == {}

    def test_from_response_no_error_code(self):
        error_message = self.random_str('error_message')
        additional_info = {'errorCode': None}
        json_response = {'error': {'message': error_message}, 'additional_info': additional_info}

        result = ExceptionFactory.from_response(json_response)

        assert isinstance(result, RequestException)
        assert str(result) == error_message
        assert result.additional_info == additional_info

    def test_from_response_error_code_bucket_paths(self):
        error_message = self.random_str('error_message')
        bucket_paths_errors = self.random_dict(key_prefix='bucket_paths_errors')
        additional_info = {'errorCode': DiscoErrorCodes.BucketPaths, 'bucketPaths': bucket_paths_errors}
        json_response = {'error': {'message': error_message}, 'additional_info': additional_info}

        result = ExceptionFactory.from_response(json_response)

        assert isinstance(result, BucketPathsException)
        assert str(result) == error_message
        assert result.bucket_paths_errors == bucket_paths_errors
