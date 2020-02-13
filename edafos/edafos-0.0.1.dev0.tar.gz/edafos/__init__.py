""" **Base units**

Internally, all algorithms perform calculations based on the following units.
Results are returned on U.S. customary units (default) or converted to S.I.

:Length: feet (ft)
:Unit weight: pounds per cubic feet (lb/ft3)

"""

from pint import UnitRegistry
units = UnitRegistry()
units.define('psf = lbf/foot**2')
units.define('ksf = 1000*lbf/foot**2')
units.define('kN_m2 = kN/m**2')

from edafos.stresses import effective_stress
