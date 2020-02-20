import pytest
import sys
from io import StringIO
from getraodata import getraodata, exceptions
import filecmp


class TestGetRAOData():

    def setup_method(self, test_method):
        self.output = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def teardown_method(self, test_method):
        self.output.close()
        sys.stdout = self.saved_stdout

    def test_parse_arguments(self, capsys, caplog, tmpdir):

        with pytest.raises(exceptions.CannotParseArguments):
            getraodata.parse_arguments()

    def test_main(self, capsys, caplog, tmpdir):
        sys.argv[1] = "SRH"
        sys.argv[2] = "fits"
        sys.argv[3] = "2019-08-08"
        sys.argv[4] = "2019-08-08"
        sys.argv[5] = str(tmpdir)
        getraodata.main()
        assert capsys.readouterr().out == (
                                           "0 of 2 files processed\r" +
                                           "1 of 2 files processed\r" +
                                           "2 of 2 files processed\n"
                                          )
        assert len(tmpdir.listdir()) == 2
        assert filecmp.cmp(str(tmpdir) + "/mf_20190808_000000.fit",
                           "tests/dataset/mf_20190808_000000.fit")
        assert filecmp.cmp(str(tmpdir) + "/srh_20190808.fit",
                           "tests/dataset/srh_20190808.fit")
