# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:34:55 2019

@author: 20185069
"""

from instrument import Instrument
from instrumess.utilities import utilities as ut

# =====================================================================
# WARNING: read the manual to know the limits of the specific equipment
# =====================================================================


class SantecTls(Instrument):
    """ Driver for Santec TSL 550 """
    
    commands={
            'output':':POW:STAT {}; *OPC?',
            'p_dBm':':POW {};*OPC?',
            'wl_nm' :':WAV {}; *OPC?',
            'reset' : '*RST', }
    com=ut.Dotdict(commands)

    def __init__(self, address='GPIB::20::INSTR',name=None):
        """Generate instance of class NiDaq_ao"""
        super().__init__(address=address, name=name)

    # ----- Instrument properties ----------------------------------------------
    on = Instrument.prop(com.output, "Set output 'ON' or 'OFF'",
                         in_set=[0, 1], name='output')
    p_dBm = Instrument.prop(com.p_dBm, docs="Set output power in dBm",
                            in_range=(0,13),  # dBm
                            name='power')
    wl_nm = Instrument.prop(com.wl_nm, docs="Set output wavelength in nm",
                            in_range=(1260,1360),
                            name='wavelength')
    # --------------------------------------------------------------------------

    def __enter__(self):
        self.instr = self._rm.open_resource(self._address)
        return self

    def reset(self):
        """Reset instrument to a known state and setup communication"""
        self.write(self.com.reset)

    def setup(self, wl_nm=None, p_dBm=None):
        """Set TLS wavelength and/or power"""
        if wl_nm is not None:
            self.wl_nm = wl_nm  # tuple
        if p_dBm is not None:
            self.p_dBm = p_dBm   # tuple

    # def output(self, on_off=0):yibvh
    #     """Turn TLS on or off"""
    #     if 'on' == on_off.lower():
    #         self.on = self._slot,1
    #     else:
    #         self.on = self._slot,0

    def __exit__(self, exception_type, exception_value, traceback):
        # self.output('off')
        ut.wait_s(0.2)
        self.instr.control_ren(0)  # go to local
        self.instr.close()         # close visa connection
