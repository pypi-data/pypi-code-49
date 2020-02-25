# -*- coding: utf-8 -*-
"""
Created on Thursday 28-March-2019 at 21:11

@author: Rastko Pajković
"""

from instrumess.utilities import utilities as ut
import matplotlib.pyplot as pltimport instrumess.utilities.load as load
from instrumess.utilities.plot_aux import fig_new  # , save_last_fig, fig_label, interactive_legend,\
from scipy.interpolate import interp1d
import gain_saturation as gs

plt.rcParams.update({'font.size': 14})  # set default font size for all plots

voa_att_path = "D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-18 SP23 Saturation meas/Transmission/voa attenuation.txt"
a = ut.df_read(voa_att_path, column_names=None, index_col=0, skip_rows=0)
fig, ax = fig_new(name='VOA attenuation')
ax.plot(a.att, a['diff']-a['diff'].mean(), marker='.')
ax.set(
    xlabel='Attenuation [dB]',
    ylabel='Deviaion [dB]',
)

# interpolate
x = a.att
y = a['diff']-a['diff'].mean()
fitf = interp1d(x, y, kind='linear', )
xfine = ut.array(start=min(x), stop=max(x), numel=1000)
ax.plot(xfine, [fitf(x) for x in xfine])

fig.tight_layout()

# remove voa abs deviation
folder = 'D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-11 SP23 Saturation meas/SOA 0500um'
files = load.folder(folder, filetype='df')

key = list(files.keys())[2]
print(key)
df = files[key]

pin_db = [ut.mw2dbm(p) for p in df.pin]
att = pin_db-max(pin_db)
pin_db_c = pin_db
for i, (p, at) in enumerate(zip(pin_db, att)):
    try:
        pin_db_c[i] = p-fitf(abs(at))
    except:
        pass

fig, ax = fig_new(name='Gain')
x = [ut.mw2dbm(p) for p in df.pin]
y1 = [ut.mw2dbm(po/pi) for pi, po in zip(df.pin, df.pout)]
y2 = [y for y in y1]
change = [y for y in y1]
for i, (pi, po) in enumerate(zip(df.pin, df.pout)):
    try:
        change[i] = fitf(abs(att[i]))
        y2[i] = ut.mw2dbm(po/pi)-fitf(abs(att[i]))
    except:
        change[i] = 0
        pass
ax.plot(x, y1)
ax.plot(x, y2)
fig.tight_layout()

df2 = gs.remove_voa(df, voa_att_filepath='D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-18 SP23 Saturation meas/Transmission/voa attenuation.txt', show=True)
gs.plot_log(folder+'/'+key, df, start_ind=0, end_ind=10, plot_sat=True)
