"""Module for working with Pason Data

"""
import re
from dateutil.parser import parse
from datetime import timedelta

from thornpy.signal import low_pass
from scipy.signal import resample, find_peaks
from numpy import gradient, absolute, mean, std
import pandas as pd

class PasonData():
    """Object representing a Pason dataset.

    Examples
    --------
    Referring to the rpm by the :attr:`rpm` attribute

        >>> filename = 'pason.csv'
        >>> pason_data = PasonData(filename)
        >>> pason_data.rpm[1000:1002]
        [84.95, 83.89]
    
    Refering to the rpm by the standard signal name 'rpm' in the :attr:`data` attribute.

        >>> pason_data.data['rpm'][1000:1002].values
        array([84.95, 83.89])
    
    Refering to the rpm by its name in the referenced .csv file

        >>> pason_data.data['rotary_rpm'][1000:1002].values
        array([84.95, 83.89])
    
    Plotting all the standard signals. NOTE: :mod:`matplotlib.pyplot` is included in the class and can be accessed via `PasonData.plt`

        >>> for signal in PasonData.STANDARD_SIGNALS:
        >>>     pason_data.plt.figure() 
        >>>     plot = pason_data.data[signal].plot())
        >>>     plot.set_ylabel('{} ({})'.format(signal.capitalize(), pason_data.units[signal]))
        >>>     plot.set_xlabel('{} ({})'.format(pason_data.data.index.name, pason_data.units[pason_data.data.index.name]))
        >>>     plot.grid()
        >>> PasonData.plt.show()
        <matplotlib.axes._subplots.AxesSubplot object at 0x000000001C517EF0>

    Attributes
    ----------
    filename : str
        Name of the file from which Pason data was loaded.
    wob : list
        Weight on bit signal
    rpm : list
        Rotary RPM signal
    flow : list
        Mud flow rate signal
    torque : list
        Surface torque signal
    md : list
        Measured depth signal
    rop : list
        Rate of penetration signal
    pressure : list
        Differential pressure signal
    mse : list
        Mechanical specific energy signal
    units : dict
        Dictionary indicicating the units associated with each column in :attr:`data` 
    data : pandas.core.frame.DataFrame
        Pandas DataFrame containing all the data from :attr:`filename`.
    STANDARD_SIGNALS : dict
        Class attribute with standard signal name as keys and lists of expected names in the pason csv files as values.
        
    """
    from matplotlib import pyplot as plt

    STANDARD_SIGNALS = {
        'torque' : ['convertible_torque', 'rotary_torque', 'top_drive_torque'],
        'md' : ['bit_depth'],
        'pressure' : ['differential_pressure'],
        'mse' : ['mechanical_specific_energy'],
        'rop' : ['rate_of_penetration'],
        'rpm' : ['rotary_rpm'],
        'wob' : ['weight_on_bit'],
        'gpm' : ['total_pump_output']
    }

    SETPOINT_FILTER_CUTOFF = .1

    # Prominence and width thresholds for peakfinder
    # NOTE: Smaller numbers = more peaks
    SETPOINT_SIGMA = 4

    # Maximum exptected decimals in timestamp seconds
    MAX_TIME_DEC = 2

    def __init__(self, filename, date_parser=None, motor_factor=None):
        """Initilizes the PasonData object.
        
        Parameters
        ----------
        filename : str
            Name of file from which Pason data will be imported.
        date_parser : function (Optional)
            Function to use to parse dates
        motor_factor : float (Optional)
            Factor to multiply the pressure (units in psi) by to create a motor torque series called 'motor_torque' (units in klbf-ft)
        
        """
        self.filename = filename
        self.wob = []
        self.rpm = []
        self.gpm = []
        self.torque = []
        self.md = []
        self.rop = []
        self.pressure = []
        self.mse = []
        self.units = {}

        # Read the csv file
        self.data = pd.read_csv(filename, sep=',', parse_dates=[[0,1]], date_parser=date_parser)

        # Create a time series and attribute and set it as the index
        self.data['time'] = (self.data[self.data.columns[0]] - self.data[self.data.columns[0]][0]).dt.total_seconds()  
        
        # Round the time signal to get rid of random decimals
        self.data['time'] = self.data['time'].round(decimals=self.MAX_TIME_DEC)
        
        self.time = list(self.data['time'].values)
        self.units['time'] = 'sec'
        self.data.set_index('time', inplace=True)

        # Get new column names and units
        name_map = {}        
        for col_name in self.data:
            # For each column name, parse the name
            [new_col_name, *unit] = [text.strip().replace(' ','_').lower() for text in re.split('[()]', col_name)]
            name_map[col_name] = new_col_name
            
            if unit:
                # If the column name contains units
                # Add to the units dictionary
                self.units[new_col_name] = unit[0]
        
        # Rename the columns
        self.data.rename(columns=name_map, inplace=True)
        
        # Extract standard variables
        for var, expct_col_nms in self.STANDARD_SIGNALS.items():
            # For each standard variable

            # Add uppercase, lowercase, and without underscores
            expct_col_nms = [nm.lower() for nm in expct_col_nms]
            expct_col_nms += [nm.upper() for nm in expct_col_nms]
            expct_col_nms += [nm.replace('_', '') for nm in expct_col_nms]

            for expct_col_nm in expct_col_nms:
                # For each possible pason column name representing the standard variable

                if expct_col_nm in self.data:
                    # If the column name is in the pason data set, copy 
                    # that column to a new dict entry and create
                    # an instance attribute for it.
                    self.data[var] = self.data[expct_col_nm]
                    self.__dict__[var] = list(self.data[expct_col_nm].values)

                    if expct_col_nm in self.units:
                        # If the column has units, add to the units dict
                        self.units[var] = self.units[expct_col_nm]
                    
                    # Break the loop if a match is found
                    # NOTE: The first name in the self.STANDARD_SIGNALS[var] list will be used
                    break
        
        if motor_factor is not None:
            self.data['motor_torque'] = self.data['pressure']*motor_factor
    
    def get_setpoints(self, signal_type, show_plot=True):
        """Gets the setpoints from the rpm or gpm Pason signals.

        Notes
        -----
        This method is experimental.  It is highly recommended to set `show_plot=True` to visually confirm that the extracted setpoints are sensible. This method has been tested on rpm and gpm signals only.  It has not been tested on other types of Pason signals.      

        Setting `show_plot=True` will halt execution until the figure window is closed.

        Parameters
        ----------
        signal_type : str
            'rpm', 'gpm', or 'wob'
        show_plot : bool, optional
            If True, shows a plot of the resulting setpoints (the default is True)        
        
        Returns
        -------
        list
            List of tuples where each tuple contains the setpoint time and setpoint value.
        
        """
        if signal_type not in self.data:
            raise ValueError('signal_type must be a key in self.data')

        signal = self.data[signal_type]

        # Apply a lowpass filter
        filt_sig, _filt_time = low_pass(signal, self.time, self.SETPOINT_FILTER_CUTOFF)

        # Take the derivative of the filtered signal
        deriv_sig = absolute(gradient(filt_sig))

        # Get the n sigma value of the derivative
        n_sigma = std(deriv_sig)*self.SETPOINT_SIGMA

        # Find the peaks of the derivative
        peaks, _props = find_peaks(deriv_sig, height=n_sigma, prominence=n_sigma)

        # Use the peaks to get the setpoint time and value
        def reject_outliers(data, m=1):
            return [d for d in data if abs(d - mean(data)) < m*std(data) or std(data)==0]
        set_points = [(self.time[peak], mean(reject_outliers(signal[peak+1:next_peak-1]))) for peak, next_peak in zip([0]+list(peaks), list(peaks)+[len(self.time)])]

        # Show a plot for confirmation
        if show_plot:
            self.plt.plot(self.time, signal, linewidth=1, marker='.', markersize=3)
            # cls.plt.plot(self.time, deriv_sig)
            # cls.plt.plot([self.time[peak] for peak in peaks], [signal[peak] for peak in peaks], linestyle='None', marker='.', markersize=10)       
            for sp, next_sp in zip(set_points, set_points[1:] + [(self.time[-1], set_points[-1][1])]):
                self.plt.plot([sp[0], next_sp[0]], [sp[1], sp[1]], linewidth=3)  
            self.plt.show()

        return set_points
    
    def slice_at_times(self, t_start, t_end, shift_time=True):
        """Returns a `:class:PasonData` object sliced at the provided times
        
        Parameters
        ----------
        t_start : float
            Time to start the slice at.
        t_end : float
            Time to end the slice at.
        
        Returns
        -------
        PasonData
            Sliced `:class:PasonData` object.

        """
        i_start = self.time.index(list(filter(lambda i: i >= t_start, self.time))[0])
        i_end = self.time.index(list(filter(lambda i: i >= t_end, self.time))[0])
        return self.slice_at_indices(i_start, i_end, shift_time=shift_time)

    def slice_at_indices(self, i_start, i_end, shift_time=True):
        """Returns a `:class:PasonData` object sliced at the provided times
        
        Parameters
        ----------
        i_start : int
            Index to start the slice at.
        i_end : int
            Index to end the slice at.
        
        Returns
        -------
        PasonData
            Sliced `:class:PasonData` object.

        """
        return _SlicedPasonData(self, i_start, i_end, shift_time)

