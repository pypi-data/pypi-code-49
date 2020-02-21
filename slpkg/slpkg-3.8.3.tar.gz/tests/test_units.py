from slpkg.sizes import units


def test_units():
    """Testing the units metrics
    """
    assert ["Kb", "Kb"], ["100", "100"] == units(['100', ['100']])