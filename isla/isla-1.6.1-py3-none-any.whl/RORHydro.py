import os

import numpy as np
import pandas as pd
from scipy.stats import rankdata, norm
from scipy.interpolate import InterpolatedUnivariateSpline

from .IntermittentComponent import IntermittentComponent

# ignore numpy errors
np.seterr(divide='ignore', invalid='ignore')


class RORHydro(IntermittentComponent):
    """Run-of-the-river hydro power plant module.

    Parameters
    ----------
    data : dict or ndarray
        Dataset. Pass a dict with 'vl_flow' as the key for the hourly water
        flow [m3/h] for one year. An ndarray can be passed as well.
    eff : str or float
        Type of turbine. Choose between 'crossflow', 'francis', 'kaplan',
        'pelton', and 'propeller'. Default is 'francis'.
        Enter a number for fixed efficiency.
    capex : float or callable
        Capital expenses [$/kW(h)]. Depends on size. Can be a callable
        function that returns capital cost starting from year zero to end of
        project lifetime.
    opex_fix : float or callable
        Fixed yearly operating expenses [$/kW(h) yr]. Depends on size. Can be
        a callable function that returns the fixed operating cost starting
        from year zero to end of project lifetime.
    opex_var : float or callable
        Variable yearly operating expenses [$/kWh yr]. Depends on energy
        produced. Can be a callable function that returns the variable
        operating cost starting from year zero to end of project lifetime.
    opex_use : float or callable
        Variable yearly operating expenses [$/h yr]. Depends on amount of
        usage. Can be a callable function that returns the variable
        operating cost starting from year zero to end of project lifetime.
    life : float
        Lifetime [y] of the component.
    fail_prob : float
        Probability of failure of the component.
    is_fail : bool
        True if failure probabilities should be simulated.

    Other Parameters
    ----------------
    repex : float or callable
        Replacement costs [$/kW(h)]. Depends on size. Equal to CapEx by
        default. Can be a callable function that returns replacement costs
        starting from year zero to end of project lifetime.
    num_case : int
        Number of scenarios to simultaneously simulate. This is set by the
        Control module.
    size : int
        Size of the component [kW]. This is set by the Control module.

    References
    ----------
    ..[1] Ozbay, A. et. al., "Interference of wind turbines with different
        yaw angles of the upstream wind turbine," 42nd AIAA Fluid Dynamics\
        Conference and Exhibit, 2012.

    """

    def __init__(
        self, data, head, eff='francis',
        capex=3500.0, opex_fix=35.0, opex_var=0.0, opex_use=0.0,
        life=20.0, fail_prob=0.01, is_fail=False, **kwargs
    ):
        """Initializes the base class."""

        # initialize component
        super().__init__(
            data, capex, opex_fix, opex_var, opex_use,
            'RunoffHydro', '#0066CC', None, None,
            life, fail_prob, is_fail, True, True, False, **kwargs
        )

        # read datasets
        dir = os.path.dirname(__file__)
        turb_eff = pd.read_csv(
            os.path.join(dir, 'hydro_eff.csv'), index_col=None
        ).values

        # initialize dataset
        self.vl_flow = 0
        self.eff_prof = 0

        # initialize hydro plant parameters
        self.pow_unit = np.array([])

        # get hydro parameters
        self.head = head
        self.eff = eff  # type of turbine

        # derivable wind plant parameters
        turb_list = ['crossflow', 'francis', 'kaplan', 'pelton', 'propeller']
        if eff in turb_list:
            ind = turb_list.index(eff)+1
            self.eff_func = InterpolatedUnivariateSpline(
                turb_eff[:, 0], turb_eff[:, ind], k=1, ext='zeros'
            )
        else:
            self.eff_func = lambda x: eff*np.ones_like(x)

        # initialize Monte-Carlo parameters
        self.spd_pin = None
        self.dir_pin = None

        # adjustable Monte-Carlo parameters
        self.ac = kwargs.pop('ac', 0.8717)  # autocorrelation factor
        self.di = kwargs.pop('di', 0.2418)  # diurnal strength
        self.t_max = kwargs.pop('t_max', 14)  # time of maximum wind speed
        self.seed = kwargs.pop('seed', 42)  # random number seed

        # update initialized parameters if essential data is complete
        self._update_init()

    def get_pow(self, n):
        """Returns the power output [kW] at the specified time [h].

        Parameters
        ----------
        n : int
            Time in the simulation.

        Returns
        -------
        pow : ndarray
            Power [kW] at the current timestep.

        Notes
        -----
        This function can be modified by the user.

        """
        # calculate fraction of max vol flow
        vf = self.vl_flow[n]*9.81*self.head/self.size
        vf = np.minimum(vf, 1)

        # calculate power
        pow = self.eff_func(vf)*9.81*self.head*self.vl_flow[n]
        pow = np.minimum(pow, self.size)

        return pow*np.ones(self.num_case)

    def update_init(self):
        """Updates other parameters once essential parameters are complete."""

        # extract dataset
        self.vl_flow = self._data_proc('vl_flow', True)  # flowrate [m3/h]
