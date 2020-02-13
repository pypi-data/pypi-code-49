#!/usr/bin/python3 -B

import sys                       # built-in module
import time                      # built-in module
import inspect                   # built-in module
import warnings                  # built-in module
import numpy as np               # pip install numpy
import matplotlib                # pip install matplotlib + apt install python3-tk
import matplotlib.pyplot as pp   # pip install matplotlib + apt install python3-tk
import matplotlib.gridspec       # pip install matplotlib + apt install python3-tk
import mpl_toolkits.mplot3d      # noqa pylint: disable=unused-import


######################################################################################
#
#  P U B L I C   A P I
#
######################################################################################


def plot(*plot_args, **kwargs):
    """
    Create a Figure, plot the given data to it, and return the Figure. The given
    keyword arguments are first passed to the Figure constructor and then to the
    plot() function of fig.axes[0], where fig is the newly created Figure.

    Example:
       x = np.linspace(0, 2 * np.pi, 100)
       fig = pyplottr.plot(x, np.sin(x), title="sine", color="red")
       fig.show()
    """
    fig = _plot(*plot_args, **kwargs)
    return fig


def plot3d(*plot_args, **kwargs):
    """
    Create a Figure with 3D projection, plot the given data to it, and return the
    Figure. Keyword arguments are treated as in plot().
    """
    fig = _plot(*plot_args, **kwargs, projection="3d")
    return fig


class Figure:

    def __init__(self, title="Figure", nrows=1, ncols=1, nplots=None, layout=None, **subplot_kwargs):
        """
        Create a Figure with one or more subplots and basic enablers for keyboard
        and mouse interaction.

        Example:
          fig = pp.Figure("Sample 3D plot", projection="3d")
          zdata = np.linspace(0, 15, 1000)
          xdata = np.sin(zline)
          ydata = np.cos(zline)
          fig.ax.plot3D(xdata, ydata, zdata)
          fig.show()
        """
        _mpl_init()
        self.exit_request = False
        self.fig = None
        self.axes = None
        self.ax = None
        self.current_subplot = None
        self.mousex = None
        self.mousey = None
        self.clickx = None
        self.clicky = None
        self.key = None
        self.valid_keys = "0123456789abcdefghijklmnopqrstuvwxyz"
        self.key_state = [False] * len(self.valid_keys)
        self.fast_redraw = False
        try:
            self.fig = pp.figure(num=title)
        except (RuntimeError, ImportError) as e:
            print(f"Error: {e}")
            print("Pro tip: Check that there's an X window server running.")
            print("Pro tip: Check that the $DISPLAY environment variable is defined.")
            sys.exit(-1)
        if 0 not in [nrows, ncols, nplots]:
            self.create_axes(nrows, ncols, nplots, layout, **subplot_kwargs)

    def create_axes(self, nrows=1, ncols=1, nplots=None, layout=None, **kwargs):
        """
        Create one or more subplots with basic enablers for keyboard and mouse
        interaction.
        """
        if layout is None:  # generate layout if not provided by user
            nplots = nplots or (nrows * ncols)  # set default value for nplots if not provided
            if nplots > nrows * ncols:  # derive nrows & ncols if only nplots is provided
                nrows = np.clip(1, 2, np.ceil(nplots / 2)).astype(np.int)
                ncols = np.ceil(nplots / nrows).astype(np.int)
            layout = np.arange(nrows * ncols).reshape(nrows, ncols)
            layout = np.clip(layout, 0, nplots - 1)  # stretch the last subplot if not evenly divided
        layout = np.array(layout)
        grid = matplotlib.gridspec.GridSpec(*layout.shape)  # pylint: disable=not-an-iterable
        axes = np.array(layout, dtype=object)
        self.axes = np.array(range(layout.max() + 1), dtype=object)
        for idx in np.unique(layout[layout >= 0]):
            yslice, xslice = np.nonzero(layout == idx)
            yslice = slice(yslice[0], yslice[-1] + 1)
            xslice = slice(xslice[0], xslice[-1] + 1)
            axes = self.fig.add_subplot(grid[yslice, xslice], **kwargs)
            self.axes[idx] = axes
        self.current_subplot = self.ax = self.axes[0]
        self.fig.tight_layout()
        self.fig.canvas.mpl_connect("close_event", self._fig_event_close)
        self.fig.canvas.mpl_connect("key_press_event", self._fig_event_keypress)
        self.fig.canvas.mpl_connect("motion_notify_event", self._fig_event_mousemove)
        self.fig.canvas.mpl_connect("button_press_event", self._fig_event_mouseclick)
        warnings.filterwarnings("ignore", category=UserWarning, module="pyplottr")
        return self.axes[0]  # return the first/only subplot

    def savefig(self, *args, **kwargs):
        """ Save the figure equivalently to pyplot.savefig(). """
        self.redraw()  # redraw twice to make sure all pendings events are handled
        self.redraw()
        pp.savefig(*args, **kwargs)

    def show(self, interval=0.0):
        """ Redraw and handle events until exit. """
        while not self.exit_request:
            self.redraw()
            time.sleep(interval)

    def events(self):
        """ Flush any pending events. """
        self.fig.canvas.flush_events()

    def redraw(self):
        """ Redraw and flush any pending events. """
        if self.fast_redraw:
            for ax in self.axes:
                ax.draw_artist(ax.patch)
                for line in ax.get_children():
                    ax.draw_artist(line)
            self.events()
        else:  # one full redraw required in the beginning
            self.fig.canvas.draw_idle()
            self.events()

    def move(self, x, y):
        """ Move the figure window upper left corner to (x, y). """
        backend = matplotlib.get_backend()
        if backend == "TkAgg":
            self.fig.canvas.manager.window.wm_geometry(f"+{x}+{y}")
        elif backend == "WXAgg":
            self.fig.canvas.manager.window.SetPosition((x, y))
        else:  # this works for QT and GTK
            self.fig.canvas.manager.window.move(x, y)

    def resize(self, width, height):  # pylint: disable=no-self-use
        """ Resize the figure window to (width, height) pixels. """
        mng = pp.get_current_fig_manager()
        mng.resize(width, height)

    def close(self):
        """ Close the figure window. """
        pp.close(self.fig)

    ######################################################################################
    #
    #  I N T E R N A L   F U N C T I O N S
    #
    ######################################################################################

    def _fig_event_close(self, _evt):
        self.exit_request = True

    def _fig_event_keypress(self, evt):
        if evt.key is not None:
            self.key = evt.key
            if evt.key in self.valid_keys:
                idx = self.valid_keys.index(evt.key)
                self.key_state[idx] = not self.key_state[idx]

    def _fig_event_mousemove(self, evt):
        # set mouse coords to None if not within the main subplot
        self.current_subplot = evt.inaxes
        if evt.inaxes == self.fig.axes[0]:
            self.mousex = int(round(evt.xdata))
            self.mousey = int(round(evt.ydata))
        else:
            self.mousex = None
            self.mousey = None

    def _fig_event_mouseclick(self, evt):
        # do nothing if this is not a left-click on the main subplot
        if evt.inaxes == self.fig.axes[0]:
            if evt.button == 1:
                self.clickx = int(round(evt.xdata))
                self.clicky = int(round(evt.ydata))


