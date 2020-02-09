############################################################
# -*- coding: utf-8 -*-
#
#       #   #  #   #   #    #
#      ##  ##  #  ##  #    #
#     # # # #  # # # #    #  #
#    #  ##  #  ##  ##    ######
#   #   #   #  #   #       #
#
# Python-based Tool for interaction with the 10micron mounts
# GUI with PyQT5 for python
# Python  v3.7.4

#
# Michael Würtenberger
# (c) 2019
#
# Licence APL2.0
#
###########################################################
# standard libraries
import logging
# external packages
import skyfield.api
import numpy
# local imports
from mountcontrol.loggerMW import CustomLogger
from mountcontrol.convert import stringToDegree
from mountcontrol.convert import valueToAngle
from mountcontrol.convert import valueToFloat
from mountcontrol.convert import valueToInt


class ModelStar(object):
    """
    The class ModelStar inherits all information and handling of one star in
    the alignment model used by the mount and the data in the mount and provides the
    abstracted interface to a 10 micron mount.
    The coordinates are in JNow topocentric

        >>> settings = ModelStar(
        >>>                     coord=None,
        >>>                     errorRMS=0,
        >>>                     errorAngle=0,
        >>>                     number=0,
        >>>                     )

    point could be from type skyfield.api.Star or just a tuple of (ha, dec) where
    the format should be float or the 10micron string format.

    Command protocol (from2.8.15 onwards):
    "HH:MM:SS.SS,+dd*mm:ss.s,eeee.e,ppp#" where HH:MM:SS.SS is the hour angle of the
    alignment star in hours, minutes, seconds and hundredths of second (from 0h to
    23h59m59.99s), +dd*mm:ss.s is the declination of the alignment star in degrees,
    arcminutes, arcseconds and tenths of arcsecond, eeee.e is the error between the star
    and the alignment model in arcseconds, ppp is the polar angle of the measured star
    with respect to the modeled star in the equatorial system in degrees from 0 to 359
    (0 towards the north pole, 90 towards east).
    """

    __all__ = ['ModelStar',
               'coord',
               'errorRMS',
               'errorAngle',
               'errorRA',
               'errorDEC',
               'number',
               ]

    logger = logging.getLogger(__name__)
    log = CustomLogger(logger, {})

    def __init__(self,
                 coord=None,
                 errorRMS=None,
                 errorAngle=None,
                 number=None,
                 ):

        self.coord = coord
        self.errorRMS = errorRMS
        self.errorAngle = errorAngle
        self.number = number

    @property
    def coord(self):
        return self._coord

    @coord.setter
    def coord(self, value):
        if isinstance(value, skyfield.api.Star):
            self._coord = value
            return
        if not isinstance(value, (tuple, list)):
            self._coord = None
            return
        if len(value) != 2:
            self._coord = None
            return
        ha, dec = value
        ha = stringToDegree(ha)
        dec = stringToDegree(dec)
        if not ha or not dec:
            self._coord = None
            self.log.error('Malformed value: {0}'.format(value))
            return
        self._coord = skyfield.api.Star(ra_hours=ha,
                                        dec_degrees=dec)

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = valueToInt(value)

    @property
    def errorRMS(self):
        return self._errorRMS

    @errorRMS.setter
    def errorRMS(self, value):
        self._errorRMS = valueToFloat(value)

    @property
    def errorAngle(self):
        return self._errorAngle

    @errorAngle.setter
    def errorAngle(self, value):
        if isinstance(value, skyfield.api.Angle):
            self._errorAngle = value
            return
        self._errorAngle = valueToAngle(value)

    def errorRA(self):
        if self._errorRMS and self._errorAngle:
            return self._errorRMS * numpy.sin(self._errorAngle.radians)
        else:
            return None

    def errorDEC(self):
        if self._errorRMS and self._errorAngle:
            return self._errorRMS * numpy.cos(self._errorAngle.radians)
        else:
            return None

    def __gt__(self, other):
        if other > self._errorRMS:
            return True
        else:
            return False

    def __ge__(self, other):
        if other >= self._errorRMS:
            return True
        else:
            return False

    def __lt__(self, other):
        if other < self._errorRMS:
            return True
        else:
            return False

    def __le__(self, other):
        if other <= self._errorRMS:
            return True
        else:
            return False
