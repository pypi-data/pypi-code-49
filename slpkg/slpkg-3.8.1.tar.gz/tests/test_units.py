from slpkg.sizes import units


def test_units():
    assert ["Kb", "Kb"], ["100", "100"] == units(['100', ['100']])