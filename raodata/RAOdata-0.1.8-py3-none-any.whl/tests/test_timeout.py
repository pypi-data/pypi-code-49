import hashlib


from raodata.File import File


class TestFile:

    def test_download(self, httpserver):
        httpserver.expect_oneshot_request("/url").respond_with_data("", 504)
        httpserver.expect_oneshot_request("/url").respond_with_data("", 504)
        httpserver.expect_oneshot_request("/url").respond_with_data("", 504)
        httpserver.expect_oneshot_request("/url").respond_with_data("", 504)
        httpserver.expect_oneshot_request("/url").respond_with_data("", 504)
        httpserver.expect_oneshot_request("/url").respond_with_data("OK", 200)

        url = httpserver.url_for("/url")

        hash = hashlib.md5("OK".encode("utf-8")).hexdigest()
        file = File("file.3", url,
                    hash, "2019-08-08T10:10:10")
        file.local_name = "./tmp/file.3"

        file.download()

        assert file.downloaded is True

        with open("./tmp/file.3", "rb") as f:
            content = f.read()
        f.close()
        assert hashlib.md5(content).hexdigest() == hash
