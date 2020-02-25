# -*- coding: utf-8 -*-
"""
Created on Wednesday 20-March-2019 at 11:22

@author: Rastko Pajković
"""
from instrumess.utilities import utilities as utimport instrumess.utilities.load as load
import gain_saturation as gs

folder = 'D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-11 SP23 Saturation meas/SOA 0500um'
files = load.folder(folder, filetype='df')

num = 8
for num in range(len(files)):
    filename = list(files.keys())[num]
    print(filename)
    filepath = ut.Path(folder)/(filename+'.txt')
    df = files[filename]
    df = gs.correct_losses(filepath,
                           voa_loss_file="D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-14 SP23 Saturation meas/Transmission/VOA+pc.txt",
                           bpf_loss_file="D:/Dropbox/PhD - ITL for SS-OCT/Measurements/2019-03-14 SP23 Saturation meas/Transmission/BPF.txt",
                           pc_loss_file=None,
                           wg_loss_db_cm=2,
                           wg_before_um=935,
                           lf2facet_loss_dB=2.43,
                           verbose=False)
    # df = gs.remove_offset(df, start_ind=0, stop_ind=10, show=False)
    # gs.plot_lin(filepath)
    gs.plot_log(filepath, df, start_ind=0, end_ind=10, plot_sat=True)

