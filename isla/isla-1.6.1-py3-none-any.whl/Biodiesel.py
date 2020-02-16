import numpy as np

from .Fuel import Fuel

# ignore numpy errors
np.seterr(divide='ignore', invalid='ignore')


class Biodiesel(Fuel):
    """Base class for biodiesel blended fuel.

    Parameters
    ----------
    blend : float
        Volume fraction of biodiesel in petroleum diesel
    den_bio : float
        Mass per liter [kg/L] of biodiesel.
    den_pet : float
        Mass per liter [kg/L] of petroleum diesel.
    lhv_bio : float
        Lower heating value [MJ/kg] of biodiesel.
    lhv_pet : float
        Lower heating value [MJ/kg] of petroleum diesel.
    cost : float or callable
        Cost per unit [$/L] of fuel. Can be a callable function that returns
        fuel cost starting from year zero to end of project lifetime.
    fl_infl : float
        Inflation rate of fuel.

    cost_ret : float or callable
        Savings per unit [$/u] of fuel produced. Can be a callable function
        that returns fuel cost starting from year zero to end of project
        lifetime.

    """

    def __init__(
        self, blend=0.2, den_bio=0.880, den_pet=0.850,
        lhv_bio=39, lhv_pet=43, cost=1, fl_infl=0.03, cost_ret=0
    ):
        """Initializes the base class."""

        # calculate lhv and density
        w_bio = den_bio*blend/(den_bio*blend+den_pet*(1-blend))
        lhv = w_bio*lhv_bio+(1-w_bio)*lhv_pet
        den = den_bio*blend+den_pet*(1-blend)

        # initialize base class
        super().__init__(
            cost, fl_infl, den, lhv, cost_ret,
            'Biodiesel', '#000000', False
        )

    def _rec_fl(self, fl_rec, hr):
        """Records fuel use at a specified time step.

        Parameters
        ----------
        fl_rec : ndarray
            Fuel use [u] to be recorded.
        hr : int
            Time [h] in the simulation.

        """

        # default
        super()._rec_fl(fl_rec, hr)
