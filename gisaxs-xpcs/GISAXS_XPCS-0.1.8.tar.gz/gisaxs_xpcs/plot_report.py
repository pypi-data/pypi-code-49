#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import abstractmethod
from typing import Tuple

import numpy as np
from scipy.ndimage.filters import gaussian_filter1d
from scipy.optimize import curve_fit

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import rc

from .extract_data import ExtractData
from .common_tools import get_pen_folder_number


font_size = 20

rc('text', usetex=True)
rc('font', size=font_size)
rc('xtick', labelsize=font_size)
rc('ytick', labelsize=font_size)
rc('axes', labelsize=font_size)

extract_data = ExtractData()
extent = extract_data.get_extent


class Fit(object):
    init_ = ()
    args = None

    def __init__(self, fit_function):
        self.fit_function = fit_function
        self.fit_res = None
        self.fitted_y = None
        self.arg_errors = ['error_%s' % er
                           for er in self.args] if self.args is not None else None

    def fit(self, x, y, p0=None):
        p0 = p0 or self.init_
        try:
            self.fit_res = curve_fit(self.fit_function, x, y, p0)
            self.fitted_y = self.fit_function(x, *self.fit_res[0])
        except RuntimeError as er:
            print(er)

    def get_fit_result(self, mode: str = 'lists'):
        if self.fit_res is None:
            return
        if self.args is None:
            return self.fit_res
        else:
            if mode not in ['lists', 'dict']:
                raise ValueError('Mode should be one of "lists", "dict". ')
            if mode == 'dict':
                return dict(zip([*self.args, *self.arg_errors],
                                [*self.fit_res[0], *np.sqrt(np.diag(self.fit_res[1]))]))
            else:
                return self.fit_res[0], np.sqrt(np.diag(self.fit_res[1]))


class AbstractLorentzian(Fit):
    number_of_peaks = 0

    def __init__(self):
        super(AbstractLorentzian, self).__init__(self.func)

    @property
    @abstractmethod
    def init_(self):
        pass

    @init_.setter
    def init_(self, value):
        self.init_ = value

    @abstractmethod
    def func(self, *args, **kwargs):
        pass

    @staticmethod
    def single_lorentzian(x, a, w, x0):
        return a / ((x - x0) ** 2 + w)

    def init_args(self):
        return self.init_

    def fit_and_plot(self, x, y):
        self.fit(x, y)
        self.plot(x, y)

    def plot(self, x, y=None, args=None):
        if args is not None:
            pass
        elif self.fit_res is not None:
            args = self.fit_res[0]
        else:
            args = self.init_args()
        if y is not None:
            plt.semilogy(x, y, label='smoothed cut', lw=5, alpha=0.7)
        plt.semilogy(x, self.func(x, *args), label='fit')

        for i in range(self.number_of_peaks):
            plt.semilogy(x, self.single_lorentzian(x, *args[i * 3:(i + 1) * 3]), '--',
                         label=r'lorentzian %d, $x_0 = %.3f^{\circ}$' % (i + 1, args[i * 3 + 2]))
        plt.legend()


class Lorentzian2(AbstractLorentzian):
    number_of_peaks = 2

    init_ = (0.001, 0.0001, 0,
             0.0005, 0.000005, 0)

    args = ['a1', 'w1', 'x1', 'a2', 'w2', 'x2']

    def func(self, x, a1, w1, x1, a2, w2, x2):
        return self.single_lorentzian(x, a1, w1, x1) + \
               self.single_lorentzian(x, a2, w2, x2)


class Lorentzian3(AbstractLorentzian):
    number_of_peaks = 3

    init_ = (0.001, 0.0001, -0.04,
             0.001, 0.0001, 0.04,
             0.0005, 0.000005, 0)

    args = ['a1', 'w1', 'x1', 'a2', 'w2', 'x2', 'a3', 'w3', 'x3']

    def func(self, x, a1, w1, x1, a2, w2, x2, a3, w3, x3):
        return self.single_lorentzian(x, a1, w1, x1) + \
               self.single_lorentzian(x, a2, w2, x2) + \
               self.single_lorentzian(x, a3, w3, x3)


