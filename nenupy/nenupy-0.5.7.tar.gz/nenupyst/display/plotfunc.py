#! /usr/bin/python3
# -*- coding: utf-8 -*-


""" 
"""


__author__ = 'Alan Loh'
__copyright__ = 'Copyright 2020, nenupy'
__credits__ = ['Alan Loh']
__maintainer__ = 'Alan'
__email__ = 'alan.loh@obspm.fr'
__status__ = 'Production'
__all__ = [
    'plot',
    'plotdb',
    'beam_config'
    ]


import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time, TimeDelta

from nenupyst.read.util import (
    SpecData,
    NenuFAR_Obs
)
from nenupysim.astro import radio_sources


# ============================================================= #
# --------------------------- plot ---------------------------- #
# ============================================================= #
def plot(specdata, savefile=None, **kwargs):
    """
    """
    if not isinstance(specdata, SpecData):
        raise TypeError(
            'SpecData object expected.'
        )

    if 'vmin' not in kwargs.keys():
        kwargs['vmin'] = np.percentile(specdata.amp, 5)
    if 'vmax' not in kwargs.keys():
        kwargs['vmax'] = np.percentile(specdata.amp, 95)
    if 'cmap' not in kwargs.keys():
        kwargs['cmap'] = 'YlGnBu_r'

    pcm = plt.pcolormesh(
        (specdata.time - specdata.time[0]).sec,
        specdata.freq,
        specdata.amp.T,
        **kwargs
    )

    cbar = plt.colorbar(pcm)

    cbar.set_label('Stokes {} (amp)'.format(specdata.meta['stokes']))
    plt.ylabel('Frequency (MHz)')
    plt.xlabel('Time (sec since {})'.format(specdata.time[0].isot))

    if savefile is None:
        plt.show()
    else:
        plt.savefig(savefile)
    return
# ============================================================= #


# ============================================================= #
# -------------------------- plotdb --------------------------- #
# ============================================================= #
def plotdb(specdata, savefile=None, **kwargs):
    """
    """
    if 'vmin' not in kwargs.keys():
        kwargs['vmin'] = np.percentile(specdata.db, 5)
    if 'vmax' not in kwargs.keys():
        kwargs['vmax'] = np.percentile(specdata.db, 95)
    if 'cmap' not in kwargs.keys():
        kwargs['cmap'] = 'YlGnBu_r'

    pcm = plt.pcolormesh(
        (specdata.time - specdata.time[0]).sec,
        specdata.freq,
        specdata.db.T,
        **kwargs
    )

    cbar = plt.colorbar(pcm)

    cbar.set_label('Stokes {} (dB)'.format(specdata.meta['stokes']))
    plt.ylabel('Frequency (MHz)')
    plt.xlabel('Time (sec since {})'.format(specdata.time[0].isot))

    if savefile is None:
        plt.show()
    else:
        plt.savefig(savefile)
    return
# ============================================================= #


# ============================================================= #
# ------------------------ beam_config ------------------------ #
# ============================================================= #
def beam_config(obs):
    """
    """
    from healpy.visufunc import (
        orthview,
        projplot,
        projtext
    )
    from healpy import nside2npix
    from matplotlib.widgets import Slider
    from tqdm import tqdm

    from nenupysim.skymodel import Skymodel
    from nenupysim.astro import to_altaz, eq_coord


    if not isinstance(obs, NenuFAR_Obs):
        raise TypeError(
            'This must be a NenuFAR statistic observation.'
        )
    
    gsm = Skymodel(
        nside=128,
        freq=50
    )
    times = Time(obs._meta['pbe']['timestamp'])
    minutes = (times - times[0]).sec / 60.
    nsamples = 100
    dmin = (minutes.max() - minutes.min())/nsamples

    # Compute every skymodel for each time frame
    skymodels = np.zeros(
        (nsamples, nside2npix(gsm.nside))
    )
    sampled_min = np.zeros(nsamples)
    sampled_time = []
    casa = np.zeros((nsamples, 2))
    for i in tqdm(range(nsamples)):
        sampled_min[i] = i*dmin
        sampled_time.append(
            times[0] + TimeDelta(sampled_min[i]*60, format='sec')
        )
        skymodels[i, :] = gsm.zenith_center(
            time=sampled_time[-1]
        )

    plt.close('all')
    orthview(skymodels[0, :],#skymap,
        fig=1,
        title='',
        min=np.percentile(skymodels[0, :], 1),
        max=np.percentile(skymodels[0, :], 99),
        cmap='YlGnBu_r',
        cbar=False,
        half_sky=True
    )

    fig = plt.gcf()
    plt.subplots_adjust(left=0., bottom=-0.25)
    axtime = plt.axes(
        [0.2, 0.01, 0.65, 0.03],
        facecolor='white'
    )

    slider_time = Slider(
        ax=axtime,
        label='Minutes',
        valmin=minutes.min(),
        valmax=minutes.max(),
        valinit=minutes[0],
        valstep=dmin
    )

    def update(val):
        dmin_val = slider_time.val
        idx = np.argmin(np.abs(dmin_val - sampled_min))
        skymap = skymodels[idx, :]
        orthview(skymap,
            fig=1,
            title='',
            min=np.percentile(skymap, 1),
            max=np.percentile(skymap, 99),
            cmap='YlGnBu_r',
            cbar=False,
            half_sky=True
        )

        # Display main sources on the sky
        src = radio_sources(time=sampled_time[idx])
        for key in src.keys():
            if src[key].alt > 0:
                projplot(
                    -src[key].az,
                    src[key].alt,
                    lonlat=True,
                    coord='C',
                    marker='o',
                    markersize=15,
                    markeredgecolor='white',
                    markerfacecolor='none',
                    alpha=0.5,
                    rot=(0, 0, 180)
                )

                projtext(
                    -src[key].az,
                    src[key].alt,
                    ' ' + key,
                    lonlat=True,
                    coord='C',
                    color='white',
                    rot=(0, 0, 180)
                )

        # Display beams on the sky
        for beam in np.unique(obs._meta['pbe']['noBeam']):
            b_mask = obs._meta['pbe']['noBeam'] == beam
            b_times = Time(obs._meta['pbe']['timestamp'][b_mask])
            if sampled_time[idx] < b_times.min():
                pass
            else:
                t_diff = sampled_time[idx] - b_times
                b_idx = t_diff[t_diff>=0].size - 1
                projplot(
                    -obs._meta['pbe']['AZ'][b_mask][b_idx],
                    obs._meta['pbe']['EL'][b_mask][b_idx],
                    lonlat=True,
                    coord='C',
                    marker='o',
                    markersize=10,
                    markeredgecolor='tab:red',
                    markerfacecolor='none',
                    alpha=0.5,
                    rot=(0, 0, 180)
                )

                projtext(
                    -obs._meta['pbe']['AZ'][b_mask][b_idx],
                    obs._meta['pbe']['EL'][b_mask][b_idx],
                    ' ' + str(beam),
                    lonlat=True,
                    coord='C',
                    color='tab:red',
                    rot=(0, 0, 180)
                )


    slider_time.on_changed(update)

    plt.show()
    plt.close('all')
# ============================================================= #


