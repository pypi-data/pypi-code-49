import matplotlib.pyplot as plt
import numpy as np

from ..tests import typecheck_vector


def plot_vector(ax, vector, scale=1, color="k", label="", origin=np.array([0, 0])):
    typecheck_vector(origin)
    assert len(origin) == 2
    typecheck_vector(vector)
    assert len(vector) == 2

    shifted_and_scaled_vector = (vector + origin) * scale
    scaled_vector = vector * scale

    if label:
        halign = "left" if vector[0] >= 0 else "right"
        valign = "bottom" if vector[1] >= 0 else "top"
        text_options = {
            "horizontalalignment": halign,
            "verticalalignment": valign,
            "color": color,
            "size": 22,
        }
        ax.text(*shifted_and_scaled_vector, label, **text_options)

    arrow_options = {
        "width": 0.3 * scale,
        "head_width": 0.4 * scale,
        "head_length": 0.3 * scale,
        "length_includes_head": True,
        "color": color,
    }
    return ax.arrow(*origin, *scaled_vector, **arrow_options)


def does_function_preserve_scalar_multiplication(
    angle, scalar, function, vector_name="$v$", scalar_name="$s$", function_name="$f$"
):
    fig, plots = plt.subplots(ncols=5, subplot_kw={"aspect": "equal"}, figsize=(50, 10))

    vector = np.array([np.cos(angle), np.sin(angle)])
    v, s, f = (vector, scalar, function)
    plot_size = (
        np.max(
            np.abs(
                [
                    v[0],
                    v[1],
                    f(v)[0],
                    f(v)[1],
                    (s * v)[0],
                    (s * v)[1],
                    f(s * v)[0],
                    f(s * v)[1],
                    (s * f(v))[0],
                    (s * f(v))[1],
                ]
            )
        )
        + 2
    )

    for i in range(0, 5):
        plots[i].set_xlim(-plot_size, plot_size)
        plots[i].set_ylim(-plot_size, plot_size)
        plots[i].set_xlabel("$x_1$ value")
        plots[i].set_ylabel("$x_2$ value")
        plots[i].axhline(linewidth=1, color="black")
        plots[i].axvline(linewidth=1, color="black")

    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
    plt.subplots_adjust(wspace=0.3)

    plot_vector(plots[0], vector, color="k", label=vector_name)
    plots[0].set_title("Individual vector")

    plot_vector(
        plots[1],
        scalar * vector,
        color="k",
        label="{}$\cdot${}".format(scalar_name, vector_name),
    )
    plots[1].set_title("Scaled vector")

    plot_vector(
        plots[2],
        function(vector),
        color="m",
        label="{}({})".format(function_name, vector_name),
    )
    plots[2].set_title("{} applied to individual vector".format(function_name))

    plot_vector(
        plots[3],
        scalar * function(vector),
        color="m",
        label="{}$\cdot${}({}))".format(scalar_name, function_name, vector_name),
    )
    plots[3].set_title("Function first, scaling second")

    plot_vector(
        plots[4],
        function(scalar * vector),
        color="m",
        label="{}({}$\cdot${})".format(function_name, scalar_name, vector_name),
    )
    plots[4].set_title("Scaling first, function second")


def does_function_preserve_addition(
    angle1,
    angle2,
    function,
    vector1_name="$v_1$",
    vector2_name="$v_2$",
    function_name="$f$",
    head_to_tail=False,
):
    fig, plots = plt.subplots(ncols=5, subplot_kw={"aspect": "equal"}, figsize=(50, 10))

    vector1 = np.array([np.cos(angle1), np.sin(angle1)])
    vector2 = np.array([np.cos(angle2), np.sin(angle2)])

    v1, v2, f = (vector1, vector2, function)
    plot_size = (
        np.max(
            np.abs(
                [
                    v1[0],
                    v1[1],
                    f(v1)[0],
                    f(v1)[1],
                    v2[0],
                    v2[1],
                    f(v2)[0],
                    f(v2)[1],
                    (v1 + v2)[0],
                    (v1 + v2)[1],
                    f(v1 + v2)[0],
                    f(v1 + v2)[1],
                    (f(v1) + f(v2))[0],
                    (f(v1) + f(v2))[1],
                ]
            )
        )
        + 2
    )

    for i in range(0, 5):
        plots[i].set_xlim(-plot_size, plot_size)
        plots[i].set_ylim(-plot_size, plot_size)
        plots[i].set_xlabel("$x_1$ value")
        plots[i].set_ylabel("$x_2$ value")
        plots[i].axhline(linewidth=1, color="black")
        plots[i].axvline(linewidth=1, color="black")

    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
    plt.subplots_adjust(wspace=0.3)

    plot_vector(plots[0], vector1, color="black", label=vector1_name)
    origin = vector1 if head_to_tail else np.array([0, 0])
    plot_vector(plots[0], vector2, color="black", label=vector2_name, origin=origin)
    plots[0].set_title("Individual vectors")

    plot_vector(
        plots[1],
        vector1 + vector2,
        color="black",
        label="{}+{}".format(vector1_name, vector2_name),
    )
    plots[1].set_title("Sum of vectors")

    plot_vector(
        plots[2],
        function(vector1),
        color="m",
        label="{}({})".format(function_name, vector1_name),
    )
    origin = function(vector1) if head_to_tail else np.array([0, 0])
    plot_vector(
        plots[2],
        function(vector2),
        color="m",
        label="{}({})".format(function_name, vector2_name),
        origin=origin,
    )
    plots[2].set_title("{} applied to individual vectors".format(function_name))

    plot_vector(
        plots[3],
        function(vector1) + function(vector2),
        color="m",
        label="{}({})+{}({})".format(
            function_name, vector1_name, function_name, vector2_name
        ),
    )
    plots[3].set_title("Function first, sum second")

    plot_vector(
        plots[4],
        function(vector1 + vector2),
        color="m",
        label="{}({}+{})".format(function_name, vector1_name, vector2_name),
    )
    plots[4].set_title("Sum first, function second")