class Lorentzian4(AbstractLorentzian):
    number_of_peaks = 4

    init_ = (0.001, 0.0001, -0.04,
             0.001, 0.0001, 0.04,
             0.001, 0.0001, -0.01,
             0.001, 0.0001, 0.01)

    args = ['a1', 'w1', 'x1', 'a2', 'w2', 'x2', 'a3', 'w3', 'x3', 'a4', 'w4', 'x4']

    def func(self, x,
             a1, w1, x1,
             a2, w2, x2,
             a3, w3, x3,
             a4, w4, x4):
        return self.single_lorentzian(x, a1, w1, x1) + \
               self.single_lorentzian(x, a2, w2, x2) + \
               self.single_lorentzian(x, a3, w3, x3) + \
               self.single_lorentzian(x, a4, w4, x4)


class Lorentzian5(AbstractLorentzian):
    number_of_peaks = 5

    args = ['a1', 'w1', 'x1',
            'a2', 'w2', 'x2',
            'a3', 'w3', 'x3',
            'a4', 'w4', 'x4',
            'a5', 'w5', 'x5']

    init_ = (0.001, 0.0001, -0.04,
             0.001, 0.0001, 0.04,
             0.0005, 0.000005, 0,
             0.001, 0.0001, -0.01,
             0.001, 0.0001, 0.01)

    def func(self, x,
             a1, w1, x1,
             a2, w2, x2,
             a3, w3, x3,
             a4, w4, x4,
             a5, w5, x5):
        return self.single_lorentzian(x, a1, w1, x1) + \
               self.single_lorentzian(x, a2, w2, x2) + \
               self.single_lorentzian(x, a3, w3, x3) + \
               self.single_lorentzian(x, a4, w4, x4) + \
               self.single_lorentzian(x, a5, w5, x5)


class Lorentzian7(AbstractLorentzian):
    number_of_peaks = 7

    init_ = (0.001, 0.0001, -0.04,
             0.001, 0.0001, 0.04,
             0.0005, 0.000005, 0,
             0.001, 0.0001, -0.01,
             0.001, 0.0001, 0.01,
             0.001, 0.0001, -0.015,
             0.001, 0.0001, 0.015)

    def func(self, x,
             a1, w1, x1,
             a2, w2, x2,
             a3, w3, x3,
             a4, w4, x4,
             a5, w5, x5,
             a6, w6, x6,
             a7, w7, x7):
        return self.single_lorentzian(x, a1, w1, x1) + \
               self.single_lorentzian(x, a2, w2, x2) + \
               self.single_lorentzian(x, a3, w3, x3) + \
               self.single_lorentzian(x, a4, w4, x4) + \
               self.single_lorentzian(x, a5, w5, x5) + \
               self.single_lorentzian(x, a6, w6, x6) + \
               self.single_lorentzian(x, a7, w7, x7)


class AbstractVerticalFit(AbstractLorentzian):
    def plot(self, x, y=None, args=None):
        if args is not None:
            pass
        elif self.fit_res is not None:
            args = self.fit_res[0]
        else:
            args = self.init_args()
        if y is not None:
            plt.semilogy(x, y, label='smoothed cut', lw=5, alpha=0.7)
        plt.semilogy(x, self.func(x, *args), label='fit')

        for i in range(self.number_of_peaks):
            plt.semilogy(x, self.single_lorentzian(x, *args[i * 3:(i + 1) * 3]), '--',
                         label=r'lorentzian %d, $x_0 = %.3f^{\circ}$' % (i + 1, args[i * 3 + 2]))
        plt.semilogy(x, args[-1] * np.exp(args[-2] + x * args[-3]), '--',
                     label='exponent')
        plt.legend()


class VerticalFit2(AbstractVerticalFit):
    number_of_peaks = 2

    init_ = (0.005, 0.0001, 0.185,
             0.001, 0.0001, 0.225,
             -55, 0, 5e5)

    def func(self, x,
             a1, w1, x1,
             a2, w2, x2,
             e_tau, e_tau_0, e_amplitude):
        return e_amplitude * np.exp(e_tau_0 + x * e_tau) + \
               self.single_lorentzian(x, a1, w1, x1) + \
               self.single_lorentzian(x, a2, w2, x2)


class VerticalFit3(AbstractVerticalFit):
    number_of_peaks = 3

    init_ = (0.007, 0.0001, 0.160,
             0.005, 0.0001, 0.185,
             0.001, 0.0001, 0.225,
             -55, 0, 5e5)

    def func(self, x,
             a1, w1, x1,
             a2, w2, x2,
             a3, w3, x3,
             e_tau, e_tau_0, e_amplitude):
        return e_amplitude * np.exp(e_tau_0 + x * e_tau) + \
               self.single_lorentzian(x, a1, w1, x1) + \
               self.single_lorentzian(x, a2, w2, x2) + \
               self.single_lorentzian(x, a3, w3, x3)


