import pytest

from unittest.mock import MagicMock
from unittest.mock import call

from dli.client.dli_client import DliClient


class Client(DliClient):

    def __init__(self):
        self.logger = MagicMock()
        self._session = MagicMock()

    @property
    def session(self):
        return self._session

    def log_debug(self):
        self.logger.debug('some debug message')

    def log_info(self):
        self.logger.info('some info message')

    def log_warning(self):
        self.logger.warning('some warning message')

    def log_error(self):
        self.logger.error('some error message')

    def log_exception(self):
        raise Exception('some exception message')


@pytest.fixture
def client():
    yield Client()


class TestComponentsAspectWrapper:

    def test_debug_logging_is_logged_correctly(self, client):
        client.log_debug()

        assert client.logger.info.call_count == 1, 'One call at info level to log details of the function.'
        assert client.logger.debug.call_args_list == [call('some debug message')]
        assert client.logger.warning.call_count == 0
        assert client.logger.error.call_count == 0

    def test_info_logging_is_logged_correctly(self, client):
        client.log_info()

        assert client.logger.debug.call_count == 0
        assert client.logger.info.call_count == 2
        assert client.logger.info.call_args_list[1] == call('some info message')
        assert client.logger.warning.call_count == 0
        assert client.logger.error.call_count == 0

    def test_warning_logging_is_logged_correctly(self, client):
        client.log_warning()

        assert client.logger.info.call_count == 1, 'One call at info level to log details of the function.'
        assert client.logger.debug.call_count == 0
        assert client.logger.warning.call_args_list == [call('some warning message')]
        assert client.logger.error.call_count == 0

    def test_error_logging_is_logged_correctly(self, client):
        client.log_error()

        assert client.logger.info.call_count == 1, 'One call at info level to log details of the function.'
        assert client.logger.debug.call_count == 0
        assert client.logger.warning.call_count == 0
        assert client.logger.error.call_args_list == [call('some error message')]

    def test_exception_logging_is_logged_correctly(self, client):
        with pytest.raises(Exception) as excinfo:
            client.log_exception()
            assert 'some exception message' in str(excinfo.value)

        assert client.logger.info.call_count == 1
        assert client.logger.debug.call_count == 0
        assert client.logger.warning.call_count == 0
        assert client.logger.error.call_count == 0
        assert client.logger.exception.call_count == 1, 'Use logger exception to capture the stack trace.'
        message, args = client.logger.exception.call_args_list[0]
        assert message == ('Unhandled Exception',)
        assert 'locals' in args['extra'], 'Local variables should be added to the message'
        assert args['stack_info'], 'Stack info should be enabled'
        assert len(args['extra']['locals']) > 0, 'The local variables must not be empty'
        # assert client.logger.exception.call_args_list == [call('Unhandled Exception', stack_info=True)]
