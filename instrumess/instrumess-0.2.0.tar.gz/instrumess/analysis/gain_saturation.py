# -*- coding: utf-8 -*-
"""
Created on Wednesday 06-March-2019 at 17:51

@author: Rastko Pajković
"""
from instrumess.utilities import utilities as ut
import matplotlib.pyplot as plt
from instrumess.utilities.plot_aux import fig_new, fig_label, colors  # , save_last_fig, interactive_legend,\
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from lmfit import Model
import instrumess.utilities.validate as validate
import matplotlib.pyplot as plt


plt.rcParams.update({'font.size': 14})  # set default font size for all plots


def parse_name(filepath):
    """Parse the filepath to extract lsoa, wl, idens, i"""
    filename = ut.Path(filepath).name
    foldername = ut.Path(filepath).parent.name
    wl = ut.find_num_in_string(filename, after='wl=')
    idens = ut.find_num_in_string(filename, after='idens=')
    try:
        lsoa = ut.find_num_in_string(foldername, before='um')
    except:
        lsoa = ut.find_num_in_string(filename, after='Lsoa=')
    i = ut.idens2i(idens, lsoa, w_um=2)
    return lsoa, wl, idens, i


def correct_losses(df_filepath,
                   voa_loss_file="D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-03 SP23 Saturation meas/Transmission/VOA.txt",
                   bpf_loss_file="D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-03 SP23 Saturation meas/Transmission/BPF.txt",
                   pc_loss_file="D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-05 SP23 Saturation meas/Transmission/PC.txt",
                   b2b_loss_file=None,
                   wg_loss_db_cm=2,
                   wg_before_um=935,
                   lf2facet_loss_dB=2.43,
                   n_mmi_after=0,
                   verbose=False):
    """Correct the absolute power measurement to account for losses"""
    df = ut.df_read(df_filepath)
    lsoa, wl, _, _ = parse_name(df_filepath)
    if b2b_loss_file is not None:
        b2b_df = ut.df_read(b2b_loss_file)
    if voa_loss_file is not None:
        voa_df = ut.df_read(voa_loss_file)
        if voa_df.loss.isnull().all():
            voa_loss = abs((b2b_df.p-voa_df.p)[b2b_df.wl==wl].values[0])
            # print(voa_loss, b2b_df.p,voa_df.p)
        else:
            voa_loss = abs(voa_df[voa_df.wl==wl].loss.values[0])  # voa can include pc
    else:
        voa_loss = 0
    bpf_df = ut.df_read(bpf_loss_file)
    if  bpf_df.loss.isnull().all():
        bpf_loss = abs((b2b_df.p-bpf_df.p)[b2b_df.wl==wl].values[0])
    else:
        bpf_loss = abs(bpf_df[bpf_df.wl==wl].loss.values[0])
    if pc_loss_file is not None:
        pc_df = ut.df_read(pc_loss_file)
        pc_loss = pc_df[pc_df.wl==wl].loss.values[0]  # this one can be negative?!
    else:
        pc_loss = 0
    wg_loss_before = wg_before_um*wg_loss_db_cm*1e-4  # before and after SOA
    # assumes that the chip width is 4600um
    wg_loss_after = (4600-wg_before_um-lsoa)*wg_loss_db_cm*1e-4
    # MMI insertion loss, after SOA
    mmi_loss = 4*n_mmi_after
    # total input loss
    lint = pc_loss+voa_loss+wg_loss_before+lf2facet_loss_dB
    # total output loss
    lout = bpf_loss+wg_loss_after+lf2facet_loss_dB+mmi_loss
    # convert losses to multiplicative factors
    mint = ut.dbm2mw(lint)
    mout = ut.dbm2mw(lout)
    df.pin = [p/mint for p in df.pin]
    df.pout = [p*mout for p in df.pout]
    if verbose:
        print('VOA (+PC) loss = ', voa_loss)
        print('Facet     loss = ', lf2facet_loss_dB)
        print('PC        loss = ', pc_loss)
        print('WG_before loss = ', wg_loss_before)
        print('BPF       loss = ', bpf_loss)
        print('WG_after  loss = ', wg_loss_after)
        print('MMI_after loss = ', mmi_loss)
    # calculate uncertainties
    return df


