# -*- coding: utf-8 -*-
"""
Created on Wednesday 17-April-2019 at 20:24

@author: Rastko Pajković
"""

from instrumess.utilities import utilities as ut
import numpy as np
import matplotlib.pyplot as plt
from instrumess.utilities.plot_aux import fig_new, colors  # , save_last_fig, fig_label, interactive_legend,\
import scipy.optimize as optimize
from lmfit import Model


plt.rcParams.update({'font.size': 14})  # set default font size for all plots

source = 'D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-04-17 Gain multi wg'

# length of the straight waveguide before the SOA as a function of Lsoa (key)
wg_len = {100:1710,
          200:885,
          250:1564,
          500:885,
          700:1120,
          1000:885}


def load_meas_info(filepath):
    """Load the measurement information and return as dotdict"""
    info = ut.df_read_hd(filepath, hd_item=None, item_type='num')
    # TODO: process info and nicely return
    return info


def get_filepath(idens=1.5, lsoa=200,
                 source='D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-04-17 Gain multi wg'):
    """Get the filepath of the file with corresponding lsoa and idens"""
    lsoa = int(lsoa)
    source = ut.Path(source)/'SOA {} um'.format(lsoa)
    filepath = list(source.glob('*idens={}.txt'.format(idens)))
    if len(filepath)==0:
        print('File not found')
        return
    elif len(filepath)>1:
        raise ValueError('{} files that match the criterion found'.format(len(filepath)))
    return filepath[0]


def load_ase(idens=1.5, lsoa=200,
             source='D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-04-17 Gain multi wg'):
    """Load one spectrum data"""
    filepath = get_filepath(idens=idens, lsoa=lsoa, source=source)
    return ut.df_read(filepath) if filepath is not None else None


def remove_losses(filepath, wg_loss_cm=2, mmi_loss=3.2):
    """Correct for all losses in the system"""
    spectrum = ut.df_read(filepath)
    lwg, coupling_loss = [ut.df_read_hd(filepath, hd_item=item, item_type='num')
                          for item in ['L wg to facet', 'Coupling loss']]
    total_loss = lwg/1e4*wg_loss_cm + coupling_loss + mmi_loss
    spectrum.p += total_loss
    return spectrum


def get_soa_lens(source='D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-04-17 Gain multi wg'):
    """Get all soa lengths measured"""
    source = ut.Path(source)
    lens = [ut.parse_floats(p.name) for p in source.glob('*um')]
    return lens


def load_ase_same_idens(idens=1.5,source='D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-04-17 Gain multi wg',
                        ls=None,
                        correct_losses=True, wg_loss_cm=2, mmi_loss=3.2):
    """Load all specta with same idens and return as dict idens:df"""
    if ls is None:
            ls = get_soa_lens(source=source)
    if correct_losses:
        res = dict()
        for l in ls:
            try:
                filepath = get_filepath(idens=idens, lsoa=l, source=source)
                spectrum = remove_losses(filepath, wg_loss_cm=wg_loss_cm,
                                         mmi_loss=mmi_loss)
            except:
                continue
            res.update({l:spectrum})
        return res
    else:
        return {l:load_ase(idens=idens, lsoa=int(l), source=source) for l in ls}


def get_p_for_wl(spectra_dict,wl=1550, ls=None):
    """Return two vectors with power and lsoa"""
    if ls is None:
        ls = list(spectra_dict.keys())
    spectra = [spectra_dict[key] for key in ls]
    for spectrum in spectra_dict.values():
        ind_wl = ut.find_closest_ind(spectrum.wl, wl)
        # print(ind_wl)
        break
    p = [p.p[ind_wl] for p in spectra]
    return p, ls


def uncertainty(p, lwg, unc_osa=0.3, unc_splitter=0.1, unc_facet=0.33, unc_wg_pc=1., osa_noise=8e-10):
    """Calculate the uncertainty of a measurement point in mW
    
    Parameters
    ----------
    p : float
        Power in dBm
    lwg : float
        waveguide length in um
    unc_osa : float
        OSA uncertainty in absolute power measurement in dB (0.3 dB)
    unc_splitter : float
        Uncertainty in splitting ratio in dB (0.1 dB)
    unc_facet : float
        Standard deviation in LF -> facet coupling in dB (0.33 dB)
    unc_wg_pc : int
        Uncertainty in waveguide absorption per centimeter in dB/cm (1 dB/cm)
    osa_noise : float
        Standard deviation of noise level of the OSA
    
    Returns
    -------
    float
        error in mW of the absolute power measurement error
    """
    p_mw = ut.dbm2mw(p)
    uncs = [ut.dbm2mw(p)-1 for p in [unc_osa, unc_splitter, unc_facet, lwg/1e4*unc_wg_pc]]
    mpl_error = np.sqrt(np.sum(np.array(uncs)**2))  # multiplicative error
    return np.sqrt((p_mw*mpl_error)**2 + osa_noise**2)


def fit_fun(L, psp, g):
    """Model function with L and psp as fit parameters"""
    L = np.array(L)
    return psp/g*(np.exp(g*L/1e4)-1)


