import pytest
import mock

from openhtf.core import test_record

from spintop_openhtf.util.gdrive import FileNotFound, load_credentials_file, GoogleDrive, Worksheet, GoogleFolder

from spintop_openhtf.callbacks.gdrive import TestRecordToSheetOutput

def create_test_record(config={}):
     return test_record.TestRecord(
        dut_id='test-device', station_id='unit-testing-station', code_info=test_record.CodeInfo(name=None, docstring=None, sourcecode=None),
        start_time_millis=0,
        metadata={'config': config}
     )
     
@pytest.mark.skip
def test_folder_created():
    test_record = create_test_record()

    with mock.patch('spintop_openhtf.util.gdrive.GoogleDrive') as GoogleDrive, \
            mock.patch('spintop_openhtf.util.gdrive.Worksheet') as Worksheet, \
            mock.patch('spintop_openhtf.util.gdrive.GoogleFolder') as GoogleFolder:

        worksheet = Worksheet.return_value
        folder = GoogleFolder()
        output = TestRecordToSheetOutput(folder)
        output(test_record)
        folder.get_or_create_spreadsheet.assert_called()

        Worksheet.assert_called()

        print(folder.get_or_create_spreadsheet.return_value)
        Worksheet.assert_called_with(folder.get_or_create_spreadsheet.return_value)


    