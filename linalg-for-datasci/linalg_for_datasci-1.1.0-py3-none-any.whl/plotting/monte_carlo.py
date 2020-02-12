from ..utils import throw_darts


def p_ball_plot(p, figure, axis, callback, trials=10000):
    """
    `callback` is meant to be the `throw_dart`
    function students write by themselves
    """
    axis.set_xlim(-1.1, 1.1)
    axis.set_ylim(-1.1, 1.1)
    axis.set_xlabel("$x_1$")
    axis.set_ylabel("$x_2$")
    axis.set_title("Scatter plot of points in the $p$-ball")
    axis.set_aspect("equal")

    # Need this line for using with widget
    axis.clear()

    darts = throw_darts(trials, lambda: callback(p))
    darts = darts.loc[darts["Inside Ball"] == True]
    x1s = darts["First Dimension"].values
    x2s = darts["Second Dimension"].values
    axis.scatter(x1s, x2s)
    figure.canvas.draw()
