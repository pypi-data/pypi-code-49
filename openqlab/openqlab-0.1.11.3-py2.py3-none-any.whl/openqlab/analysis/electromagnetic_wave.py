import warnings

import numpy as np
from scipy import constants as const

from openqlab.conversion.utils import human_readable


def wien_law(x: float) -> float:
    """Implements Wien's displacement law.

    Parameters
    ----------
    x: float
        Temperature or peak wavelength

    Returns
    -------
    float
    """
    # see Wikipedia, "Wien's displacement law"
    b = 2.897771955e-3
    return b / x


class ElectromagneticWave:
    """
    Electromagnetic wave with useful methods for calculations.
    """

    def __init__(self, wavelength: float):
        self._wavelength = wavelength

    @classmethod
    def from_f(cls, f):
        """Return ElektromagneticWave with frequency f.

        Parameters
        ----------
        f: float
            Frequency in Hz

        Returns
        -------
        ElectromagneticWave
        """
        return cls(const.c / f)

    @classmethod
    def from_omega(cls, omega: float):
        """Return ElektromagneticWave with angular frequency omega.

        Parameters
        ----------
        omega: float
            Angular frequency with unit 1/s

        Returns
        -------
        ElectromagneticWave
        """
        return cls.from_f(omega / (2 * np.pi))

    @classmethod
    def from_wavenumber(cls, wavenumber: float):
        """

        Parameters
        ----------
        wavenumber: float
            Wavenumber in 1/m.

        Returns
        -------
        ElectromagneticWave
        """

        return cls(1.0 / wavenumber)

    @classmethod
    def from_eV(cls, eV):
        return cls.from_f(eV * const.e / const.h)

    @classmethod
    def from_temperature(cls, T):
        return cls(wien_law(T))

    @property
    def omega(self):
        """
        Angular frequency in 1/s.
        """
        return 2 * np.pi * self.f

    @property
    def f(self):
        """
        Frequency in Hz.
        """
        return const.c / self.wavelength

    @property
    def wavelength(self):
        """
        Wavelength in m.
        """
        return self._wavelength

    @property
    def lambda0(self):
        warnings.warn(
            "ElectromagneticWave.lambda0 is deprecated: Use ElectromagneticWave.wavelength instead",
            DeprecationWarning,
        )
        return self.wavelength

    @property
    def wavenumber(self):
        """
        Wavenumber in 1/m.
        """
        return 1 / self.wavelength

    @property
    def eV(self):
        """
        Photon energy in eV.
        """
        return const.h * self.f / const.e

    @property
    def temperature(self):
        """
        Temperature of a black body whose wavelength distribution
        peaks at this wavelength.
        """
        return wien_law(self.wavelength)

    @property
    def ideal_responsivity(self) -> float:
        """
        Calculate the responsivity (A/W) for an ideal photo detector with
        a quantum efficiency of 1.

        Returns
        -------
        float
            The ideal responsivity in A/W
        """
        return 1.0 / self.eV

    def quantum_efficiency(self, responsivity) -> float:
        """
        Calculate the quantum efficiency for a given responsivity at a specific
        wavelength.

        Parameters
        ----------
        responsivity: float
            The actual responsivity

        Returns
        -------
        float
            Fraction of real vs. ideal responsivity.
        """
        return responsivity / self.ideal_responsivity

    def shotnoise(self, P):
        """
        Calculate shot noise of a laser beam.

        Parameters
        ----------
        P: float
            The laser power in Watts.

        Returns
        -------
        float
            The shot noise in W/√(Hz).
        """
        return np.sqrt(2 * const.h * self.f * P)

    def RIN(self, P):
        """
        Calculate the relative intensity noise (RIN) of a shot-noise limited
        laser beam.

        Parameters
        ----------
        P: float
            The laser power in Watts.

        Returns
        -------
        float
            The RIN in 1/√(Hz).
        """
        return self.shotnoise(P) / P

    def __repr__(self):
        return f'{self.__class__.__name__}(wavelength={human_readable(self.wavelength, "m")})'
