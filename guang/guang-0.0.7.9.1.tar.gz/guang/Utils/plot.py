import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn
import numpy as np

mpl.rcParams['ytick.direction'] = 'in'
mpl.rc('mathtext',fontset = 'cm',rm = 'serif')
mpl.rc(["xtick"], direction="in", top=1)
mpl.rc(["ytick"], direction="in", right=1)
# mpl.rc('font', family='Times New Roman', size=12)
mpl.rc('lines', linewidth=1)
seaborn.set_style('white')


def fillplot(*args, scalex=True, scaley=True, data=None, **kwargs):
    fillplot.__doc__ = 'fill_y_min:阴影下界, fill_y_max: 阴影上界\n' + plt.plot.__doc__
    if type(args[0]) != type(args[1]):
        y = args[0]
        x = np.arange(len(y))
    else:
        y = args[1]
        x = args[0]
    fill_y_min = kwargs.get('fill_y_min', 0)
    fill_y_max = kwargs.get('fill_y_max', y) 

    plt.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
    plt.fill_between(x, y1=fill_y_min, y2=fill_y_max, color='b', alpha=.2)
   