def error_multipl(error_array_percent, output='db'):
    """Calculates total multiplicative error, input percent"""
    validate.in_set(output, ['db', 'percent'], name='output')
    error_perc = np.sqrt(np.sum(np.array(error_array_percent)**2))
    error_db = ut.mw2dbm(error_perc+1)
    if output=='db':
        result = error_db
    elif output=='percent':
        result = error_perc
    return result



def remove_offset(df, start_ind=0, stop_ind=10, show=False):
    """Remove zero offset in the measurement"""
    x = df.pin[start_ind:stop_ind]
    y = df.pout[start_ind:stop_ind]
    coeff = np.polyfit(x, y, 1)
    df.pout -= coeff[1]
    if show:
        y2 = y-coeff[1]
        fig, ax = fig_new(name='Offset ')
        ax.plot(x, y, marker='.')
        ax.plot(x, y2, marker='.')
        ax.plot([0], np.polyval(coeff,0), marker='o', color='r')
        ax.set(
            xlabel='Input power [mW]',
            ylabel='Output power [mW]',
        )
        fig.tight_layout()
    return df
    

def remove_voa(df, show=False, voa_att_filepath='D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-18 SP23 Saturation meas/Transmission/voa attenuation.txt'):
    """Remove the absorption error in VOA"""
    # this function must be run before other error correction
    # otherwise attenuation estimation will be off
    
    # load attenuation file and interpolate
    df = df.copy()
    voa_att = ut.df_read(voa_att_filepath)
    x = voa_att.att
    y = voa_att['diff']-voa_att['diff'].mean()
    interpf = interp1d(x, y, kind='linear', fill_value=0, bounds_error=False)

    pin_db = [ut.mw2dbm(p) for p in df.pin]
    att = pin_db - max(pin_db)
    correction = interpf(abs(att))
    if show:
        print(correction)
    df.pin = [ut.dbm2mw(ut.mw2dbm(p)+interpf(abs(a)))
              for p, a in zip(df.pin, att)]
    return df


def load_gain(filepath,
              gain_root_folder='D:/Dropbox/PhD - ITL for SS-OCT/Laser documentation and modeling/Gain Dima/'):
    """Load the modal gain measurements for the correct wl, idens"""
    lsoa, wl, idens, i = parse_name(filepath)
    g_m_d = pd.read_csv(gain_root_folder+'net modal gain.txt', delimiter=' ', header=None)
    wl_d = pd.read_csv(gain_root_folder+'wavelength.txt', delimiter=' ')
    Id_d = pd.read_csv(gain_root_folder+'current density.txt')
    id_index = ut.df_find_closest_ind(Id_d.iloc[:,0], target=idens)
    wl_index = ut.df_find_closest_ind(wl_d.iloc[:,0], wl)
    gm = g_m_d.iloc[id_index,wl_index]   # modal gain 1/cm
    G = ut.mw2dbm(np.exp(gm*lsoa*1e-4))  # total gain in dB
    return gm, G


def calc_gain(df):
    """Calculate the total and unsaturated modal SOA gain"""
    G = ut.mw2dbm(df.pout/df.pin)
    return G


