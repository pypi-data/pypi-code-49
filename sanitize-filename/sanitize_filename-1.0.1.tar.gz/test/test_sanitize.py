"""Tests for the sanitize function."""
from sanitize_filename import sanitize


def test_invalid_chars():
    """Make sure invalid characters are removed in filenames."""
    assert(sanitize("A/B/C") == "ABC")
    assert(sanitize("A*C.d") == "AC.d")


def test_invalid_suffix():
    """Dots are not allowed at the end."""
    assert(sanitize("def.") == "def")
    assert(sanitize("def.ghi") == "def.ghi")


def test_reserved_words():
    """Make sure reserved Windows words are prefixed."""
    assert(sanitize("NUL") == "__NUL")
    assert(sanitize("..") == "__")


def test_long_names():
    """Make sure long names are truncated."""
    assert(len(sanitize("X" * 300)) == 255)


def test_unicode_normalization():
    """Names should be NFKD normalized."""
    assert(sanitize("ў") == chr(1091)+chr(774))
