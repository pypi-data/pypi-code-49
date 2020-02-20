from io import BytesIO

from monitaur import hash_file


def test_hash_file_returns_sha256_hash_of_a_file(mocker):
    mock_open = mocker.patch("builtins.open")
    mock_open.return_value = BytesIO(b"12345")

    result = hash_file("filename")

    mock_open.assert_called_once_with("filename", "rb")
    assert result == "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"
