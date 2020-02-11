import numpy as np

from .LoadComponent import LoadComponent

# ignore numpy errors
np.seterr(divide='ignore', invalid='ignore')


class DesalLoad(LoadComponent):
    """Reverse osmosis desalination plant module.

    Notes
    -----
    This module models only the power [kW] demand of the desalination plant. A
    DesalSink and DesalStorage module should also be initialized to model the
    desalination power sink and water storage respectively.

    """

    def __init__(self, data, **kwargs):
        """Initializes the base class."""

        # initialize component
        super().__init__(
            data, 0.0, 0.0, 0.0, 0.0,
            None, None, 'DesalLoad', '#666666',
            20.0, 0.0, False, False, False, True, **kwargs
        )

        # initialize dataset
        self.water = 0

        # adjustable Monte-Carlo parameters
        self.var_dy = kwargs.pop('var_dy', 0)
        self.var_hr = kwargs.pop('var_hr', 0)
        self.seed = kwargs.pop('seed', 42)  # random number seed

        # derivable Monte-Carlo parameters
        np.random.seed(self.seed)
        varh_arr = np.random.normal(0, self.var_hr, 8760)
        vard_arr = np.repeat(np.random.normal(0, self.var_dy, 365), 24)
        self.pert_arr = 1+vard_arr+varh_arr

        # update initialized parameters if essential data is complete
        self._update_init()

    def load_derive(self):
        """Derives energy parameters from dataset.

        Returns
        -------
        pow_max : ndarray
            Maximum power in the load.
        enr_tot : ndarray
            Total power in the load.

        Notes
        -----
        This function can be modified by the user.

        """
        return (np.zeros(self.num_case), np.zeros(self.num_case))

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
        return self.pow

    def update_init(self):
        """Updates other parameters once essential parameters are complete.

        """
        # extract dataset
        self.water = self.pert_arr*self._data_proc('water', True)
