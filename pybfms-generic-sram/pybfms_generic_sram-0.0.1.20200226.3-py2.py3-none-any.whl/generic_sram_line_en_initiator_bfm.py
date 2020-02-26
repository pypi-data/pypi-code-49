'''
Created on Oct 8, 2019

@author: ballance
'''
from cocotb.drivers import Driver
from cocotb.triggers import RisingEdge, ReadOnly

import bfm_core
import os


@bfm_core.bfm({
    "sv_dpi" : os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "hdl", "generic_sram_line_en_initiator_bfm.sv")
    })
class GenericSramLineEnInitiatorBFM(Driver):
    
    def __init__(self, bfm):
        self.bfm = bfm 
        
    def write(self, addr, data):
        yield RisingEdge(self.bfm.clock)
        self.addr    = addr
        self.wr_data = data
        self.wr_enable = 1
        self.rd_enable = 0
        
        yield RisingEdge(self.bfm.clock)
        yield ReadOnly()
        
    
    def read(self, addr):
        yield RisingEdge(self.bfm.clock)
        self.addr    = addr
        self.wr_enable = 0
        self.rd_enable = 1
        
        yield RisingEdge(self.bfm.clock)
        yield ReadOnly()
        
        return self.rd_data
        