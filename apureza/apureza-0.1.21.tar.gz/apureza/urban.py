# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""

__author__ = 'Benjamin Pillot'
__copyright__ = 'Copyright 2019, Benjamin Pillot'
__email__ = 'benjaminpillot@riseup.net'

from fototex.foto import Foto
from utils.sys.timer import Timer

test = Foto("/home/benjamin/Desktop/APUREZA/FOTO/SUBSET_PLEIADES_20160915_Pan.tif", method="moving")
for w_size in [7, 11, 15, 19, 21, 25, 29, 35]:
    with Timer() as t:
        test.run(w_size, progress_bar=True, sklearn_pca=True)
    print("spent time (%d): %s" % (w_size, t))
    test.save_rgb(f"/home/benjamin/Desktop/APUREZA/FOTO/rgb_moving_{w_size}.tif")
