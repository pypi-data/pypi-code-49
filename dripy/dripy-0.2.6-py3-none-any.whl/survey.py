import pandas
from numpy import arange
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from thornpy import plotting

class SurveyData():
    """Stores data from a well survey.
    
    Parameters
    ----------
    filename : str
        Filename of raw survey data file.  Can be in excel format or csv format.
    vendor : str
        Vendor that produced the file.  This determines the expected format of the file.  For options see the keys of :attr:`VENDOR_SETTINGS`.

    Attributes
    ----------
    x : pandas.Series
        x coordinates of wellbore
    y : pandas.Series
        y coordinates of wellbore
    z : pandas.Series
        z coordinates of wellbore
    tvd : pandas.Series
        True vertical depth of wellbore
    md : pandas.Series
        Measured depth of wellbore
    VENDOR_SETTINGS : dict
        Class attribute containing information about how the survey file should be read depending on what vendor provided it.

    """   
    VENDOR_SETTINGS = {
        'leam': {
            'read_settings': {
                'skiprows': list(arange(13)) + [14],
                'header': 0,        
            },
            'column_names': {
                'x': 'N-S ',
                'y': 'E-W ',
                'z': 'TVD',
                'md': 'MD'
            }             
        }
    }

    def __init__(self, filename, vendor='leam', _corva_params=None):

        if _corva_params is None:
            if filename.endswith('.csv'):
                self.data = pandas.read_csv(filename, **self.VENDOR_SETTINGS[vendor]['read_settings'])
            elif filename.endswith('.xls') or filename.endswith('.xlsx'):
                self.data = pandas.read_excel(filename, **self.VENDOR_SETTINGS[vendor]['read_settings'])
            
            self.data.dropna(subset=[self.VENDOR_SETTINGS[vendor]['column_names']['md']], inplace=True)

            self.x = self.data[self.VENDOR_SETTINGS[vendor]['column_names']['x']]
            self.y = self.data[self.VENDOR_SETTINGS[vendor]['column_names']['y']]        
            self.z = self.data[self.VENDOR_SETTINGS[vendor]['column_names']['z']]        
            self.tvd = self.data[self.VENDOR_SETTINGS[vendor]['column_names']['z']]
            self.md = self.data[self.VENDOR_SETTINGS[vendor]['column_names']['md']]
        
        else:


        
    def plot_3d(self, figure=None):
        """Plots the survey data on a 3d
        
        Parameters
        ----------
        figure : matplotlib.figure.Figure, optional
            An existing  (the default is None, which [default_description])
        
        Returns
        -------
        matplotlib.figure.Figure
            3D plot of wellbore

        """
        figure = plotting.plot_3d(x=self.x-self.x[0], y=self.y-self.y[0], z=-self.z, x_label='X (ft)', y_label='Y (ft)', z_label='Z (ft)', figure=figure)

        return figure
