# -*- coding: utf-8 -*-
"""
Created on Thursday 04-April-2019 at 19:58

@author: Rastko Pajković
"""
from instrumess.utilities import utilities as ut
import matplotlib.pyplot as plt
from instrumess.utilities.plot_aux import fig_new, fig_3y_stacked, colors, fig_2y
import pandas as pd
import numpy as np
from findpeaks import detect_peaks

plt.rcParams.update({'font.size': 14})  # set default font size for all plots


def analyze_file(filepath, crit='2nd derivative', mph=0.0001,
                 ma_after_th=10, ma_skip=1, show=False, plot_type='li_th_slope'):
    """Analyze an LIV measurement file with column names 'i', 'p', 'v'
    
    Parameters
    ----------
    filepath : STR
        Full filepath to measurement file
    crit : str
        How threshold is established, options:
        '2nd derivative' - first peak above mph is threshold
    mph : float
        Minimum peak hight of second derivative to be considered threshold
    ma_after_th : float
        Current span after th to perform a linear fit on
    ma_skip : float
        Skip current span after th when fiting
    show : bool
        Plot the LIV curve, choose which type with plot_type
    plot_type : str
        Types of plots: 'li(v)', 'li_th', 'li_th_slope'
    
    Returns
    -------
    FLOAT
        ith, slope in mA and mW/A
    """
    i_ma = df.i
    p_mw = df.p
    v = df.v
    ith = find_ith(i_ma, p_mw, crit='2nd derivative', mph=mph, show=False)
    fit_coefs = find_efficiency(i_ma, p_mw, ma_after_th=ma_after_th,
                                ma_skip=ma_skip, show=False)
    slope = fit_coefs[0]
    if show:
        v_plot = v if 'liv' in plot_type else None
        ith_plot = ith if 'th' in plot_type else None
        fit_coef_plot = fit_coefs if 'slope' in plot_type else None
        plot_liv(i_ma, p_mw, v=v_plot, ith=ith_plot, efficiency=fit_coef_plot)
    return ith, slope  # mA, mW/A


def find_ith(i_ma, p_mw, crit='2nd derivative', mph=0.0001, show=False):
    """Find threshold based on a criterion"""
    i = pd.Series(data=i_ma)
    p = p_mw
    if crit=='2nd derivative':
        # find second derivative
        d2 = p.diff().diff(periods=-1)
        di2 = (i[0]-i[1])**2
        peak_ind = detect_peaks(-d2.values/di2, x_pos=df.i.values,
                                mph=mph,
                                mpd=1,
                                threshold=0,
                                edge='rising',
                                kpsh=False,
                                valley=False,
                                show=show,
                                ax=None,
                                sort=None)
        ith = peak_ind[0]
    if show:
        plot_liv(i_ma, p, ith=ith, efficiency=None)
    return ith


def find_efficiency(i_ma, p_mw, ma_after_th=10, ma_skip=1, show=False):
    """Find the slope efficiency
    
    Parameters
    ----------
    i_ma : float
        Current of the IV curve
    p_mw : float
        Power of the IV curve
    ma_after_th : float
        Length of the section in mA after threshold to perform the linfit on
    ma_skip : float
        Skip a section after threshold, don't consider for lin fit
    show : bool
        Plot what you are doing, for debugging purposes
    
    Returns
    -------
    ARRAY
        Coefficients slope and offset of a linear fit
    """
    ith = find_ith(i_ma, p_mw, crit='2nd derivative', show=False)
    start_ind = ut.find_closest_ind(i_ma, ith+ma_skip)
    end_ind = ut.find_closest_ind(i_ma, ith+ma_skip+ma_after_th)
    p = p_mw
    fit_coeffs = np.polyfit(i_ma[start_ind:end_ind], p[start_ind:end_ind], 1)
    if show:
        plot_liv(i_ma, p_mw, ith=ith, efficiency=fit_coeffs)
    return fit_coeffs  # fit_coeffs[0] is the efficiency


