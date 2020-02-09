import sympy as sp
from rigidbodysimulator.rigid_body_dynamics import S,N
from rigidbodysimulator.substitute_dynamic_symbols import lambdify

import ipyvolume as ipv
import ipywidgets as widgets
import numpy as np
import pandas as pd

p_x = sp.Symbol('p_x')
p_y = sp.Symbol('p_y')
p_z = sp.Symbol('p_z')
P = p_x*S.x + p_y*S.y + p_z*S.z

rotation_lambda = lambdify(P.to_matrix(N))


def rotate2(p, phi_=0, theta_=0, psi_=0):
    args = {
        'p_x': p[0],
        'p_y': p[1],
        'p_z': p[2],
        'phi': phi_,
        'theta': theta_,
        'psi': psi_
    }

    result = rotation_lambda(**args)
    return result.reshape(3, result.shape[2]).T




class TrackPlot3dWidget:
    def __init__(self, df: pd.DataFrame):
        self.figure = ipv.figure(animation=0., animation_exponent=0, width=800, height=800)
        #self.figure.camera_control = 'orbit'

        self.lpp = lpp = 1

        x_min = np.min([-lpp, df['x0'].min()])
        x_max = np.max([lpp, df['x0'].max()])
        y_min = np.min([-lpp, df['y0'].min()])
        y_max = np.max([lpp, df['y0'].max()])
        z_min = np.min([-lpp, df['z0'].min()])
        z_max = np.max([lpp, df['z0'].max()])

        ipv.xlim(x_min, x_max)
        ipv.ylim(y_min, y_max)
        ipv.zlim(z_min, x_max)
        ipv.style.box_off()

        self.track = ipv.pylab.plot(df['x0'].values, df['y0'].values, df['z0'].values)

        self.load_ship_geometry()
        self.port = ipv.plot_mesh(self.X, self.Y_port, self.Z, wireframe=False)
        self.stbd = ipv.plot_mesh(self.X, self.Y_starboard, self.Z, wireframe=False)

        ipv.pylab.view(azimuth=180, elevation=60, distance=1)
        ipv.show()

        self.df = df

        min = df.index[0]
        max = df.index[-1]
        step = (max-min)/100
        self.ui = widgets.interact(self.update,
                                   t=widgets.FloatSlider(value=0, min=min, max=max, step=step))

    def load_ship_geometry(self):
        self.N = 10
        L = self.lpp
        B = 0.1 * self.lpp
        T = 0.05 * self.lpp

        x = np.linspace(0, L, self.N)
        y = np.linspace(0, B, self.N)
        z = np.linspace(0, T, self.N)

        X, Y = np.meshgrid(x, y)
        Z = T - np.array(Y)
        Y *= (L - X) ** (0.4)

        self.X = X - L / 2
        self.Z = Z
        self.Y_port = Y
        self.Y_starboard = -Y

    def update(self, t):
        index = np.argmin(np.abs(self.df.index - t))
        s = self.df.iloc[index]

        phi = s['phi']
        theta = s['theta']
        psi = s['psi']
        x0 = s['x0']
        y0 = s['y0']
        z0 = s['z0']

        print("t:%0.1f [s]" % t)
        print("phi:%0.1f [deg]" % np.rad2deg(phi))
        print("theta:%0.1f [deg]" % np.rad2deg(theta))
        print("psi:%0.1f [deg]" % np.rad2deg(psi))


        angles = [phi, theta, psi]

        X = self.X.flatten()
        Y = self.Y_starboard.flatten()
        Z = self.Z.flatten()
        result = rotate2(p=[X, Y, Z], phi_=angles[0], theta_=angles[1], psi_=angles[2])
        X_ = result[:, 0] + x0
        Y_ = result[:, 1] + y0
        Z_ = result[:, 2] + z0
        self.stbd.x = X_
        self.stbd.y = Y_
        self.stbd.z = Z_

        X = self.X.flatten()
        Y = self.Y_port.flatten()
        Z = self.Z.flatten()
        result = rotate2(p=[X, Y, Z], phi_=angles[0], theta_=angles[1], psi_=angles[2])
        X_ = result[:, 0] + x0
        Y_ = result[:, 1] + y0
        Z_ = result[:, 2] + z0
        self.port.x = X_
        self.port.y = Y_
        self.port.z = Z_


def track_plot(df, ax, l=1, time_step='1S', **kwargs):
    df.plot(x='y0', y='x0', ax=ax, **kwargs)

    df_ = df.copy()
    df_.index = pd.TimedeltaIndex(df_.index, unit='s')
    df_ = df_.resample(time_step).first()

    def plot_body(row):
        x = row['y0']
        y = row['x0']
        psi = row['psi']
        xs = [x - l / 2 * np.sin(psi), x + l / 2 * np.sin(psi)]
        ys = [y - l / 2 * np.cos(psi), y + l / 2 * np.cos(psi)]
        ax.plot(xs, ys, 'k-')

    for index, row in df_.iterrows():
        plot_body(row)

    ax.set_xlabel('y0')
    ax.set_ylabel('x0')
    ax.axis('equal')