class VerticalFit4(AbstractVerticalFit):
    number_of_peaks = 4

    init_ = (0.007, 0.0001, 0.160,
             0.005, 0.0001, 0.185,
             0.001, 0.0001, 0.225,
             0.0005, 0.0001, 0.280,
             -55, 0, 5e5)

    args = ['a1', 'w1', 'x1',
            'a2', 'w2', 'x2',
            'a3', 'w3', 'x3',
            'a4', 'w4', 'x4',
            'e_tau', 'e_tau_0', 'e_amplitude']

    def func(self, x,
             a1, w1, x1,
             a2, w2, x2,
             a3, w3, x3,
             a4, w4, x4,
             e_tau, e_tau_0, e_amplitude):
        return e_amplitude * np.exp(e_tau_0 + x * e_tau) + \
               self.single_lorentzian(x, a1, w1, x1) + \
               self.single_lorentzian(x, a2, w2, x2) + \
               self.single_lorentzian(x, a3, w3, x3) + \
               self.single_lorentzian(x, a4, w4, x4)


class Cut(object):
    def __init__(self, cut_region: Tuple[float, float, float, float], axis: int, *,
                 sigma: float = 1, fit: Fit = None):
        """

        :param cut_region: tuple(y_min, y_max, x_min, x_max) in deg.
        :param axis: 0 or 1 - axis number to calculate mean
        :param sigma: gaussian filter sigma (applied if sigma > 0)
        :param fit: fit object (if None, don't fit)
        """
        self.cut_region = cut_region
        self.sigma = sigma
        self.axis = axis
        self.fit = fit
        self.x = None
        self.y = None

    def set_df(self, df):
        cut = self.cut_region
        df = np.exp(df.iloc[(df.index > cut[0]) * (df.index < cut[1]),
                            (df.columns > cut[2]) * (df.columns < cut[3])])
        axes = (df.columns, df.index)
        y = df.mean(axis=self.axis)
        if self.sigma > 0:
            y = gaussian_filter1d(y, sigma=self.sigma)

        self.x, self.y = axes[self.axis], y

    def plot_cut(self, df):
        self.set_df(df)
        y = self.y

        if isinstance(self.fit, AbstractLorentzian):
            self.fit.fit_and_plot(self.x, y)
        else:
            plt.semilogy(self.x, y)
            if self.fit is not None:
                try:
                    self.plot_fit()
                except Exception as err:
                    print(err)
                    return
        ax = plt.gca()
        if self.axis == 0:
            ax.set_xlabel(r'$2 \theta$, deg')
            plt.title('Horizontal cut (smoothed)')
        else:
            ax.set_xlabel(r'$\alpha$, deg')
            plt.title('Vertical cut (smoothed)')
        ax.set_ylabel(r'$log(I)$')
        ax.grid(linestyle='--', linewidth=0.5)
        ax.set_ylim([np.min(y) * 0.95, np.max(y) * 1.05])

    def plot_fit(self):
        if self.fit is None or self.x is None:
            return
        self.fit.fit(self.x, self.y)
        if self.fit.fitted_y is None:
            return
        plt.semilogy(self.x, self.fit.fitted_y)


class PlotReport(object):
    def __init__(self, fn: int, n: int, cut_x: Cut, cut_y: Cut, *,
                 background: float = 0.1, **kwargs):
        self.fn = fn
        self.n = n
        self.cut_x = cut_x
        self.cut_y = cut_y
        self.background = background
        self.rectangle_props = dict(fill=False, color='red', alpha=1, lw=1, ls='--')
        self.rectangle_props.update(kwargs.pop('rect', dict()))
        self.df = extract_data.get_images(self.fn, self.n, apply_log=True,
                                          plot=False, background=self.background, **kwargs)

    def plot_im(self, ax=None):
        df = self.df
        if ax is None:
            plt.figure(figsize=(7, 7))
            ax = plt.gca()
        extent_ = extent(df)
        im = ax.imshow(df, extent=extent_, cmap='jet')
        ax.set_title(self.get_title())
        cbar = plt.colorbar(im, fraction=0.046, pad=0.04)
        cbar.set_label(r'$log(I)$')
        ax.set_xlabel(r'$2 \theta$, deg')
        ax.set_ylabel(r'$\alpha$, deg')

        self.add_rect(self.cut_x, ax)
        self.add_rect(self.cut_y, ax)

    def plot(self, figsize: Tuple[int, int] = (5, 15)):
        self.plot_im()
        df = self.df
        plt.figure(figsize=figsize)
        plt.subplot(211)
        self.cut_x.plot_cut(df)
        plt.subplot(212)
        self.cut_y.plot_cut(df)
        plt.tight_layout()

    def get_title(self):
        fn, n = self.fn, self.n
        title = 'Pentacene sample %d' % get_pen_folder_number(fn)
        try:
            title = r'%s%s \textit{(folder %d, image %d)}' % (
                title,
                extract_data.metadata.get_latex_title(fn, n),
                fn, n)
        except Exception as err:
            print(err)
        return title

    def add_rect(self, cut_obj: Cut, ax):
        if cut_obj is not None:
            cut = cut_obj.cut_region
            r = patches.Rectangle((cut[2], cut[0]), cut[3] - cut[2], cut[1] - cut[0], **self.rectangle_props)
            ax.add_patch(r)


