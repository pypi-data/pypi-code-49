"""
ObsPlus instructions for downloading dataset.
"""
from pathlib import Path

import obsplus
import obspy
from obspy.clients.fdsn import Client

from opsdata_sulphur_peak import __version__, source_path


class Sulphur_peak(obsplus.DataSet):
    """
    A 2017 earthquake sequence occurring in southern Idaho.
    """
    name = "sulphur_peak"
    base_path = Path(__file__).parent
    version = __version__
    longitudes = (-111.6, -111.25)
    latitudes = (42.5, 42.7)
    starttime = obspy.UTCDateTime('2017-01-01')
    endtime = obspy.UTCDateTime('2019-01-01')
    min_magnitude = 4.0

    station_search_degrees = 0.5

    # --- functions used to specify how data are downloaded

    def download_events(self):
        """ download event data and store them in self.event_path """
        client = Client("IRIS")
        # Define inputs to event query
        event_params = dict(
            minlongitude=self.longitudes[0],
            maxlongitude=self.longitudes[1],
            minlatitude=self.latitudes[0],
            maxlatitude=self.latitudes[1],
            starttime=self.starttime,
            endtime=self.endtime,
            minmagnitude=self.min_magnitude,  # minimum magnitude
        )
        # Query iris for data and plot
        cat = client.get_events(**event_params)
        # save event to self.event_path
        obsplus.EventBank(self.event_path).put_events(cat)

    def download_waveforms(self):
        """ download waveform data and store them in self.waveform_path """
        client = Client("IRIS")
        NSLC = ['network', 'station', 'location', 'channel']
        # Times before/after origin to include in waveforms
        time_before = 5  # time before origin to download
        time_after = 95  # time after origin to download
        # Since we need to use the inventory and catalog to determine which
        # channels/times to get data for, make sure those are downloaded first.
        if self.events_need_downloading:
            self.download_events()
        if self.stations_need_downloading:
            self.download_stations()
        # Load inventory and catalog into dataframes.
        inv_df = obsplus.stations_to_df(self.station_path)
        cat_df = obsplus.events_to_df(self.event_path)
        # Create bulk requests for each event and put into a wave bank.
        wbank = obsplus.WaveBank(self.waveform_path)
        for _, event_series in cat_df.iterrows():
            event_df = inv_df[NSLC]
            time = obsplus.utils.to_utc(event_series['time'])
            event_df['starttime'] = time - time_before
            event_df['endtime'] = time + time_after
            bulk = obsplus.utils.pd.get_waveforms_bulk_args(event_df)
            st = client.get_waveforms_bulk(bulk)
            wbank.put_waveforms(st)

    def download_stations(self):
        """ download station data and store them in self.station_path """
        station_path = Path(self.station_path)
        station_path.mkdir(exist_ok=True, parents=True)
        client = Client("IRIS")

        station_params = dict(
            starttime=self.starttime,
            endtime=self.endtime,
            latitude=sum(self.latitudes) / 2.,
            longitude=sum(self.longitudes) / 2.,
            maxradius=self.station_search_degrees,  # radius in degrees
            channel='H*',  # only include channels that start with H
            level='response',  # indicates we want instrument responses
        )

        inv = client.get_stations(**station_params)
        inv.write(str(station_path / 'inventory.xml'), 'stationxml')

    # --- properties to specify when data need to be downloaded

    # @property
    # def waveforms_need_downloading(self):
    #     """ Return True if the waveforms should be downloaded """

    # @property
    # def stations_need_downloading(self):
    #     """ Return True if the stations should be downloaded """

    # @property
    # def events_need_downloading(self):
    #     """ Return True if the events should be downloaded """

    # --- functions to return clients

    # @property
    # @lru_cache()
    # def waveform_client(self) -> Optional[WaveBank]:
    #     """ A cached property for a waveform client """

    # @property
    # @lru_cache()
    # def event_client(self) -> Optional[EventBank]:
    #     """ A cached property for an event client """

    # @property
    # @lru_cache()
    # def station_client(self) -> Optional[obspy.Inventory]:
    #     """ A cached property for a station client """

    # --- post download hook

    # def pre_download_hook(self):
    #     """ This code gets run before downloading any data. """

    def post_download(self):
        """ This code get run after downloading all data types. """
        # by default create a file with hash values for each. This will issue
        # a warning if any of the downloaded files change in the future.
        self.create_sha256_hash()
