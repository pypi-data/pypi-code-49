# The MIT License (MIT)
#
# Copyright (c) 2018 Institute for Molecular Systems Biology, ETH Zurich.
# Copyright (c) 2019 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import warnings  # Silence NEP 18 warning

import numpy as np
import pint


# Disable Pint's old fallback behavior (must come before importing Pint)
os.environ["PINT_ARRAY_PROTOCOL_FALLBACK"] = "0"

ureg = pint.UnitRegistry(system="mks")
Q_ = ureg.Quantity

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    Q_([])


R = Q_(8.31e-3, "kJ / mol / K")
LOG10 = np.log(10)
FARADAY = Q_(96.485, "kC / mol")
default_T = Q_(298.15, "K")
default_I = Q_(0.25, "M")
default_pH = Q_(7.0)
default_pMg = Q_(10)
default_RT = R * default_T
default_c_mid = Q_(1e-3, "M")
default_c_range = (Q_(1e-6, "M"), Q_(1e-2, "M"))
standard_dg_formation_mg = Q_(-455.3, "kJ/mol")  # Mg2+ formation energy

standard_concentration = Q_(1.0, "M")
physiological_concentration = Q_(1.0e-3, "M")


@ureg.check("[concentration]", "[temperature]")
def debye_hueckel(ionic_strength: Q_, temperature: Q_) -> Q_:
    """
    Compute the ionic-strength-dependent transformation coefficient.

    For the Legendre transform to convert between chemical and biochemical
    Gibbs energies, we use the extended Debye-Hueckel theory to calculate the
    dependence on ionic strength and temperature.

    Parameters
    ----------
    ionic_strength : Quantity
        The ionic-strength
    temperature : Quantity
        The temperature

    Returns
    -------
    Quantity
        The ionic-strength-dependent transform coefficient

    """
    if ionic_strength <= 0.0:
        return Q_(0.0)

    _a1 = Q_(1.108, "1 / M**0.5")
    _a2 = Q_(1.546e-3, "1 / M**0.5 / K")
    _a3 = Q_(5.959e-6, "1 / M**0.5 / K**2")
    alpha = _a1 - _a2 * temperature + _a3 * temperature ** 2
    B = Q_(1.6, "1 / M**0.5")

    return alpha * ionic_strength ** 0.5 / (1.0 + B * ionic_strength ** 0.5)


@ureg.check("", "[concentration]", "[temperature]", None, None, "", None)
def legendre_transform(
    p_h: Q_,
    ionic_strength: Q_,
    temperature: Q_,
    num_protons: float,
    charge: float,
    p_mg: Q_ = default_pMg,
    num_magnesiums: float = 0.0,
) -> Q_:

    r"""
    Calculate the Legendre Transform value for a certain microspecies.

    at a certain pH, I, T

    Parameters
    ----------
    p_h : Quantity
        The pH value, i.e., the logarithmic scale for the molar
        concentration of hydrogen ions :math:`-log10([H+])`.
    ionic_strength : Quantity
        The ionic-strength.
    temperature : Quantity
        The temperature.
    num_protons : float
        The number of protons.
    charge : float
        The electric charge of the microspecies.
    p_mg : Quantity, optional
        The logarithmic molar concentration of magnesium ions
        :math:`-log10([Mg2+])`.
    num_magnesiums : float, optional
        The number of magnesium ions associated to the microspecies.

    Returns
    -------
    Quantity
        The transformed relative :math:`\Delta G` (in units of RT).

    """

    # The Debye-Hueckel factor in units of RT.
    dh_factor = debye_hueckel(ionic_strength, temperature)

    if num_magnesiums > 0:
        mg_part = num_magnesiums * (
            p_mg * LOG10 - standard_dg_formation_mg / (R * temperature)
        )
    else:
        mg_part = Q_(0)

    return (
        num_protons * LOG10 * p_h
        + (num_protons - charge ** 2) * dh_factor
        + mg_part
    )
