import logging as log
from time import time

import numpy as np
from ADwin import ADwinError
from scipy import signal

from . import general, settings


class MockADwin:
    NUM_SERVOS = 8

    def __init__(self, DeviceNo=0, raiseError=False):
        self.DeviceNo = DeviceNo
        self._par = [0] * 80
        self._fpar = [0] * 80
        self._running = [0] * 10
        self._data_double = [[]] * 200
        self._data_long = [[]] * 200
        self.ADwindir = "mock"
        self._boot_time = time()
        self._last_read = 0
        self._n_last = 0

        self._raiseError = False
        self.reset_trigger = True
        self._raiseError = raiseError

        self._data_long[settings.DATA_LAST_OUTPUT - 1] = [0] * self.NUM_SERVOS
        self._data_long[settings.DATA_MONITORS - 1] = [0] * self.NUM_SERVOS
        # lock parameters
        self._data_double[settings.DATA_LOCK - 1] = [0] * (self.NUM_SERVOS * 3)
        # helper field, exposes the lockIterator
        self._data_long[settings.DATA_LOCK_ITER - 1] = [0] * self.NUM_SERVOS
        # helper field, exposes recent lock output as test value
        self._data_long[settings.DATA_LOCK_OUTPUT - 1] = [0] * self.NUM_SERVOS
        # internal field, direction of the lock step, either +1 or -1
        self._lockStep = [1] * self.NUM_SERVOS
        # time difference
        self.Set_Par(settings.PAR_TIMEDIFF, 3000)

    def Boot(self, file):
        self._boot_time = time()

    def Workload(self):  # pylint: disable=no-self-use
        return 42

    def Process_Status(self, no):
        return self._running[no - 1]

    def Load_Process(self, process):
        pass

    def Start_Process(self, no):
        self._running[no - 1] = 1

    def Set_FPar(self, index, par):
        self._fpar[index - 1] = float(par)

    def Set_Par(self, index, par):
        if self._raiseError:
            raise ADwinError("test", "Test Error", 13)

        if index == 3 and par != 0:
            self._last_read = time()
        self._par[index - 1] = int(par)

    def Get_Par(self, index):
        self._par_special_functions()
        return self._par[index - 1]

    def Get_FPar(self, index):
        self._fpar_special_functions()
        return self._fpar[index - 1]

    def GetData_Double(self, DataNo, Startindex, Count):
        return list(
            self._data_double[DataNo - 1][Startindex - 1 : Startindex + Count - 1]
        )

    def SetData_Double(self, Data, DataNo, Startindex, Count):
        self._data_double[DataNo - 1][Startindex - 1 : Startindex + Count - 1] = Data

    def GetData_Long(self, DataNo, Startindex, Count):
        self._data_long_special_functions(DataNo)
        return list(
            self._data_long[DataNo - 1][Startindex - 1 : Startindex - 1 + Count]
        )

    def _data_long_special_functions(self, no):
        if no == settings.DATA_LAST_OUTPUT:
            for i in range(1, 9):
                if self._isRamp():
                    out = np.random.randint(0, 2 ** 16)
                else:
                    out = 2 ** 15
                self.SetData_Long([out], settings.DATA_LAST_OUTPUT, i, 1)
        elif no == settings.DATA_LOCK_ITER:
            for i in range(1, 9):
                # lock stuff
                indexoffset = (i - 1) * 3
                data = self._data_double[settings.DATA_LOCK - 1]
                start = data[indexoffset + 1]
                end = data[indexoffset + 2]
                out = np.random.randint(start, end)
                log.debug(f"range {start} {end}")
                self.SetData_Long([out], settings.DATA_LOCK_ITER, i, 1)

    def SetData_Long(self, Data, DataNo, Startindex, Count):
        self._data_long[DataNo - 1][Startindex - 1 : Startindex + Count - 1] = Data

    def Fifo_Full(self, index):
        diff = time() - self._last_read
        fifoStepsize = self.Get_Par(6)
        n = int(diff * settings.SAMPLING_RATE / fifoStepsize)
        n = n + self._n_last
        if n > settings.FIFO_BUFFER_SIZE:
            n = settings.FIFO_BUFFER_SIZE
        self._n_last = n
        return int(n)

    def _rampChannel(self):
        return self.Get_Par(settings.PAR_ACTIVE_CHANNEL)

    def _isRamp(self):
        channel = self._rampChannel()
        if channel == 0:
            return False
        control = self.Get_Par(settings.PAR_RCR)
        if control & 15 == channel:
            return True
        return False

    def _readSwitches(self, channel):
        c = self.Get_Par(10 + channel)
        # read control bits
        auxSw = general.readBit(c, 9)
        offsetSw = general.readBit(c, 2)
        outputSw = general.readBit(c, 1)
        inputSw = general.readBit(c, 0)
        return inputSw, offsetSw, auxSw, outputSw

    @staticmethod
    def _limitOutput(output):
        # Limit the output to 16bit
        output[output > 0xFFFF] = 0xFFFF
        output[output < 0] = 0
        return output

    def _constructOutput(self, amount, input_, aux):
        channel = self.Get_Par(settings.PAR_ACTIVE_CHANNEL)
        inputSw, offsetSw, auxSw, outputSw = self._readSwitches(channel)

        # lock stuff
        lock = general.readBit(self._par[settings.PAR_LCR - 1], (channel - 1) * 3)
        locked = general.readBit(self._par[settings.PAR_LCR - 1], (channel - 1) * 3 + 1)

        start = self._data_double[settings.DATA_LOCK - 1][(channel - 1) * 3 + 1]
        end = self._data_double[settings.DATA_LOCK - 1][(channel - 1) * 3 + 2]
        if lock and not locked:
            # dont be confused by the sensitivity thing below, this is just the aux sensitivity for a given channel, extracted via bitshifting and a mask

            output = (
                # this is the amplitude
                general.convertFloat2Volt(
                    end - start + 0x8000,  # take the difference of both, add zero point
                    self._par[settings.PAR_SENSITIVITY - 1] >> channel * 2 + 14 & 3,
                    False,
                )
                # and some constructed signal
                * (signal.sawtooth(np.linspace(0, 2 * np.pi, amount), 0.5) + 1)
                / 2
            )

            output = general.convertVolt2Float(output) + start
        elif locked:
            output = np.full(
                amount, self._data_long[settings.DATA_LOCK_ITER - 1][channel - 1]
            ).astype(int)
        else:
            output = np.full(amount, 0x8000).astype(int)
            if not outputSw:
                return output
            if inputSw:
                output = input_
            if offsetSw:
                offset = self.GetData_Double(settings.DATA_OFFSETGAIN, channel + 8, 1)
                output = output + offset
            output = (output - 0x8000) * self.GetData_Double(
                settings.DATA_OFFSETGAIN, channel, 1
            ) + 0x8000
            if auxSw:
                output = output + (aux - 0x8000)

        return self._limitOutput(output)

    @staticmethod
    def _extract_value(par, offset=0):
        shifted = np.right_shift(par, offset)
        return np.bitwise_and(shifted, 0xFF)

    def GetFifo_Double(self, index, amount):
        assert index == settings.DATA_FIFO, f"Index has to be {settings.DATA_FIFO}."

        amount = int(amount)
        # is ramp enabled
        isRamp = self._isRamp()
        # Creating random data
        input_ = np.random.normal(0x8000, 10, size=amount).astype(int)
        aux = np.random.normal(0x8000, 10, size=amount).astype(int)

        # if ramp has been set the output will just be the ramp signal
        if not isRamp:
            output = self._constructOutput(amount, input_, aux)
        else:
            # construct the ramp signal
            rampPar = self.Get_Par(settings.PAR_RCR)

            # first extracting the stepsize, then converting to frequency
            frequency = general.convertStepsize2Frequency(
                self._extract_value(rampPar, 8)
            )
            amplitude = self.Get_FPar(settings.FPAR_RAMPAMP) * 10
            lin = np.linspace(0, 1, amount)
            output = amplitude * signal.sawtooth(2 * np.pi * frequency * lin, 0.5)
            output = general.convertVolt2Int(output) + 0x8000
        # concatenating bits
        crunch = np.left_shift(input_, 32)
        crunch = np.add(crunch, np.left_shift(aux, 16))
        crunch = np.add(crunch, output)
        # setting last readout time to current
        self._last_read = time()
        self._n_last = self._n_last - amount
        return crunch

    def Get_Processdelay(self, index):  # pylint: disable=no-self-use
        return 1e9 / settings.SAMPLING_RATE

    def _par_special_functions(self):
        self._par[0] = time() - self._boot_time  # Timestamp
        if self.reset_trigger:
            self._par[1] = 0  # Resetting trigger
        else:
            self._par[1] = 0xFFFF  # Not resetting trigger

        # locking emulation
        aux = 0x8000
        data = self._data_double[settings.DATA_LOCK - 1]
        for servo in range(1, 9):

            indexoffset = (servo - 1) * 3

            lcr = self._par[settings.PAR_LCR - 1]
            gcr = self._par[settings.PAR_GCR - 1]

            lock = general.readBit(lcr, indexoffset)
            locked = general.readBit(lcr, indexoffset + 1)
            relock = general.readBit(lcr, indexoffset + 2)
            greater = general.readBit(gcr, (servo - 1))

            threshold = data[indexoffset]
            start = data[indexoffset + 1]
            end = data[indexoffset + 2]

            if not lock and not locked:
                # not searching, lock iter
                self._data_long[settings.DATA_LOCK_ITER - 1][servo - 1] = 0

            if lock:
                log.debug(
                    f"using aux {general.convertFloat2Volt(aux, self._par[settings.PAR_SENSITIVITY - 1] >> servo * 2 + 14 & 3, False)}"
                )
                # ensure locked is 0 when searching
                self._par[settings.PAR_LCR - 1] = general.clearBit(
                    self._par[settings.PAR_LCR - 1], indexoffset + 1
                )
                if self._data_long[settings.DATA_LOCK_ITER - 1][servo - 1] == 0:
                    self._data_long[settings.DATA_LOCK_ITER - 1][servo - 1] = start
                    # turn off input, output, aux
                    c = self._par[10 + (servo - 1)]
                    # clear control bits
                    c = general.clearBit(c, 0)  # input
                    c = general.clearBit(c, 1)  # output
                    c = general.clearBit(c, 9)  # aux
                    self._par[10 + (servo - 1)] = c
                    # technically filter history is cleared here, but its not implemented on mockADwin

                # a lock is found
                if (greater and aux > threshold) or ((aux < threshold) and not greater):
                    log.debug("found lock ")
                    log.debug(
                        f"lcr {self._par[settings.PAR_LCR - 1]} gcr {self._par[settings.PAR_GCR - 1]} offset {indexoffset}"
                    )
                    # set locked
                    self._par[settings.PAR_LCR - 1] = general.setBit(
                        self._par[settings.PAR_LCR - 1], indexoffset + 1
                    )
                    # set not searching (lock = 0)
                    self._par[settings.PAR_LCR - 1] = general.clearBit(
                        self._par[settings.PAR_LCR - 1], indexoffset
                    )
                    c = self._par[10 + (servo - 1)]
                    c = general.setBit(c, 0)  # enable input
                    c = general.setBit(c, 1)  # enable output
                    self._par[10 + (servo - 1)] = c
                else:  # searching for lock
                    if self._data_long[settings.DATA_LOCK_ITER - 1][servo - 1] == start:
                        self._lockStep[servo - 1] = 1
                    elif self._data_long[settings.DATA_LOCK_ITER - 1][servo - 1] == end:
                        self._lockStep[servo - 1] = -1

                    self._data_long[settings.DATA_LOCK_ITER - 1][servo - 1] = (
                        self._data_long[settings.DATA_LOCK_ITER - 1][servo - 1]
                        + self._lockStep[servo - 1]
                    )
                    c = self._par[10 + (servo - 1)]
                    # clear control bits
                    c = general.clearBit(c, 0)  # input
                    c = general.clearBit(c, 1)  # output
                    self._par[10 + (servo - 1)] = c

            if locked:
                # if lock fails, set locked to 0
                if (greater and (aux < threshold * 0.9)) or (
                    not greater and (aux > threshold * 1.1)
                ):
                    if relock:
                        self._par[settings.PAR_LCR - 1] = general.setBit(
                            self._par[settings.PAR_LCR - 1], indexoffset
                        )  # activate lock search again
                    self._par[settings.PAR_LCR - 1] = general.clearBit(
                        self._par[settings.PAR_LCR - 1], indexoffset + 1
                    )
                    self._data_long[settings.DATA_LOCK_ITER - 1][servo - 1] = 0
                self._data_long[settings.DATA_LOCK_OUTPUT - 1][servo - 1] = 0x8000

    def _fpar_special_functions(self):
        pass
