#! /usr/bin/env python

"""Catalog-related photometric tools

e.g. Translate magnitudes from one filter to another

"""

import astropy.units as u


def translate(input_spectrum, magnitude, band, new_band, renormalize=False):
    """Calculate a source's magnitude in a given filter given the magnitude in
    a different band and a spectrum.

    If renormalize is False, then the spectrum is will be used directly.
    If renormalize is True, then the input spectrum will be renormalized
    such that it produces the given magnitude in 'band'. The magnitude in
    'new_band" is then calculated.

    Parameters
    ----------
    input_spectrum : ??

    magnitude : float
        astropy magnitude unit attached?

    band : str
        Name of filter passband corresponding to 'magnitude'
        (This implies Mirage knows about the magnitude band by name. What about
        a case where the user supplies the filter passband?)

    new_band : str
        Name of band to translate source's brightness into. Again, this assumes mirage
        knows the name of the filter. What about a case where the user provides a filter
        bandpass?

    renormalize : bool
        If False, the input spectrum is used directly and 'magnitude' is ignored.
    """
    something
    return new_magnitude

