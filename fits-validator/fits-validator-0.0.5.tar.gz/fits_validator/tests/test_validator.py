import pytest
from astropy.io import fits
from dataclasses import dataclass, asdict
#from fits_validator import FitsValidator
from fits_validator.validator import Spec122Validation
from fits_validator.exceptions import *

hdr_valid = {
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

hdr_invalid = {
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


'''@pytest.fixture(scope="module")
def validator():
    """
    Fixture that constructs Spec0122 yaml schema
    """
    return FitsValidator()
'''

@pytest.fixture(scope="module")
def validator():
    """
    Fixture that constructs Spec0122 yaml schema
    """
    return Spec122Validation()


@pytest.mark.parametrize(
    "summit_data",
    [
        pytest.param(
            "fits_validator/tests/resources/valid_dkist_hdr.fits", id="valid_dkist_hdr.fits"
        ),
        pytest.param(hdr_valid, id="hdr_valid"),
        pytest.param(
            fits.open("fits_validator/tests/resources/valid_dkist_hdr.fits"),
            id="valid_HDUList",
        ),
    ],
)
def test_validate_valid(summit_data, validator):
    """
    Validates Spec0122 data expected to pass
    Given: Data from summit
    When: validate headers agaist Spec0122
    Then: return an empty dictionary
    :param summit_data: Data to validate
    :param validator: Fixture providing and instance of the spec 122 validator
    """
    #add exception catching? Spec122ValidationException
    assert validator.validate(summit_data)
    #assert True  # if the above line didn't throw an exception the test passes


@pytest.mark.parametrize(
    "summit_data",
    [
        pytest.param(
            "fits_validator/tests/resources/invalid_dkist_hdr.fits",
            id="invalid_dkist_hdr.fits",
        ),
        pytest.param(hdr_invalid, id="hdr_invalid"),
        pytest.param(
            fits.open("fits_validator/tests/resources/invalid_dkist_hdr.fits"),
            id="invalid_HDUList",
        ),
    ],
)
def test_validate_invalid(summit_data, validator):
    """
    Validates Spec0122 data expected to fail
    Given: Data from summit
    When: validate headers agaist Spec0122
    Then: return a dictionary of ingest errors
    :param summit_data: Data to validate
    :param validator: Fixture providing and instance of the spec 122 validator
    """

    with pytest.raises(Spec122ValidationException):
        validator.validate(summit_data)

@pytest.mark.skip
@pytest.mark.parametrize(
    "summit_data",
    [
        pytest.param(
            fits.util.get_testdata_filepath('test0.fits'),
            id="too_many_images_in_fits_file",
        ),
    ],
)
def test_validate_toomanyimages(summit_data, validator):
    """
    Validates Spec122 data expected to fail
    Given: Data from summit
    When: validate headers agaist Spec0122
    Then: return a dictionary of ingest errors
    :param summit_data: Data to validate
    :param validator: Fixture providing and instance of the spec 122 validator
    """
    
    with pytest.raises(IndexError):
        validator.validate(summit_data)

@pytest.mark.parametrize(
    "summit_data",
    [
        pytest.param(
            "fits_validator/tests/20170530_obs015800000.fits",
            id="file_not_found",
        ),
    ],
)
def test_validate_filenotfound(summit_data, validator):
    """
    Validates Spec0122 data expected to fail
    Given: Data from summit
    When: validate headers agaist Spec0122
    Then: return a dictionary of ingest errors
    :param summit_data: Data to validate
    :param validator: Fixture providing and instance of the spec 122 validator
    """
    
    with pytest.raises(Exception):
        validator.validate(summit_data)

@pytest.mark.parametrize(
    "summit_data",
    [
        pytest.param(
            "fits_validator/tests/resources/20170530_obs0151100000.sav",
            id="file_not_found",
        ),
    ],
)
def test_validate_filenotfits(summit_data, validator):
    """
    Validates Spec0122 data expected to fail
    Given: Data from summit
    When: validate headers agaist Spec0122
    Then: return a dictionary of ingest errors
    :param summit_data: Data to validate
    :param validator: Fixture providing and instance of the spec 122 validator
    """
    
    with pytest.raises(Exception):
        validator.validate(summit_data)

@pytest.mark.parametrize(
    "summit_data",
    [
        pytest.param(
            "fits_validator/tests/resources/dkist_rosa0181200000_observation_good.fits",
            id="maxheaders",
        ),
    ],
)
def test_validate_maxheaders(summit_data, validator):
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
    validator.validate(hdus)




