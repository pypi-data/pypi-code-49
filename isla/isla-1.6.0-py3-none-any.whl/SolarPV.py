import numpy as np
from scipy.special import gamma, betaincinv, erf
from scipy.optimize import fsolve

from .IntermittentComponent import IntermittentComponent

# ignore numpy errors
np.seterr(divide='ignore', invalid='ignore')


class SolarPV(IntermittentComponent):
    """Photovoltaic (PV) solar plant module.
    Parameters
    ----------
    data : dict or ndarray
        Dataset. Pass a dict with 'ghi' as the key for the hourly GHI [kW/m^2]
        and 'temp' for the hourly ambient temperature [K] (optional).
        Temperature effects will be neglected if no temperature data is given.
        If only an ndarray is given, it will be assumed to be the the hourly
        GHI.
    lat : float
        Latitude [deg] of the location of the PV plant.
    eff : float
        Derating factor of the PV panels.
    track : int
        Indicates tracking. Set to '0' for no tracking (fixed axis) or '1' for
        horizontal axis tracking.
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
    rad_stc : float
        Radiance [kW/m^2] on the PV panel under standard test conditons (STC).
        Equal to 1 kW/m^2.
    temp_stc : float
        Temperature [K] at STC. Equal to 25 deg C.
    temp_cf : float
        Temperature coefficient of performance [/K].
    temp_noct : float
        Nominal operating cell temperature (NOCT) [K]. Equal to 47 deg C.
    temp_nocta : float
        Ambient temperature at NOCT [K]. Equal to 20 deg C.
    rad_noct : float
        Radiance [kW/m^2] at NOCT. Equal to 0.8 kW/m^2.
    mp_stc : float
        Maximum power point efficiency at STC.
    trabs : float
        Product of solar transmittance and solar absorptance.
    tol : float
        Tolerance in GHI calculations.
    """

    def __init__(
        self, data, lat, eff=0.8, track=0,
        capex=1200.0, opex_fix=25.0, opex_var=0.0, opex_use=0.0,
        life=20.0, fail_prob=0.0083, is_fail=False, **kwargs
    ):
        """Initializes the base class."""

        # initialize base class
        super().__init__(
            data, capex, opex_fix, opex_var, opex_use,
            'Solar', '#FFCC00', None, None,
            life, fail_prob, is_fail, True, True, False,
            **kwargs
        )

        # get PV plant parameters
        self.lat = lat
        self.eff = eff
        self.track = track

        # initialize datasets
        self.ghi = None
        self.temp_amb = None

        # adjustable PV plant parameters
        self.rad_stc = kwargs.pop('rad_stc', 1)
        self.temp_stc = kwargs.pop('temp_stc', 298.15)
        self.temp_cf = kwargs.pop('temp_cf', -5e-3)
        self.temp_noct = kwargs.pop('temp_noct', 320.15)
        self.temp_nocta = kwargs.pop('temp_nocta', 293.15)
        self.rad_noct = kwargs.pop('rad_noct', 0.8)
        self.mp_stc = kwargs.pop('mp_stc', 0.13)
        self.trabs = kwargs.pop('trabs', 0.9)
        self.albedo = kwargs.pop('albedo', 0.07)
        self.tol = kwargs.pop('tol', 1e-5)

        # initialize PV plant parameters
        self.rad_tilt = np.array([])
        self.temp_cell = np.array([])
        self.pow_unit = np.array([])

        # initialize Monte-Carlo parameters
        self.ghi_pin = None
        self.temp_pin = None

        # adjustable Monte-Carlo parameters
        self.ac_dy = kwargs.pop('ac_dy', 0.29)
        self.var_dy = kwargs.pop('var_dy', 0.2)
        self.ac_hr = kwargs.pop('ac_hr', 0.54)
        self.seed = kwargs.pop('seed', 42)  # random number seed

        # update initialized parameters if essential data is complete
        self._update_init()

    def get_pow(self, n):
        """Returns the power output [kW] at the specified time [h].
        Parameters
        ----------
        n : int
            Time [h] in the simulation.
        Returns
        -------
        pow : ndarray
            Power [kW] at the current timestep.
        Notes
        -----
        This function can be modified by the user.
        """
        return self.size*self.pow_unit[n]*np.ones(self.num_case)

    def _irrad_calc(self, ghi):
        """Calculates the irradiation on a tilted surface.
        Parameters
        ----------
        ghi : ndarray
            Global horizontal irradiance [kW/m^2] on the PV plant.
        """
        # convert to radians
        lat = np.deg2rad(self.lat)

        # generate list of days
        days = np.linspace(0, self.nt*self.dt/24, num=self.nt, endpoint=False)

        # calculate declination
        dec = np.deg2rad(23.45*np.sin(2*np.pi*(284+days)/365))

        # generate list of solar times
        sol_time = 24*np.mod(days, 1)

        # generate hour angle
        hang = np.deg2rad(15*(sol_time-12))

        # determine PV slope
        if self.track == 1:
            slp = np.arctan(
                (
                    -np.sin(dec)*np.cos(lat) +
                    np.cos(dec)*np.sin(lat)*np.cos(hang)
                ) /
                (np.sin(dec)*np.sin(lat)+np.cos(dec)*np.cos(lat)*np.cos(hang))
            )
        else:
            slp = lat

        # calculate cosine of angle of incidence
        cos_inc = np.cos(np.arccos(
            np.sin(dec)*np.sin(lat)*np.cos(slp) -
            np.sin(dec)*np.cos(lat)*np.sin(slp) +
            np.cos(dec)*np.cos(lat)*np.cos(slp)*np.cos(hang) +
            np.cos(dec)*np.sin(lat)*np.sin(slp)*np.cos(hang) - self.tol
        ))

        # calculate zenith angle
        cos_zen = np.cos(lat)*np.cos(dec)*np.cos(hang)+np.sin(lat)*np.sin(dec)

        # calculate extraterrestrial radiation
        g_on = 1.367*(1+0.033*np.cos(2*np.pi*days/365))
        g_o = g_on*cos_zen

        # calculate average ET radiation
        hang_shift = np.append(hang[1:], hang[0])
        rad_et = 12/np.pi*g_on*(
            np.cos(lat)*np.cos(dec)*(np.sin(hang_shift)-np.sin(hang)) +
            (hang_shift-hang)*np.sin(lat)*np.sin(dec)
        )

        # clearness index
        k = self.ghi/rad_et

        # get ratio between diffuse and total GHI
        def diff_ratio(k):

            # remove negative values
            k = np.minimum(k, 0)

            # classify as low, med, high
            low = k <= 0.22
            high = k > 0.8
            med = np.logical_not(np.logical_or(low, high))

            # calc diffusion ratio
            dr = (
                (1-0.09*k)*low +
                0.165*high +
                (0.9511-0.1604*k+4.388*k**2-16.638*k**3+12.336*k**4)*med
            )

            return dr

        # get diffuse and beam components
        rad_diff = self.ghi*diff_ratio(k)
        rad_beam = self.ghi-rad_diff

        # calculate ratio of beam on tilted to horizontal
        r = cos_inc/cos_zen

        # calculate anisotropy index
        a = rad_beam/rad_et

        # calculate cloudiness
        f = np.sqrt(rad_beam/self.ghi)

        # calculate irradiance on tilted surface
        rad_surf = (
            (rad_beam+rad_diff*a)*r +
            rad_diff*(1-a)*(1+np.cos(slp))/2*(1+f*np.sin(slp/2)**3) +
            self.ghi*self.albedo*(1-np.cos(slp))/2
        )

        # remove negative answers
        rad_surf[rad_surf < 0] = 0

        # convert nans to zero
        self.rad_tilt = np.nan_to_num(rad_surf)

    def _temp_calc(self):
        """Calculates the cell temperature [K]."""

        # calculate the cell temperature [K]
        a = (self.temp_noct-self.temp_nocta)*(self.rad_tilt/self.rad_noct)
        b = 1-self.mp_stc*(1-self.temp_cf*self.temp_stc)/self.trabs
        c = self.temp_cf*self.mp_stc/self.trabs

        # calculate cell temperature [K]
        self.temp_cell = (self.temp_amb+a*b)/(1+a*c)

    def mc_prof(self, mo_ave, k_tu=0.9, k_tl=0):
        """Generate a synthetic profile from monthly data.

        Parameter
        ---------
        mo_ave : ndarray
            Monthly average values.

        Returns
        -------
        hr_synth : ndarray
            Synthetic hourly data.

        """

        # set random seed
        np.random.seed(self.seed)

        def sol_calc(lat):
            """Returns the cosine of the zenith angle and ET adiation."""

            # calculate zenith angle
            lat = np.deg2rad(lat)
            days = np.linspace(0, 365, num=8760, endpoint=False)
            dec = np.deg2rad(23.45*np.sin(2*np.pi*(284+days)/365))
            sol_time = 24*np.mod(days, 1)
            hang = np.deg2rad(15*(sol_time-12))
            cos_zen = (
                np.cos(lat)*np.cos(dec)*np.cos(hang) +
                np.sin(lat)*np.sin(dec)
            )

            # calculate extraterrestrial radiation
            g_on = 1.367*(1+0.033*np.cos(2*np.pi*days/365))
            g_o = g_on*cos_zen

            # calculate average ET radiation
            hang_shift = np.append(hang[1:], hang[0])
            rad_et = 12/np.pi*g_on*(
                np.cos(lat)*np.cos(dec)*(np.sin(hang_shift)-np.sin(hang)) +
                (hang_shift-hang)*np.sin(lat)*np.sin(dec)
            )

            return (cos_zen, rad_et)

        def k_daily(k_mo, ac_dy, var_dy, k_min=0.05, k_max=0.8):

            def gamma_tz(g, k_ave, k_min, k_max):
                """Equation to set to zero to solve for gamma."""
                num = (k_min-1/g)*np.exp(g*k_min)-(k_max-1/g)*np.exp(g*k_max)
                den = np.exp(g*k_min)-np.exp(g*k_max)
                return num/den-k_ave

            def day_expand(t_ser):
                """Expand monthly data into daily data."""
                day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                expand = np.array([])
                for i, d in enumerate(day):
                    expand = np.append(expand, np.repeat(t_ser[i], d))
                return expand

            # generate random numbers
            w_arr = np.random.normal(0, var_dy, 366)

            # generate daily time series
            x_arr = np.append(w_arr[0], np.zeros(365))
            for i in range(365):
                x_arr[i+1] = ac_dy*x_arr[i]+w_arr[i+1]
            x_arr = x_arr[1:]

            # calculate f values
            f_arr = 0.5+0.5*erf(x_arr/np.sqrt(2))

            # solve for gammma
            g_mo = fsolve(gamma_tz, np.full(12, 0.5), (k_mo, k_min, k_max))
            g_arr = day_expand(g_mo)

            # solve for k
            f_den = np.exp(g_arr*k_min)-np.exp(g_arr*k_max)
            k_day = np.log(np.exp(g_arr*k_min)-f_arr*f_den)/g_arr

            return k_day

        def mo_average(t_ser):
            """Monthly average of yearlong data."""

            # days per month
            day_mo = 24*np.cumsum(
                [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], dtype=int
            )

            # loop
            ave_mo = []
            for x1, x2 in zip(day_mo[:-1], day_mo[1:]):
                ave_mo.append(np.average(t_ser[x1:x2])) 
            ave_mo = np.array(ave_mo)

            return ave_mo

        # solve for angles
        cos_zen, rad_et = sol_calc(self.lat)

        # get average monthly clearness index
        k_mo = mo_ave/mo_average(rad_et)

        # calculate k_lm
        k_day = np.repeat(k_daily(mo_ave, self.ac_dy, self.var_dy), 24)
        am = 1/cos_zen  # air mass
        lm = k_day-1.167*k_day**3*(1-k_day)
        ep = 0.979*(1-k_day)
        kp = 1.141*(1-k_day)/k_day
        k_tm = lm+ep*np.exp(-kp*am)
        k_tm[am < 0] = lm[am < 0]

        # calculate std dev of random comp
        sd_a = 0.16*np.sin(np.pi*k_day/0.9)

        # generate random numbers
        w_arr = np.random.normal(0, (1-self.ac_hr**2), 8761)
        b_arr = np.append(w_arr[0], np.zeros(8760))
        for i in range(8760):
            b_arr[i+1] = self.ac_hr*b_arr[i]+w_arr[i+1]
        b_arr = b_arr[1:]

        # transform beta to alpha values
        u_bar = (k_tm-k_tl)/(k_tu-k_tl)
        sd_u = sd_a/(k_tu-k_tl)
        p = u_bar**2*(1-u_bar)/sd_u**2-u_bar
        q = p*(1-u_bar)/u_bar
        f_arr = 0.5+0.5*erf(b_arr/np.sqrt(2))
        u_arr = betaincinv(p, q, f_arr)

        # get GHI
        k = u_arr*(k_tu-k_tl)+k_tl
        ghi_yr = k*rad_et
        ghi_yr[ghi_yr < 0] = 0
        ghi_yr[am < 0] = 0

        return ghi_yr

    @staticmethod
    def exp_curve(yr, yr_0=2020, **kwargs):
        """Experience curve for Solar PV.
        Returns the cost [USD/kW] at the given year
        Parameters
        ----------
        yr : int
            Index of the year.
        yr_0 : int
            Year where index is set to zero.
        """
        # get regression parameters
        a_sat = kwargs.pop('a_sat', 200)
        a_base = kwargs.pop('a_base', 1)
        r = kwargs.pop('r', 0.328)
        a = kwargs.pop('a', 5282)
        b = kwargs.pop('b', 0.376)

        # calculate cost [USD/kWh]
        cap = a_sat/(1+(a_sat-a_base)/a_base*np.exp(-r*(yr+(yr_0-2004))))
        cost = a*cap**(-b)

        return cost

    def update_init(self):
        """Updates other parameters once essential parameters are complete."""

        # extract dataset
        self.ghi = self._data_proc('ghi', True, self.ghi_pin)
        self.temp_amb = self._data_proc('temp', False, self.temp_pin)

        # convert dataset to 1D array
        self.ghi = np.ravel(self.ghi)
        if self.temp_amb is not None:
            self.temp_amb = np.ravel(self.temp_amb)

        # calculate irradiance [kW/m^2] on tilted surface
        self._irrad_calc(self.ghi)

        # check if temperature effects are to be considered
        temp_fc = 1  # temperature factor
        if self.temp_amb is not None:  # use temp effects

            # calculate temperature [K] of PV cells
            self._temp_calc()

            # redefine temperature factor
            temp_fc = 1+self.temp_cf*(self.temp_cell-self.temp_stc)

        # calcualate power per kW size over a year
        self.pow_unit = self.eff*(self.rad_tilt/self.rad_stc)*temp_fc
