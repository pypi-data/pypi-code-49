import os
import pytest
import tempfile

from seeq.base import system
from seeq import spy

from . import test_load


@pytest.mark.system
def test_bad_filename():
    workbooks = test_load.load_example_export()
    assert len(workbooks) == 2

    workbook = [w for w in workbooks if 'Analysis' in w.name][0]
    workbook.name = r'My\Workbook&Has|Bad\Characters*In?It:And"That<Sucks>Dude'
    with tempfile.TemporaryDirectory() as temp:
        if system.is_windows():
            with pytest.raises(OSError):
                # We just barf immediately if we are supplied a bad folder name
                spy.workbooks.save(workbook, os.path.join(temp, r'Bad|Folder*Name'))

        spy.workbooks.save(workbook, temp)

        assert os.path.exists(os.path.join(temp, 'My_Workbook_Has_Bad_Characters_In_It_And_That_Sucks_Dude '
                                                 '(D833DC83-9A38-48DE-BF45-EB787E9E8375)'))
