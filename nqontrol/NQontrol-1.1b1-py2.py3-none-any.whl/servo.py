"""Servo class."""
import json
import logging as log
import multiprocessing as mp
from math import copysign, pow
from time import sleep, time
from tkinter import TclError
from typing import Optional

import jsonpickle
import numpy as np
from ADwin import ADwinError
from matplotlib import pyplot as plt
from openqlab.analysis.servo_design import ServoDesign
from pandas import DataFrame

from . import general, settings
from .errors import Bug, ConfigurationError, DeviceError, UserInputError
from .feedbackController import FeedbackController
from .general import (
    convertFloat2Volt,
    convertFrequency2Stepsize,
    convertStepsize2Frequency,
    convertVolt2Float,
    rearrange_filter_coeffs,
)


class Servo:
    """
    Servo object that communicates with a control channel of the ADwin.

    `readFromFile` overwrites all other parameters.

    Parameters
    ----------
    channel: :obj:`int`
        Channel used vor the Servo.
        Possible is `1..8`
        Channel number is used for input,
        output and process number
    adw: :obj:`ADwin`
        For all servos of a :obj:`ServoDevice` to use the same
        :obj:`ADwin` object,
        it is necessary to pass an ADwin object.
    applySettings: :obj:`str` or `dict`
        Apply settings directly from file or dict.
    offset: :obj:`offset`
        Overall offset.
    gain: :obj:`float`

    filters: 5 * 5 :obj:`list`
        Filter coefficient matrix. Default is a 0.0 matrix.
    name: :obj:`str`
        Choose an optional name for this servo.

    """

    DONT_SERIALIZE = ["_adw", "_subProcess", "_fifoBuffer", "_tempFeedback"]
    REALTIME_DICTS = ["realtime", "_ramp", "_fifo"]
    JSONPICKLE = ["servoDesign"]
    MIN_REFRESH_TIME = 0.02
    DEFAULT_FILTERS = [
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
    ]
    DEFAULT_COLUMNS = ["input", "aux", "output"]
    _manager = mp.Manager()
    realtime = _manager.dict(
        {"enabled": False, "ydata": DEFAULT_COLUMNS, "ylim": None, "refreshTime": 0.1}
    )
    DEFAULT_FIFO_STEPSIZE = 10
    """
    Control realtime plotting.

    .. code:: python

        realtime = {
            'enabled': False,
            'ydata': ['input', 'aux', 'output'],
            'ylim': None,
            'refreshTime': 0.1,
        }
    """

    # TODO ramp speed
    ########################################
    # Predefined methods
    ########################################
    def __init__(
        self,
        channel,
        adw,
        applySettings=None,
        offset=0.0,
        gain=1.0,
        filters=None,
        name=None,
    ):
        """
        Create the servo object, also on ADwin.

        `readFromFile` overwrites all other parameters.

        Parameters
        ----------
        deviceNumber: Number of the ADwin-Pro device.
        channel:      Channel used for the Servo.
                      Possible is `1..8`
                      Channel number is used for input,
                      output and process number
        offset=0.0:   Overall offset
        filters:      Filter coefficient matrix. Default is a 0.0 matrix.

        """
        MAX_CHANNELS = 8

        if not 1 <= channel <= MAX_CHANNELS:
            raise ValueError(f"There are max {MAX_CHANNELS} channels.")
        self._channel = channel
        if name is None:
            self.name = "Servo " + str(channel)
        else:
            self.name = name
        if filters is None:
            filters = self.DEFAULT_FILTERS

        # State dictionaries
        self._state = dict(
            {
                # Control parameters
                "offset": offset,
                "gain": gain,
                "filters": filters,
                "inputSensitivity": 0,
                "auxSensitivity": 0,
                # Control flags
                "filtersEnabled": [False] * 5,
                "auxSw": False,
                "offsetSw": False,
                "outputSw": False,
                "inputSw": False,
                # 'snapSw': False,
            }
        )
        self._ramp = self._manager.dict(
            {"amplitude": 0.1, "minimum": 0, "stepsize": 20}
        )
        self._autolock = dict(
            {
                "lock": 0,
                "locked": 0,
                "relock": 0,
                "greater": 1,
                "threshold": 0,
                "start": -10,
                "end": 10,
            }
        )
        self._fifo = self._manager.dict(
            {"stepsize": self.DEFAULT_FIFO_STEPSIZE, "maxlen": settings.FIFO_MAXLEN}
        )
        if self._fifo["maxlen"] * 2 > settings.FIFO_BUFFER_SIZE:
            raise ConfigurationError(
                "FIFO_BUFFER_SIZE must be at least twice as big as _fifo['maxlen']."
            )
        self._fifoBuffer = None
        self._subProcess = None

        # has to be initalized as None / could maybe include in the loading?
        self._tempFeedback = None
        self._tempFeedbackSettings = self._manager.dict(
            {"dT": None, "mtd": None, "update_interval": 1, "voltage_limit": 5}
        )

        # ServoDesign object
        self.servoDesign: ServoDesign = ServoDesign()

        # Use adwin object
        self._adw = adw

        # initialize lock values
        self._sendLockControl()
        self._sendLockValues()

        try:
            if applySettings:
                # loadSettings calls `_sendAllToAdwin()`
                self.loadSettings(applySettings)
            else:
                self._sendAllToAdwin()
        except ADwinError as e:
            log.error(f"{e} Servo {self._channel}: Couldn't write to ADwin.")

    def __repr__(self):
        """Name of the object."""
        return f"Name: {self.name}, channel: {self._channel}"

    ########################################
    # Help methods
    ########################################

    def _sendAllToAdwin(self):
        """Write all settings to ADwin."""
        # Control parameters
        self.offset = self._state["offset"]
        self.gain = self._state["gain"]
        self.filters = self._state["filters"]
        self.inputSensitivity = self._state["inputSensitivity"]
        self.auxSensitivity = self._state["auxSensitivity"]

        self._sendLockControl()
        # Control flags
        self._sendFilterControl()

    def _readAllFromAdwin(self):
        self._readFilterControl()
        _ = self.offset
        _ = self.gain
        _ = self.filters
        _ = self.inputSensitivity
        _ = self.auxSensitivity

    def _triggerReload(self):
        """Trigger bit to trigger reloading of parameters."""
        par = self._adw.Get_Par(settings.PAR_RELOADBIT)
        # only trigger if untriggered
        if not general.readBit(par, self._channel - 1):
            par = general.changeBit(par, self._channel - 1, True)
            self._adw.Set_Par(settings.PAR_RELOADBIT, par)
        else:
            raise DeviceError(
                "ADwin has been triggered to reload the shared RAM within 10µs or the realtime program doesn't run properly."
            )

    def _readFilterControl(self):
        c = self._adw.Get_Par(settings.PAR_FCR + self._channel)
        # read control bits
        self._state["auxSw"] = general.readBit(c, 9)
        for i in range(5):
            bit = general.readBit(c, 4 + i)
            self._state["filtersEnabled"][i] = bit
            assert (
                list(self._state["filtersEnabled"])[i] == bit
            ), f'dict: {list(self._state["filtersEnabled"])[i]}, bit: {bit}'
        # self._state['snapSw'] = general.readBit(c, 3)
        self._state["offsetSw"] = general.readBit(c, 2)
        self._state["outputSw"] = general.readBit(c, 1)
        self._state["inputSw"] = general.readBit(c, 0)

    def _sendFilterControl(self):
        # read current state
        c = self._adw.Get_Par(settings.PAR_FCR + self._channel)

        # set control bits
        c = general.changeBit(c, 9, self._state["auxSw"])
        for i in range(5):
            c = general.changeBit(c, 4 + i, self._state["filtersEnabled"][i])
        # c = general.changeBit(c, 3, self._state['snapSw'])
        c = general.changeBit(c, 2, self._state["offsetSw"])
        c = general.changeBit(c, 1, self._state["outputSw"])
        c = general.changeBit(c, 0, self._state["inputSw"])

        self._adw.Set_Par(settings.PAR_FCR + self._channel, c)

    @property
    def channel(self):
        return self._channel

    ########################################
    # Change servo state
    ########################################
    def enableRamp(self, frequency=None, amplitude=None, enableFifo=True):
        """
        Enable the ramp on this servo.

        Parameters
        ----------
        frequency: :obj:`float` in Hz.
            The frequency will be translated to a step size which is a 1 byte value.
            Therefore it is a rather discrete value with a low possible range.
        amplitude: :obj:`float` from 0 to 10
            ramp amplitude in volt.
        enableFifo: :obj:`bool`
            Defaults to :obj:`True`.
            Possible not to enable the FIFO buffering for this servo.

        """
        if self._autolock["lock"]:
            raise UserInputError(
                "Autolock is searching, ramp cannot be activated on this channel."
            )

        if self._autolock["locked"]:
            raise UserInputError(
                "Autolock is active, ramp cannot be activated on this channel."
            )

        if frequency is None:
            stepsize = self._ramp["stepsize"]
        else:
            stepsize = convertFrequency2Stepsize(frequency)
            self._ramp["stepsize"] = stepsize

        if amplitude is None:
            amplitude = self._ramp["amplitude"]
        else:
            self._ramp["amplitude"] = amplitude

        if not 0 <= amplitude <= 10:
            raise ValueError("The amplitude must be between 0 and 10!")

        self._ramp["minimum"] = 0

        control = stepsize * 0x100
        control += self._channel
        self._adw.Set_Par(settings.PAR_RCR, control)
        self._adw.Set_FPar(settings.FPAR_RAMPAMP, amplitude / 10)

        if enableFifo:
            factor = 1.2
            fifoStepsize = int(
                factor * settings.RAMP_DATA_POINTS / self._fifo["maxlen"] / stepsize
            )
            if fifoStepsize == 0:
                fifoStepsize = 1
            self.enableFifo(fifoStepsize)
            assert self.fifoStepsize == fifoStepsize

    def disableRamp(self):
        """Stop the ramp."""
        self._ramp["minimum"] = 0
        self._adw.Set_Par(settings.PAR_RCR, 0)

    @property
    def filterStates(self):
        """
        List of all filter states.

        :getter: Return the filter states.
        :setter: Set all filter states.
        :type: :obj:`list` of :code:`5*`:obj:`bool`.
        """
        self._readFilterControl()
        return self._state["filtersEnabled"]

    @filterStates.setter
    def filterStates(self, filtersEnabled):
        self._state["filtersEnabled"] = filtersEnabled
        self._sendFilterControl()

    def filterState(self, id, enabled):
        """Enable or disable the SOS filter with number `id`.

        Parameters
        ----------
        id: :obj:`int` index from 0 to 4
            Index of the filter to control.
        enabled: :obj:`bool`
            :obj:`True` to enable.

        """
        filtersEnabled = self._state["filtersEnabled"]
        filtersEnabled[id] = enabled
        self._state["filtersEnabled"] = filtersEnabled
        self._sendFilterControl()

    @property
    def auxSw(self):
        """
        Switch for mixing the aux signal to the output.

        :getter: Return the state of aux mixing.
        :setter: Enable or disable the aux mixing.
        :type: :obj:`bool`
        """
        self._readFilterControl()
        return self._state["auxSw"]

    @auxSw.setter
    def auxSw(self, enabled):
        self._state["auxSw"] = enabled
        self._sendFilterControl()

    @property
    def rampEnabled(self):
        control = self._adw.Get_Par(settings.PAR_RCR)
        if control & 15 == self._channel:
            return True
        return False

    @property
    def rampAmplitude(self):
        """
        Amplitude of servo ramp.

        :getter: Return amplitude of ramp channel.
        :setter: Set the amplitude of ramp channel.
        :type: :obj:`int`
        """
        return self._ramp["amplitude"]

    @rampAmplitude.setter
    def rampAmplitude(self, amplitude):
        if not 0 <= amplitude <= 10:
            raise UserInputError("The amplitude must be between 0 and 10!")
        self._ramp["amplitude"] = amplitude
        if self.rampEnabled:
            self.enableRamp()

    @property
    def rampFrequencyMax(self):
        """Maximum frequency that is possible for a ramp at the current sampling frequency."""
        return convertStepsize2Frequency(255)

    @property
    def rampFrequencyMin(self):
        """Minimum frequency that is possible for a ramp at the current sampling frequency."""
        return convertStepsize2Frequency(1)

    @property
    def rampFrequency(self):
        """
        Step size of servo ramp.

        :getter: Return step size of ramp channel.
        :setter: Set the step size of ramp channel.
        :type: :obj:`int`
        """
        return convertStepsize2Frequency(self._ramp["stepsize"])

    @rampFrequency.setter
    def rampFrequency(self, frequency):
        self._ramp["stepsize"] = convertFrequency2Stepsize(frequency)
        if self.rampEnabled:
            self.enableRamp()

    @property
    def offsetSw(self):
        """
        Enable or disable offset switch.

        :getter: Return the state of the switch.
        :setter: Enable or disable the offset.
        :type: :obj:`bool`
        """
        self._readFilterControl()
        return self._state["offsetSw"]

    @offsetSw.setter
    def offsetSw(self, enabled):
        self._state["offsetSw"] = enabled
        self._sendFilterControl()

    # TODO Not working robustly, yet
    # def offsetAutoSet(self):
    # """
    # Automatically adjust the input offset.

    # Before using it ensure to block the beam.
    # It takes the mean value of {} data points.
    # After changing the input amplification it may be necessary to adjust the offset.
    # """.format(10 * settings.FIFO_MAXLEN)
    # self.enableFifo(1)
    # n = 10000
    # self._waitForBufferFilling(n)
    # df = self._readoutNewData(n=n)

    # self.offset = - df['input'].mean()

    def _readLockControl(self):
        indexoffset = (self._channel - 1) * 3
        # voltage values
        self._autolock["threshold"] = convertFloat2Volt(
            self._adw.GetData_Double(settings.DATA_LOCK, 1 + indexoffset, 1)[0],
            self.auxSensitivity,
            signed=False,
        )
        self._autolock["start"] = convertFloat2Volt(
            self._adw.GetData_Double(settings.DATA_LOCK, 2 + indexoffset, 1)[0],
            self.auxSensitivity,
            signed=False,
        )
        self._autolock["end"] = convertFloat2Volt(
            self._adw.GetData_Double(settings.DATA_LOCK, 3 + indexoffset, 1)[0],
            self.auxSensitivity,
            signed=False,
        )

        # boolean values
        lcr = self._adw.Get_Par(settings.PAR_LCR)
        gcr = self._adw.Get_Par(settings.PAR_GCR)
        log.debug(bin(lcr))
        bitoffset = (self._channel - 1) * 3
        self._autolock["lock"] = general.readBit(lcr, bitoffset)
        self._autolock["locked"] = general.readBit(lcr, bitoffset + 1)
        self._autolock["relock"] = general.readBit(lcr, bitoffset + 2)
        self._autolock["greater"] = general.readBit(gcr, self._channel - 1)
        log.debug(
            f"Read out lock pars on servo {self._channel}: lcr {bin(lcr)} and {bin(gcr)}."
        )

    def _sendLockControl(self):
        # this send the control register and greater boolean
        lcr = self._adw.Get_Par(settings.PAR_LCR)
        gcr = self._adw.Get_Par(settings.PAR_GCR)
        bitoffset = (self._channel - 1) * 3
        lcr = general.changeBit(lcr, bitoffset, self._autolock["lock"])
        lcr = general.changeBit(lcr, bitoffset + 1, self._autolock["locked"])
        lcr = general.changeBit(lcr, bitoffset + 2, self._autolock["relock"])
        gcr = general.changeBit(gcr, (self._channel - 1), self._autolock["greater"])
        log.debug(
            f"Sending lock pars on servo {self._channel}: lcr {bin(lcr)} and gcr {bin(gcr)}."
        )
        self._adw.Set_Par(settings.PAR_LCR, lcr)
        self._adw.Set_Par(settings.PAR_GCR, gcr)

    def _sendLockValues(self):
        # split from _sendLockControl to avoid recursion
        # voltage values for the lock parameters
        self.lockThreshold = self._autolock["threshold"]
        self.lockSearchRange = [self._autolock["start"], self._autolock["end"]]

    def _lockIter(self):
        # just a helper method to expose the lockIterator for testing

        lockIter = self._adw.GetData_Long(settings.DATA_LOCK_ITER, self._channel, 1)[0]
        lockIter = general.convertFloat2Volt(
            lockIter, self.auxSensitivity, signed=False
        )
        return lockIter

    def _testLockOutput(self):
        # a helper to expose the last output used in locking
        # specifically, when locked this is the output value added to the lockIter of where the lock was found, meaning the new output is set as
        # out_new = lockIter + out_old
        # it is this out_old we wish to expose
        testOutput = self._adw.GetData_Long(
            settings.DATA_LOCK_OUTPUT, self._channel, 1
        )[0]
        testOutput = general.convertFloat2Volt(
            testOutput, self.auxSensitivity, signed=False
        )
        return testOutput

    @property
    def lock(self):
        """Return the lock state.

        `0`: off
        `1`: search

        :getter: Trigger a read from ADwin. Return current value.
        :setter: Set new lock state. Will convert given value to bool and then back to int.
        :type: :obj:`int`

        """
        self._readLockControl()
        return self._autolock["lock"]

    @lock.setter
    def lock(self, lock):
        if not isinstance(lock, (int, bool)):
            raise TypeError("Must be given as either an integer or a boolean.")
        lock = int(bool(lock))
        if lock:
            if self.rampEnabled:
                self.disableRamp()
            # disabling input, output and aux while searching
            self.outputSw = False
            self.inputSw = False
            self.auxSw = False
            self._autolock["locked"] = 0
        # self._readLockControl()  # os this necessary?
        self._autolock["lock"] = lock
        self._sendLockControl()

    @property
    def locked(self):
        """Return the locked state.

        `0`: not locked
        `1`: locked

        :getter: Trigger a read from ADwin. Return current value.
        :setter: Set new locked state. Will convert given value to bool and then back to int. Really only makes sense to turn this off manually, not on. Still, when manually switchig on, will make sure to turn off lock search.
        :type: :obj:`int`

        """
        self._readLockControl()
        return self._autolock["locked"]

    @locked.setter
    def locked(self, locked):
        if not isinstance(locked, (int, bool)):
            raise TypeError("Must be given as either an integer or a boolean.")
        locked = int(bool(locked))
        if locked:
            self._autolock["lock"] = 0
        self._autolock["locked"] = locked
        self._sendLockControl()

    @property
    def relock(self):
        """
        Set the lock to trigger a relock automatically when falling below or above threshold (according to `greater` setting). The `relock` parameter is either 0 or 1, can also be passed as a boolean.

        :getter: Return the current value.
        :setter: Set the condition.
        :type: :obj:`int`
        """
        self._readLockControl()
        return self._autolock["relock"]

    @relock.setter
    def relock(self, relock):
        if not isinstance(relock, (int, bool)):
            raise TypeError("Must be given as either an integer or a boolean.")
        relock = int(bool(relock))
        self._autolock["relock"] = relock
        self._sendLockControl()

    @property
    def lockGreater(self):
        """
        Set the lock direction to either greater (True) or lesser (False) than the threshold.

        :getter: Return the current value.
        :setter: Set the condition.
        :type: :obj:`bool`
        """
        self._readLockControl()
        return self._autolock["greater"]

    @lockGreater.setter
    def lockGreater(self, greater):
        if not isinstance(greater, (int, bool)):
            raise TypeError("Must be given as either an integer or a boolean.")
        greater = int(bool(greater))
        self._autolock["greater"] = greater
        self._sendLockControl()

    @property
    def lockThreshold(self):
        """Get or set the autolock threshold.

        :getter: Trigger a read from ADwin. Return the threshold.
        :setter: Set the threshold.
        :type: :obj:`float`
        """
        self._readLockControl()
        return self._autolock["threshold"]

    @lockThreshold.setter
    def lockThreshold(self, threshold):
        try:
            threshold = float(threshold)
        except (ValueError, TypeError):
            raise TypeError("threshold must be a float or int.")
        if not -10 <= threshold <= 10:
            raise ValueError(
                f"Threshold can't be outside -10 and 10 volts, was {threshold}."
            )
        # the lock state parameter is set on index 1, 6, 12 etc., as each servo channel occupies 5 indices (as of current version)
        indexoffset = (self._channel - 1) * 3
        self._autolock["threshold"] = threshold
        threshold = convertVolt2Float(threshold, self.auxSensitivity, unsigned=True)
        # Sending values to ADwin
        self._adw.SetData_Double([threshold], settings.DATA_LOCK, 1 + indexoffset, 1)

    @property
    def lockSearchRange(self):
        """Get or set the autolock search range.

        :getter: Return the a list of [start, end].
        :setter: Set the new start and end points.
        :type: :obj:`float`
        """
        self._readLockControl()
        return [self._autolock["start"], self._autolock["end"]]

    @lockSearchRange.setter
    def lockSearchRange(self, search):
        if not isinstance(search, (list, tuple)):
            raise TypeError("Search range values should come in a list or tuple-")
        if len(search) != 2:
            raise ValueError(
                f"Expected a list or tuple containing two values, was {search}."
            )

        start, end = search[0], search[1]
        try:
            float(start)
        except ValueError:
            raise TypeError(f"Start value must be a float or int, was {start}.")

        try:
            float(start)
        except ValueError:
            raise TypeError(f"End value must be a float or int, was {end}.")

        if not -10 <= start <= 10:
            raise ValueError(
                f"Search minimum has to be between -10 and 10 volts, was {start}."
            )

        if not -10 <= end <= 10:
            raise ValueError(
                f"Search maximum has to be between -10 and 10 volts, was {end}."
            )
        if (start >= end) or (end <= start):
            raise ValueError(
                f"Please make sure start and end values are different and in the correct order. Were start {start} and end {end}."
            )
        self._readLockControl()
        # simplest way to make sure nothing goes wrong is to disable a current search
        currentlock = self.lock
        if currentlock == 1:
            self.lock = 0
        # occupied indices in the data field
        indexoffset = (self._channel - 1) * 3
        self._autolock["start"] = start
        self._autolock["end"] = end
        start = convertVolt2Float(start, unsigned=True)
        end = convertVolt2Float(end, unsigned=True)
        # Sending values to ADwin
        self._adw.SetData_Double(
            [start, end], settings.DATA_LOCK, 2 + indexoffset, 2
        )  # sets both values at the same time
        if currentlock == 1:
            self.lock = 1

    @property
    def lockSearchMin(self):
        """Get only (!) the autolock search range minimum. For setting please use the `lockSearchRange` property.

        :getter: Return the threshold.
        :type: :obj:`float`
        """
        self._readLockControl()
        return self._autolock["start"]

    @property
    def lockSearchMax(self):
        """Get only (!) the autolock search range maximum. For setting please use the `lockSearchRange` property.

        :getter: Return the threshold.
        :type: :obj:`float`
        """
        self._readLockControl()
        return self._autolock["end"]

    @property
    def outputSw(self):
        """
        Enable or disable output switch.

        :getter: Return the state of the switch.
        :setter: Enable or disable the output.
        :type: :obj:`bool`
        """
        self._readFilterControl()
        return self._state["outputSw"]

    @outputSw.setter
    def outputSw(self, enabled):
        self._state["outputSw"] = enabled
        self._sendFilterControl()

    @property
    def inputSw(self):
        """
        Enable or disable input switch.

        :getter: Return the state of the switch.
        :setter: Enable or disable the input.
        :type: :obj:`bool`
        """
        self._readFilterControl()
        return self._state["inputSw"]

    @inputSw.setter
    def inputSw(self, enabled):
        self._state["inputSw"] = enabled
        self._sendFilterControl()

    @property
    def offset(self):
        """
        Offset value in volt. (-10 to 10)

        :getter: Return the offset value.
        :setter: Set the offset.
        :type: :obj:`float`
        """
        index = self._channel + 8
        data = self._adw.GetData_Double(settings.DATA_OFFSETGAIN, index, 1)[0]
        offset = convertFloat2Volt(data, self.inputSensitivity, signed=True)
        self._state["offset"] = offset

        return offset

    @offset.setter
    def offset(self, offset: float):
        limit = round(10 / pow(2, self.inputSensitivity), 2)
        if abs(offset) > limit:
            offset = copysign(limit, offset)
            log.warning(
                f"With the selected mode the offset must be in the limits of ±{limit}V. "
                "Adjusting to {offset}V..."
            )
        self._state["offset"] = offset
        index = self._channel + 8
        offsetInt = convertVolt2Float(offset, self.inputSensitivity)
        self._adw.SetData_Double([offsetInt], settings.DATA_OFFSETGAIN, index, 1)

    @property
    def gain(self):
        """
        Overall gain factor.

        :getter: Return the gain value.
        :setter: Set the gain.
        :type: :obj:`float`
        """
        index = self._channel
        data = self._adw.GetData_Double(settings.DATA_OFFSETGAIN, index, 1)[0]
        gain = data * pow(2, self.inputSensitivity)
        self._state["gain"] = gain

        return gain

    @gain.setter
    def gain(self, gain):
        self._state["gain"] = gain
        index = self._channel
        effectiveGain = gain / pow(2, self.inputSensitivity)
        self._adw.SetData_Double([effectiveGain], settings.DATA_OFFSETGAIN, index, 1)

    @property
    def inputSensitivity(self):
        r"""
        Input sensitivity mode (0 to 3).

        The input voltage is amplified by :math:`2^\mathrm{mode}`.

        +------+---------------+------------+
        | mode | amplification | limits (V) |
        +======+===============+============+
        | 0    | 1             | 10         |
        +------+---------------+------------+
        | 1    | 2             | 5          |
        +------+---------------+------------+
        | 2    | 4             | 2.5        |
        +------+---------------+------------+
        | 3    | 8             | 1.25       |
        +------+---------------+------------+

        :getter: Return the sensitivity mode.
        :setter: Set the mode.
        :type: :obj:`int`
        """
        data = self._adw.Get_Par(settings.PAR_SENSITIVITY)
        mask = 3
        # bit shifting backwards
        mode = data >> self._channel * 2 - 2 & mask
        self._state["inputSensitivity"] = mode

        return mode

    @inputSensitivity.setter
    def inputSensitivity(self, mode):
        if not 0 <= mode <= 3:
            raise ValueError("Choose a mode between 0 and 3")
        gain = self.gain
        offset = self.offset

        self._state["inputSensitivity"] = mode

        currentRegister = self._adw.Get_Par(settings.PAR_SENSITIVITY)
        register = general.clearBit(currentRegister, self._channel * 2 - 2)
        register = general.clearBit(register, self._channel * 2 - 1)

        # bit shifting
        register += mode << self._channel * 2 - 2

        self._adw.Set_Par(settings.PAR_SENSITIVITY, register)

        # Update gain to correct gain change from input sensitivity
        self.gain = gain
        self.offset = offset

    @property
    def auxSensitivity(self):
        r"""
        Aux sensitivity mode (0 to 3).

        The input voltage is amplified by :math:`2^\mathrm{mode}`.

        +------+---------------+------------+
        | mode | amplification | limits (V) |
        +======+===============+============+
        | 0    | 1             | 10         |
        +------+---------------+------------+
        | 1    | 2             | 5          |
        +------+---------------+------------+
        | 2    | 4             | 2.5        |
        +------+---------------+------------+
        | 3    | 8             | 1.25       |
        +------+---------------+------------+

        :getter: Return the sensitivity mode.
        :setter: Set the mode.
        :type: :obj:`int`
        """

        data = self._adw.Get_Par(settings.PAR_SENSITIVITY)
        mask = 3
        # bit shifting backwards
        mode = data >> self._channel * 2 + 14 & mask
        self._state["auxSensitivity"] = mode

        return mode

    @auxSensitivity.setter
    def auxSensitivity(self, mode):
        if not 0 <= mode <= 3:
            raise ValueError(f"Choose a mode between 0 and 3, was {mode}.")

        # saving old lock parameters
        threshold = self.lockThreshold

        self._state["auxSensitivity"] = mode

        currentRegister = self._adw.Get_Par(settings.PAR_SENSITIVITY)
        register = general.clearBit(currentRegister, self._channel * 2 + 14)
        register = general.clearBit(register, self._channel * 2 + 15)

        register += mode << self._channel * 2 + 14

        self._adw.Set_Par(settings.PAR_SENSITIVITY, register)

        # setting lock parameters with new sensitivity
        self.lockThreshold = threshold

    @property
    def filters(self):
        """
        All second order sections (SOS) of all filters.

        A neutral filter matrix looks like:

        .. code:: python

            [ [1, 0, 0, 0, 0],
              [1, 0, 0, 0, 0],
              [1, 0, 0, 0, 0],
              [1, 0, 0, 0, 0],
              [1, 0, 0, 0, 0] ]

        Use :obj:`ServoDesign` from :obj:`openqlab.analysis` to create your filters.
        That object you can simply pass to a servo using :obj:`applyServoDesign`.

        :getter: Return all filter values.
        :setter: Write all 5 filters to ADwin and trigger reloading.
        :type: :code:`(5, 5)` matrix with filter values (:obj:`float`).
        """
        startIndex = (
            self._channel - 1
        ) * settings.NUMBER_OF_FILTERS * settings.NUMBER_OF_SOS + 1

        data = self._adw.GetData_Double(
            settings.DATA_FILTERCOEFFS,
            startIndex,
            settings.NUMBER_OF_FILTERS * settings.NUMBER_OF_SOS,
        )

        for i in range(settings.NUMBER_OF_FILTERS):
            for j in range(settings.NUMBER_OF_SOS):
                self._state["filters"][i][j] = data[i * settings.NUMBER_OF_FILTERS + j]

        return list(self._state["filters"])

    @filters.setter
    def filters(self, filters):
        if not len(filters) == settings.NUMBER_OF_FILTERS:
            raise IndexError(
                f"A servo must have exactly {settings.NUMBER_OF_FILTERS} filters!"
            )
        for filter in filters:
            if not len(filter) == settings.NUMBER_OF_SOS:
                raise IndexError(
                    f"A servo must have exactly {settings.NUMBER_OF_FILTERS} filters with {settings.NUMBER_OF_SOS} SOS!"
                )

        self._state["filters"] = filters

        startIndex = (
            self._channel - 1
        ) * settings.NUMBER_OF_FILTERS * settings.NUMBER_OF_SOS + 1

        data = []
        for filter in filters:
            for i in filter:
                data.append(i)

        self._adw.SetData_Double(
            data, settings.DATA_FILTERCOEFFS, startIndex, len(data)
        )

        self._triggerReload()

    def applyServoDesign(self, servoDesign=None):
        """
        Apply filters from a :obj:`ServoDesign` object.

        Parameters
        ----------
        servoDesign: :obj:`openqlab.analysis.ServoDesign`
            Object to apply filters from.
        """
        if servoDesign is None:
            servoDesign = self.servoDesign
        else:
            self.servoDesign = servoDesign
        discreteServoDesign = servoDesign.discrete_form(
            sampling_frequency=settings.SAMPLING_RATE
        )
        filters6 = discreteServoDesign["filters"]  # returns a list of dicts
        filters = [[1.0, 0, 0, 0, 0]] * servoDesign.MAX_FILTERS
        filtersEnabled = [False] * servoDesign.MAX_FILTERS

        for f in filters6:
            j = f["index"]
            filters[j] = rearrange_filter_coeffs(f["sos"])
            filtersEnabled[j] = f["enabled"]

        log.info(servoDesign)

        self.gain = discreteServoDesign["gain"]
        self.filters = filters
        self.filterStates = filtersEnabled

    #########################################
    # Realtime plotting
    #########################################
    def _calculateRefreshTime(self):
        bufferFillingLevel = 0.5
        if self.rampEnabled:
            bufferFillingLevel = 1

        refreshTime = (
            self._fifo["stepsize"]
            / settings.SAMPLING_RATE
            * bufferFillingLevel
            * self._fifo["maxlen"]
        )

        if refreshTime < self.MIN_REFRESH_TIME:
            refreshTime = self.MIN_REFRESH_TIME
        self.realtime["refreshTime"] = refreshTime

    @property
    def _fifoBufferSize(self) -> int:
        """Get the current size of the fifo buffer on ADwin."""
        return self._adw.Fifo_Full(settings.DATA_FIFO)

    @property
    def fifoStepsize(self) -> int:
        """
        Setter DEPRECATED: Use :obj:`nqontrol.Servo.enableFifo()`

        Trigger ADwin to write the three channels of this servo to the FIFO buffer to read it with the PC over LAN.

        :code:`input`, :code:`aux` and :code:`output` will be sent.

        :getter: Number of program cycles between each data point.
        :setter: Set the number or choose `None` to disable the FiFo output.
        :type: :obj:`int`
        """
        return self._fifo["stepsize"]

    @property
    def realtimeEnabled(self) -> bool:
        if self.realtime["enabled"] and self.fifoEnabled:
            return True

        return False

    @property
    def fifoEnabled(self) -> bool:
        if self._adw.Get_Par(settings.PAR_ACTIVE_CHANNEL) == self._channel:
            return True

        return False

    def enableFifo(
        self, stepsize: Optional[int] = None, frequency: Optional[float] = None
    ):
        """
        Trigger ADwin to write the three channels of this servo to the
        FIFO buffer to read it with the PC over LAN.

        :code:`input`, :code:`aux` and :code:`output` will be sent.

        Parameters
        ----------
            stepsize: :obj:`int`
                Number of program cycles between each data point.
                If unset it will stay the same or use the default ({})

        """.format(
            self.DEFAULT_FIFO_STEPSIZE
        )
        if frequency is not None:
            self.rampFrequency = frequency
        if stepsize is None:
            stepsize = self._fifo["stepsize"]
        if not isinstance(stepsize, int) or stepsize < 1:
            raise ValueError(
                f"The stepsize must be a positive integer, but it was: {stepsize}"
            )

        self._fifo["stepsize"] = stepsize
        # Enable on adwin
        self._adw.Set_Par(settings.PAR_ACTIVE_CHANNEL, self._channel)
        if stepsize is not None:
            self._adw.Set_Par(settings.PAR_FIFOSTEPSIZE, stepsize)
        # set refresh time
        self._calculateRefreshTime()
        # Create local buffer
        self._createDataFrame()

    def disableFifo(self):
        """Disable the FiFo output if it is enabled on this channel."""
        if self.fifoEnabled:
            # Disable on adwin only if this channel is activated
            self._adw.Set_Par(settings.PAR_ACTIVE_CHANNEL, 0)
            self._adw.Set_Par(settings.PAR_FIFOSTEPSIZE, 0)
            # Destroy local buffer
            self._fifoBuffer = None

    def _readoutNewData(self, n: int) -> DataFrame:
        m: int = self._fifoBufferSize
        if n > m:
            n = m

        newData: DataFrame = DataFrame(columns=self.DEFAULT_COLUMNS)

        if n == 0:
            log.warning("I should readout 0 data.")
            return newData

        # Saving 3 16bit channels in a 64bit long variable
        # Byte    | 7 6 | 5 4   | 3 2 | 1 0    |
        # Channel |     | input | aux | output |
        combined = np.array(
            self._adw.GetFifo_Double(settings.DATA_FIFO, n)[:], dtype="int"
        )

        def extractValue(combined, offset=0):
            shifted = np.right_shift(combined, offset)
            return np.bitwise_and(shifted, 0xFFFF)

        log.debug(extractValue(combined[0], 32))
        log.debug(extractValue(combined[0], 16))
        log.debug(extractValue(combined[0]))

        newData["input"] = convertFloat2Volt(
            extractValue(combined, 32), self._state["inputSensitivity"]
        )
        newData["aux"] = convertFloat2Volt(
            extractValue(combined, 16), self._state["auxSensitivity"]
        )
        newData["output"] = convertFloat2Volt(extractValue(combined))

        log.debug(newData["input"][0])
        log.debug(newData["aux"][0])
        log.debug(newData["output"][0])

        return newData

    def _prepareContinuousData(self) -> None:
        # if we will get speed problems we should implement a more efficient version,
        # e.g. a ring array behaviour.
        n: int = self._fifoBufferSize
        if n == 0:
            return

        maxLen: int = self._fifo["maxlen"]
        buf: DataFrame = DataFrame()

        if n >= maxLen:
            n = maxLen
        else:
            # local copy of the `maxlen-n` newest entries.
            if self._fifo["maxlen"] < len(buf) + n:
                raise Bug(
                    f'That check should not fail. maxlen = {self._fifo["maxlen"]}, '
                    "len(buf) = {len(DataFrame(self._fifoBuffer[n:]))}, "
                    "lenBefore = {len(self._fifoBuffer)}, n = {n}"
                )

        # Read new data
        newData: DataFrame = self._readoutNewData(n)
        # Append to the local DataFrame
        self._fifoBuffer = buf.append(newData, sort=False)

        newLen: int = len(self._fifoBuffer)
        if newLen > self._fifo["maxlen"]:
            raise Bug(
                f"That is a bug. Please report it. "
                "len(newData): {len(newData)}, len(buf): {len(buf)}"
            )

        dt: float = self._timeForFifoCycles(1)
        self._fifoBuffer.index = np.arange(0, newLen * dt, dt)[:newLen]

    def _prepareRampData(self, tries=3):
        # TODO: some refactoring...
        # The logic, when to search a new minimum is semi-good
        if tries < 1:
            log.warning("tries must be at least 1.")
            tries = 1

        found_min = False

        for i in range(tries):
            log.info("Try {0} of {1}".format(i + 1, tries))
            maxlen = self._fifo["maxlen"]
            if self._ramp["minimum"] == 0:
                self._ramp["minimum"] = self._searchRampMinimum()
            if self._ramp["minimum"] is None:
                continue  # Next try when there could not be found a minimum
            # Wait untill we have enough entries
            self._waitForBufferFilling(n=3 * self._fifo["maxlen"])
            # Take data
            newData = self._readoutNewData(3 * self._fifo["maxlen"])
            # Find the first minimum
            try:
                start = newData.loc[
                    (newData["output"] - self._ramp["minimum"]) <= 1e-2
                ].index[0]
                found_min = True
                break
            except IndexError:
                log.warning("Could not find a ramp minimum.")
                self._ramp["minimum"] = self._searchRampMinimum()

        if not found_min:
            log.warning(
                f"Unable to find the ramp minimum '\
                        '{self._ramp['minimum']} in {tries} tries. Giving up..."
            )
            return

        # Copy data from the first minimum untill the end
        localBuffer = DataFrame(newData[start : start + self._fifo["maxlen"]])

        # Calculate times for the index
        length = len(localBuffer)
        dt = self._timeForFifoCycles(1)
        localBuffer.index = np.arange(0, length * dt, dt)[:length]

        # print a message if n != maxlen
        # update only if n = maxlen
        if length == maxlen:
            self._fifoBuffer = DataFrame(localBuffer)
        else:
            log.warning(
                f"Could not read the correct length of ramp data. "
                "It was: {len(localBuffer)}"
            )

    def _timeForFifoCycles(self, n):
        return n * self._fifo["stepsize"] / settings.SAMPLING_RATE

    def _waitForBufferFilling(self, n=None, refill=True):
        if n is None:
            n = self._fifo["maxlen"]
        if refill:
            cycles = n
        else:
            bufferSize = self._fifoBufferSize
            if bufferSize < n:
                cycles = n - bufferSize
            else:
                return
        sleep(self._timeForFifoCycles(cycles))

    def _createDataFrame(self):
        data = {"input": [], "aux": [], "output": []}
        self._fifoBuffer = DataFrame(data=data)

    def _searchRampMinimum(self, tries=6):
        allowed_error = 0.1 * self._ramp["amplitude"]

        for i in range(tries):
            log.info("Try {0} of {1}".format(i + 1, tries))
            self._waitForBufferFilling(n=4 * self._fifo["maxlen"])
            data = self._readoutNewData(2 * self._fifo["maxlen"])

            if len(data) != 2 * self._fifo["maxlen"]:
                log.warning(
                    "Want to read {} entries, but got {}.".format(
                        2 * self._fifo["maxlen"], len(data)
                    )
                )

            minimum = data.min()["output"]

            if minimum is None:
                log.warning("Could not find a minimum.")

            if self._ramp["amplitude"] + minimum < allowed_error:
                log.info("Found the minimum of {}.".format(minimum))
                assert minimum is not None
                return minimum
            log.info(
                "The minimum I found, was {}, but it should be {}.".format(
                    minimum, -self._ramp["amplitude"]
                )
            )

        log.warning(
            "Could not find the correct minimum after {0} tries. The method should be optimized if it happens often.".format(
                tries
            )
        )
        return None

    def _prepareData(self):
        """Return new data from ADwin."""
        if not self.fifoEnabled:
            log.warning("The FiFo output was not activated. Enabling now...")
            self.enableFifo()
        if self.rampEnabled:
            self._prepareRampData()
        else:
            self._prepareContinuousData()
        return self._fifoBuffer[self.realtime["ydata"]]

    def _realtimeLoop(self):
        # plotting loop
        assert (
            self.realtimeEnabled
        ), "Realtime should be enabled when starting the loop."

        # generate plot
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.ion()  # interactive mode

        try:
            while self.realtimeEnabled:
                timeStart = time()
                ax.clear()
                if self.realtime["ylim"] is None:
                    ax.set_ylim(auto=True)
                else:
                    ax.set_ylim(self.realtime["ylim"])
                ax.plot(self._prepareData())
                ax.legend(self.realtime["ydata"], loc=1)

                timePause = self.realtime["refreshTime"] - time() + timeStart
                if timePause <= 0:
                    timePause = 1e-6

                plt.pause(timePause)
        except (KeyboardInterrupt, TclError):
            plt.close("all")
            log.info("Plot closed")
        finally:
            # Ensure that `realtime` is disabled if the plot is closed
            log.info("Stop plotting...")
            self.realtime["enabled"] = False
            self._subProcess = None

    def stopRealtimePlot(self):
        """Stop the realtime plot."""
        self.realtime["enabled"] = False
        if self._subProcess is not None:
            self._subProcess.join()
        else:
            log.warning("No subprocess had been started.")
            return
        assert not self._subProcess.is_alive(), "The subprocess should be finished!"

    def realtimePlot(self, ydata=None, refreshTime=None, multiprocessing=True):
        """
        Enable parallel realtime plotting.

        To stop the running job call `stopRealtimePlot()`.

        Parameters
        ----------
        ydata: :obj:`list` of :obj:`str`
            Choose the data to be plotted: :code:`['input', 'aux', 'output']`.
        refreshTime: :obj:`float`
            Sleeping time (s) between plot updates.

        """
        if self._subProcess is not None and self._subProcess.is_alive():
            raise UserInputError(
                "Do you really want more than one plot of the same data? It is not implemented..."
            )
        if self._fifoBuffer is None:
            log.info(
                "Enabling the FiFo buffer with a default step size of {}...".format(
                    self.DEFAULT_FIFO_STEPSIZE
                )
            )
            self.enableFifo()

        # Update local parameters
        self.realtime["enabled"] = True
        if ydata:
            self.realtime["ydata"] = ydata
        if refreshTime:
            self.realtime["refreshTime"] = refreshTime

        # Start plotting process
        if multiprocessing:
            self._subProcess = mp.Process(target=self._realtimeLoop)
            self._subProcess.start()
        else:
            self._realtimeLoop()

    ########################################
    # Temperature feedback
    ########################################
    @property
    def tempFeedback(self):
        """The temperature feedback server associated with the servo.

        :getter: Return the :obj:`FeedbackController`.
        :setter: Set a new :obj:`FeedbackController`.
        :type: :obj:`FeedbackController`.
        """
        return self._tempFeedback

    def tempFeedbackStart(
        self,
        dT=None,
        mtd=None,
        voltage_limit=None,
        server=settings.DEFAULT_TEMP_HOST,
        port=settings.DEFAULT_TEMP_PORT,
        update_interval=None,
    ):
        """Start the temperature feedback server. Setup a server if it hasn't been previously set.

        Parameters
        ----------
        dT : :obj:`float`
            Description of parameter `dT`.
        mtd : :obj:`tuple`
            (1, 1)
        voltage_limit : :obj:`float`
            The maximum voltage to which one can go using the temperature control (the default is 5).
        server : type
            Description of parameter `server` (the default is settings.DEFAULT_TEMP_HOST).
        port : type
            Description of parameter `port` (the default is settings.DEFAULT_TEMP_PORT).
        update_interval : :obj:`float`
            Description of parameter `update_interval` (the default is 1).

        """
        if dT is None:
            dT = self._tempFeedbackSettings["dT"]
        if mtd is None:
            mtd = self._tempFeedbackSettings["mtd"]
        if voltage_limit is None:
            voltage_limit = self._tempFeedbackSettings["voltage_limit"]
        if update_interval is None:
            update_interval = self._tempFeedbackSettings["update_interval"]

        self._tempFeedback = FeedbackController(
            self, dT, mtd, voltage_limit, server, port, update_interval
        )
        self.tempFeedback.start()

    def tempFeedbackStop(self):
        self.tempFeedback.enabled = False
        self.tempFeedback.join()
        self._tempFeedback = None

    ########################################
    # Save and load settings
    ########################################
    def _applySettingsDict(self, data):
        # Don't import the channel because it isn't possible to change it.
        DONT_SERIALIZE = self.DONT_SERIALIZE + ["_channel"]
        for d in self.__dict__:
            value = data.get(d.__str__())
            if (d.__str__() not in DONT_SERIALIZE) and (value is not None):
                if d.__str__() in self.JSONPICKLE:
                    self.__dict__[d.__str__()] = jsonpickle.decode(value)
                elif isinstance(value, dict):
                    self.__dict__[d.__str__()].update(value)
                else:
                    self.__dict__[d.__str__()] = value

    def getSettingsDict(self):
        """
        Get a dict with all servo settings.

        Returns
        -------
        :obj:`dict`
            Return all important settings for the current servo state.
        """
        # load state from adwin
        self._readAllFromAdwin()

        # save settings
        data = {}
        for d in self.__dict__:
            if d.__str__() not in self.DONT_SERIALIZE:
                value = self.__dict__[d.__str__()]
                # Convert dicts from multiprocessing
                if isinstance(value, (dict, mp.managers.DictProxy)):
                    value = dict(value)
                elif d.__str__() in self.JSONPICKLE:
                    value = jsonpickle.encode(value)
                data[d.__str__()] = value
        return data

    def saveJsonToFile(self, filename):
        """
        Save this single servo as json to a file.

        Parameters
        ----------
        filename: :obj:`str`
            Filename to save the json file.

        """
        data = {self.__class__.__name__: self.getSettingsDict()}
        with open(filename, "w+") as file:
            json.dump(data, file, indent=2)

    def loadSettings(self, applySettings):
        """
        Load settings from file or dict.

        Not reading the channel, it can only be set on creating a servo object.

        Parameters
        ----------
        applySettings: :obj:`str` or :obj:`dict`
            Settings to load for this servo.

        """
        if isinstance(applySettings, dict):
            load_settings = applySettings
        elif isinstance(applySettings, str):
            load_settings = self._readJsonFromFile(applySettings)
        else:
            raise ValueError("You can only apply settings from a file or a dict.")

        self._applySettingsDict(load_settings)
        self._sendAllToAdwin()

    def _readJsonFromFile(self, filename):
        """
        Read settings from a single servo file.

        return: dict with only the servo settings
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError as e:
            raise e

        if not data.get(self.__class__.__name__):
            raise SyntaxError("Invalid file.")

        return data[self.__class__.__name__]
