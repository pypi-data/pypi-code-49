from mlcore.datahelper.oss.oss_data_helper import OSSDataHelper
from datetime import datetime
import json
import os

import sys
import logging

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format='%(asctime)-s %(levelname)-7s %(name)-s.%(funcName)s(): %(message)s',
                    datefmt='%Y-%m-%dT%H:%M:%S')


class RawdataPathHelper():
    def __init__(self, baseprefix='ml/'):
        self.root_dir = '%s%s' % (baseprefix, 'rawdata-workspace')
        self.local_root_dir = 'tmpdata/rawdata-workspace'
    
    def get_rawdata_key(self, name):
        return {
            'vm_list': 'vm-list',
            'vm_nearby': 'vm-nearby',
            'es_rate': 'es-rate',
            'battery_status': 'battery-status'
        }[name]

    def get_vm_list_dirs(self):
        return self.get_dirs_by_name('vm_list')

    def get_vm_nearby_dirs(self):
        return self.get_dirs_by_name('vm_nearby')

    def get_es_rate_dirs(self):
        return self.get_dirs_by_name('es_rate')

    def get_dirs_by_name(self, name):
        key = self.get_rawdata_key(name)
        path = {}
        path['ossfolder'] = '%s/%s/' % (self.root_dir, key)
        path['local_dir'] = '%s/%s/' % (self.local_root_dir, key)
        return path


class ETLPathHelper():

    def __init__(self, baseprefix='ml/'):
        self.root_dir = '%s%s' % (baseprefix, 'etl-workspace')
        self.local_root_dir = 'tmpdata/etl-workspace'

    def get_etl_key(self, etl_name):
        return {
            'battery_status': 'battery-status',
            'battery_swap_log': 'battery-swap-log',
            'vm_battery_count': 'vm-battery-count',
            'vm_battery_count_all': 'vm-battery-count-all',
            'vm_exchange_count': 'vm-exchange-count',
            'vm_status': 'vm-status'
        }[etl_name] 

    def get_battery_swap_log_dirs(self, dt_hour_str):
        etl_key = self.get_etl_key('battery_swap_log')
        return self.get_dirs_by_etl_key(etl_key, dt_hour_str)

    def get_vm_status_dirs(self, dt_hour_str):
        etl_key = self.get_etl_key('vm_status')
        return self.get_dirs_by_etl_key(etl_key, dt_hour_str)

    def get_vm_battery_count_dirs(self, dt_hour_str):
        etl_key = self.get_etl_key('vm_battery_count')
        return self.get_dirs_by_etl_key(etl_key, dt_hour_str)

    def get_vm_exchange_count_dirs(self, dt_hour_str):
        etl_key = self.get_etl_key('vm_exchange_count')
        return self.get_dirs_by_etl_key(etl_key, dt_hour_str)


    def get_dirs_by_etl_key(self, etl_key, dt_hour_str):
        path = {}
        path['ossfolder'] = '%s/%s/dt=%s/' % (self.root_dir, etl_key, dt_hour_str)
        path['local_dir'] = '%s/%s/%s/' % (self.local_root_dir, etl_key, dt_hour_str)

        return path


