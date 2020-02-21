"""Some prebuilt visualization"""

import logging
import matplotlib.pyplot as plt
import pandas as pd


def peak_plot(peak, sample_table=None, max_dist=None, norm_on_center=True, log_y=True,
              marker_list=None, color_list=None, guidelines=None, guideline_colors=None,
              legend_off=False, legend_col=2, ax=None, figsize=None, save_fig_to=None):
    """Plot the distribution of spike_in peak
    Plot a scatter-line plot of [adjusted] number of sequences with i edit distance from center sequence (spike-in seq)

    Args:
        peak (Peak): a Peak instance
        sample_table (pd.DataFrame): abundance of sequence in samples. With samples as columns. If None, try `peak.seqs`
        max_dist (int): maximum distance to survey. If None, try `peak.radius`
        norm_on_center (bool): if the counts/abundance are normalized to the peak center
        log_y (bool): if set the y scale as log
        marker_list (list of str): overwrite default marker scheme if not `None`, same length and order as
          samples in sample_table
        color_list (list of str): overwrite default color scheme if not `None`, same length and order as
          samples in sample_table
        guidelines (list of float): add a series of guidelines of the peak shape with certain mutation rates, optional
        guideline_colors (list of color): the color of guidelines, same shape as guidelines
        legend_off (bool): do not show the legend if True
        legend_col (int): number of col for legend if show
        ax (matplotlib.Axis): if use external ax object to plot. Create a new figure if None
        figsize (2-tuple): size of the figure
        save_fig_to (str): save the figure to file if not None

    Returns:
        ax for plotted figure
    """

    import numpy as np

    if sample_table is None:
        if isinstance(peak.seqs, pd.DataFrame):
            sample_table = peak.seqs
        else:
            logging.error('Please indicate sample_table')
            raise ValueError('Please indicate sample_table')

    if max_dist is None:
        if peak.radius is None:
            logging.error('Please indicate the maximum distance to survey')
            raise ValueError('Please indicate the maximum distance to survey')
        else:
            max_dist = peak.radius

    if marker_list is None:
        marker_list = Presets.markers(num=sample_table.shape[1], with_line=True)
    elif len(marker_list) != sample_table.shape[1]:
        logging.error('Error: length of marker_list does not align with the number of valid samples to plot')
        raise Exception('Error: length of marker_list does not align with the number of valid samples to plot')
    if color_list is None:
        color_list = Presets.color_tab10(num=sample_table.shape[1])
    elif len(color_list) != sample_table.shape[1]:
        logging.error('Error: length of color_list does not align with the number of valid samples to plot')
        raise Exception('Error: length of color_list does not align with the number of valid samples to plot')

    if ax is None:
        if figsize is None:
            figsize = (max_dist / 2, 6) if legend_off else (max_dist / 2 + 5, 6)
        fig, ax = plt.subplots(1, 1, figsize=figsize)

    rel_abun, _ = peak.peak_abun(max_radius=max_dist, table=sample_table, use_relative=norm_on_center)

    for sample, color, marker in zip(sample_table.columns, color_list, marker_list):
        ax.plot(rel_abun.index, rel_abun[sample], marker, color=color, label=sample,
                ls='-', alpha=0.5, markeredgewidth=2)
    if log_y:
        ax.set_yscale('log')
    ylim = ax.get_ylim()

    # add guide line if applicable
    if guidelines is not None:
        if not norm_on_center:
            logging.warning('Can only add guidelines if peaks are normed on center, skip guidelines')
        else:
            # assuming a fix error rate per nt, iid on binom
            from scipy.stats import binom
            if isinstance(guidelines, (float, int)):
                err_guild_lines = [guidelines]
            if guideline_colors is None:
                guideline_colors = Presets.color_tab10(num=len(guidelines))

            dist_series = np.arange(max_dist + 1)
            for ix, (p, color) in enumerate(zip(guidelines, guideline_colors)):
                rv = binom(len(peak.center_seq), p)
                pmfs = np.array([rv.pmf(x) for x in dist_series])
                pmfs_normed = pmfs / pmfs[0]
                ax.plot(dist_series, pmfs_normed,
                        color=color, ls='--', alpha=(ix + 1) / len(guidelines), label=f'p = {p}')
    ax.set_ylim(ylim)
    y_label = ''
    if norm_on_center:
        y_label += ' normed'
    y_label += ' counts'
    ax.set_ylabel(y_label.title(), fontsize=14)
    ax.set_xlabel('Distance to peak center', fontsize=14)
    if not legend_off:
        ax.legend(loc=[1.02, 0], fontsize=9, frameon=False, ncol=legend_col)
    plt.tight_layout()

    if save_fig_to:
        fig = plt.gcf()
        fig.patch.set_facecolor('none')
        fig.patch.set_alpha(0)
        plt.savefig(save_fig_to, bbox_inches='tight', dpi=300)
    return ax


class Presets:
    """Collection of preset colors/markers"""

    @staticmethod
    def _cycle_list(num, prop_list):
        """Generate a list of properties, cycle if num > len(prop_list)"""
        return [prop_list[i % len(prop_list)] for i in range(num)]

    @staticmethod
    def from_list(prop_list):
        from functools import partial
        return partial(Presets._cycle_list, prop_list=prop_list)

    @staticmethod
    def color_cat10(num=5):
        colors = [
            '#1F77B4',
            '#FF7F0E',
            '#2CA02C',
            '#D62728',
            '#9467BD',
            '#8C564B',
            '#E377C2',
            '#7F7F7F',
            '#BCBD22',
            '#17BECF'
        ]
        return Presets._cycle_list(num, colors)

    @staticmethod
    def color_tab10(num=5):
        colors = [
            '#4C78A8',
            '#F58518',
            '#E45756',
            '#72B7B2',
            '#54A24B',
            '#EECA3B',
            '#B279A2',
            '#FF9DA6',
            '#9D755D',
            '#BAB0AC'
        ]
        return Presets._cycle_list(num, colors)

    @staticmethod
    def color_pastel1(num=5):
        colors = [
            "#FBB5AE",
            "#B3CDE3",
            "#CCEBC5",
            "#DECBE4",
            "#FED9A6",
            "#FFFFCC",
            "#E5D8BD",
            "#FDDAEC",
            "#F2F2F2"
        ]
        return Presets._cycle_list(num, colors)

    @staticmethod
    def markers(num=5, with_line=False):
        from math import ceil

        full_marker_list = ['o', '^', 's', '+', 'x', 'D', 'v', '1', 'p', 'H']
        marker_list = []
        for i in range(ceil(num/10)):
            marker_list += full_marker_list
        if with_line:
            return ['-' + marker for marker in marker_list[:num]]
        else:
            return marker_list[:num]
