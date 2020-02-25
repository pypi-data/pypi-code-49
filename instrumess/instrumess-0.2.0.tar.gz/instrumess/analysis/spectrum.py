# -*- coding: utf-8 -*-
"""
Created on Wednesday 15-May-2019 at 15:42

@author: Rastko Pajković
"""

from findpeaks import detect_peaks


def get_smsr(wl, p, mpd_nm=0.01):
    """Calculate the Side Mode Supression Ratio of the spectrum"""
    inds = detect_peaks(p, x_pos=wl, mpd=mpd_nm)
    return p[inds[0]]-p[inds[1]]

def find_peaks(wl, p, n_peaks=2, mpd_nm=0.01):
    """Find n highest peaks in a spectrum"""
    inds = detect_peaks(p, x_pos=wl, mpd=mpd_nm)
    if len(inds) < n_peaks:
        n_peaks = len(inds)
        raise Warning(f"This spectrum contains {len(inds)} peaks")
    inds = detect_peaks(p, x_pos=wl, mpd=mpd_nm)
    peak_wls = wl[inds[:n_peaks]]
    peak_p = p[inds[:n_peaks]]
    return peak_wls, peak_p
