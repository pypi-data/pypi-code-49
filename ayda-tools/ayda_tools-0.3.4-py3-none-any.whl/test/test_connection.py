from ayda_tools.client.connection import ServerConnection
from mock import patch, ANY


def test_server_connection():
    with patch(
        "ayda_tools.client.connection.requests", autospec=True
    ) as requests_mock, patch("ayda_tools.client.connection.sleep"):
        return_data = {"return_data": 2}
        requests_mock.post.return_value.status_code = 200
        requests_mock.post.return_value.json.return_value = return_data
        url = "test.server.com"
        port = "443"
        user = "user"
        password = " password"
        api_call = "test_call"
        data = {"my_data": 1}
        server = ServerConnection(url, port, user, password)
        ret = server.send_server_request(api_call, data)
        requests_mock.post.assert_called_once_with(ANY, auth=ANY, data=data)
        assert ret == return_data