def plot_log(filepath, df, start_ind=0, end_ind=10, plot_sat=True):
    """Plot measurement results, options=log, lin"""
    lsoa, wl, idens, i = parse_name(filepath)
    gain = calc_gain(df)  # measured gain in dB
    gain_exp = load_gain(filepath,  # gain that Dima measured
                            gain_root_folder='D:/Dropbox/PhD - ITL for SS-OCT/Laser documentation and modeling/Gain Dima/')[1]
    # Define figure
    fig, ax = fig_new(name='SOA Psat, lsoa={:.0f}, idens={:.1f}, wl={}'.format(lsoa, idens, wl))
    ax.set(
        xlabel='Input power [dBm]',
        ylabel='Gain [dB]',
    )
    # Plot gain
    pin_db = [ut.mw2dbm(p) for p in df.pin]
    ax.plot(pin_db, gain, marker='.', zorder=10)
    if plot_sat:
        # Plot expected unsaturated gain
        plt.axhline(y=gain_exp, color='gray')
        # Plot measured unsaturated gain
        g0 = np.mean(gain[start_ind:end_ind])
        plt.axhline(y=g0)
        # label start and stop points
        ax.scatter([pin_db[start_ind], pin_db[end_ind]],
                   [gain[start_ind], gain[end_ind]], marker='|', s=12**2)
        # Plot 3dB drop line
        gsat = g0-3
        plt.axhline(y=gsat)
        # Plot 3dB point and label it
        ind = (np.abs(gain-gsat)).argsort()                        # sort
        x1, x2 = [ut.mw2dbm(p) for p in df.pin[[ind[0], ind[1]]]]  # closest
        y1, y2 = gain[[ind[0], ind[1]]]                            # points
        coeff = np.polyfit([y1,y2], [x1, x2], 1)                   # interp between
        pinsat = np.polyval(coeff, gsat)                           # 2 points
        ax.plot([pinsat], [gsat], marker='o', color='r')
        ax.text(pinsat-2, gsat-0.5, 'Psat = {:.4f} dBm'.format(pinsat), ha='right', va='top')
        # print gain difference
        gdif = gain_exp-g0  # difference in dB
        gdif_lin = ut.G2g(gain_exp, lsoa)-ut.G2g(g0, lsoa)  # difference in 1/cm
        text = fig_label(ax,
                         string='Gain diff = {:.2f} dB ({:.1f} '.format(gdif, gdif_lin) + r'$\mathrm{cm}^{-1}$)',
                         pos='tr', offset=0.04)
        text.set_color('gray')
        text.set_size(10)
    # label soa length, wavelength and current density
    fig_label(ax,
              string='Id = {:.1f} kA/cm2\nλ = {:.0f} nm\nLsoa = {} μm'.format(idens, wl, lsoa),
              pos='bl')

    fig.tight_layout()


def analyze(filepath, df, start_ind=0, end_ind=10, show=False):
    """Analyze measurement results, return g0, psat, gdif, gdif_lin"""
    lsoa, wl, idens, i = parse_name(filepath)
    gain = calc_gain(df)  # measured gain in dB
    gain_exp = load_gain(filepath,  # gain that Dima measured
                            gain_root_folder='D:/Dropbox/PhD - ITL for SS-OCT/Laser documentation and modeling/Gain Dima/')[1]
    pin_db = [ut.mw2dbm(p) for p in df.pin]
    # unsaturated gain
    g0 = np.mean(gain[start_ind:end_ind])
    # 3dB drop line
    gsat = g0-3
    # saturation power
    ind = (np.abs(gain-gsat)).argsort()                        # sort
    x1, x2 = [ut.mw2dbm(p) for p in df.pin[[ind[0], ind[1]]]]  # closest
    y1, y2 = gain[[ind[0], ind[1]]]                            # points
    coeff = np.polyfit([y1,y2], [x1, x2], 1)                   # interp between
    pinsat = np.polyval(coeff, gsat)                           # 2 points
    # gain difference
    gdif = gain_exp-g0  # difference in dB
    gdif_lin = ut.G2g(gain_exp, lsoa)-ut.G2g(g0, lsoa)  # difference in 1/cm
    if show:
        plot_log(filepath, df, start_ind=start_ind, end_ind=end_ind, plot_sat=True)
    return g0, pinsat, gdif, gdif_lin, gain_exp
    

