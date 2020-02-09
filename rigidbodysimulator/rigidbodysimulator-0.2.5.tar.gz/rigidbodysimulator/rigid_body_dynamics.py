import sympy as sp
import sympy.physics.mechanics as me
import pandas as pd
import numpy as np

from pydy.codegen.ode_function_generators import generate_ode_function
from scipy.integrate import odeint


x0,y0,z0 = me.dynamicsymbols('x0 y0 z0')
x01d,y01d,z01d = me.dynamicsymbols('x01d y01d z01d')
u,v,w = me.dynamicsymbols('u v w')

phi,theta,psi = me.dynamicsymbols('phi theta psi')
phi1d,theta1d,psi1d = me.dynamicsymbols('phi1d theta1d psi1d')

N = me.ReferenceFrame('N')

S = N.orientnew('S', 'Body', [psi,theta,phi],'ZYX')

M = me.Point('M')
O = M.locatenew('P',0)
M.set_vel(N,0)
O.set_vel(S,u*S.x + v*S.y + w*S.z)
O.v1pt_theory(M,N,S)

velocity_matrix = O.vel(N).to_matrix(N)

mass = sp.symbols('m')

I_xx, I_yy, I_zz = sp.symbols('I_xx, I_yy, I_zz')
body_inertia_dyadic = me.inertia(S, ixx=I_xx, iyy=I_yy, izz=I_zz)

body_central_inertia = (body_inertia_dyadic, O)

body = me.RigidBody('Rigid body', masscenter=O, frame = S,
                      mass=mass, inertia=body_central_inertia)

fx, fy, fz, mx, my, mz = sp.symbols('f_x f_y f_z m_x m_y m_z')
force_vector = fx*S.x + fy*S.y + fz*S.z
torque_vector = mx*S.x + my*S.y + mz*S.z
force = (O, force_vector)
torque = (S, torque_vector)


kinematical_differential_equations = [x0.diff() - velocity_matrix[0],
                                      y0.diff() - velocity_matrix[1],
                                      z0.diff() - velocity_matrix[2],
                                      phi.diff() - phi1d,
                                      theta.diff() - theta1d,
                                      psi.diff() - psi1d,
                                     ]

coordinates = [x0, y0, z0, phi, theta, psi]
speeds = [u, v, w, phi1d, theta1d, psi1d]
kane = me.KanesMethod(N, coordinates, speeds, kinematical_differential_equations)

loads = [force,
         torque]

bodies = [body]
fr, frstar = kane.kanes_equations(bodies, loads)

constants = [I_xx, I_yy, I_zz,mass]

specified = [fx, fy, fz, mx, my, mz]  # External force/torque

right_hand_side = generate_ode_function(kane.forcing_full, coordinates,
                                        speeds, constants,
                                        mass_matrix=kane.mass_matrix_full,specifieds=specified)


def simulate(t, force_torque, I_xx, I_yy, I_zz, mass, initial_coordinates=[0, 0, 0, 0, 0, 0],
             initial_speeds=[0, 0, 0, 0, 0, 0])->pd.DataFrame:
    """
    Simulate a rigid body in 6 degrees of freedom under the influence of external torque and forces applied in the body
    reference frame

    :param t: time vector
    :param force_torque: External force and torque: [fx, fy, fx, mx, my, mz] applied in the body
        reference frame

    :param I_xx: roll inertia [kg*m^2]
    :param I_yy: pitch inertia [kg*m^2]
    :param I_zz: yaw inertia [kg*m^2]
    :param mass: mass of body [kg]
    :param initial_coordinates: [x0, y0, z0, phi, theta, psi]
    :param initial_speeds: [u, v, w, phi1d, theta1d, psi1d]  Where u, v w are speeds in ship fixed system
    :return: Pandas data frame with time series.
    """

    start = np.array(initial_coordinates + initial_speeds)

    numerical_specified = force_torque

    numerical_constants = np.array([I_xx, I_yy, I_zz, mass])

    df = pd.DataFrame(index=t)
    y = odeint(right_hand_side, start, t, args=(numerical_specified, numerical_constants))

    for i, symbol in enumerate(coordinates + speeds):
        name = symbol.name
        df[name] = y[:, i]

    return df



