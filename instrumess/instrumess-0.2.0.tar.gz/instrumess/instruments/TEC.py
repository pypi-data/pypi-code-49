# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 12:05:20 2018
 
@author: 20171304
"""
 
# driver for pro800
import visa
import re
import time
from datetime import datetime
# import matplotlib.pyplot as plt
import numpy as np

from instrumess.utilities.plot_aux import fig_new
from instrumess.instruments.LDC import Ldc
from instrumess.instruments.instrument import Instrument
from instrumess.utilities import utilities as ut
 
address = "GPIB0::18::INSTR"


class Tec(Instrument):
    """PRO8000 TEC driver"""

    com = ut.Dotdict({
            'set_p'       : ':SHAREP:SET {:.1f}',
            'set_i'       : ':SHAREI:SET {:.1f}',
            'set_d'       : ':SHARED:SET {:.1f}',
            'get_p'       : ':SHAREP:SET?',
            'get_i'       : ':SHAREI:SET?',
            'get_d'       : ':SHARED:SET?',
            'set_i_on'    : ':INTEG {:s}',
            'get_i_on'    : ':INTEG?',
            'set_ch'      : ':SLOT {}',
            'get_ch'      : ':SLOT?',
            'set_temp'    : ':TEMP:SET {}',
            'get_set_temp': ':TEMP:SET?',
            'meas_temp'   : ':TEMP:ACT?',
            'output'      : ':TEC {}',
    })

    # ----- Instrument properties ----------------------------------------------
    p = Instrument.prop(com.set_p, docs="Set proportional term of PID in percent",
                        in_range=(0,100),
                        name='P')
    i = Instrument.prop(com.set_i, docs="Set integral term of PID in percent",
                        in_range=(0,100),
                        name='I')
    d = Instrument.prop(com.set_d, docs="Set differential term of PID in percent",
                        in_range=(0,100),
                        name='D')
    i_on = Instrument.prop(com.set_i_on, docs="Enable or disable differential term of PID",
                           in_set=['ON','OFF'],
                           name='I_on')
    ch = Instrument.prop(com.set_ch, docs="Select channel(slot) number",
                         in_set=[1,2,3,4,5,6,7,8],
                         name='Channel')
    temp = Instrument.prop(com.set_temp, docs="Set temperature in deg C",
                           in_range=(15, 90),  # reasonable numbers, otherwise arb
                           name='Temperature')
    on = Instrument.prop(com.output, docs="Turn TEC on or off",
                         in_set=['ON','OFF'],
                         name='output')
    # --------------------------------------------------------------------------

    def __init__(self, address="GPIB0::18::INSTR"):
        """Initialize the instrument"""
        self.address = address
        self._rm = visa.ResourceManager()

    def __enter__(self):
        self.instr = self._rm.open_resource(self.address)
        self.instr.timeout = 5000
        return self
         
    def set_pid(self, p=None, i=None, d=None, i_on=None):
        """Set PID shares in % and switch I on or off"""
        if p is not None:
            self.p = p
        if i is not None:
            self.i = i
        if d is not None:
            self.d = d
        if i_on is not None:
            self.i_on = i_on
        self.get_pid()

    def get_pid(self, show=False):
        """Get the PID settings"""
        com_keys = ['get_p',
                    'get_i',
                    'get_d',
                    'get_i_on',]
        p, i, d, ion = [self.instr.query(self.com[key]) for key in com_keys]  # raw
        p, i ,d = [self._parse_first_float(elem) for elem in [p,i,d]]
        if 'OFF' in ion:
            i = 0
        if show:
            print('P: {:5.1f}%'.format(p))
            print('I: {:5.1f}%'.format(i))
            print('D: {:5.1f}%'.format(d))
        return p, i, d

    def test_stabilization(self, duration=10, p=None, i=None, d=None,
                           i_on=None, plot_res=True):
        """Set the PID values, swing Tset from 18 to 20deg, monitor temp"""
        self.set_pid(p=p, i=i, d=d, i_on=i_on)
        t_set = self.get_temp()
        if 17.9 < t_set < 18.1:
            lvl=20
            self.set_temp(20)
        elif 19.9 < t_set < 20.1:
            lvl=18
            self.set_temp(18)
        else:
            raise ValueError('Set temperature should be 18 or 20deg, not {:.1f}'
                             .format(t_set))
        t0 = time.time()
        temp = []
        t = []
        np
        while time.time()-t0 < duration:
            temp.append(self.meas_temp())
            t.append(time.time()-t0)
        if plot_res:
            fig, ax = fig_new(name='TEC response')
            ax.axhline(lvl, c='r')
            ax.plot(t, temp)
            ax.set(
                xlabel='Time [s]',
                ylabel='Temperature [°C]',
            )
        return t, temp

    def test_distribution(self, duration=30, avg=1, nbin=60, wait_s=None, show=True):
        """Record temperature over duration seconds and plot histogram"""
        t0 = time.time()
        temp = []
        t = []
        while time.time()-t0 < duration:
            temp.append(self.meas_mean_temp(n_iter=avg))
            t.append(time.time()-t0)
            if wait_s:
                time.sleep(wait_s)
        if show:
            fig, ax = fig_new(name='Temp histogram')
            ax.hist(temp, bins=nbin)
            ax.set(
                xlabel='Temp [°C]',
                ylabel='N occurences/bin',
            )
        return t, temp

    def get_temp_sampling_f(self, duration=10, wait_s=0, show_distr=True):
        """Sample temperature and get sampling frequency"""
        t, _ = self.test_distribution(duration=duration, wait_s=wait_s, show=False)
        dt = np.diff(t)
        if show_distr:
            fig, ax = fig_new(name='Time between temp samples')
            ax.hist(dt)
            ax.set(
                xlabel='Time [s]',
                ylabel='Count in bin',
            )
            fig.tight_layout()
        return 1/np.mean(dt)

    def set_channel(self, ch=1):
        """Todo"""
        self.ch = ch
     
    def get_channel(self):
        """Return active channel"""
        return self._parse_first_float(self.instr.query(self.com.get_ch))
     
    def set_temp(self, temp):
        """Set target temperature"""
        self.temp = temp
     
    def get_set_temp(self):
        """Get the set temperature value"""
        answer_raw = self.instr.query(self.com.get_set_temp)
        return self._parse_first_float(answer_raw)
    
    def meas_temp(self):
        """Measure temperature"""
        answer_raw = self.instr.query(self.com.meas_temp)
        return self._parse_first_float(answer_raw)
    
    def meas_mean_temp(self, n_iter=9):
        """Measure mean temperature over n iterations"""
        return np.mean([self.meas_temp() for _ in range(n_iter)])
    
    def output(self, state='OFF'):
        """Turn the temperature control on or off"""
        self.on = state
                 
    def _parse_first_float(self, string):
        """Parse first float in a string"""
        re_float = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?"
        float_string = re.findall(re_float, string)[0]
        return float(float_string)
 

def start(i=120):
    """Startup the TEC and LDC slowly"""
    with Tec(address="GPIB0::18::INSTR") as tec, \
         Ldc(address="GPIB0::18::INSTR") as ldc:
        tec.set_temp(18)
        tec.output(state='ON')
        time.sleep(5)
        ldc.set_current_mA(0)
        ldc.output(state='ON')
        ldc.slow_start_mA(i=i, step=5, wait=0.1)


def stop():
    """Turn the TEC output off"""
    with Tec(address="GPIB0::18::INSTR") as tec,\
         Ldc(address="GPIB0::18::INSTR") as ldc:
        ldc.slow_stop(step=5, wait=0.1)
        time.sleep(1)
        tec.output(state='OFF')