class _SlicedPasonData(PasonData):

    def __init__(self, pason_data, i_start, i_end, shift_time=True):
        
        self.filename = pason_data.filename
        self.wob = pason_data.wob[i_start:i_end+1]
        self.rpm = pason_data.rpm[i_start:i_end+1]
        self.gpm = pason_data.gpm[i_start:i_end+1]
        self.torque = pason_data.torque[i_start:i_end+1]
        self.md = pason_data.md[i_start:i_end+1]
        self.rop = pason_data.rop[i_start:i_end+1]
        self.pressure = pason_data.pressure[i_start:i_end+1]
        self.mse = pason_data.mse[i_start:i_end+1]
        self.time = pason_data.time[i_start:i_end+1]
        self.units = pason_data.units

        self.data = pason_data.data.iloc[i_start:i_end+1]

        # Zero time signal
        if shift_time is True:
            self.data.index = self.data.index - self.data.index[0]
            self.time = self.time - self.time[0]

def pason_post_processing(t, sig):
    """
    Process a signal as it would be processed by pason
    
    This function applies the following processing steps:
        1. Sample at 50 Hz    
        2. Apply a digital low pass filter with a cutoff frequency of 0.99 Hz
        3. Resample at 5 Hz
        4. Calculate maximum over each 1 second period

    Parameters
    ----------
    t : list
        Time series corresponding to the signal to be processed
    
    sig : list
        Signal to be processed
                  
    Returns
    -------
    tuple
        time, processed signal
    """

    def sample(sig, time, freq_samp):                
        num = int((time[-1] - time[0])*freq_samp + 1)
        return resample(sig,num,t)        

    def maximum(sig, time, period):  
        # Number of samples to between taking each maximum
        num = int(period/(time[1]-time[0]))   
        
        # Initialize `time_max` with the starting value of `time`   
        time_max = [time[0]]
        
        # Initilize `sig_max` with zero as a starting value
        sig_max = [0]
        
        counter = 0
        for i, t in enumerate(time):
            if counter == num:
                time_max.append(t)
                sig_max.append(max(sig[i-num:i]))
                counter = 0
            counter += 1

        # Set the first value equal to the second value to make the line look nice
        sig_max[0] = sig_max[1]

        return sig_max, time_max

    # (1) Sample at 50 Hz
    sig_1, t_1 = sample(sig, t, 50)

    # (2) 0.99 Hz Digital Low Pass Filter
    sig_2, t_2 = low_pass(sig_1, t_1, 0.99)

    # (3) resample at 5 Hz
    sig_3, t_3 = sample(sig_2, t_2, 5)

    # (4) calculate maximum over each 1 sec period
    sig_4, t_4 = maximum(sig_3, t_3, 1)

    return t_4, sig_4

