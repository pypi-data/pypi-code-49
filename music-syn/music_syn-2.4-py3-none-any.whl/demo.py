# -*- coding: utf-8 -*-
from .demosongs import *
from .mixfiles import mix_files
from .pysynth import make_wav


def demo():
    print()
    print("Creating Demo Songs... (this might take about a minute)")
    print()

    # SONG 1
    make_wav(song1, fn="pysynth_scale.wav")

    # SONG 2
    make_wav(song2, bpm=95, boost=1.2, fn="pysynth_anthem.wav")

    # SONG 3
    make_wav(song3, bpm=132 // 2, pause=0., boost=1.1, fn="pysynth_chopin.wav")

    # SONG 4
    # right hand part
    make_wav(song4_rh, bpm=130, transpose=1, pause=.1, boost=1.15, repeat=1, fn="pysynth_bach_rh.wav")
    # left hand part
    make_wav(song4_lh, bpm=130, transpose=1, pause=.1, boost=1.15, repeat=1, fn="pysynth_bach_lh.wav")
    # mix both files together
    mix_files("pysynth_bach_rh.wav", "pysynth_bach_lh.wav", "pysynth_bach.wav")
