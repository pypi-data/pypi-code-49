'''
Created on Feb 1, 2020

@author: ballance
'''

import cocotb
from cocotb.decorators import bfm_uint32_t

@cocotb.bfm(hdl={
    cocotb.bfm_sv : cocotb.bfm_hdl_path(__file__, "hdl/generic_sram_byte_en_target_bfm.sv"),
    cocotb.bfm_vlog : cocotb.bfm_hdl_path(__file__, "hdl/generic_sram_byte_en_target_bfm.sv")
    }, has_init=True)
class GenericSramByteEnTargetBFM():

    def __init__(self):
        self.data_width = 0
        self.addr_width = 0
        self.endian = 0
        
    @cocotb.bfm_export(bfm_uint32_t, bfm_uint32_t)
    def set_parameters(self, data_width, addr_width):
        """Called to set parameter values at initialization"""
        self.data_width = data_width
        self.addr_width = addr_width
        
    
        
    