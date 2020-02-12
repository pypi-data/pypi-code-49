#! /usr/bin/python3
# -*- coding: utf-8 -*-


""" 
"""


__author__ = 'Alan Loh'
__copyright__ = 'Copyright 2020, nenupy'
__credits__ = ['Alan Loh']
__maintainer__ = 'Alan'
__email__ = 'alan.loh@obspm.fr'
__status__ = 'Production'
__all__ = [
    'Skymodel'
    ]


import numpy as np
import sys
import os

from pygsm import GlobalSkyModel
from healpy import (
    pix2ang,
    ang2pix,
    nside2npix,
    Rotator
)
from healpy.pixelfunc import ud_grade

from nenupysim.astro import (
    to_radec,
    eq_zenith
)


# ============================================================= #
# ------------------------- Skymodel -------------------------- #
# ============================================================= #
class Skymodel(object):
    """
    """

    def __init__(self, nside=128, freq=50):
        self.nside = nside
        self.freq = freq
        self._load_gsm_model()


    # --------------------------------------------------------- #
    # --------------------- Getter/Setter --------------------- #


    # --------------------------------------------------------- #
    # ------------------------ Methods ------------------------ #
    def zenith_center(self, time):
        """ Get the GSM skymodel centered on the local zenith

            :param time:
                Time at which the local zenith coordinates should
                be computed. It can either be provided as an 
                :class:`astropy.time.Time` object or a string in
                ISO or ISOT format.
            :type time: str, :class:`astropy.time.Time`

            :returns: HEALPix array of skymodel
            :rtype: :class:`np.ndarray`
        """
        eq_zen = eq_zenith(
            time=time
        )
        return self._rotate_map_to(eq_zen)


    # --------------------------------------------------------- #
    # ----------------------- Internal ------------------------ #
    def _load_gsm_model(self):
        """
        """
        gsm = GlobalSkyModel(freq_unit='MHz')
        gsmap = gsm.generate(self.freq)
        self.map = ud_grade(
            map_in=gsmap,
            nside_out=self.nside
        )
        return


    def _rotate_map_to(self, radec):
        """
        """
        ra = radec.ra.rad % (2.*np.pi)
        dec = radec.dec.rad
        rot = Rotator(
            deg=False,
            rot=[ra, dec],
            coord=['G', 'C']
        )
        sys.stdout = open(os.devnull, 'w')
        rotated_map = rot.rotate_map_alms(self.map)
        sys.stdout = sys.__stdout__
        return rotated_map
# ============================================================= #

