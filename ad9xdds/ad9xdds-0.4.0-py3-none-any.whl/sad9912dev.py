# -*- coding: utf-8 -*-

"""package ad9xdds
author    Benoit Dubois
copyright FEMTO ENGINEERING, 2019
license   GPL v3.0+
brief     API to control AD9912 DDS development board with signals/slots
          facilities.
details   Class derived Ad9912Dev class to add signals/slots facilities
"""

import signalslot as ss
import ad9xdds.ad9912dev as ad9912dev


class SAd9912Dev(ad9912dev.Ad9912Dev):
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
