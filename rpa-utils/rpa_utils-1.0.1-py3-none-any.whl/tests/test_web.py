import pytest

from rpa_utils import web


class TestWeb:
    """
    pytest -s test_web.py::TestWeb::test_custom_request
    """

    def test_custom_request(self):
        res = web.custom_request('https://jsonplaceholder.typicode.com/todos/1', 'GET')
        assert isinstance(res, dict)
        print(res)


if __name__ == '__main__':
    pytest.main()
