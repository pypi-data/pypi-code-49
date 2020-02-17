import pytest
import six


def test_python_2_import_warns():
    warn_text = "Support for Python 2 is deprecated will be " +\
                 "removed in the next version release after " +\
                 "April 1, 2020."
    with pytest.warns(None) as warn:
        import civis  # NOQA
    if six.PY2:
        assert len(warn) == 1
        assert issubclass(warn[0].category, DeprecationWarning)
        assert warn[0].message == warn_text
    else:
        assert len(warn) == 0
