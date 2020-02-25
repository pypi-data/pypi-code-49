import os
import re
import pickle
from numpy import argmax
import pandas as pd

class LodeStarData():

    STANDARD_SIGNALS = {
        'torque' : ['tob'],
        'rpm' : ['rpmacc'],
        'wob' : ['wob'],
        'moment' : ['bobmag']
    }
    
    MAX_TIME_DEC = 4

    def __init__(self, filename, stack_order=None, date_parser=None, write_pickle=True):
        if self._came_from_pickle is False: #pylint:disable=access-member-before-definition
            self.filename = filename
            self.name = os.path.splitext(os.path.split(filename)[-1])[0]
            self.torque = []
            self.rpm = []
            self.wob = []
            self.moment = []
            self.stack_order = stack_order
            self.units = {}
            self._came_from_pickle = False

            # Read the csv file
            self.data = pd.read_csv(filename, sep=',', parse_dates=[0], date_parser=date_parser, infer_datetime_format=True)

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
            
            # Write the pickle file
            if write_pickle is True:
                pickle_filename = os.path.join(os.path.dirname(filename), '.' + os.path.splitext(os.path.split(filename)[-1])[0] + '.pkl')
                with open(pickle_filename, 'wb') as fid:
                    pickle.dump(self, fid)
    
    def __new__(cls, *args, **kwargs):
        """Overriden to look for a pickle file in the same directory as `:arg:filename` with the filename .`:arg:filename`.pkl.
        
        Parameters
        ----------
        filename : str
            Filename of lodestar data
        
        Returns
        -------
        LodeStarData
            The instantiated `:class:LodeStarData` object.

        """
        if len(args) == 0 or not os.path.isfile(os.path.join(os.path.dirname(args[0]), '.' + os.path.splitext(os.path.split(args[0])[-1])[0] + '.pkl')):
            inst = super().__new__(cls)
            inst._came_from_pickle = False
        
        else:
            pickle_filename = os.path.join(os.path.dirname(args[0]), '.' + os.path.splitext(os.path.split(args[0])[-1])[0] + '.pkl')        
            with open(pickle_filename, 'rb') as fid:
                inst = pickle.load(fid)
            inst._came_from_pickle = True
        
        return inst
    
    def slice_at_indices(self, i_start, i_end, shift_time=True):
        """Returns a `:class:LodeStarData` object sliced at the provided times
        
        Parameters
        ----------
        i_start : int
            Index to start the slice at.
        i_end : int
            Index to end the slice at.
        
        Returns
        -------
        LodeStarData
            Sliced `:class:LodeStarData` object.

        """
        return _SlicedLodeStarData(self, i_start, i_end, shift_time=shift_time)

    def slice_at_times(self, t_start, t_end, shift_time=True):
        """Returns a `:class:LodeStarData` object sliced at the provided times
        
        Parameters
        ----------
        t_start : float
            Time to start the slice at.
        t_end : float
            Time to end the slice at.
        
        Returns
        -------
        LodeStarData
            Sliced `:class:LodeStarData` object.

        """
        i_start = self.time.index(list(filter(lambda i: i >= t_start, self.time))[0])
        i_end = self.time.index(list(filter(lambda i: i >= t_end, self.time))[0])
        return self.slice_at_indices(i_start, i_end, shift_time=shift_time)

class _SlicedLodeStarData(LodeStarData):
    def __init__(self, lodestar_data, i_start, i_end, shift_time=True):        
        self.filename = lodestar_data.filename
        self.wob = lodestar_data.wob[i_start:i_end+1]
        self.rpm = lodestar_data.rpm[i_start:i_end+1]
        self.torque = lodestar_data.torque[i_start:i_end+1]
        self.moment = lodestar_data.moment[i_start:i_end+1]
        self.time = lodestar_data.time[i_start:i_end+1]
        self.units = lodestar_data.units
        self.stack_order = lodestar_data.stack_order
        
        self.data = lodestar_data.data.iloc[i_start:i_end+1]

        # Zero time signal
        if shift_time is True:
            self.data.index = self.data.index - self.data.index[0]
            self.time = self.time - self.time[0]
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

def combine_with_pason(lodestar_dataframe, pason_dataframe, pickle_file=None):
    """Combine a pandas `:obj:DataFrame` containing Lodestar data with a pandas `:obj:DataFrame` containing Pason Data.
    
    Parameters
    ----------
    lodestar_dataframe : DataFrame
        pandas `:obj:DataFrame` containing Lodestar data 
    pason_dataframe : DataFrame
        pandas `:obj:DataFrame` containing Pason Data.
    pickle_file : str (Optional)
        If given, resulting dataframe will be pickled.  
        
    Returns
    -------
    DataFrame
        Compined pandas `:obj:DataFrame`

    """
    # Combine the dataframe
    combined_dataframe = pason_dataframe.join(lodestar_dataframe, how='outer')
    combined_dataframe = combined_dataframe.apply(pd.Series.interpolate, args=('time',))
    combined_dataframe = combined_dataframe.fillna(method='backfill')

    # Build the pickle filename
    start_time_string = combined_dataframe.index[0].strftime('%Y%m%d_%H%M%S')
    end_time_string = combined_dataframe.index[-1].strftime('%Y%m%d_%H%M%S')
    sample_rate_string = '{:1.2f}'.format(1/(combined_dataframe.index[1] - combined_dataframe.index[0]).total_seconds()).replace('.', 'p')

    # If requested, pickle the dataframe if it isn't already pickled
    if pickle_file is not None:
        
        # Raise an error if the file already exists
        if os.path.isfile(pickle_file) is True:
            raise FileExistsError(f'{pickle_file}  was not written because it already exists!')
        
        # Pickle the file
        combined_dataframe.to_pickle(pickle_file)

    return combined_dataframe
