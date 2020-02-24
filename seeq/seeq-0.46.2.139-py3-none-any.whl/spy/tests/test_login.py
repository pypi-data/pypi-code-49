import pytest

from seeq import spy

from .. import _login
from .. import _config
from . import test_common


@pytest.mark.unit
def test_cleanse_url():
    assert _login.cleanse_url('http://localhost:80') == 'http://localhost'
    assert _login.cleanse_url('http://localhost:443') == 'http://localhost:443'
    assert _login.cleanse_url('https://localhost:80') == 'https://localhost:80'
    assert _login.cleanse_url('https://localhost:443') == 'https://localhost'
    assert _login.cleanse_url('https://chevron.seeq.site/') == 'https://chevron.seeq.site'
    assert _login.cleanse_url('https://chevron.seeq.site:8254/this/is/cool') == 'https://chevron.seeq.site:8254'


@pytest.mark.system
def test_bad_login():
    with pytest.raises(RuntimeError):
        spy.login('mark.derbecker@seeq.com', 'DataLab!', url='https://bogus')

    # Remove overrides that resulted from spy.login() with bogus URL
    _config.unset_seeq_url()

    try:
        spy.login('mark.derbecker@seeq.com', 'DataLab!', auth_provider='bogus')
        assert False, 'Exception was not raised with bogus auth_provider'
    except RuntimeError:
        pass


@pytest.mark.system
def test_good_login():
    test_common.login()


@pytest.mark.system
def test_credentials_file_with_username():
    with pytest.raises(ValueError):
        spy.login('mark.derbecker@seeq.com', 'DataLab!', credentials_file='credentials.key')
