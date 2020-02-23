# # Initializes matplotlib to work with Qt5
#   =======================================
if not 'matplotlib.backends' in sys.modules:
    def init_agg():
        import matplotlib
        matplotlib.use('Qt5Agg')
    init_agg()
    del init_agg

from .matplotlibaux import *