def fit_wl(L, p):
    """Take powers for a single wl and idens and fit"""
    def min_fun(coeffs):
        return ut.dbm2mw(p) - fit_fun(L, *coeffs)

    psp_start = 20
    g_start = 20

    sol, _ = optimize.leastsq(min_fun, x0=(psp_start, g_start))
    return sol

gain_model = Model(fit_fun, independent_vars=('L'))
params = gain_model.make_params(g=40, psp=2e-4)  # make initial guesses


def fit_weighted(p, lsoa, show=False):
    """Weighted fit of g and psp for a single wl, different soa lengths"""
    unc = np.array([uncertainty(p, wg_len[int(lsoa)]) for p, lsoa in zip(p, lsoa)])
    result = gain_model.fit(data=ut.dbm2mw(p), params=params, method='leastsq', L=lsoa, weights=1/unc)
    if show:
        fig, ax = fig_new(name='Weighted fit')
        ax.errorbar(lsoa, ut.dbm2mw(p), yerr=unc, fmt='o', markerfacecolor='none', capsize=6)
        L_array = ut.array(start=0, stop=max(lsoa), numel=100)
        fit_y = gain_model.eval(params=None, L=L_array, **result.best_values)
        ax.plot(L_array, fit_y)
        ax.set(
            xlabel='SOA length [μm]',
            ylabel='Power [mW]',
        )
        fig.tight_layout()
    return result


# idens = 2
# spectra = load_ase_same_idens(idens=idens)
# spectra_uc = load_ase_same_idens(idens=idens, correct_losses=False)

# fig, ax = fig_new(name='Spectra')
# for key, spectrum in spectra.items():
#     s_uc = spectra_uc[key]
#     ax.plot(spectrum.wl, spectrum.p, label=key)
#     # ax.plot(s_uc.wl, s_uc.p, ':')
# ax.set(
#     xlabel='Wavelength [nm]',
#     ylabel='Power [dBm]',
# )
# fig.tight_layout()
# plt.legend()


# p, L = get_p_for_wl(spectra, wl=1550)
# fit = fit_wl(L, p)
# unc = [uncertainty(p, wg_len[int(lsoa)]) for p, lsoa in zip(p, L)]
# fig, ax = fig_new(name='Fit')
# ax.errorbar(L, ut.dbm2mw(p), yerr=unc, fmt='o', markerfacecolor='none', capsize=6)
# L_array = ut.array(start=0, stop=max(L), numel=100)
# ax.plot(L_array, fit_fun(L_array, *fit), color=colors[0])
# ax.set(
#     xlabel='SOA length [μm]',
#     ylabel='Power [mW]',
# )
# fig.tight_layout()

# # ==============================================================================
# #  lmfit example
# # ==============================================================================
# result = gain_model.fit(data=ut.dbm2mw(p), params=params, method='leastsq', L=L, weights=1/np.array(unc))
# fit_y = gain_model.eval(params=None, L=L_array, **result.best_values)

# ax.plot(L_array, fit_y, color=colors[1])
# # =============================================================================


# # calculate gain fit for all wl and plot
# fig, ax = fig_new(name='gain')
# ax.set(
#     xlabel='Wavelewngth [nm]',
#     ylabel='Gain [1/cm]',
#     ylim=[-20, 60],
# )
# idens = [1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10]
# # idens = [1.5, 2, 2.5, 3, 3.5, 4, 5, 6]
# # idens = [5]
# wls = load_ase(idens=1.5, lsoa=200).wl
# ls = [100, 200, 250, 500, 700]
# for idens in idens:
#     spectra = load_ase_same_idens(idens=idens, ls=ls)
#     gain = np.zeros((len(wls),1))
#     for i, wl in enumerate(wls):
#         p, L = get_p_for_wl(spectra, wl=wl, ls=ls)
#         fit = fit_wl(L, p)
#         gain[i] = fit[1]
#     ax.plot(wls, gain, label=idens)

# plt.legend()
# fig.tight_layout()

# # calculate gain fit for all wl and plot
# fig, ax = fig_new(name='gain, weighted fit')
# ax.set(
#     xlabel='Wavelewngth [nm]',
#     ylabel='Gain [1/cm]',
#     ylim=[-20, 60],
# )
# idens = [1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10]
# # idens = [1.5, 2, 2.5, 3, 3.5, 4, 5, 6]
# # idens = [5]
# wls = load_ase(idens=1.5, lsoa=200).wl
# ls = [100, 200, 250, 500, 700]
# for idens in idens:
#     spectra = load_ase_same_idens(idens=idens, ls=ls)
#     results = [result]*len(wls)
#     gain = np.zeros((len(wls),1))
#     for i, wl in enumerate(wls):
#         p, L = get_p_for_wl(spectra, wl=wl, ls=ls)
#         results[i] = fit_weighted(p, L, show=False)
#         gain[i] = results[i].values['g']
#     ax.plot(wls, gain, label=idens)

# plt.legend()
# fig.tight_layout()
