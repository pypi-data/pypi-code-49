import logging as log
from typing import List, Union

import numpy as np

from . import settings


def setBit(x, offset):
    mask = 1 << offset
    return x | mask


def clearBit(x, offset):
    mask = ~(1 << offset)
    return x & mask


def testBit(x, offset):
    mask = 1 << offset
    if x & mask:
        return 1
    return 0


def changeBit(x, offset, enabled):
    if enabled:
        return setBit(x, offset)
    return clearBit(x, offset)


def readBit(x, offset):
    if testBit(x, offset):
        return True
    return False


def convertVolt2Float(
    value: Union[list, np.number, np.ndarray], mode: int = 0, unsigned=False
) -> Union[float, np.ndarray]:
    """Converts a volt scala value (in case of ADwin e.g. volt range from -10 to 10, because the outputs are limited) to a Float value. The supported range is divided onto the whole 16-bit float, so -10 Volt would e.g. correspond with 0, 10 V with 65535 for unsigned or -32768 to 32767 when signed.

    Parameters
    ----------
    value: :obj:`list`, :obj:`numpy.number`, :obj:`numpy.ndarray`
        The value(s) to be converted.
    mode: :obj:`int`
        Integer from 0 to 3, sensitivity mode. Decides how the bins are divided. See :obj:`nqontrol.servo.inputSensitivity` or `auxSensitivity` for more info.
    unsigned: :obj:`bool`
        Whether the Integer is supposed to have a sign or not, see above.

    Returns
    -------
    :obj:`list`, :obj:`numpy.number`, :obj:`numpy.ndarray`
        Converted value. Exact type depends on input type.
    """
    if isinstance(value, list):
        value = np.array(value)
    result = 0.1 * value * 0x8000 * pow(2, mode)

    upper_limit = 0x7FFF
    lower_limit = -0x8000
    if isinstance(result, (float, np.float64, np.float32)):
        if result > upper_limit:
            result = upper_limit
        if result < lower_limit:
            result = lower_limit
    elif isinstance(result, np.ndarray):
        result[result > upper_limit] = upper_limit
        result[result < lower_limit] = lower_limit
    else:
        raise TypeError("The type {} is not supported.".format(type(value)))

    if unsigned:
        result += 32768
    return result


def convertVolt2Int(
    value: Union[list, np.number, np.ndarray], mode: int = 0, unsigned=False
) -> Union[int, np.ndarray]:
    """[DEPRECATED] Converts a volt scala value (in case of ADwin e.g. volt range from -10 to 10, because the outputs are limited) to an Integer value. There is an equivalent function for Floats. The supported range is divided onto the whole 16-bit integer, so -10 Volt would e.g. correspond with 0, 10 V with 65535 for unsigned or -32768 to 32767 when signed.

    Parameters
    ----------
    value: :obj:`list`, :obj:`numpy.number`, :obj:`numpy.ndarray`
        The value(s) to be converted.
    mode: :obj:`int`
        Integer from 0 to 3, sensitivity mode. Decides how the bins are divided. See :obj:`nqontrol.servo.inputSensitivity` or `auxSensitivity` for more info.
    unsigned: :obj:`bool`
        Whether the Integer is supposed to have a sign or not, see above.

    Returns
    -------
    :obj:`list`, :obj:`numpy.number`, :obj:`numpy.ndarray`
        Converted value. Exact type depends on input type.
    """
    log.warning(
        DeprecationWarning(
            "This method is deprecated, please use `convertVolt2Float` for higher accuracy."
        )
    )
    result = convertVolt2Float(value, mode, unsigned)
    if isinstance(result, (float, np.float64, np.float32)):
        return int(round(result, 0))
    if isinstance(result, np.ndarray):
        return result.astype(int)
    return result


def convertFloat2Volt(
    value: Union[List[float], np.array, float], mode: int = 0, signed=False
) -> Union[float, np.ndarray]:
    if isinstance(value, list):
        value = np.array(value)
    if signed:
        value += 32768
    return 10.0 * (value / 0x8000 - 1) / pow(2, mode)


def rearrange_filter_coeffs(inputFilter: List[float]) -> List[float]:
    """Rearrage coefficients from `a, b` to `c`."""
    b = inputFilter[0:3]
    a = inputFilter[3:6]
    return [b[0], a[1], a[2], b[1] / b[0], b[2] / b[0]]


def convertStepsize2Frequency(stepsize: int) -> float:
    return stepsize * settings.SAMPLING_RATE / settings.RAMP_DATA_POINTS


def convertFrequency2Stepsize(frequency: float) -> int:
    # period_time = RAMP_DATA_POINTS/stepsize / SAMPLING_RATE
    # f = stepsize * SAMPLING_RATE / RAMP_DATA_POINTS
    # stepsize = f / SAMPLING_RATE * RAMP_DATA_POINTS
    stepsize = int(frequency * settings.RAMP_DATA_POINTS / settings.SAMPLING_RATE)
    if stepsize < 1:
        stepsize = 1
        log.warning("The frequency is too low, using the lowest possible.")
    elif stepsize > 255:
        stepsize = 255
        log.warning("The frequency is too high, using the highest possible.")

    frequency = convertStepsize2Frequency(stepsize)
    log.info("frequency: {:.2f} Hz".format(frequency))

    return stepsize
