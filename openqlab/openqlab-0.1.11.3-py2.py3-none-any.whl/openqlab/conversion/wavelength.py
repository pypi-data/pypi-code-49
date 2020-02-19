import warnings

import openqlab.analysis.electromagnetic_wave


def Wavelength(lambda0):
    warnings.warn(
        f"Class Wavelength is deprecated! Use {openqlab.analysis.electromagnetic_wave.ElectromagneticWave} instead.",
        DeprecationWarning,
    )
    return openqlab.analysis.electromagnetic_wave.ElectromagneticWave(lambda0)
