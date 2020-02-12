import pytest
import types
from dateutil import parser
from raodata import exceptions
from raodata.Data import Data


class TestData:

    def test_connection_exception_exception(self):

        Data.SERVICE_URL = "localhost"
        with pytest.raises(exceptions.CannotConnect):
            Data().get_instruments()

        Data.SERVICE_URL = "127.0.0.1"
        with pytest.raises(exceptions.CannotConnect):
            Data().get_instruments()

        Data.SERVICE_URL = "data.rao.istp.ac.ru/test.wsdl"
        with pytest.raises(exceptions.CannotConnect):
            Data().get_instruments()

        Data.SERVICE_URL = "data.rao.istp.ac.ru/Access.wsdl"

    def test_check_arguments_exceptions(self):

        date = parser.parse("2019-08-08")

        with pytest.raises(exceptions.InstrumentNotString):
            files = Data().get_files(date, "fits", date, date)
            list(files)

        with pytest.raises(exceptions.FiletypeNotString):
            files = Data().get_files("SRH", 1, date, date)
            list(files)

        with pytest.raises(exceptions.InvalidTime):
            files = Data().get_files("SRH", "fits", "D", date)
            list(files)

        with pytest.raises(exceptions.InvalidTime):
            files = Data().get_files("SRH", "fits", date, "D")
            list(files)

    def test_get_instruments(self):

        instruments = Data().get_instruments()
        for instrument in instruments:
            assert type(instrument) is str

    def test_get_file_types(self):

        instruments = Data().get_instruments()
        for instrument in instruments:
            types = Data().get_file_types(instrument)
            for tp in types:
                assert type(tp) is str

    def test_get_types_by_instruments(self):

        instruments = Data().get_types_by_instruments()
        for instrument in instruments:
            assert type(instrument["instrument"]) is str
            for tp in instrument["types"]["type"]:
                assert type(tp) is str

    def test_get_files(self):

        files = Data().get_files("SRH", "cp",
                                 parser.parse("2019-08-08T00:00:00"),
                                 parser.parse("2019-08-08T23:59:59"))
        assert isinstance(files, types.GeneratorType) is True
        list(files)

    def test_get_files_exception(self):

        with pytest.raises(exceptions.NoDataForThePeriod):
            files = Data().get_files("SRH", "cp",
                                     parser.parse("2019-08-08T11:11:11"),
                                     parser.parse("2019-08-08T11:11:11"))
            list(files)