def slice_step_tests(pason, step_test_times, include_tagging_bottom=False, expand_forward=None, expand_backward=None):    
    """Slices the step test data out of the pason data
    
    Parameters
    ----------
    pason : PasonData
        `:class:PasonData` object
    step_test_times : list of lists of strs
        list of pairs of date strings containing the start and end times of the slice
    include_tagging_bottom : bool (Optional)
        If True, slices the test starting at the preceeding bottom tag time
    expand_forward : float (Optional)
        Number of seconds to expand slice forward in time
    expand_backward : float (Optional)
        Number of seconds to expand slice backward in time
    
    Returns
    -------
    PasonData
        Sliced `:class:PasonData` object

    """    
    step_tests = []

    for step_test_time in step_test_times:
    
        if include_tagging_bottom is False:
            time_range = step_test_time
        else:
            new_start_time = _backup_to_tag(pason, step_test_time[0])
            time_range = [new_start_time, step_test_time[1]]

        if expand_backward is not None:
            time_range[0] = time_range[0] - timedelta(seconds=expand_backward)
        
        if expand_forward is not None:
            time_range[1] = time_range[1] + timedelta(seconds=expand_forward)
        
        # Slice data
        step_test = pason.slice_at_times(int((pason.data['yyyy/mm/dd_hh:mm:ss'] >= time_range[0]).argmax()), int((pason.data['yyyy/mm/dd_hh:mm:ss'] >= time_range[1]).argmax()))
        step_tests.append(step_test)

    # Delete the unsliced data from memory
    del pason

    return step_tests

def _backup_to_tag(pason, time):
    """Finds the last time that the bit tagged bottom before `time`
    
    Parameters
    ----------
    pason : PasonData
        A `:obj:PasonData` object
    time : datetime
        `:obj:datetime` object representing a time following a bottom tag.
    
    Returns
    -------
    datetime
        `:obj:datetime` object representing the time of the last bottom tag before `time`
    
    Raises
    ------
    UnexpectedData
        Raised if 'bit_depth' or 'hole_depth' aren't in `pason.data`

    """
    if 'bit_depth' not in pason.data.columns or 'hole_depth' not in pason.data.columns:
        raise ValueError(f'{pason.filename} must contain Bit Depth AND Hole Depths to find the last bottom tag!')
    
    i = int((pason.data['yyyy/mm/dd_hh:mm:ss'] >= time).argmax())

    # Make a list of off-bottom values ending at the step test
    off_bottom = pason.data['hole_depth'].iloc[:i] - pason.data['bit_depth'].iloc[:i]

    # Reverse the off bottom signal and find the first non-zero off bottom 
    last_off_bottom_idx = int((off_bottom>1)[::-1].idxmax())

    return pason.data['yyyy/mm/dd_hh:mm:ss'].iloc[last_off_bottom_idx]
