# -*- coding: utf-8 -*-
"""
Created on Wednesday 20-March-2019 at 11:22

@author: Rastko Pajković
"""
from instrumess.utilities import utilities as utimport instrumess.utilities.load as load
import gain_saturation as gs
from instrumess.utilities.plot_aux import save_last_fig, fig_new  # , , fig_label, interactive_legend,\
import matplotlib.pyplot as plt

file1 = 'D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-11 SP23 Saturation meas/Transmission/bpf.txt'
file2 = 'D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-14 SP23 Saturation meas/Transmission/bpf.txt'
file3 = 'D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-03 SP23 Saturation meas/Transmission/bpf.txt'
file4 = 'D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-09 SP23 Saturation meas/Transmission/bpf.txt'
# files = load.folder(folder, filetype='df')
df1, df2, df3, df4 = [ut.df_read(f) for f in [file1,file2, file3,file4]]

fig, ax = fig_new(name='BPF loss variation')
ax.plot(df1.wl, df1.loss.abs(), label='2019-03-11', marker='.')
ax.plot(df2.wl, df2.loss.abs(), label='2019-03-14', marker='.')
ax.plot(df3.wl, df3.loss.abs(), label='2019-03-03', marker='.')
ax.plot(df4.wl, df4.loss.abs(), label='2019-03-09', marker='.')
ax.set(
    xlabel='Wavelength [nm]',
    ylabel='Loss [dB]',
)
fig.tight_layout()
plt.legend()
