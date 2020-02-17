from pathlib import Path

import pytest

from tests import RESOURCE_PATH
from yeahyeah.persistence import JSONSettingsFile, YeahYeahPersistenceException


def test_persistence(tmpdir):
    a_file = JSONSettingsFile(path=Path(tmpdir) / "some_file.json")
    a_file.save({'foo': 'bar'})

    with pytest.raises(YeahYeahPersistenceException):
        a_file.save(Path("not/serialisable!"))