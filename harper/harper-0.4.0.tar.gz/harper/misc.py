"""Miscallaneous utility functionality."""
import io
import typing

from harper.audio.signal import Signal


# TODO: implement in C
def window(
    iterable: iter, size: int, stride: int = 2, unequal: str = "pad", padval=0
) -> list:
    """Pass through an iterable and return certain windowed segments.

    It's basically a moving window of a certain size and stride
    that extracts subsets of an iiterable.

    Parameters
    ----------
    iterable : iter
        The thing to move through
    size: int
        The size of the window to pan with. This is how many
        elements will be considered as part of a subset.
    stride: int
        After getting a subset, how many steps should the window
        move before selecting the next chunk?
    unequal : str
        Can be 'pad' or 'drop'. It's very possible that the
        end of a list wont contain the expected number of items,
        eg.
        [1,2,3]
        with a size of 4 would only find 3 elements. What should happen?
        If 'pad' we add a value to that subset. Specify the value with the
        padval keyword argument. If 'drop' we simply let the subset be
        3 items.


    Examples
    --------
    orig = [1,2,3,4,5,6,7,8]
    window(orig, size=2, stride=3)

      -> [(1,2),3,4,5,6,7,8]
      -> [1,2,3,(4,5),6,7,8]
      -> [1,2,3,4,5,6,(7,8)]

    would return [[1,2], [4,5], [7,8]]

    """
    finished = list()

    start = 0
    end = start + size
    final = len(iterable)

    # when to break:
    # if end is exactly final, thats the last time we should run
    # if end is greater than final, thats the last time we should run

    while start <= final:
        current = iterable[start:end]
        if len(current) == 0:
            break
        if len(current) < size:
            if unequal == "pad":
                while len(current) < size:
                    if isinstance(current, bytes):
                        current = current + b"\x00"
                    else:
                        current.append(padval)
            if unequal == "drop":
                pass
        finished.append(current)
        if end >= final:
            break
        start += stride
        end += stride
    return finished


# TODO: interleave should be generic. takes multiple iterables and a step size.
# takes a step of iterable1, step of iterable2, etc.

# TODO: implement in C
def interleave_signals(signals: typing.List[Signal]) -> Signal:
    """Combine two signals into one.

    Opposite of window. Takes two things and smushes them together,
    in alternating capacity. Primarily a zip with some flavor added in.

    Parameters
    ----------
    signals : harper.misc.signal.Signals
        A list of signals to be interleaved.

    Returns
    -------
    Signal
        A harper Signal object
    """
    source = dict()
    new = list()

    for idx, element in enumerate(signals):
        source[idx] = dict()
        x = element.reversed_timeseries
        source[idx]["data"] = x

    def keep_going(source):
        for signal in source.values():
            if signal["data"] != list():
                return True
        return False

    n_channels = len(source)
    current_signal = 0
    done = False
    while not done:
        try:
            add_me = source[current_signal]["data"].pop()
        except IndexError:
            add_me = 0
        new.append(add_me)
        current_signal += 1
        if current_signal >= n_channels:
            current_signal = 0
            if not keep_going(source):
                done = True
    return Signal(new)


# TODO: implement in C
def interleave_bytes(signals, style="pad"):
    """Combine two byte strings into one.

    Opposite of window. Takes two things and smushes them together,
    in alternating capacity. Primarily a zip with some flavor added in.

    Parameters
    ----------
    signals : harper.misc.signal.Signals
        A list of signals to be interleaved.

    Returns
    -------
    bytes
        An interleaved byte string.
    """
    source = dict()
    new = list()

    for idx, element in enumerate(signals):
        source[idx] = dict()
        x = io.BytesIO(element.reversed_bytes)
        source[idx]["data"] = x
        source[idx]["width"] = element.minimum_bytes

    def keep_going(source):
        for signal in source.values():
            if signal["data"].tell() < len(signal["data"].getvalue()):
                return True
        return False

    n_channels = len(source)
    current_signal = 0
    while keep_going(source):
        add_me = source[current_signal]["data"].read(
            source[current_signal]["width"]
        )
        while len(add_me) < source[current_signal]["width"]:
            add_me = add_me + b" "
        new.append(add_me)
        current_signal += 1
        if current_signal >= n_channels:
            current_signal = 0
    return new
