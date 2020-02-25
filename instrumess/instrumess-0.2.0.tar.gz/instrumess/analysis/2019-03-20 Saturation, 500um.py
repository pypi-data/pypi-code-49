# -*- coding: utf-8 -*-
"""
Created on Wednesday 20-March-2019 at 11:22

@author: Rastko Pajković
"""
from instrumess.utilities import utilities as utimport instrumess.utilities.load as load
import gain_saturation as gs
from instrumess.utilities.plot_aux import save_last_fig, fig_new  # , , fig_label, interactive_legend,\
import matplotlib.pyplot as plt

folder = 'D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-11 SP23 Saturation meas/SOA 0500um'
files = load.folder(folder, filetype='df')

num = len(files)
# num = 1
res = ut.df_init(['idens', 'psat', 'g0', 'gdif_lin', 'g_exp'],
                 numel=len(files),
                 units=['kA/cm2', 'dBm', 'dB', '1/cm', 'dB'])
for num in range(0,num):
    filename = list(files.keys())[num]
    filepath = ut.Path(folder)/(filename+'.txt')
    df = files[filename]
    df = gs.correct_losses(filepath,
                           voa_loss_file="D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-11 SP23 Saturation meas/Transmission/VOA+pc.txt",
                           bpf_loss_file="D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-11 SP23 Saturation meas/Transmission/BPF.txt",
                           pc_loss_file=None,
                           wg_loss_db_cm=2,
                           wg_before_um=935,
                           lf2facet_loss_dB=2.43,
                           verbose=False)
    if num==0:
        df.drop([0,1,2,3,4,5,6], inplace=True)
        df.reset_index(drop=True, inplace=True)
    df = gs.remove_offset(df, start_ind=0, stop_ind=10, show=False)
    df = gs.remove_voa(df)
    # gs.plot_lin(filepath)
    # gs.plot_log(filepath, df, start_ind=0, end_ind=10, plot_sat=True)
    lsoa, wl, idens, i = gs.parse_name(filepath)
    g0, psat, gdif, gdif_lin, g_exp = gs.analyze(filepath, df,
                                                 start_ind=0,
                                                 end_ind=10,
                                                 show=True)
    res.loc[num] = idens, psat, g0, gdif_lin, g_exp

fig, ax = fig_new(name='Psat')
ax.scatter(res.idens[1:], res.psat[1:])
ax. scatter(res.idens[2:], res.gdif_lin[2:])
ax.set(
    xlabel='Current density [kA/cm2]',
    ylabel='Saturation power [dBm]',
)
fig.tight_layout()

fig, ax = fig_new(name='Gain')
ax.scatter(res.idens[1:], [ut.G2g(g, lsoa) for g in res.g0[1:]], label='SP23')
ax.scatter(res.idens[1:], [ut.G2g(g, lsoa) for g in res.g_exp[1:]], label='Dima')
ax.set(
    xlabel='Id [kA/cm2]',
    ylabel='Unsaturated gain [1/cm]',
    title='Lsoa=500μm, λ=1550nm'
)
fig.tight_layout()
plt.legend()
plt.grid(b=None, which='major', axis='both')

