# -*- coding: utf-8 -*-

"""package ad9xdds
author    Benoit Dubois
copyright FEMTO ENGINEERING, 2019
license   GPL v3.0+
brief     Emulation of basic DDS board AD9912Dev
"""

import logging
import signalslot as ss
from ad9xdds.dds_core import AbstractDds

AD_VENDOR_ID = 0x0456
AD9912DEV_PRODUCT_ID = 0xee09
AD9549DEV_PRODUCT_ID = 0xee08
DDS_DEVICE_LIST = {'AD9912': 'Ad9912Dev'}


# =============================================================================
class Ad9912Emul(AbstractDds):
    """Class 'emulating' a DDS development card.
    Used for test when no real device is available.
    """

    FTW_SIZE = 48               # Frequency Tuning Word register size (bit)
    PHASE_SIZE = 14             # Phase register size (bit)
    DAC_OUT_SIZE = 10           # Output DAC resolution (bit)
    IFMAX = 1000000000          # Input maximum frequency (Hz)
    OFMAX = 400000000           # Output maximum frequency (Hz)
    AMAX = (1 << DAC_OUT_SIZE) - 1

    def __init__(self):
        super().__init__()
        self._ifreq = None
        self._ofreq = None
        self._phy = None
        self._amp = None
        self._is_connected = False
        logging.info("Init DDS test device: %r", self)

    def connect(self):
        logging.info("Connect to DDS test device")
        self._is_connected = True
        return True

    def is_connected(self):
        return self._is_connected

    def set_ifreq(self, ifreq):
        logging.debug("DdsTestDev.set_ifreq(" + str(ifreq) + ")")
        self._ifreq = float(ifreq)

    def get_ifreq(self):
        logging.debug("DdsTestDev.get_ifreq() = " + str(self._ifreq))
        return self._ifreq

    def set_ofreq(self, ofreq):
        logging.info("DdsTestDev.set_ofreq(" + str(ofreq) + ")")
        self._ofreq = float(ofreq)
        return ofreq

    def get_ofreq(self):
        logging.debug("DdsTestDev.get_ofreq() = %r", self._ofreq)
        return self._ofreq

    def set_phy(self, phy):
        logging.debug("DdsTestDev.set_phy(" + str(phy) + ")")
        self._phy = phy
        return phy

    def get_phy(self):
        logging.debug("DdsTestDev.get_phy() = " + str(self._phy))
        return self._phy

    def set_amp(self, fsc):
        logging.debug("DdsTestDev.set_amp(" + str(fsc) + ")")
        self._amp = fsc
        return fsc

    def get_amp(self):
        logging.debug("DdsTestDev.get_amp() = " + str(self._amp))
        return self._amp

    def set_hstl_output_state(self, state=False):
        logging.debug("Set HSTL output state to: " + str(state))

    def get_hstl_output_state(self):
        pass

    def set_cmos_output_state(self, state=False):
        logging.debug("Set CMOS output state to: " + str(state))

    def get_cmos_output_state(self):
        pass

    def set_pll_state(self, state=False):
        logging.debug("Set PLL state to: %s", str(state))

    def get_pll_state(self):
        pass

    def set_cp_current(self, value=0):
        logging.debug("Set charge pump current to: " + str(value))

    def get_cp_current(self):
        pass

    def set_vco_range(self, value=None):
        logging.debug("Set VCO range to: " + str(value))

    def get_vco_range(self):
        pass

    def set_hstl_doubler_state(self, flag=False):
        logging.debug("Set HSTL doubler state to: " + str(flag))

    def get_hstl_doubler_state(self):
        pass

    def set_pll_doubler_state(self, flag=False):
        logging.debug("Set PLL doubler state to: " + str(flag))

    def get_pll_doubler_state(self):
        pass

    def set_pll_multiplier_factor(self, factor):
        logging.debug("Set PLL multiplier factor to: " + str(factor))

    def get_pll_multiplier_factor(self):
        pass

    def set_led(self, flag=False):
        logging.debug("Set LED blink: " + str(flag))

    def set_reg(self, address, value):
        logging.debug("Set " + str(value) + " @adress " + str(address))

    def get_reg(self, address):
        logging.debug("Request value @adress " + str(address))


# =============================================================================
class SAd9912Emul(Ad9912Emul):
    """Class derived from Ad9912Dev class to add signal/slot facilities.
    """

    ifreqUpdated = ss.Signal(['value'])
    ofreqUpdated = ss.Signal(['value'])
    phaseUpdated = ss.Signal(['value'])
    ampUpdated = ss.Signal(['value'])
    pllStateUpdated = ss.Signal(['flag'])
    pllDoublerUpdated = ss.Signal(['flag'])
    pllFactorUpdated = ss.Signal(['value'])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def connect(self, **kwargs):
        return super().connect(**kwargs)

    def set_ifreq(self, value, **kwargs):
        super().set_ifreq(value)
        self.ifreqUpdated.emit(value=value)

    def set_ofreq(self, value, **kwargs):
        aofreq = super().set_ofreq(value)
        self.ofreqUpdated.emit(value=aofreq)
        return aofreq

    def set_phy(self, value, **kwargs):
        aphy = super().set_phy(value)
        self.phaseUpdated.emit(value=aphy)
        return aphy

    def set_amp(self, value, **kwargs):
        aamp = super().set_amp(value)
        self.ampUpdated.emit(value=aamp)
        return aamp

    def set_pll_state(self, flag, **kwargs):
        super().set_pll_state(flag)
        self.pllStateUpdated.emit(flag=flag)

    def set_pll_doubler_state(self, flag, **kwargs):
        super().set_pll_doubler_state(flag)
        self.pllDoublerUpdated.emit(flag=flag)

    def set_pll_multiplier_factor(self, value, **kwargs):
        super().set_pll_multiplier_factor(value)
        self.pllFactorUpdated.emit(value=value)
