import matplotlib.pyplot as plt
import numpy as np


def plot_sequence(seq, dim, lattice=True, quads=True, aperture=True):
    fig, ax = plt.subplots(2, 1)
    if lattice:
        plot_lattice(ax[0], seq)
    if quads:
        plot_quadrupole(ax[0], seq)
    if aperture:
        plot_aperture(ax[1], seq, dim)
    return fig, ax


def plot_lattice(ax, seq):
    """
    Plot the labels of the sequence's elements along the beamline axis.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes object representing the beamline.
    seq : list
        List of beamline elements as returned by `madplot.madx.parser.Parser.parse`.
    """
    thick = [*filter(lambda x: x.attributes.get('l', 0) > 0, seq)]
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_position('zero')
    ax.xaxis.tick_top()
    ax.xaxis.set_ticks([x['at'] for x in thick])
    ax.xaxis.set_ticklabels([x.label for x in thick])
    ax.xaxis.set_tick_params(rotation=90)
    ax.set_xlim([0, seq[-1]['at'] + seq[-1].attributes.get('l', 0)/2])
    ax.yaxis.set_label(r'$\rm k1 \; [mrad\,mm^{-1}]$')
    ax.yaxis.set_label_position('right')
    ax.yaxis.tick_right()


def plot_quadrupole(ax, seq):
    """
    Plot quadrupole strengths along the beamline axis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes object representing the beamline.
    seq : list
        List of beamline elements as returned by `madplot.madx.parser.Parser.parse`.
    """
    quadrupoles = [*filter(lambda x: x.keyword == 'quadrupole', seq)]
    q_pos, q_k1, q_l = zip(*[(q['at'], q['k1'], q['l']) for q in quadrupoles])
    return ax.bar(
        q_pos, np.abs(q_k1), q_l, np.minimum(q_k1, 0),
        align='center', color=['royalblue' if k < 0 else 'indianred' for k in q_k1]
    )


def plot_aperture(ax, seq, dim):
    """
    Plot the aperture along the beamline axis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes object representing the beamline.
    seq : list
        List of beamline elements as returned by `madplot.madx.parser.Parser.parse`.
    dim : str, one of ('x', 'y')
        Indicates the dimension for which the aperture is plotted.
    """
    ax.set_xlabel('s [m]')
    ax.set_ylabel('[mm]')
    seq_a = [*filter(lambda x: 'aperture' in x.attributes, seq)]
    aperture = np.array(
        [2 * [x['aperture']] if x['apertype'] == 'circle' else x['aperture'] for x in seq_a])
    aperture = np.repeat(aperture, 2, axis=0)  # Aperture at start and end of elements.
    aperture = aperture[:, 0 if dim == 'x' else 1]
    pos = np.array([
        [x['at'] - x.attributes.get('l', 0)/2, x['at'] + x.attributes.get('l', 0)/2]
        for x in seq_a
    ]).ravel()
    ax.set_xlim([0, seq[-1]['at'] + seq[-1].attributes.get('l', 0) / 2])
    return ax.fill_between(pos, -aperture * 1e3, aperture * 1e3,
                           color='forestgreen', alpha=0.15, label='Aperture')


def plot_twiss(ax, twiss, name, label, style='-'):
    """
    Plot beta function along the beamline axis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes object representing the beamline.
    seq : pd.DataFrame
        Twiss table as returned by `madplot.utils.Convert.tfs`.
    dim : str, one of ('x', 'y')
        Indicates the dimension for which the Twiss parameters are plotted.
    """
    twiss = twiss.set_index('NAME')
    ax.set_xlim([twiss.loc['SIS18_HADES$START'].S, twiss.loc['SIS18_HADES$END'].S])
    return ax.plot(twiss.S, twiss[name.upper()], style,
                   color='royalblue' if 'x' in name.lower() else 'indianred', label=label)
