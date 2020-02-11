""" Simple WIP interface for people who just want to plot things.

This is not ready for usage yet, use `concur.integrations.glfw.main` instead.
"""


from functools import partial
from concur.integrations import main
from concur.extra_widgets import frame, Frame
from concurrent.futures import ThreadPoolExecutor


executor = ThreadPoolExecutor()


def plot(content_gen, data_gen, xlim, ylim, width=500, height=500):
    def app():
        fr = Frame((xlim[0], ylim[0]), (xlim[1], ylim[1]))
        data = next(data_gen)
        while True:
            tag, value = yield from frame("Frame", fr, partial(content_gen, data))
            if tag == "Frame":
                fr = value
            yield

    # widget = c.extra_widgets.plot.
    main("Plot", app(), width, height)


def content(data, tf):
    import concur.draw as d
    from concur import nothing
    return nothing()


def data():
    yield None

if __name__ == "__main__":
    plot(content, data(), (0,1), (0, 1))
