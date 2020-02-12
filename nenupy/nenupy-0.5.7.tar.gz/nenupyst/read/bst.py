#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Alan Loh'
__copyright__ = 'Copyright 2020, nenupy'
__credits__ = ['Alan Loh']
__maintainer__ = 'Alan Loh'
__email__ = 'alan.loh@obspm.fr'
__status__ = 'WIP'
__all__ = ['BST']


import numpy as np 
import warnings
import astropy.units as u

from .util import NenuFAR_Obs, SpecData


# ============================================================= #
# ---------------------------- BST ---------------------------- #
# ============================================================= #
class BST(NenuFAR_Obs):
    """
    """
    def __init__(self, bst):
        super().__init__(bst)
        self.bstfile = self.fitsfile
        self.track_beam = None
        self.pointing = 0
        self.polar = None
        self.freq = None
        self.time = None
        self._keywords = [
            'track_dbeam',
            'pointing',
            'freq',
            'time',
            'polar']

    # ------------------------- Setter -------------------------#
    @property
    def bstfile(self):
        """ Path toward the NenuFAR BST FITS file.
        """
        return self._bstfile
    @bstfile.setter
    def bstfile(self, b):
        assert 'beamlet' in self._meta['hea']['Object'],\
            '{} is not a BST file.'.format(b)
        self._read_bst(bst=b)
        self._bstfile = b
        return

    @property
    def pointing(self):
        """ Pointing beam index selection

            Parameters
            ----------
            pointing: int or mask_array
                If an `int` is given, it is understood as the index
                of pointing (e.g. one particular numerical beam in a tracking).
                If a `mask_array` is given, it is understood as a condition
                upon the numerical beams (e.g. `(self.dbeams==0)` to select
                all the pointings corresponding to the numerical beam index 0).
        """
        return self._digibeams[self._pointing]
        # return self._pointing
    @pointing.setter
    def pointing(self, b):
        if isinstance(b, int):
            assert b < self._n_points,\
                'Maximum beam index is {}'.format(self._n_points-1)
            tmp_b = np.zeros(self._digibeams.size, dtype=bool)
            #tmp_b[ self._digibeams == b ] = True ## 
            tmp_b[b] = True
            b = tmp_b
        else:
            b = np.array(b)
            if b.dtype == bool:
                assert b.size == self._n_points,\
                    'Provide a mask array of size {}'.format(self._n_points)
            else:
                assert np.all(np.array(b) < self._n_points),\
                    'Some indices are greater than {}'.format(self._n_points)
        self._pointing = b
        return

    @property
    def polar(self):
        """ Polarization selection.
            Could be 'NE' or 'NW' 
        """
        return self._polar
    @polar.setter
    def polar(self, p):
        if p is None:
            p = 'NW'
        p = p.upper()
        assert p in self._meta['ins']['spol'],\
            'Polarization should be NE or NW'
        obs_pols = self._meta['ins']['spol'].ravel()
        self._pmask = (obs_pols == p)
        self._polar = obs_pols[self._pmask]
        return

    @property
    def time(self):
        """ Time selection, must be given in ISO/ISOT format.
        """
        self._tmask = np.ones(self.times.size, dtype=bool)
        self._tmask *= (
            (self.times >= self.beam_start[0]) &\
            (self.times <= self.beam_stop[-1])
            )

        if self._time.size == 2:
            if (self._time[0] > self.beam_stop[-1]) or\
                (self._time[1] < self.beam_start[0]):
                pass 
            else:
                self._tmask *= (
                    (self.times >= self._time[0]) &\
                    (self.times <= self._time[1])
                    )
        else:
            if (self._time[0] > self.beam_stop[-1]) or\
                (self._time[0] < self.beam_start[0]):
                pass 
            else:
                self._tmask *= (
                    (self.times >= self._time[0]) |\
                    (self.times <= self._time[0])
                    )
            idx = (np.abs(self.times - self._time[0])).argmin()
            self._tmask[idx] = True
        
        return self.times[self._tmask]
    @time.setter
    def time(self, t):
        if t is None:
            t = [self.obs_start, self.obs_stop]
        t = np.array([t], dtype='datetime64').ravel()
        assert t.size <= 2,\
            'time attribute must be of size 2 maximum.'
        for ti in t:
            assert (self.obs_start <= ti) &\
                (ti <= self.obs_stop),\
                '{} not within {} -- {}'.format(
                        ti,
                        self.obs_start,
                        self.obs_stop)
        if t.size == 2:
            assert t[0] < t[1],\
            '{} should be before {}.'.format(t[0], t[1])
        self._time = t
        return

    @property
    def freq(self):
        """ Frequency selection in MHz
        """
        freqs = self._meta['bea']['freqlist'][self.db] * u.MHz
        if len(freqs.shape) == 2:
            freqs = freqs[0, :]
        self._fmask = np.zeros(freqs.size, dtype=bool)
        if self._freq.size == 2:
            idx1 = (np.abs(freqs - self._freq[0])).argmin()
            idx2 = (np.abs(freqs - self._freq[1])).argmin()
            self._fmask[idx1:idx2+1] = True
        else:
            idx = (np.abs(freqs - self._freq[0])).argmin()
            self._fmask[idx] = True
        selected_freq = freqs[self._fmask]
        # Shift the mask accordingly to the db index
        self._fmask = np.roll(
            self._fmask,
            self._meta['bea']['BeamletList'][self.db][0]
            )
        return selected_freq
    @freq.setter
    def freq(self, f):
        if f is None:
            f = self.freq_min.value
        # Convert to scalar if `Quantity` are entered
        if isinstance(f, list):
            f = [fi.value if isinstance(fi, u.Quantity) else fi for fi in f]
            f = sorted(f)
        else:
            f = [f.value] if isinstance(f, u.Quantity) else [f]
        f = np.array(f) * u.MHz
        assert f.size <= 2,\
            'freq attribute must be of size 2 maximum.'
        for i, fi in enumerate(f):
            if self.freq_min > fi:
                warnings.warn(
                    '\nWarning: {} < {}, setting to fmin.'.format(
                        fi,
                        self.freq_min
                        )
                    )
                f[i] = self.freq_min.copy()
            if self.freq_max < fi:
                warnings.warn(
                    '\nWarning: {} > {}, setting to fmax.'.format(
                        fi,
                        self.freq_max
                        )
                    )
                f[i] = self.freq_max.copy()
        self._freq = f
        return

    @property
    def track_dbeam(self):
        """ Choose one numerical beam index to follow
        """
        return self._track_dbeam
    @track_dbeam.setter
    def track_dbeam(self, t):
        if t is not None:
            self.pointing = self._digibeams == t
        self._track_dbeam = t
        return    


    # ------------------------- Getter -------------------------#
    @property
    def obs_start(self):
        """ First time record
        """
        return self.times[0]

    @property
    def obs_stop(self):
        """ Last time record
        """
        return self.times[-1]

    @property
    def beam_start(self):
        """ Start of the selected numerical pointing
        """
        start = self._meta['pbe']['timestamp'][self._pointing]
        start = np.array(
            [s.replace('Z', '') for s in start],
            dtype='datetime64[s]')
        return start

    @property
    def beam_stop(self):
        """ End of the selected numerical pointing
        """
        stop = self._meta['pbe']['timestamp'][np.roll(self._pointing, 1)]
        stop = np.array(
                [s.replace('Z', '') for s in stop],
                dtype='datetime64[s]')
        for i, s in enumerate(stop):
            if s <= self.beam_start[0]:
                stop[i] = self.obs_stop
        # if not self._pointing[-1]:
        #     # Last element is False: don't go to the last timestamp
        #     stop = self._meta['pbe']['timestamp'][np.roll(self._pointing, 1)]
        #     # if not isinstance(stop, str):
        #     #     stop = stop[-1]
        #     # stop = np.datetime64(stop.replace('Z', ''), 's')
        #     stop = np.array(
        #         [s.replace('Z', '') for s in stop],
        #         dtype='datetime64[s]')
        # else:
        #     stop = self.obs_stop
        # for i, s in enumerate(stop):
        #     if s <= self.beam_start:
        #         stop[i] = self.obs_stop
        return stop

    @property
    def duration(self):
        """ Duration of the selected beam
        """
        return self.beam_stop - self.beam_start

    @property
    def freq_min(self):
        """ Minimum observed frequency in MHz
        """
        freqs = self._meta['bea']['freqlist'][self.db]
        fmin = freqs[freqs > 0].min()
        return fmin * u.MHz

    @property
    def freq_max(self):
        """ Maximum observd frequency in MHz
        """
        f_max = self._meta['bea']['freqlist'][self.db].max()
        return f_max * u.MHz

    @property
    def db(self):
        """ Corresponding numerical beam index
        """
        return self._meta['pbe']['noBeam'][self._pointing][0]

    @property
    def ab(self):
        """ Corresponding analogic beam
        """
        return self._dig2ana[self.db]
    

    @property
    def azana(self):
        """ Pointed azimuth in degrees
            for the analog beam
        """
        a_mask = self._ana_start >= self.beam_start
        a_mask *= self._ana_stop <= self.beam_stop
        # a_mask = self.abeams == np.unique(self.ab)
        az = self.all_azana[a_mask]
        return az * u.deg

    @property
    def elana(self):
        """ Pointed elevation in degrees
            for the analog beam
        """
        a_mask = self._ana_start >= self.beam_start
        a_mask *= self._ana_stop <= self.beam_stop
        # a_mask = self.abeams == np.unique(self.ab)
        el = self.all_elana[a_mask]
        return el * u.deg

    @property
    def azdig(self):
        """ Pointed azimuth in degrees
            for the numerical beam
        """
        az = self.all_azdig[self._pointing]
        return az * u.deg

    @property
    def eldig(self):
        """ Pointed elevation in degrees
            for the numerical beam
        """
        el = self.all_eldig[self._pointing]
        return el * u.deg


    @property
    def ma(self):
        """ Mini-array used
        """
        n = self._meta['ana']['nbMRUsed'][self.ab]
        return self._meta['ana']['MRList'][self.ab, :n]


    @property
    def ma_position(self):
        """ Positions of mini-arrays
        """
        pos = self._meta['ins']['noPosition']
        pos = pos.reshape((pos.size//3, 3))
        return pos[self.ma]


    @property
    def ma_rotation(self):
        """ Rotations of mini-arrays
        """
        rot = self._meta['ins']['rotation']
        rot = rot[0]
        return rot[self.ma]
    

    # ------------------------- Method -------------------------#
    def select(self, **kwargs):
        """ Select and load BST data.
            
            Parameters
            ----------

            beam : int
                Beam index.

            freq : (float, array_like)
                Frequency selection in MHz.
                Single frequency:
                    `>>> freq=55`
                Frequency range selection:
                    `>>>freq=[20, 30]`

            time : (str or array_like)
                Time selection in ISO/ISOT format.
                Single time selection:
                    `>>> time='2019-08-07 12:00:00'`
                Time range selection:
                    `>>> time=['2019-08-07 12:00:00', '2019-08-07 13:00:00']`

            polar : str
                Polarization selection


            Returns
            -------

            data : SpecData
                Selected data are loaded and stored in the `data` attribute.
                This is a `SpecData` object.
        """
        for key in self._keywords:
            if key in kwargs.keys():
                self.__setattr__(key, kwargs[key])

        self.data = SpecData(
            time=self.time,
            freq=self.freq,
            polar=self.polar,
            data=self._alldata[np.ix_(self._tmask,
                self._pmask,
                self._fmask)]
            )
        return self.data


    def to_stmoc(self):
        """ Method to create a CDS STMOC from the current BST observation.
        """
        # self._meta['pbe']['timestamp']
        # self.all_azdig
        # self.all_eldig
        return


    def fit_transit(self, data=None):
        """ After a data selection (via `select()`),
            this performs a gaussian fitting.

            Example
            -------
            ```
            >>> from BST_v2 import BST
            >>> import matplotlib.pyplot as plt
            >>> b = BST('filename_BST.fits')
            >>> data = b.select(freq=50, pointing=0)
            >>> fit = b.fit_transit()
            >>> plt.plot(data.time, data.db, label='raw')
            >>> plt.plt(fit.time, fit.db, label='fitted')
            >>> plt.legend()
            >>> plt.show()
            ```
        """
        # import matplotlib.pyplot as plt
        from scipy.optimize import curve_fit
        def gauss(x, a, x0, sigma):
            return a * np.exp(-(x - x0)**2 / (2 * sigma**2))
        def linear(x, a, b):
            return a * x + b

        # Remove data spikes
        if data is None:
            if self.freq.size > 1:
                filtered_data = self.data.fmean(method='median', clean=True).amp
            else:
                filtered_data = self.data.filter(kernel=31).amp 
        else:
            assert isinstance(data, SpecData),\
                'data must be of type SpecData'
            if data.freq.size > 1:
                filtered_data = data.fmean(method='median', clean=True).amp
            else:
                filtered_data = data.filter(kernel=31).amp
        main_time = self.data.time

        # plt.figure()
        # plt.plot(self.data.time, filtered_data, label='raw')

        # Subtract a linear fit to the data prior to searching for max
        filtered_data_to_fit = filtered_data/filtered_data.max()
        popt_lin, pcov_lin = curve_fit(
            f=linear,
            xdata=self.data.jd,
            ydata=filtered_data_to_fit,
            p0=[0, filtered_data_to_fit.min()] # estimated parameters after normalization
            )
        # plt.plot(self.data.time, linear(self.data.jd, *popt_lin)*filtered_data.max(), label='fit lin')

        # Find the highest amplitude point
        # this should roughly be the transit source
        ind_max = np.argmax(filtered_data - linear(self.data.jd, *popt_lin))

        # Just consider a reduced time interval to fit a gaussian
        # +/- 15 min from the maximum
        dt = np.timedelta64(5, 'm')
        t_mask = main_time >= main_time[ind_max] - dt
        t_mask *= main_time <= main_time[ind_max] + dt
        
        # Data to fit
        time = self.data.jd[t_mask]
        data = filtered_data[t_mask]
        # Normalize them, which helps the fit
        t_fit = (time - np.median(time)) / (time - np.median(time)).max()
        d_fit = (data - data.min()) / (data - data.min()).max()
        
        # Perform the fit
        popt, pcov = curve_fit(
            f=gauss,
            xdata=t_fit,
            ydata=d_fit,
            sigma=np.ones(d_fit.size)*0.1,
            absolute_sigma=True,
            p0=[1, 0, 1] # estimated parameters after normalization
            )

        # Show the fitted data and rescale them
        d_rescaled = gauss(t_fit, *popt) * (data - data.min()).max() + data.min()

        # t_fit_extended = (self.data.jd - np.median(time)) / (time - np.median(time)).max()
        # d_rescaled_extended = gauss(t_fit_extended, *popt) * (data - data.min()).max() + data.min()


        # plt.plot(main_time[t_mask], d_rescaled, label='fit gauss')
        # plt.show()

        fit = SpecData(
            time=main_time[t_mask],
            freq=np.mean(self.freq),
            polar=self.polar,
            data=d_rescaled.reshape(d_rescaled.size, 1, 1)
            )

        # fit_extended = SpecData(
        #     time=main_time,
        #     freq=self.freq,
        #     polar=self.polar,
        #     data=d_rescaled_extended.reshape(d_rescaled_extended.size, 1, 1)
        #     )

        # plt.savefig('/Users/aloh/Desktop/Angular_Shift_2019_July/{}.png'.format(self.pointing[0]))
        # plt.close('all')

        peak_amp = popt[0] * (data - data.min()).max() + data.min()
        peak_t = popt[1] * (time - np.median(time)).max() + np.median(time)
        return fit, peak_amp, peak_t#, popt[2]

    def fit_transit_v0(self, data=None):
        """ After a data selection (via `select()`),
            this performs a gaussian fitting.

            Example
            -------
            ```
            >>> from BST_v2 import BST
            >>> import matplotlib.pyplot as plt
            >>> b = BST('filename_BST.fits')
            >>> data = b.select(freq=50, pointing=0)
            >>> fit = b.fit_transit()
            >>> plt.plot(data.time, data.db, label='raw')
            >>> plt.plt(fit.time, fit.db, label='fitted')
            >>> plt.legend()
            >>> plt.show()
            ```
        """
        from scipy.optimize import curve_fit
        def gauss(x, a, x0, sigma):
            return a * np.exp(-(x - x0)**2 / (2 * sigma**2))

        # Remove data spikes
        if data is None:
            filtered_data = self.data.filter(kernel=31).amp
        else:
            assert isinstance(data, SpecData),\
                'data must be of type SpecData'
            filtered_data = data.filter(kernel=31).amp
        main_time = self.data.time

        # Find the highest amplitude point
        # this should roughly be the transit source
        ind_max = np.argmax(filtered_data)

        # Just consider a reduced time interval to fit a gaussian
        # +/- 15 min from the maximum
        dt = np.timedelta64(5, 'm')
        t_mask = main_time >= main_time[ind_max] - dt
        t_mask *= main_time <= main_time[ind_max] + dt
        
        # Data to fit
        time = self.data.jd[t_mask]
        data = filtered_data[t_mask]
        # Normalize them, which helps the fit
        t_fit = (time - np.median(time)) / (time - np.median(time)).max()
        d_fit = (data - data.min()) / (data - data.min()).max()
        
        # Perform the fit
        popt, pcov = curve_fit(
            f=gauss,
            xdata=t_fit,
            ydata=d_fit,
            sigma=np.ones(d_fit.size)*0.1,
            absolute_sigma=True,
            p0=[1, 0, 1] # estimated parameters after normalization
            )

        # Show the fitted data and rescale them
        d_rescaled = gauss(t_fit, *popt) * (data - data.min()).max() + data.min()

        fit = SpecData(
            time=main_time[t_mask],
            freq=self.freq,
            polar=self.polar,
            data=d_rescaled.reshape(d_rescaled.size, 1, 1)
            )

        return fit


    def _read_bst(self, bst):
        """ Low-level BST reader, mainly used to parse beam informations.
        """
        self.abeams = self._meta['ana']['NoAnaBeam']
        self._n_anapoints = self._meta['ana']['NbPointingAB']
        self.dbeams = self._meta['bea']['noBeam']
        self._n_digpoints = self._meta['bea']['NbPointingB']
        self._dig2ana = self._meta['bea']['NoAnaBeam']
        self._n_points = np.sum(self._n_digpoints)

        self._anabeams = self._meta['pan']['noAnaBeam']
        self.all_azana = self._meta['pan']['AZ']
        self.all_elana = self._meta['pan']['EL']
        self._digibeams = self._meta['pbe']['noBeam']
        self.all_azdig = self._meta['pbe']['AZ']
        self.all_eldig = self._meta['pbe']['EL']

        self._ana_start = np.array(
            self._meta['pan']['timestamp'].replace('Z', ''),
            dtype='datetime64[s]'
            )
        self._ana_stop = np.append(self._ana_start[1:],
            self.times[-1].astype('datetime64[s]'))

        return
# ============================================================= #

