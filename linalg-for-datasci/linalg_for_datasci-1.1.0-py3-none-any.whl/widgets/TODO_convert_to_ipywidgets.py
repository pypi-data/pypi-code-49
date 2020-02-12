##### CHOOSING LINEAR FUNCTIONS DEMO
# ## Choosing Matrices that correspond to a Linear Function
# Now that you've seen what some matrices do to the $\mathbb{R}^2$ space, let's see if you can create your own matrix to match a given linear function. In this section, you will be shown the results of functions and/or told a description of what the desired function will do, and then you will construct a $2\times2$ matrix that matches that function. Don't worry about being exact down to the last decimal place, as long as the general idea is there. As long as the resulting warped regions look close enough it will count as a correct solution. Feel free to run each cell multiple times to play around with different matrices. And pay close attention to the orientation of the region by looking at the colors of the quadrants!
# To help with this, we also designed an interactive tool that will let you explore what happens when you position the $e_1$ and $e_2$ vectors in various places. Simply choose where to map $e_1$ and $e_2$ to, and observe how the $\mathbb{R}^2$ space warps with it.

threshold = 0.15

fig = plt.figure(figsize=(5, 10))
ax1 = fig.add_subplot(211, aspect="equal")
ax2 = fig.add_subplot(212, aspect="equal")


ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2.5)
vector1 = np.array([1, 0])
vector2 = np.array([0, 1])
e1 = plot_vector(ax1, vector1, label="e1")
e2 = plot_vector(ax1, vector2, label="e2")


A = np.eye(2)
plot_region_with_func(A, fig=fig, ax=ax2)

sel_vec = 0

color = lambda a: "c" if sel_vec == a else "k"
d = lambda x, y: math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


def onclick(event):
    global sel_vec
    global e1
    global e2
    if event.inaxes is ax1:
        if sel_vec:
            col = 1 if sel_vec == 2 else 0
            A[0, col] = event.xdata
            A[1, col] = event.ydata
            sel_vec = 0
        else:
            d1 = d((event.xdata, event.ydata), (A[0, 0], A[1, 0]))
            d2 = d((event.xdata, event.ydata), (A[0, 1], A[1, 1]))
            if d1 < threshold:
                sel_vec = 1
            elif d2 < threshold:
                sel_vec = 2
        ax1.clear()
        ax1.set_xlim(-2.5, 2.5)
        ax1.set_ylim(-2.5, 2.5)
        e1 = plot_vector(ax1, A[0, 0], A[1, 0], color=color(1), label="e1")
        e2 = plot_vector(ax1, A[0, 1], A[1, 1], color=color(2), label="e2")

    else:
        return

    ax2.clear()
    plot_region_with_func(ax2, A, alpha=0.7)

    fig.canvas.draw_idle()


cid = fig.canvas.mpl_connect("button_press_event", onclick)


##### 2D SPECTRAL DECOMPOSITIONS DEMO

# ## 3. Interactive Spectral Decomposition Demo

# From above, we see that any symmetric matrix can be decomposed into a rotation + stretch + rotate back. Using the tool below, play with building different symmetric matrices by choosing rotation angles and stretch factors (eigenvalues).

# Additional imports for plotting


from matplotlib.widgets import Slider


### This would probably be turned into the __init__ method of the custom ipywidgets class

# Draw the initial plot
A = np.array([[2.5, np.sqrt(3) / 2], [np.sqrt(3) / 2, 1.5]])
plot_spectral_decomp_for_matrix(A)

text = fig.text(0.01, 0.5, "{}".format(stringify_matrix(A)))

# Add sliders
rot_slider_ax = fig.add_axes([0.25, 0.15, 0.65, 0.03])
rot_slider = Slider(rot_slider_ax, "Angle", -90, 90, valinit=0, valstep=1)

xsc_slider_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03])
xsc_slider = Slider(xsc_slider_ax, "1st eigval", 0.1, 5, valinit=0.1, valstep=0.1)

ysc_slider_ax = fig.add_axes([0.25, 0.05, 0.65, 0.03])
ysc_slider = Slider(ysc_slider_ax, "2nd eigval", 0.1, 5, valinit=0.1, valstep=0.1)