if __name__ == '__main__':
    from pprint import pprint

    lfit2 = Lorentzian2()
    lfit3 = Lorentzian3()
    lfit4 = Lorentzian4()
    lfit5 = Lorentzian5()
    lfit7 = Lorentzian7()
    vfit2 = VerticalFit2()
    vfit3 = VerticalFit3()
    vfit4 = VerticalFit4()

    # fit for 99 - 1500 (low central peak)

    lfit5.init_ = (0.0005, 0.0001, -0.04,
                   0.0005, 0.0001, 0.04,
                   0.005, 0.001, 0,
                   0.0007, 0.00002, -0.005,
                   0.0007, 0.00002, 0.005)

    # fit for 97 - 1 (low central peak)

    # lfit5.init_ = (0.0005, 0.0001, -0.04,
    #                0.0005, 0.0001, 0.04,
    #                0.001, 0.001, 0,
    #                0.0003, 0.00002, -0.005,
    #                0.0003, 0.00002, 0.005)

    # for two central peaks 96 - 1:

    # lfit4.init_ = [2.22402770e-03, 3.22734594e-04, - 3.58788410e-02,
    #                3.27324732e-03, 4.52631052e-04, 3.70929532e-02,
    #                2.66907060e-04, 5.16160062e-06, 1.44646801e-03,
    #                1.85142830e-03, 3.41261952e-04, 0]

    # cut_x = Cut((0.18, 0.20, -0.07, 0.07), 0, sigma=2, fit=lfit3)

    #####
    # cut for 89

    # vfit2.init_ = (0.007, 0.0001, 0.160,
    #                0.001, 0.0001, 0.234,
    #                -55, 0, 5e5)
    # cut_x = Cut((0.22, 0.24, -0.07, 0.07), 0, sigma=2, fit=lfit3)
    # cut_y = Cut((0.15, 0.3, -0.05, -0.03), 1, sigma=1, fit=vfit2)
    #####


    def get_nm(delta, name=''):
        print(name, ':\n', 8.77 / delta, ' nm')


    cut_x = Cut((0.22, 0.24, -0.07, 0.07), 0, sigma=1, fit=lfit5)
    cut_y = Cut((0.15, 0.3, -0.01, 0.01), 1, sigma=2, fit=vfit4)
    # cut_y = Cut((0.15, 0.3, -0.01, 0.01), 1, sigma=2
    plot = PlotReport(99, 1, cut_x=cut_x, cut_y=cut_y)
    plot.plot(figsize=(10, 10))
    plt.show()
    dh = lfit5.get_fit_result()
    dv = vfit4.get_fit_result()

    get_nm((dh['x5'] - dh['x4']) / 2, 'big x')
    get_nm((dh['x2'] - dh['x1']) / 2, 'usual x')
    get_nm(dv['x2'] - dv['x1'], 'y1')
    get_nm(dv['x3'] - dv['x2'], 'y2')
    get_nm(dv['x4'] - dv['x3'], 'y3')

    # for i in [500, 550, 600, 650, 700, 750]:
    #
    #     plot = PlotReport(87, i, cut_x=cut_x, cut_y=cut_y)
    #     plt.figure(figsize=(10, 10))
    #     plot.plot_im()
    #     plt.savefig('images_for_report/87_%d.png' % i)
    #     plt.figure(figsize=(10, 5))
    #     cut_x.plot_cut(plot.df)
    #     # plot.plot(figsize=(10, 10))
    #     plt.savefig('images_for_report/87_%d_hcut.png' % i)

    # print(list(lfit5.get_fit_result()))
