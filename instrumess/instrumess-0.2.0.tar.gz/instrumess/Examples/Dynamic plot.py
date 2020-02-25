# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 23:06:24 2020

@author: Rastko
"""

import pylab as plt
import numpy as np
import instrumess.utilities.utilities as ut
from instrumess.utilities.plot_aux import fig_new
from instrumess.utilities.dynamic_plot import dp_prep, dp_update


df = ut.df_read("D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2020-02-06 SP23 saturation meas/var Lsoa, wl=1550, id=7/Results/Lsoa=0500um, wl=1550nm, idens=7kA_cm2.txt")

Pin = df.pin
Pout = df.pout
x = [ut.mw2dbm(el) for el in Pin]
y = [ut.mw2dbm(pout/pin) for pin, pout in zip(Pin, Pout)]

fig, ax = fig_new(name='Dynamic figure')
line, = ax.plot([], [], lw=0, marker='.')    # DYNAMIC
ax.set(
    xlabel='Input power [dBm]',
    ylabel='Gain [dB]',
)
dp_prep(x, ax)                               # DYNAMIC
# update figure
for i, yel in enumerate(y):
    dp_update(line, x[:i], y[:i], fig, ax)   # DYNAMIC
    ut.wait_s(0.1)
fig.tight_layout()
