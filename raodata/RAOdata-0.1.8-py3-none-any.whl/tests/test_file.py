import os
import hashlib
import io

from raodata.File import File


class TestFile:

    def test_init_file(self):
        file = File("file1", "127.0.0.1/url1", "hash1", "2018-09-09T10:11:11")
        assert file.hash == "hash1"
        assert file.local_name == (
                                   os.path.expanduser('~') +
                                   "/.cache/raodata/hash1"
                                  )
        assert file.name == "file1"
        assert file.url == "127.0.0.1/url1"
        assert file.date.year == 2018
        assert file.date.month == 9
        assert file.date.day == 9
        assert file.date.hour == 10
        assert file.date.minute == 11
        assert file.date.second == 11

        file = File("file2", "127.0.0.1/url2", "hash2", "2018-10-09T22:22:22")
        assert file.hash == "hash2"
        assert file.local_name == (
                                   os.path.expanduser('~') +
                                   "/.cache/raodata/hash2"
                                  )
        assert file.name == "file2"
        assert file.url == "127.0.0.1/url2"
        assert file.date.year == 2018
        assert file.date.month == 10
        assert file.date.day == 9
        assert file.date.hour == 22
        assert file.date.minute == 22
        assert file.date.second == 22

    def test_download(self):
        hash = "58d2abeb51810c208828fd101c46541b"
        path = os.path.dirname(os.path.realpath(__file__))
        file = File("file.1", "file://" + path + "/dataset/file.1",
                    hash, "2019-08-08T10:10:10")
        file.local_name = "./tmp/file.1"

        file.download()

        assert file.downloaded is True

        with open("./tmp/file.1", "rb") as f:
            content = f.read()
        f.close()
        assert hashlib.md5(content).hexdigest() == hash

        content = file.contents()
        assert hashlib.md5(content).hexdigest() == hash

        handler = file.handle()
        assert isinstance(handler, io.IOBase) is True
        content = handler.read()
        assert hashlib.md5(content).hexdigest() == hash

        file.save_to("./tmp/file.2")
        with open("./tmp/file.2", "rb") as f:
            content = f.read()
        f.close()
        assert hashlib.md5(content).hexdigest() == hash