def fit_bowers(filepath, df, show=False, fig_name=None, G0_init=5, Ps_init=10,
               p_max_fit=None):
    """Fit G = G0(1+(Pin-Pout)/Ps) to the measurements"""
    def sat_ucsb(Pin, Pout, G0, Ps):
        return G0*(1+ (Pin-Pout)/Ps)

    def sat_pin(G0, Ps, Pin):
        g = G0*(1+Pin/Ps)/(1+G0*Pin/Ps)
        return ut.mw2dbm(g)

    sat_model_ucsb    = Model(sat_ucsb, independent_vars=('Pin', 'Pout'))
    params_u = sat_model_ucsb.make_params(G0=G0_init, Ps=Ps_init)  # make initial guesses
    
    if p_max_fit is None:
        ind = len(df)
    else:
        ind = ut.find_closest_ind(df.pin, p_max_fit)
    Pin = df.pin[:ind]
    Pout = df.pout[:ind]
    Gain = calc_gain(df[:ind])
    Pin_db = ut.mw2dbm(Pin)
    gain = np.array([ut.dbm2mw(G) for G in Gain])
    res_u = sat_model_ucsb.fit(gain,
                               params=params_u,
                               weights=None,
                               method='leastsq',
                               Pin=Pin,
                               Pout=Pout)
    # load full vectors again
    Pin = df.pin
    Pout = df.pout
    Gain = calc_gain(df)
    Pin_db = ut.mw2dbm(Pin)
    # calculate G0 and Pin_sat in dB
    G0_db = ut.mw2dbm(res_u.best_values['G0'])
    Pin_sat_db = ut.mw2dbm(res_u.best_values['Ps']/(res_u.best_values['G0']-2))
    if show:
        if fig_name is None:
            fig_name='Bowers fit'
        fig, ax = fig_new(name=fig_name)
        ax.plot(Pin_db, Gain, marker='.')
        # y_u = sat_model_ucsb.eval(Pin=Pin, Pout=Pout, **res_u.best_values)
        # ax.plot(Pin_db, [ut.mw2dbm(el) for el in y_u], c='g')
        ax.plot(Pin_db, sat_pin(res_u.best_values['G0'],
                                res_u.best_values['Ps'],
                                Pin))
        ax.plot(Pin_sat_db, G0_db-3, '.r')
        ax.set(
            xlabel='Input power [dBm]',
            ylabel='Gain [dB]',
        )
        fig.tight_layout()
    return res_u.best_values


def gain_ucsb(Pin, G0, Ps):
        """G0 is a ratio (not in dB) and Ps and Pin are in mW"""
        return G0*(Ps+Pin)/(Ps+G0*Pin)


def fit_ucsb(filepath, df, show=False, fig_name=None, G0_init=5, Ps_init=10,
             p_max_fit=None, weights=None):
    """Fit the saturation measurement to G = G0*(Ps+Pin)/(Ps+G0*Pin)"""
    sat_model_ucsb    = Model(gain_ucsb, independent_vars=('Pin',))
    params_u = sat_model_ucsb.make_params(G0=G0_init, Ps=Ps_init)  # make initial guesses
    if p_max_fit is None:
        ind = len(df)
    else:
        ind = ut.find_closest_ind(df.pin, p_max_fit)
    Pin = df.pin[:ind]
    Gain = calc_gain(df[:ind])
    Pin_db = ut.mw2dbm(Pin)
    gain = np.array([ut.dbm2mw(G) for G in Gain])
    res_u = sat_model_ucsb.fit(gain,
                               params=params_u,
                               method='leastsq',
                               Pin=Pin,
                               weights=weights)
    # load full vectors again
    Pin = df.pin
    Gain = calc_gain(df)
    Pin_db = ut.mw2dbm(Pin)
    # calculate G0 and Pin_sat in dB
    G0_db = ut.mw2dbm(res_u.best_values['G0'])
    Pin_sat_db = ut.mw2dbm(res_u.best_values['Ps']/(res_u.best_values['G0']-2))
    if show:
        if fig_name is None:
            fig_name='Bowers fit'
        fig, ax = fig_new(name=fig_name)
        ax.plot(Pin_db, Gain, marker='.')
        y_u = sat_model_ucsb.eval(Pin=Pin, **res_u.best_values)
        ax.plot(Pin_db, [ut.mw2dbm(el) for el in y_u])
        ax.plot(Pin_sat_db, G0_db-3, '.r')
        ax.set(
            xlabel='Input power [dBm]',
            ylabel='Gain [dB]',
        )
        fig.tight_layout()
    res = res_u.best_values
    res['G0_db'] = G0_db
    res['Pin_sat_db'] = Pin_sat_db
    return res


