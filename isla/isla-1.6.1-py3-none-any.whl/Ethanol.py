import numpy as np

from .Fuel import Fuel

# ignore numpy errors
np.seterr(divide='ignore', invalid='ignore')


class Ethanol(Fuel):
    """Base class for ethanol.

    Parameters
    ----------
    blend : float
        Volume fraction of biodiesel in petroleum diesel
    den_eth : float
        Mass per liter [kg/L] of ethnaol.
    den_pet : float
        Mass per liter [kg/L] of petroleum diesel.
    lhv_eth : float
        Lower heating value [MJ/kg] of ethanol.
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
        self, blend=0.1, den_eth=0.789, den_pet=0.850,
        lhv_eth=26.7, lhv_pet=43, cost=1, fl_infl=0.03, cost_ret=0
    ):
        """Initializes the base class."""

        # calculate lhv and density
        w_eth = den_eth*blend/(den_eth*blend+den_pet*(1-blend))
        lhv = w_eth*lhv_eth+(1-w_eth)*lhv_pet
        den = den_eth*blend+den_pet*(1-blend)

        # initialize base class
        super().__init__(
            cost, fl_infl, den, lhv, cost_ret,
            'Ethanol', '#000000', False
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