def _mpl_init():
    pp.ion()  # must enable interactive mode before creating any figures
    # free up some hotkeys for our own use: a, s, f, c, v, h, g, G, k, L, l, o, p, W, Q
    matplotlib.rcParams["keymap.all_axes"] = ''  # a
    matplotlib.rcParams["keymap.save"] = 'ctrl+s'  # s
    matplotlib.rcParams["keymap.fullscreen"] = 'ctrl+f'  # f
    matplotlib.rcParams["keymap.back"] = 'backspace'  # c
    matplotlib.rcParams["keymap.forward"] = ''  # v
    matplotlib.rcParams["keymap.home"] = ''  # h
    matplotlib.rcParams["keymap.grid"] = ''  # g
    matplotlib.rcParams["keymap.grid_minor"] = ''  # G
    matplotlib.rcParams["keymap.xscale"] = ''  # k, L
    matplotlib.rcParams["keymap.yscale"] = ''  # l
    matplotlib.rcParams["keymap.zoom"] = ''  # o
    matplotlib.rcParams["keymap.pan"] = ''  # p
    matplotlib.rcParams["keymap.quit_all"] = ''  # W, Q
    matplotlib.rcParams["keymap.quit"] = ['q', 'escape']
    matplotlib.rcParams["figure.autolayout"] = True


def _plot(*plot_args, projection=None, **kwargs):
    init_kwargs = _extract_kwargs(Figure.__init__, **kwargs)
    axes_kwargs = _extract_kwargs(matplotlib.figure.Figure.add_subplot, **kwargs)
    fig_kwargs = {**init_kwargs, **axes_kwargs}
    fig = Figure(**fig_kwargs, projection=projection)
    line_kwargs = _extract_kwargs(matplotlib.lines.Line2D, **kwargs)
    axes_kwargs = _extract_kwargs(matplotlib.axes.Axes, **kwargs)
    plot_kwargs = {**line_kwargs, **axes_kwargs}
    fig.ax.plot(*plot_args, **plot_kwargs)
    return fig


def _extract_kwargs(func, **kwargs):
    func_kwargs = [k for k, v in inspect.signature(func).parameters.items()]
    func_dict = {k: kwargs.pop(k) for k in dict(kwargs) if k in func_kwargs}
    return func_dict


def _selftest():
    # simple one-liners
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    plot(x, np.sin(x), x, np.cos(x), title="sin & cos").show()
    plot(x, np.sin(np.pi * x) / (np.pi * x), title="sinc").show()
    # subplot layouts
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    for nplots in np.arange(2, 9):
        fig = Figure(f"nplots={nplots}", nplots=nplots)
        fig.axes[0].plot(xline, xline)
        fig.axes[-1].plot(xline, zline)
        fig.show()
    for nrows, ncols in [[2, 1], [1, 3], [2, 4]]:
        fig = Figure(f"nrows={nrows}, ncols={ncols}", nrows=nrows, ncols=ncols)
        fig.axes[0].plot(xline, xline)
        fig.axes[-1].plot(xline, zline)
        fig.show()
    # 3D projection
    plot3d(xline, yline, zline, title="3D plot", color="black").show()


if __name__ == "__main__":
    _selftest()