# # Initialize slider values to match A
d, U = np.linalg.eigh(A)
d = np.flip(d, axis=0)
U = np.flip(U, axis=1)

angle = get_angle_of_rot_mat(U)

rot_slider.set_val(angle)
xsc_slider.set_val(d[0])
ysc_slider.set_val(d[1])

### This of course would probably be turned into the event method of the custom ipywidgets class


def sliders_on_changed(val):
    # Build new A matrix
    global A
    global text
    U = get_rot_mat(rot_slider.val)
    D = np.array([[xsc_slider.val, 0], [0, ysc_slider.val]])
    A = U @ D @ U.T

    # Clear old plot
    ax11.clear()
    ax12.clear()
    ax21.clear()
    ax22.clear()
    ax31.clear()

    # Draw new plot
    plot_spectral_decomp_for_matrix(A)
    text.set_text("{}".format(stringify_matrix(A)))
    fig.canvas.draw_idle()


rot_slider.on_changed(sliders_on_changed)
xsc_slider.on_changed(sliders_on_changed)
ysc_slider.on_changed(sliders_on_changed)

plt.show()

### This plot_spectral_decomp_for_matrix function could probably be made a method of the custom ipywidgets class
### Might have to be adjusted along with __init__ a bit to change to decide whether it produces fig and/or ax's itself or has them as input

from linalg_for_datasci.linear_func import get_angle_of_rot_mat
from linalg_for_datasci.tests import typecheck_symmetric_matrix
from linalg_for_datasci.plotting import (
    plot_region_with_func,
    plot_region_with_two_basises,
)


def plot_spectral_decomp_for_matrix(A, plot_size=5):

    # Initialize figure and axes
    fig = plt.figure(figsize=(8.25, 10.25))

    ax11 = fig.add_subplot(3, 2, 1, aspect="equal")
    ax12 = fig.add_subplot(3, 2, 2, aspect="equal")
    ax21 = fig.add_subplot(3, 2, 3, aspect="equal")
    ax22 = fig.add_subplot(3, 2, 4, aspect="equal")
    ax31 = fig.add_subplot(3, 2, (5, 6), aspect="equal")

    # Adjust the subplots region to leave some space for the sliders and buttons
    fig.subplots_adjust(left=0.25, bottom=0.25)

    typecheck_symmetric_matrix(A)

    d, U = np.linalg.eigh(A)
    d = np.flip(d, axis=0)
    U = np.flip(U, axis=1)
    U *= np.sign(U[0, 0])
    angle = get_angle_of_rot_mat(U)

    u1 = U[:, 0]
    u2 = U[:, 1]
    e1 = np.array([1, 0])
    e2 = np.array([0, 1])

    plot_region_with_func(
        np.eye(2), "Before linear function", fig=fig, ax=ax11, plot_size=plot_size
    )

    plot_region_with_two_basises(
        np.eye(2),
        "Before function, eigenbasis overlaid",
        [u1, u2],
        [e1, e2],
        fig=fig,
        ax=ax12,
        plot_size=plot_size,
    )

    alternative_basis = apply_func_to_basis(U.T, [u1, u2])
    standard_basis = apply_func_to_basis(U.T, [e1, e2])

    plot_region_with_two_basises(
        U.T,
        "After $1$st linear function",
        alternative_basis,
        standard_basis,
        fig=fig,
        ax=ax21,
        plot_size=plot_size,
    )

    alternative_basis = apply_func_to_basis(np.diag(d) @ U.T, [u1, u2])
    standard_basis = apply_func_to_basis(np.diag(d) @ U.T, [e1, e2])

    plot_region_with_two_basises(
        np.diag(d) @ U.T,
        "After $2$nd linear function",
        alternative_basis,
        standard_basis,
        fig=fig,
        ax=ax22,
        plot_size=plot_size,
    )

    alternative_basis = apply_func_to_basis(U @ np.diag(d) @ U.T, [u1, u2])
    standard_basis = apply_func_to_basis(U @ np.diag(d) @ U.T, [e1, e2])

    plot_region_with_two_basises(
        U @ np.diag(d) @ U.T,
        "After $3$rd linear function",
        alternative_basis,
        standard_basis,
        fig=fig,
        ax=ax31,
        plot_size=plot_size,
    )

    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
    plt.subplots_adjust(hspace=0.5)
