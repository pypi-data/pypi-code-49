from typing import Dict, Tuple, Union

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

from openqlab.analysis.electromagnetic_wave import ElectromagneticWave
from openqlab.conversion.utils import human_readable
from openqlab.plots.gaussian_beam import beam_profile


class GaussianBeam(ElectromagneticWave):
    """
    Represents a complex gaussian beam parameter
    """

    def __init__(self, q=0 + 1j, wavelength=1.064e-6):
        if wavelength <= 0:
            raise ValueError("Wavelength must be a positiv number")
        super().__init__(wavelength)
        self._q = q

    @classmethod
    def from_waist(cls, w0: float, z0: float, wavelength: float = 1.064e-6):
        """Create Gaussian beam from waist size and position.

        Parameters
        ----------
        w0: float
            Waist size in meters
        z0: float
            Waist position in meters
        wavelength: float
            Wavelength in meters

        Returns
        -------

        """
        return cls(1j * (np.pi * w0 ** 2 / wavelength) - z0, wavelength)

    def propagate(self, d):
        """
        Returns the beam parameter after free-space propagation of d
        """
        return GaussianBeam(self._q + d, self._wavelength)

    def get_profile(self, zpoints):
        """
        Returns the beam width at points zpoints along the beam axis.
        """
        quotient = (self._q.real + zpoints) / self._q.imag
        return self.w0 * np.sqrt(1 + quotient ** 2)

    @property
    def wavelength(self) -> float:
        return self._wavelength

    @property
    def w0(self) -> float:
        """
        Waist size in meters.
        Returns
        -------

        """
        return np.sqrt(self._q.imag * self._wavelength / np.pi)

    @property
    def z0(self) -> float:
        """
        The position of the beam waist on the z axis in meters.
        """
        return -self._q.real  # pylint: disable=invalid-unary-operand-type

    @property
    def zR(self):
        return self._q.imag

    @property
    def R(self):
        qi = 1 / self._q
        if qi.real == 0:
            return np.infty
        return 1 / (qi.real)

    @property
    def w(self):
        return self.get_profile(0.0)

    @property
    def divergence(self):
        """
        Beam divergence (in radian).
        """
        return np.arctan(self._wavelength / np.pi / self.w0)

    def __repr__(self):
        return "w0={w0} @ z0={z0}".format(
            w0=human_readable(self.w0, "m"), z0=human_readable(self.z0, "m")
        )


def fit_beam_data(  # pylint: disable=too-many-arguments
    data: pd.DataFrame,
    bounds=([0, -np.inf], [np.inf, np.inf]),
    guess_w0: float = 300e-6,
    guess_z0: float = 0.0,
    wavelength: float = 1064e-9,
    plot: bool = True,
    errors: bool = False,
) -> Union[
    Dict[str, GaussianBeam], Tuple[Dict[str, GaussianBeam], Dict[str, np.ndarray]]
]:
    """Fit beam data to the gaussian beam model using non-linear least squares. Returns GaussianBeam object and dictionary of standarddeviations for waist size and position. Optionally plots the datapoints and beam width function with fit parameters.

    Parameters
    ----------
    data: :obj:`DataFrame`
        Data to fit in the form of a :obj:`DataFrame` containing the position data in m as index and the 1/e^2 (13%) radius in m for X (and Y) direction in the 1st (and 2nd) column.
    bounds: :obj:`2-tuple of array_like`
        2-tuple of array-like bounds for all fit parameters. The first array-like object containing the lower and the second containing the upper ones.
    guess_w0: :obj:`float`
        Initial estimate of the beam waist in m (default: 300um)
    guess_z0: :obj:`float`
        Initial estimate of the waist position in m (default: 0)
    wavelength: :obj:`float`
        Wavelength of the light in m (default: 1064nm)
    plot: :obj:`bool`
        Create plot after fitting (default: True)
    errors: :obj:`bool`
        Additionally return standard deviations (default: False)

    Returns
    -------
    results: :obj:`dict` of :obj:`GaussianBeam`
        A dictionary containing :obj:`GaussianBeam` object for each fit result,
        with descriptive labels as dictionary keys.
    fit_errors: :obj:`dict` of :obj:`ndarray`
        A dictionary containing :obj:`ndarray` for each fit result, with the standard deviations of waist size (index 0) and position (index 1) obtained from the fit in m.

    """
    initial_guess = [guess_w0, guess_z0]

    def fit_function(z, w0, z0):
        return GaussianBeam.from_waist(w0, z0, wavelength).get_profile(z)

    results = {}
    fit_errors = {}
    for column in data:
        popt, pcov = curve_fit(
            fit_function, data.index, data[column], bounds=bounds, p0=initial_guess
        )
        results[column] = GaussianBeam.from_waist(popt[0], popt[1], wavelength)
        perr = np.sqrt(np.diag(pcov))
        fit_errors[column] = perr
        print(
            u'Results for "{plane}" plane: ({w0:.1f} ± {w0s:.1f})µm @'
            u" ({z0:.3f} ± {z0s:.3f})cm".format(
                plane=column,
                w0=popt[0] * 1e6,
                w0s=perr[0] * 1e6,
                z0=popt[1] * 1e2,
                z0s=perr[1] * 1e2,
            )
        )
    if plot:
        beam_profile(results, data)
    if errors:
        return results, fit_errors
    return results
