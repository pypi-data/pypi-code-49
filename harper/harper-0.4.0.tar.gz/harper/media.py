"""Functions and interfaces regarding the creation of audio/visual media."""
import abc

import alsaaudio
from matplotlib import pyplot as plt


class Visual(metaclass=abc.ABCMeta):
    """Interface that signifies an object can be plotted."""

    @property
    @abc.abstractmethod
    def x_plot_time():
        """Abstract method to return plottable domain element."""
        pass

    @property
    @abc.abstractmethod
    def y_plot_time():
        """Abstract method to return plottable domain element."""
        pass


class Audio(metaclass=abc.ABCMeta):
    """Interface that signifies an object can be played."""

    @abc.abstractmethod
    def read_bytes():
        """Abstract method to return file like read operation."""
        pass

    @abc.abstractmethod
    def bytesPerSample():
        """Abstract method to return sample width in bytes."""
        pass

    @abc.abstractmethod
    def seek():
        """Abstract method to change byte read position."""
        pass


def play(audio_object, sample_rate=44100, n_channels=1, device="default"):
    """Play an Audio interfacing object on system ALSA device.

    Parameters
    ----------
    audio_object: media.Audio interface
        The object to be played.
    sample_rate: int
        The rate at which audio should be played back. Optional,
        defaults to 44100 (CD quality).
    n_channels: int
        The number of channels encoded by the byte samples.
        Optional, defaults to 1.
    device: str
        The name of the ALSA device to use. Optional, defaults to 'default.'

    Returns
    -------
    None

    """
    device = alsaaudio.PCM(device=device)

    device.setchannels(n_channels)
    frame_rate = int(sample_rate / n_channels)
    device.setrate(frame_rate)
    device.setchannels(n_channels)

    bytesPerSample = audio_object.bytesPerSample
    if bytesPerSample == 1:
        device.setformat(alsaaudio.PCM_FORMAT_U8)
    # Otherwise we assume signed data, little endian
    elif bytesPerSample == 2:
        device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    elif bytesPerSample == 3:
        device.setformat(alsaaudio.PCM_FORMAT_S24_3LE)
    elif bytesPerSample == 4:
        device.setformat(alsaaudio.PCM_FORMAT_S32_LE)
    else:
        raise ValueError("Unsupported format")

    bytesPerFrame = bytesPerSample * n_channels * 10
    periodsize = bytesPerFrame * 10
    device.setperiodsize(periodsize)

    audio_object.seek()

    chunk = audio_object.read_bytes(periodsize)
    while chunk:
        while len(chunk) != periodsize:
            chunk = chunk + b" "
        device.write(chunk)
        chunk = audio_object.read_bytes(periodsize)


# TODO: calculate a reasaable default xlim, ylim
def plot_time(
    visual_object,
    outfile,
    x_lim=None,
    y_lim=None,
    x_attr=None,
    y_attr=None,
    **kwargs
):
    """Plot timeseries via matplotlib and save to disk.

    Parameters
    ----------
    visual_object: Visual-interface object
        An object that inherits from the Visal abc.
    outfile: str
        The path to the file you'd like to save to.
    y_lim : (int, int)
        Range of the y axis to display in matplotlib. Optional
    x_lim : (int, int)
        Range of the x axis to display in matplotlib. Optional
    x_attr: str
        Passed in as x attribute. Optional, defaults to the `x_plot_time` of
        the visual_object.
    kwargs: additional keyword arguments
        Right now, the only supported ker
    Returns
    -------
    None

    """
    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    if not x_attr:
        x_attr = visual_object.x_plot_time
    if not y_attr:
        y_attr = visual_object.y_plot_time

    axes.plot(x_attr, y_attr, **kwargs)

    if x_lim:
        axes.set_xlim(x_lim)
    if y_lim:
        axes.set_ylim(y_lim)

    fig.savefig(outfile)


# TODO: make this calculate an appropraite default ylim, xlim.
def plot_spectrum(
    visual_object,
    outfile,
    x_lim=None,
    y_lim=None,
    x_attr=None,
    y_attr=None,
    **kwargs
):
    """Plot signal spectra via matplotlib and save to disk.

    Parameters
    ----------
    visual_object: Visual-interface object
        An object that inherits from the Visal abc.
    outfile: str
        The path to the file you'd like to save to.
    y_lim : (int, int)
        Range of the y axis to display in matplotlib. Optional
    x_lim : (int, int)
        Range of the x axis to display in matplotlib. Optional
    x_attr: str
        Passed in as x attribute. Optional, defaults to the `x_plot_time` of
        the visual_object.
    kwargs: additional keyword arguments to pass to matplotlib plot function.

    Returns
    -------
    None

    """
    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    if not x_attr:
        x_attr = visual_object.x_plot_spectrum
    if not y_attr:
        y_attr = visual_object.y_plot_spectrum

    axes.plot(x_attr, y_attr, **kwargs)

    if x_lim:
        axes.set_xlim(x_lim)
    if y_lim:
        axes.set_ylim(y_lim)

    fig.savefig(outfile)


# TODO: make this slighlty more flexible.
def plot(
    visual_object,
    outfile,
    x_lim=None,
    y_lim=None,
    x_attr=None,
    y_attr=None,
    **kwargs
):
    """Plot signal spectra via matplotlib and save to disk.

    Parameters
    ----------
    visual_object: Visual-interface object
        An object that inherits from the Visal abc.
    outfile: str
        The path to the file you'd like to save to.
    y_lim : (int, int)
        Range of the y axis to display in matplotlib. Optional
    x_lim : (int, int)
        Range of the x axis to display in matplotlib. Optional
    x_attr: str
        Passed in as x attribute. Optional, defaults to the `x_plot_time` of
        the visual_object.
    kwargs: additional keyword arguments to pass to matplotlib plot function.

    Returns
    -------
    None

    """
    fig = plt.figure()
    time_plot = fig.add_subplot(2, 1, 1)
    spectrum_plot = fig.add_subplot(2, 1, 2)

    xlim_time_max = max(visual_object.x_plot_time)

    time_plot.plot(visual_object.x_plot_time, visual_object.y_plot_time)
    time_plot.set_xlim(0, xlim_time_max)

    spectrum_plot.plot(
        visual_object.x_plot_spectrum, visual_object.y_plot_spectrum
    )
    spectrum_plot.set_xlim(0, 10000)

    fig.savefig(outfile)
