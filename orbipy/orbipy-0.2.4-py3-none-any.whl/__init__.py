# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 13:36:50 2018

@author: stasb
"""

__name__ = "orbipy"

from .models import (crtbp3_model, 
                     crtbp3_custom_model)

from .model_builder import crtbp3_model_builder

from .integrators import (dop853_integrator, 
                          dopri5_integrator, 
                          quasi_integrator)

from .events import *
from .plotter import plotter, plottable, point
from .scaler import scaler
from .mapper import mapper

from . import lines

from .stepper import (stepper, 
                      iteration_printer)

from .extrapolator import (const_extrapolator, 
                           linear_extrapolator, 
                           quadratic_extrapolator, 
                           cubic_extrapolator)

from .interpolators import (linear_interpolator,
                            log_interpolator,
                            ABab_mapper,
                            flipX_interpolator,
                            flipY_interpolator,
                            chain_interpolator)

from .directions import (x_direction,
                         y_direction,
                         xy_angle_direction, 
						 yz_angle_direction,
                         velocity_direction, 
                         unstable_direction,
                         unstable_direction_stm)

from .corrections import (border_correction, 
                          max_time_correction)

from .station_keeping import (simple_station_keeping,
                              strict_station_keeping,
                              montecarlo_station_keeping)

from .manifold import manifold

from .diff_corr import differential_correction

from .multiprocessor import mp