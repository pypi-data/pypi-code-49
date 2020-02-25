# -*- coding: utf-8 -*-
"""
Created on Sunday 03-March-2019 at 18:11

@author: Rastko Pajković
"""
import instrumess.utilities.load as load
from instrumess.utilities import utilities as ut
import matplotlib.pyplot as plt
from instrumess.utilities.plot_aux import fig_new  # , save_last_fig, fig_label, interactive_legend,\

plt.rcParams.update({'font.size': 14})  # set default font size for all plots

lsoa = 500
idens = '3'
folder = 'D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-03 SP23 Saturation meas/SOA {:04d}um'.format(lsoa)
files = load.folder(folder, filetype='df')

fig, ax = fig_new(name='Saturation power, l={}um, idens={}kA/cm2'.format(lsoa, idens))
ax.set(
    xlabel='xlab',
    ylabel='ylab',
)

for key, df in files.items():
    if '3kA' in key:
        ax.plot(df.pin, df.pout, marker='.', label=ut.parse_floats(key)[0])
plt.legend()
fig.tight_layout()

