# -*- coding: utf-8 -*-
"""
Created on Saturday 13-April-2019 at 01:43

@author: Rastko Pajković
"""


from instrumess.utilities import utilities as utimport instrumess.utilities.load as load
import gain_saturation as gs
from instrumess.utilities.plot_aux import save_last_fig, fig_new  # , , fig_label, interactive_legend,\
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

folder = 'D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-11 SP23 Saturation meas/SOA 0500um'
files = load.folder(folder, filetype='df')

num = len(files)
# num = 1
res = ut.df_init(['idens', 'psat', 'g0', 'gdif_lin', 'g_exp'],
                 numel=len(files),
                 units=['kA/cm2', 'dBm', 'dB', '1/cm', 'dB'])
num=12
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
# ------------------------------------------------------------------------------
fit_to_ind = 10
df = gs.remove_offset(df, start_ind=0, stop_ind=fit_to_ind, show=False)
df = gs.remove_voa(df)
# gs.plot_lin(filepath)
# gs.plot_log(filepath, df, start_ind=0, end_ind=10, plot_sat=True)
lsoa, wl, idens, i = gs.parse_name(filepath)
g0, psat, gdif, gdif_lin, g_exp = gs.analyze(filepath, df,
                                             start_ind=0,
                                             end_ind=fit_to_ind,
                                             show=True)
gain = gs.calc_gain(df)  # measured gain in dB

res.loc[num] = idens, psat, g0, gdif_lin, g_exp
xdata = df.pin
ydata = np.array([ut.dbm2mw(p) for p in gain])

# fit boundaries
start_ind = 1
stop_ind = ut.find_closest_ind(xdata, 4)  # index closest to -10 dBm

xdata = xdata[start_ind:stop_ind]
xedata = (df.pin-df.pout)[start_ind:stop_ind]
ydata = ydata[start_ind:stop_ind]

# ----- Aproximation fun -------------------------------------------------------
def G(Pin, G0, Ps):
    return G0*(1+Pin/Ps)/(1+G0*Pin/Ps)

def min_fun(coeffs):
    return ydata - G(xdata, *coeffs)

# # ----- Exact fun --------------------------------------------------------------
# def Ge(Pin_Pout, G0, Ps):
#     return G0*np.exp((Pin_Pout)/Ps)

# def min_fune(coeffs):
#     return ydata - Ge(xedata, *coeffs)

G0_start = ut.dbm2mw(g0)
Ps_start = 3.98

par_opt, par_cov = opt.leastsq(func=min_fun, x0=(G0_start, Ps_start))
# par_opte, par_cove = opt.leastsq(func=min_fune, x0=(G0_start, Ps_start))
ax = plt.gca()
ax.plot(ut.mw2dbm(df.pin),
        [ut.mw2dbm(g) for g in G(df.pin, *par_opt)], zorder=20)
# ax.plot(ut.mw2dbm(df.pin),
#         [ut.mw2dbm(g) for g in Ge(df.pin-df.pout, *par_opte)], zorder=20)

psat_fit = ut.mw2dbm(par_opt[1]/(par_opt[0]-2))
g0_fit = ut.mw2dbm(par_opt[0])
# psate_fit = ut.mw2dbm(2*np.log(2)*par_opte[1]/(par_opte[0]-2))
# g0e_fit = ut.mw2dbm(par_opte[0])


print(g0_fit, par_opt[1], psat_fit)
# print(g0e_fit, par_opte[1], psate_fit)
