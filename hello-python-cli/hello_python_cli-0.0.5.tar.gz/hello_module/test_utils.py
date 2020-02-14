import hello_module.utils


def test_lower():
    assert hello_module.utils.lower("Mike") == "mike"
