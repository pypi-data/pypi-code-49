import pytest
from astropy.io import fits
from fits_validator import spec122_validator, Spec122ValidationException
from fits_validator.exceptions import ValidationException, SpecSchemaDefinitionException


valid_spec_122_dict = {
    "NAXIS": 3,
    "BITPIX": 16,
    "NAXIS1": 2060,
    "NAXIS2": 2050,
    "NAXIS3": 1,
    "INSTRUME": "VBI-BLUE",
    "WAVELNTH": 430.0,
    "DATE-OBS": "2017-05-30T00:46:13.952",
    "ID___002": "YVPS4YRBSXUT9Z17Z4HRH3VIH7T6KO",
    "ID___003": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
    "ID___008": "JX3O8NXFI6FGTVZ1D7G7U8OVUWDZQL",
    "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
    "DKIST003": "OSZ4FBHWKXRWQGOVG9BJNUWNG5795B",
    "DKIST004": "Observation",
}

invalid_spec_122_dict = {
    "NAXIS": 2,
    "BITPIX": 16,
    "NAXIS1": 2060,
    "NAXIS2": 2050,
    "WAVELNTH": "NOTSUPPOSEDTOBEASTRING",
    "DATE-OBS": "2017-05-30T00:46:13.952",
    "ID___002": "YVPS4YRBSXUT9Z17Z4HRH3VIH7T6KO",
    "ID___003": "POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF",
    "ID___012": "1XXPIDR5CEXMZ0SQ8LT3HMF83FW4HJ",
    "DKIST003": "OSZ4FBHWKXRWQGOVG9BJNUWNG5795B",
    "DKIST004": "Observation",
}


@pytest.mark.parametrize(
    "summit_data",
    [
        pytest.param(
            "fits_validator/tests/resources/valid_dkist_hdr.fits", id="valid_dkist_hdr.fits"
        ),
        pytest.param(valid_spec_122_dict, id="valid_spec_122_dict"),
        pytest.param(
            fits.open("fits_validator/tests/resources/valid_dkist_hdr.fits"),
            id="valid_HDUList",
        ),
        pytest.param(
            fits.open("fits_validator/tests/resources/valid_dkist_hdr.fits")[0].header,
            id="valid_Header",
        ),
    ],
)
def test_spec122_valid(summit_data):
    """
    Validates Spec0122 data
    Given: Data from summit
    When: validate headers agaist Spec0122
    Then: return an empty dictionary
    :param summit_data: Data to validate
    """
    spec122_validator(summit_data)  # raises exception on failure
    assert True



@pytest.mark.parametrize(
    "summit_data",
    [
        pytest.param(
            "fits_validator/tests/resources/invalid_dkist_hdr.fits",
            id="invalid_dkist_hdr.fits",
        ),
        pytest.param(invalid_spec_122_dict, id="invalid_spec_122_dict"),
        pytest.param(
            fits.open("fits_validator/tests/resources/invalid_dkist_hdr.fits"),
            id="invalid_HDUList",
        ),
    ],
)
def test_validate_invalid(summit_data):
    """
    Validates Spec0122 data expected to fail
    Given: Data from summit
    When: validate headers agaist Spec0122
    Then: return a dictionary of ingest errors
    :param summit_data: Data to validate
    :param validator: Fixture providing and instance of the spec 122 validator
    """

    with pytest.raises(Spec122ValidationException):
        spec122_validator(summit_data)


@pytest.mark.parametrize(
    "summit_data",
    [
        pytest.param(
            "fits_validator/tests/20170530_obs015800000.fits",
            id="file_not_found",
        ),
    ],
)
def test_validate_filenotfound(summit_data):
    """
    Validates Spec0122 data expected to fail
    Given: Data from summit
    When: validate headers agaist Spec0122
    Then: return a dictionary of ingest errors
    :param summit_data: Data to validate
    :param validator: Fixture providing and instance of the spec 122 validator
    """
    
    with pytest.raises(ValidationException):
        spec122_validator(summit_data)

@pytest.mark.parametrize(
    "summit_data",
    [
        pytest.param(
            "fits_validator/tests/resources/20170530_obs0151100000.sav",
            id="file_not_found",
        ),
    ],
)
def test_validate_filenotfits(summit_data):
    """
    Validates Spec0122 data expected to fail
    Given: Data from summit
    When: validate headers agaist Spec0122
    Then: return a dictionary of ingest errors
    :param summit_data: Data to validate
    :param validator: Fixture providing and instance of the spec 122 validator
    """
    
    with pytest.raises(ValidationException):
        spec122_validator(summit_data)

@pytest.mark.parametrize(
    "summit_data",
    [
        pytest.param(
            "fits_validator/tests/resources/dkist_rosa0181200000_observation_good.fits",
            id="maxheaders",
        ),
    ],
)
def test_validate_maxheaders(summit_data):
    """
    Validates Spec0122 data expected to pass
    Given: Data from summit
    When: validate headers agaist Spec0122
    Then: return a dictionary of ingest errors
    :param summit_data: Data to validate
    :param validator: Fixture providing and instance of the spec 122 validator
    """
    hdul = fits.open(summit_data)
    hdu = hdul[0].header
    hdu['NAXIS'] = 3 
    hdu['NAXIS3'] = 1
    hdu['PAC__007'] = 'string'
    hdu['ID___003'] = 'POLETJWHTN2PMM1ZPPLPWQ1KBAKIUF'
    hdus = dict(hdu)
    spec122_validator(hdus)