def plot_lin(filepath):
    """Main function that does all the analysis and ploting"""
    df = ut.df_read(filepath)
    lsoa, wl, idens, i = parse_name(filepath)
    name = 'lsoa={}μm, wl={}nm, idens={}kA/cm2'.format(lsoa, wl, idens)
    # plot the measurement
    fig, ax = fig_new(name=name)
    ax.plot(df.pin, df.pout, marker='.')
    ax.set(
        xlabel='Input power [mW]',
        ylabel='Output power [mW]',
    )
    fig.tight_layout()

def load_g_ssg(wl, idens,
               filepath='D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-04-17 Gain multi wg/gain_matrix.txt',
               answer='1/cm',
               lsoa=None):
    """Load small signal gain measurement for a given wl and Idens"""
    validate.in_set(answer, ['1/cm', 'db'], name='answer')
    gain_matrix = ut.df_read(filepath)
    idens_str = f'{idens:g}'
    if idens_str not in gain_matrix.keys():
        raise(f'You have to select idens in set: {gain_matrix.keys()}')
    wl_index = ut.find_closest_ind(gain_matrix.wl, wl)
    g = gain_matrix[idens_str][wl_index]
    if answer=='1/cm':
        return g
    else:
        if lsoa is None:
            raise('If you want to get gain in dB you have to specify SOA length')
        return ut.g2G(g, lsoa)

def plot_curve(ax, df, color=colors[0], label=None,
               error=None, fit_res=None):
    pin_db = [ut.mw2dbm(p) for p in df.pin]  # x
    gain = calc_gain(df)  # y, measured gain in dB
    # plot the measurement points
    line, = ax.plot(pin_db, gain, '.', color=color)
    # add errorbars on a single measurement points
    if error is not None:
        ax.errorbar(pin_db[1], gain[1], yerr=error,
                    fmt='.', markerfacecolor='none', capsize=5,
                    color=color)
    if fit_res is not None:
        G0 = fit_res['G0']
        Ps = fit_res['Ps']
        g_fit = gain_ucsb(df.pin, G0, Ps)
        G_fit = [ut.mw2dbm(g) for g in g_fit]
        ax.plot(pin_db, G_fit, color=color, label=label)
        ax.plot([fit_res['Pin_sat_db']], [fit_res['G0_db']-3],
                marker='s', color=color, markersize=8,
                markerfacecolor='white')
    return line

def load_gain_unc(idens='2.5', sigma=1, error_str='F-test', source=ut.Path('D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-04-17 Gain multi wg')):
    wl = ut.df_read(source/'gain_matrix.txt')['wl']
    gain = ut.df_read(source/'gain_matrix.txt')[idens]
    if error_str=='F-test':
        conf_low = ut.df_read(source/'Uncertainties/g_{}s_low.txt'.format(sigma))[idens]
        conf_high = ut.df_read(source/'Uncertainties/g_{}s_high.txt'.format(sigma))[idens]
    elif error_str=='stderr':
        conf_low = gain-ut.df_read(source/'Uncertainties/stderr_g.txt')[idens]*sigma
        conf_high = gain+ut.df_read(source/'Uncertainties/stderr_g.txt')[idens]*sigma
    return wl, gain, conf_low, conf_high
    