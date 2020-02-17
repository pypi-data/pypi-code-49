""" Provides the DataQuality and EvalData class

DataQuality provides a data structure for storing the quality of LF data
EvalData provides a set of evaluation methods for determining the quality of
data stored in an LFData object
"""

from configparser import ConfigParser
import numpy as np
from sklearn.linear_model import LinearRegression
import lf


class DataQuality(object):

    """ Store quality metrics for LF Data"""

    def __init__(self):
        """ Initilize quality metrics to None """
        metrics = [
            "total_time_off",
            "longest_time_off",
            "time_under_threshold",
            "full_day",
            "tx_on",
            "phase_slope",
            "phase_yint",
        ]
        for metric in metrics:
            setattr(self, metric, None)


class EvalLF(object):

    """ Evaluate the quality of LF Data"""

    def __init__(self, lf_data, config=None):
        """ Initiliaze config file if supplied

        Parameters
        ----------
        lf_data : LFData
            Object containing one path of data
        config : str
            Path to config file with quality rules
        """
        self.data = lf_data
        if config is not None:
            self.load_config(config)
        else:
            self.config = None
        self.quality = DataQuality()

    def load_config(self, config):
        """ Load a config into the object

        Parameters
        ----------
        config : str
            Path to config file

        """
        self.config = ConfigParser()
        self.config.read(config)

    def eval_receiver(self):
        """ Determine the quality of the receiver

        Returns
        -------
        TODO

        """
        if hasattr(self.data, "amp_lin"):
            amp_data = self.data.amp_lin
        elif hasattr(self.data, "amp_db"):
            amp_data = self.data.amp_db
        else:
            self.data.to_amp_phase()
            amp_data = self.data.amp_lin
        if hasattr(self.data, "phase_deg"):
            phase_data = self.data.phase_deg
        elif hasattr(self.data, "phase_rad"):
            phase_data = self.data.phase_rad
        off_time_amp = lf.utils.repeatedNans(amp_data) / self.data.Fs
        off_time_phase = lf.utils.repeatedNans(phase_data) / self.data.Fs
        if off_time_amp != off_time_phase:
            print("Amplitude and phase data differ in off time. Please Verify")
        else:
            self.quality.total_time_off = np.sum(off_time_phase)
            self.quality.max_time_off = np.max(off_time_phase)

    def eval_amp(self):
        """ Evaluate the amplitude data

        Returns
        -------
        Float
            Time under the desired threshold
        """
        if self.config is not None:
            threshold = float(self.config["EvalInfo"]["AmplitudeThreshold"])
        else:
            threshold = 10.0
        if hasattr(self.data, "amp_lin") or hasattr(self.data, "amp_db"):
            data = self.data.to_db()
        else:
            self.data.to_amp_phase()
            data = self.data.to_db()
        # Remove Nans
        data = data[np.invert(np.isnan(data))]
        low_signal = data[data < threshold]
        time_under_threshold = len(low_signal) / self.data.Fs
        self.quality.time_under_threshold = time_under_threshold
        return self.quality.time_under_threshold

    def eval_phase(self):
        """ Determine whether the phase is ramping

        Returns
        -------
        TODO

        """
        if hasattr(self.data, "phase_rad") or hasattr(self.data, "phase_deg"):
            data = self.data.to_deg()
        else:
            self.data.to_amp_phase()
            data = np.copy(self.data.to_deg())
        # Replace Nans with value on either side
        idx = lf.utils.findNans(data)
        if idx is not None:
            for start, stop in zip(idx[::2], idx[1::2]):
                # Prefer value before nan string unless at beginning of array
                if start == 0:
                    data[range(start, stop)] = data[stop]
                else:
                    data[range(start, stop)] = data[start - 1]
        # Fit linear model to determine slope
        time = np.linspace(0, 24, len(data)).reshape((-1, 1))
        unwrapped = np.unwrap(data)
        model = LinearRegression().fit(time, unwrapped)
        self.quality.phase_slope = model.coef_
        self.quality.phase_yint = model.intercept_
