import hashlib
import os
from dateutil import parser
import types
from raodata.File import File
from raodata.Data import Data
import requests_mock


class TestTimeoute:

    i = 0

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

    def test_get_types_by_instruments_meta(self):

        self.i = 0
        with requests_mock.Mocker() as m:

            self.response = """
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
    <SOAP-ENV:Body>
        <SOAP-ENV:typesByInstrumentsListResponse>
            <typesByInstrumentsListResponse>
                <response>
                    <instrument>SMD</instrument>
                    <types>
                        <type>smdbinary</type>
                    </types>
                </response>
                <response>
                    <instrument>SP2-24</instrument>
                    <types>
                        <type>fits</type>
                        <type>png</type>
                    </types>
                </response>
                <response>
                    <instrument>SP4-8</instrument>
                    <types>
                        <type>fits</type>
                        <type>png</type>
                    </types>
                </response>
                <response>
                    <instrument>SRH</instrument>
                    <types>
                        <type>cp</type>
                        <type>fits</type>
                        <type>png</type>
                        <type>sav</type>
                    </types>
                </response>
                <response>
                    <instrument>SSRT</instrument>
                    <types>
                        <type>bmp</type>
                            <type>fits</type>
                        <type>gif</type>
                        <type>png</type>
                    </types>
                </response>
            </typesByInstrumentsListResponse>
        </SOAP-ENV:typesByInstrumentsListResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
            """.strip()
            m.register_uri('GET', 'http://localhost:5000/wsdl',
                           text=self._wsdl_response)
            m.register_uri('POST', 'http://localhost:5000/soap',
                           text=self._soap_response)

            data = Data()
            data.SERVICE_URL = "localhost:5000/wsdl"
            types = data.get_types_by_instruments()

        assert len(types) == 5

    def test_get_file_types_meta(self):

        self.i = 0
        with requests_mock.Mocker() as m:

            self.response = """
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
    <SOAP-ENV:Body>
        <SOAP-ENV:instrumentFileTypesResponse>
            <instrumentFileTypesResponse>
                <types>cp</types>
                <types>fits</types>
                <types>png</types>
                <types>sav</types>
            </instrumentFileTypesResponse>
        </SOAP-ENV:instrumentFileTypesResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
            """.strip()
            m.register_uri('GET', 'http://localhost:5000/wsdl',
                           text=self._wsdl_response)
            m.register_uri('POST', 'http://localhost:5000/soap',
                           text=self._soap_response)

            data = Data()
            data.SERVICE_URL = "localhost:5000/wsdl"
            types = data.get_file_types("SRH")

        assert len(types) == 4

        assert "cp" in types
        assert "fits" in types
        assert "png" in types
        assert "sav" in types

    def test_get_instruments_meta(self):

        self.i = 0
        with requests_mock.Mocker() as m:

            self.response = """
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
    <SOAP-ENV:Body>
        <SOAP-ENV:instrumentsListResponse>
            <instrumentsListResponse>
                <instruments>SRH</instruments>
                <instruments>SMD</instruments>
                <instruments>SP2-24</instruments>
                <instruments>SP4-8</instruments>
                <instruments>SSRT</instruments>
            </instrumentsListResponse>
        </SOAP-ENV:instrumentsListResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
            """.strip()
            m.register_uri('GET', 'http://localhost:5000/wsdl',
                           text=self._wsdl_response)
            m.register_uri('POST', 'http://localhost:5000/soap',
                           text=self._soap_response)

            data = Data()
            data.SERVICE_URL = "localhost:5000/wsdl"
            instruments = data.get_instruments()

        assert len(instruments) == 5

        assert "SRH" in instruments
        assert "SP2-24" in instruments
        assert "SSRT" in instruments
        assert "SMD" in instruments
        assert "SP4-8" in instruments

    def test_get_files_meta(self):

        self.i = 0
        with requests_mock.Mocker() as m:

            self.response = """<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
    <SOAP-ENV:Body>
        <SOAP-ENV:getFilesResponse>
            <getFilesResponse>
                <files>
                  <URL>http://archive.rao.istp.ac.ru/SRH/srh_cp_20190808.fits\
?versionId=gklZRKuVyTPhYM1C9Vk8lcetTl6K-z3</URL>
                 <hash>e16bda71ec7016c6ded3652411a1029c</hash>
                  <filename>srh_cp_20190808.fits</filename>
                  <date>2019-08-08T00:00:00</date>
                </files>
            </getFilesResponse>
        </SOAP-ENV:getFilesResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>""".strip()
            m.register_uri('GET', 'http://localhost:5000/wsdl',
                           text=self._wsdl_response)
            m.register_uri('POST', 'http://localhost:5000/soap',
                           text=self._soap_response)

            data = Data()
            data.SERVICE_URL = "localhost:5000/wsdl"
            files = data.get_files("SRH", "cp",
                                   parser.parse("2019-08-08T00:00:00"),
                                   parser.parse("2019-08-08T23:59:59"))

            assert isinstance(files, types.GeneratorType) is True
            files = list(files)

        assert len(files) == 1

        file = files[0]

        assert file.name == "srh_cp_20190808.fits"
        assert file.url == "http://archive.rao.istp.ac.ru/SRH/\
srh_cp_20190808.fits?versionId=gklZRKuVyTPhYM1C9Vk8lcetTl6K-z3"
        assert file.date.year == 2019
        assert file.date.month == 8
        assert file.date.day == 8
        assert file.date.hour == 0
        assert file.date.minute == 0
        assert file.date.second == 0

    def test_connect_meta(self):

        self.i = 0
        path = os.path.dirname(os.path.realpath(__file__))
        with open(path + "/dataset/Access.wsdl", "rb") as f:
            wsdl = f.read()
            f.close()

        with requests_mock.Mocker() as m:
            def wsdl_timeout_response(request, context):
                context.status_code = 504
                response = """
            <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
                <html>
                    <head>
                        <title>504 Gateway Timeout</title>
                    </head>
                    <body>
                        <h1>Gateway Timeout</h1>
                        <p>
                            The gateway did not receive a timely response
                            from the upstream server or application.
                        </p>
                    </body>
                </html>
                """.strip()
                self.i += 1
                if self.i > 5:
                    response = self.response.strip()
                    context.status_code = 200
                return response

            self.response = wsdl.decode("utf-8")
            m.register_uri('GET', 'http://localhost:5000/wsdl',
                           text=wsdl_timeout_response)

            data = Data()
            data.SERVICE_URL = "localhost:5000/wsdl"
            files = data._connect()

    def _wsdl_response(self, request, context):
        path = os.path.dirname(os.path.realpath(__file__))
        with open(path + "/dataset/Access.wsdl", "rb") as f:
            wsdl = f.read()
            f.close()
        return wsdl.decode("utf-8")

    def _soap_response(self, request, context):
        response = """<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
        <html>
            <head>
                <title>504 Gateway Timeout</title>
            </head>
            <body>
                <h1>Gateway Timeout</h1>
                <p>
                    The gateway did not receive a timely response
                    from the upstream server or application.
                </p>
            </body>
        </html>
        """.strip()
        context.status_code = 504
        self.i += 1
        if self.i > 5:
            response = self.response.strip()
            context.status_code = 200

        return response