class DataHelper(OSSDataHelper):

    def __init__(self, config):

        self.config = config['mlcore']['datahelper']['oss']['mllearningdb']
        super().__init__(self.config)
        self.logger = logging.getLogger(self.__class__.__name__)

    def connect(self):
        super().connect()

    #####################################################
    #
    #   rawdata access
    #
    #####################################################

    def write_rawdata_by_path(self, data_dict, rawdata_path):
        # write local file and upload
        self.mkdir(rawdata_path['local_dir'])

        json_data = {}
        json_data['data'] = data_dict
        with open('%s%s' % (rawdata_path['local_dir'], "part00000.parquet"), 'w') as fp:
            json.dump(json_data, fp)
        # upload
        self.upload_folder(rawdata_path['ossfolder'], rawdata_path['local_dir'])
        # remove local file
        self.rmdir(rawdata_path['local_dir'])  


    def write_vm_list(self, data_dict):
        if len(data_dict)==0:
            self.logger.warn('Empty input of vm list')
            return

        self.write_rawdata_by_path(data_dict, RawdataPathHelper().get_vm_list_dirs())

    def write_vm_nearby(self, data_dict):
        if len(data_dict)==0:
            self.logger.warn('Empty input of vm nearby')
            return

        self.write_rawdata_by_path(data_dict, RawdataPathHelper().get_vm_nearby_dirs())

    def write_es_rates(self, data_dict):
        if len(data_dict)==0:
            self.logger.warn('Empty input of es rates')
            return

        self.write_rawdata_by_path(data_dict, RawdataPathHelper().get_es_rate_dirs())


    def get_rawdata_by_path(self, rawdata_path):
        if self.list_objects(prefix=rawdata_path) == []:
            return []

        self.download_folder(rawdata_path['ossfolder'], rawdata_path['local_dir'])

        # read local files
        files = os.listdir(rawdata_path['local_dir'])
        data = None
        for file in files:
            if file[-5:] != '.json' and file[-8:] != '.parquet':
                continue
            local_path = '%s%s' % (rawdata_path['local_dir'], file)
            with open(local_path) as fp:
                json_data = json.load(fp)
                data = json_data['data']

        # remove local files
        self.rmdir(rawdata_path['local_dir'])

        return data

    def get_vm_list(self):
        data = self.get_rawdata_by_path(RawdataPathHelper().get_vm_list_dirs())
        
        self.logger.info('Read %s logs from vm_list' % (len(data)))
        
        if len(data)==0:
            self.logger.warn('Empty vm_list.')
        else:
            self.logger.info('vm_list[0] = %s' % data[0])
        return data

    def get_vm_nearby(self):
        data = self.get_rawdata_by_path(RawdataPathHelper().get_vm_nearby_dirs())

        self.logger.info('Read %s logs from vm_nearby' % (len(data)))
        if len(data)==0:
            self.logger.warn('Empty vm_nearby.')
        else:
            self.logger.info('vm_nearby[0] = %s' % data[0])
        return data

    def get_es_rates(self):
        data = self.get_rawdata_by_path(RawdataPathHelper().get_es_rate_dirs())

        self.logger.info('Read es_rates = %s' % data)
        return data


    #####################################################
    #
    #   ETL access
    #
    #####################################################

    def write_etl_by_path(self, etl_path, data, dt_hour_str):
        # write local file and upload
        self.mkdir(etl_path['local_dir'])
        json_data = {}
        json_data['data'] = data
        with open('%s%s' % (etl_path['local_dir'], "part00000.parquet"), 'w') as fp:
            json.dump(json_data, fp)

        # upload
        self.upload_folder(etl_path['ossfolder'], etl_path['local_dir'])
        # remove local file
        self.rmdir(etl_path['local_dir'])  

    def write_battery_swap_log(self, item_dict_list):
        if (len(item_dict_list))==0:
            self.logger.warn('Empty input of battey swap log')
            return

        # data preprocessing
        dict_dt_hour = {}
        for item_dict in item_dict_list:
            dt_hour_str = self.get_dt_str_by_timestamp(item_dict['exchange_time'])['dt_hour_str']
            if dt_hour_str in dict_dt_hour:
                dict_dt_hour[dt_hour_str].append(item_dict)
            else:
                dict_dt_hour[dt_hour_str] = [item_dict]
        
        # upload data to oss
        for dt_hour_str, item_list in dict_dt_hour.items():

            etl_path = ETLPathHelper().get_battery_swap_log_dirs(dt_hour_str)

            self.logger.info('write %s battery_swap_log in %s' % (len(item_list), dt_hour_str))
            self.write_etl_by_path(etl_path, item_list, dt_hour_str)

    def write_vm_status(self, item_dict_list):
        if (len(item_dict_list))==0:
            self.logger.warn('Empty input of vm status')
            return

        # data preprocessing
        dict_dt_hour = {}
        for item_dict in item_dict_list:
            dt_hour_str = self.get_dt_str_by_timestamp(item_dict['snap_time'])['dt_hour_str']
            if dt_hour_str in dict_dt_hour:
                dict_dt_hour[dt_hour_str].append(item_dict)
            else:
                dict_dt_hour[dt_hour_str] = [item_dict]

        # upload data to oss
        for dt_hour_str, item_list in dict_dt_hour.items():
            etl_path = ETLPathHelper().get_vm_status_dirs(dt_hour_str)

            self.logger.info('write %s vm_status in %s' % (len(item_list), dt_hour_str))
            self.write_etl_by_path(etl_path, item_list, dt_hour_str)

    def write_vm_battery_count(self, data, dt_hour_str):
        if len(data)==0:
            self.logger.warn('Empty input of vm_battery_count')
            return []
            
        etl_path = ETLPathHelper().get_vm_battery_count_dirs(dt_hour_str)
        self.logger.info('write %s vm_battery_count in %s' % (len(data), dt_hour_str))
        self.write_etl_by_path(etl_path, data, dt_hour_str)

    def write_vm_exchange_count(self, data, dt_hour_str):
        if len(data)==0:
            self.logger.warn('Empty input of vm_exchange_count')
            return []
        etl_path = ETLPathHelper().get_vm_exchange_count_dirs(dt_hour_str)
        self.logger.info('write %s vm_exchange_count in %s' % (len(data), dt_hour_str))
        self.write_etl_by_path(etl_path, data, dt_hour_str)

    def get_etl_data_by_path(self, etl_path):
        self.download_folder(etl_path['ossfolder'], etl_path['local_dir'])

        # read local files
        files = os.listdir(etl_path['local_dir'])
        data = None
        for file in files:
            if file[-5:] != '.json' and file[-8:] != '.parquet':
                continue
            local_path = '%s%s' % (etl_path['local_dir'], file)
            with open(local_path) as fp:
                json_data = json.load(fp)
                data = json_data['data']

        # remove local files
        self.rmdir(etl_path['local_dir'])

        return data

    def get_battery_swap_log(self, dt_hour_str):
        etl_path = ETLPathHelper().get_battery_swap_log_dirs(dt_hour_str)
        if etl_path is None or self.list_objects(prefix=etl_path) == []:
            self.logger.warn('No battery_swap_log in %s', dt_hour_str)
            return []

        data = self.get_etl_data_by_path(etl_path)

        if isinstance(data, list)==False:
            data = [data]
        self.logger.info('Read %s logs from battery_swap_log in %s' % (len(data), dt_hour_str))
        self.logger.info('battery_swap_log[0] = %s' % data[0])
        return data

    def get_vm_status(self, dt_hour_str):
        etl_path = ETLPathHelper().get_vm_status_dirs(dt_hour_str)
        if etl_path is None or self.list_objects(prefix=etl_path) == []:
            self.logger.warn('No vm_status in %s', dt_hour_str)
            return []

        data = self.get_etl_data_by_path(etl_path)

        if isinstance(data, list)==False:
            data = [data]
        self.logger.info('Read %s logs from vm_status in %s' % (len(data), dt_hour_str))
        self.logger.info('vm_status[0] = %s' % data[0])
        return data

    
    def get_vm_battery_count(self, dt_hour_str):
        etl_path = ETLPathHelper().get_vm_battery_count_dirs(dt_hour_str)
        if etl_path is None or self.list_objects(prefix=etl_path) == []:
            self.logger.warn('No vm_battery_count in %s', dt_hour_str)
            return []

        data = self.get_etl_data_by_path(etl_path)

        self.logger.info('Read %s logs from vm_battery_count in %s' % (len(data), dt_hour_str))
        #self.logger.info('vm_battery_count.keys() = %s' % list(data.keys()))
        return data 

    def get_vm_exchange_count(self, dt_hour_str):
        etl_path = ETLPathHelper().get_vm_exchange_count_dirs(dt_hour_str)
        if etl_path is None or self.list_objects(prefix=etl_path) == []:
            self.logger.warn('No vm_exchange_count in %s', dt_hour_str)
            return []

        data = self.get_etl_data_by_path(etl_path)

        self.logger.info('Read %s logs from vm_exchange_count in %s' % (len(data), dt_hour_str))
        self.logger.info('vm_exchange_count[0] = %s' % data[0])
        return data 

    #####################################################
    #
    #   general
    #
    #####################################################

    def get_dt_str_by_timestamp(self, timestamp):
        '''
        Return a string format dict by given timestamp
        '''
        dt_str = {}
        dt_str['dt'] = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%S')
        dt_str['dt_hour_str'] = dt_str['dt'][:13]
        dt_str['dt_minute_str'] = dt_str['dt'][:16]
        dt_str['time_str'] = dt_str['dt'][-8:]
        return dt_str