def plot_liv(i_ma, p_mw, v=None, ith=None, efficiency=None):
    """Plot the LI curve and threshold"""
    p = p_mw
    if v is None:
        fig, ax = fig_new(name='LI curve')
    else:
        fig, ax, ax2 = fig_2y(color_left=colors[0], color_right=colors[1],
                              name='LIV curve')
        ax2.plot(i_ma, v, color=colors[1])
        ax2.set_ylabel('Voltage [V]')
    ax.plot(i_ma, p)
    ax.set(
        xlabel='Current [mA]',
        ylabel='Power [mW]',
    )
    fig.tight_layout()
    ax.grid(linestyle=':')
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    xspan = abs(xlim[1]-xlim[0])
    yspan = abs(ylim[1]-ylim[0])
    if ith is not None:
        ind_th = ut.find_closest_ind(i_ma, ith)
        p_th = p[ind_th]
        ax.plot([ith], [p_th], marker='|', markersize=14, color='r', zorder=0)
        ax.annotate('$\mathrm{I_{th} = }$' + '{:.3g} mA'.format(ith),
                    xy=(ith, p_th), xytext=(ith-xspan*0.1, p_th+yspan*0.1),
                    ha='right',
                    arrowprops=dict(facecolor='black', shrink=0.1, width=2,
                                    headwidth=7),
                    )
        if efficiency is not None:
            slope = efficiency[0]
            offset = efficiency[1]
            x_fit = [ith, ((max(ylim)-yspan*0.05)-offset)/slope]
            y_fit = np.polyval(efficiency, x_fit)
            # print(x_fit, y_fit)
            ax.plot(x_fit, y_fit, ':', color=colors[0])
            # find the angle of the line as plotted
            p1 = ax.transData.transform_point((x_fit[0], y_fit[0]))
            p2 = ax.transData.transform_point((x_fit[1], y_fit[1]))
            dy = (p2[1] - p1[1])
            dx = (p2[0] - p1[0])
            rotn = np.degrees(np.arctan2(dy, dx))
            ax.text(x_fit[1], y_fit[1], '{:.2g} mW/A'.format(slope*1e3),
                    rotation=rotn,
                    rotation_mode='anchor',
                    ha='right',
                    va='bottom',
                    color=colors[0],
                    size=12)
    return fig, ax


def plot_derivs(i_ma, p_mw):p
    """Plot LI curve and first and second derivative"""
    p = pd.Series(p_mw)
    i = pd.Series(data=i_ma)
    d1 = p.diff()
    d2 = p.diff().diff(periods=-1)
    # get parameters to plot
    ith = find_ith(i_ma, p_mw, crit='2nd derivative', show=False)
    ith_ind = ut.find_closest_ind(i, ith)
    pth = p[ith_ind]
    eff = find_efficiency(i_ma, p_mw, ma_after_th=10, ma_skip=1, show=False)
    slope = eff[0]
    
    fig, ax, ax2, ax3 = fig_3y_stacked(name='LIV debug')
    ax.plot(df.i, df.p)
    ax.plot(ith, pth, marker='|', color='r')
    ax2.plot(df.i, d1)
    ax2.axhline(slope, color='r')
    ax3.plot(df.i, d2)
    ax3.plot(ith, d2[ith_ind], marker='+', color='r')
    ax3.set(
        xlabel='Current [mA]',
        ylabel='d2',
    )
    ax2.set_ylabel('d1')
    ax.set_ylabel('Power [mW]')

    plt.tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)
    fig.subplots_adjust(hspace=0)

if __name__ == '__main__':
    test_file = "D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-25 SP24 LIV and crosstalk/LIV, L2, boost=False.txt"
    df = ut.df_read(test_file, column_names=None)

    i_ma = df.i
    p_mw = df.p
    v = df.v
    print(analyze_file(test_file, crit='2nd derivative', mph=0.0001,
                       ma_after_th=10, ma_skip=1,
                       show=False, plot_type='li_th_slope'))
