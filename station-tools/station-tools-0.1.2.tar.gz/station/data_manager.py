import os
import datetime
from pytz import utc
import glob
import pandas as pd
import logging
logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO)

class DataManager:
    """Utility for managing CTT Sensor Station data files"""
    beep_pattern = '*-data*'
    gps_pattern = '*-gps*'
    health_pattern = '*-node*'

    def __init__(self):
        """initialize data frames for beep data, node health data, and gps data"""
        self.beep_data = None
        self.health_data = None
        self.gps_data = None

    def load_data(self, directory_name):
        """load data files from a directory that contains all the compressed (or uncompressed) data files straight off the station"""
        # load beep data
        path = '{}{}{}'.format(directory_name, os.path.sep, self.beep_pattern)
        beep_files = glob.glob(path)
        dfs_to_merge = []
        logging.info('preparing {:,} beep files for merge from {}'.format(len(beep_files), path))
        for filename in sorted(beep_files):
            if filename.find('node') == -1:
                # only process if node is not part of the pattern ...
                logging.info('merging file: {}'.format(filename))
                try:
                    df = pd.read_csv(filename)
                except pd.errors.EmptyDataError:
                    logging.info('ignoring file {} - no data'.format(filename))
                df['Time'] = pd.to_datetime(df['Time'])
                dfs_to_merge.append(df)
        if len(dfs_to_merge) > 0:
            self.beep_data = pd.concat(dfs_to_merge, axis=0).sort_values('Time')
        else:
            logging.info('no beep files found in directory')
        
        path = '{}{}{}'.format(directory_name, os.path.sep, self.health_pattern)
        node_health_files = glob.glob(path)
        dfs_to_merge = []
        logging.info('preparing {:,} node health files for merge'.format(len(node_health_files)))
        for filename in sorted(node_health_files):
            logging.info('merging file: {}'.format(filename))
            try:
                df = pd.read_csv(filename)
            except pd.errors.EmptyDataError:
                logging.info('ignoring file {} - no data'.format(filename))

            df['Time'] = pd.to_datetime(df['Time'])
            dfs_to_merge.append(df)
        if len(dfs_to_merge) > 0:
            self.health_data = pd.concat(dfs_to_merge, axis=0).sort_values('Time')
        else:
            logging.info('no node health files found in directory')


        path = '{}{}{}'.format(directory_name, os.path.sep, self.gps_pattern)
        gps_files = glob.glob(path)
        dfs_to_merge = []
        logging.info('preparing {:,} gps files for merge'.format(len(gps_files)))
        for filename in sorted(gps_files):
            logging.info('merging file: {}'.format(filename))
            try:
                df = pd.read_csv(filename)
            except pd.errors.EmptyDataError:
                logging.info('ignoring file {} - no data'.format(filename))

            df['recorded at'] = pd.to_datetime(df['recorded at'])
            dfs_to_merge.append(df)
        if len(dfs_to_merge) > 0:
            self.gps_data = pd.concat(dfs_to_merge, axis=0).sort_values('recorded at')
        else:
            logging.info('no gps files found in directory')
    
    def export_data(self, begin=None, end=None, tags=None):
        """export loaded data into output merged files stamped with current time the script is run
            specify begin and end dates to only export data between a set of dates
        """
        now = datetime.datetime.utcnow()
        beeps = self.beep_data
        health = self.health_data
        gps = self.gps_data
        if begin is not None:
            if beeps is not None:
                beeps = beeps[beeps.Time > begin]
            if health is not None:
                health = health[health.Time > begin]
            if gps is not None:
                gps = gps[gps['recorded at'] > begin]
        if end is not None:
            if beeps is not None:
                beeps = beeps[beeps.Time < end]
            if health is not None:
                health = health[health.Time < end]
            if gps is not None:
                gps = gps[gps['recorded at'] < end]

        if beeps is not None:
            outfilename = 'station-beep-data.merged.{}.csv'.format(now.strftime('%Y-%m-%d_%H%M%S'))
            beeps.to_csv(outfilename, index=False)
        if health is not None:
            outfilename = 'station-health-data.merged.{}.csv'.format(now.strftime('%Y-%m-%d_%H%M%S'))
            health.to_csv(outfilename, index=False)
        if gps is not None:
            outfilename = 'station-gps-data.merged.{}.csv'.format(now.strftime('%Y-%m-%d_%H%M%S'))
            gps.to_csv(outfilename, index=False)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('expected a command line argument to specify the directory')
        sys.exit(-1)
    directory_name = sys.argv[1]

    manager = DataManager()
    manager.load_data(directory_name)

    # you can export data during a time window by specifying begin and end dates during export
    begin = datetime.datetime(2019,11,1).replace(tzinfo=utc)
    end = datetime.datetime(2019,11,7).replace(tzinfo=utc)
    #manager.export_data(begin=begin, end=end)
    manager.export_data()