import pandas as pd
import numpy as np
import uuid
import os
import pickle
import gzip
from numba import jit
from .constants import TIME_FREQ


def add_column_datetime(df, totalrows, reference_date, t):
    fr = {1: 'H', 0.5: '30min', 0.25: '15min'}
    freq = fr[t]
    start_date = pd.to_datetime(reference_date)
    drange = pd.date_range(start_date, periods=totalrows, freq=freq)
    df = pd.DataFrame(df.values, columns=df.columns, index=drange)
    df = df.rename_axis('date').copy()
    return df


##############################################################################
# These functions are for charging availability profile creation
##############################################################################
# TODO:
# - CHECK CONSISTSTENCY WITH MORE OPTIONS in function SOC()

# function descriptions pending
class Availability:
    """
        self.__init__(input)
        self.setScenario(charging_data)
        self.setVehicleFeature(battery_capacity, charging_eff)
        self.setBatteryRules(soc_init, soc_min, altern=[])
        self.loadSettingDriving(DataBase)
        self.run()
        self.save_profile(folder, description=' ')
    """

    def __init__(self, input):
        '''
        input: string. File name of input.
        '''
        self.kind = 'availability'
        self.input = input

    def setScenario(self, charging_data):
        '''
        charging_data: dictionary. See example
        eg.

        {'prob_charging_point' :
             {'errands':  {'public':0.3,'none':0.7},
              'escort':   {'public':0.3,'none':0.7},
              'leisure':  {'public':0.3,'none':0.7},
              'shopping': {'public':0.3,'none':0.7},
              'home':     {'public':0.3,'none':0.7},
              'workplace':{'public':0.0,'workplace':0.3,'none':0.7},
              'driving':  {'none':1.0}
              },
        'capacity_charging_point' :
              {'public':11,'home':1.8,'workplace':5.5,'none':0}
        }

        '''
        self.chargingdata = charging_data

    def setVehicleFeature(self, battery_capacity, charging_eff):
        '''
        battery_capacity: int, kWh
        charging_eff: float
        '''
        self.battery_capacity = battery_capacity
        self.charging_eff = charging_eff

    def setBatteryRules(self, soc_init, soc_min, altern=[]):
        '''
        soc_init: float, [0-1]
        soc_min: float, [0-1]
        altern: list, kWh larger than battery_capacity.
        '''
        self.soc_init = soc_init
        self.soc_min = soc_min
        self.storage_altern = altern[:]

    def loadSettingDriving(self, DataBase):
        '''
        DataBase: object DataBase(). see example,
        eg. manager = DataBase(dir)
            "manager" is a class instance that contains the profiles

        Then, the following attributes can be called
            self.df
            self.t
            self.totalrows
            self.hours
            self.freq
            self.refdate
            self.energy_consumption
            self.states
        '''
        if DataBase.db[self.input]:
            if DataBase.db[self.input]['kind'] == 'driving':
                self.df = DataBase.db[self.input]['profile'].copy()
                self.t = DataBase.db[self.input]['t']
                self.totalrows = DataBase.db[self.input]['totalrows']
                self.hours = DataBase.db[self.input]['hours']
                self.freq = TIME_FREQ[self.t]['f']
                self.refdate = DataBase.db[self.input]['refdate']
                self.energy_consumption = DataBase.db[self.input]['energy_consumption']
                self.states = DataBase.db[self.input]['states']
            else:
                raise ValueError('The driving profile {} can not be found in the database'.format(self.input))
        else:
            raise ValueError('The driving profile {} can not be found in the database'.format(self.input))

    def initial_conf(self):
        self.prob_charging_point = self.chargingdata['prob_charging_point']
        self.capacity_charging_point = self.chargingdata['capacity_charging_point']
        self.name = self.input + '_avai_' + uuid.uuid4().hex[0:5]

    def ChooseChargingPoint(self, state):
        self.chrg_points = [key for key in self.prob_charging_point[state].keys()]
        self.prob = [val for val in self.prob_charging_point[state].values()]
        self.rnd_name = np.random.choice(self.chrg_points, p=self.prob)
        return self.rnd_name

    def fill_rows(self):
        self.repeats = ['hr', 'state', 'charging_point', 'charging_cap']
        self.fixed = ['distance', 'consumption']
        self.copied = ['departure', 'last_dep', 'purpose', 'duration', 'weekday', 'person']
        self.calc = ['dayhrs']
        self.same = []

        self.dt = pd.DataFrame(columns=self.db.columns)
        self.dt.loc[:, 'hh'] = np.arange(0, self.hours, self.t)
        self.idx = self.dt[self.dt['hh'].isin(self.db['hr'].tolist())].index.tolist()
        self.mixed = self.repeats + self.fixed + self.copied
        for r in self.mixed:
            self.val = self.db[r].values.tolist()
            self.dt.loc[self.idx, r] = self.val
        self.dt.loc[self.totalrows-1, 'state'] = self.db['state'].iloc[-1]
        self.dt.loc[self.totalrows-1, 'hr'] = self.dt['hh'][self.totalrows-1]
        self.rp = self.dt[::-1].reset_index(drop=True)
        self.rp.loc[:, self.repeats] = self.rp[self.repeats].fillna(method='ffill')
        self.rp.loc[:, self.fixed] = self.rp[self.fixed].fillna(0)
        self.dt = self.rp[::-1].reset_index(drop=True)
        for sm in self.same:
            self.dt.loc[:, sm] = self.db[sm].values.tolist()[0]
        for cal in self.calc:
            self.dt.loc[:, cal] = self.dt['hh'].apply(lambda x: x % 24)

    def drawing_soc(self):
        numpy_array = self.dt[['consumption', 'charging_cap']].values.T
        self.dt.loc[:, 'soc'] = self.soc(self.charging_eff, self.battery_capacity, self.soc_init, *numpy_array, self.t)

    @staticmethod
    @jit(nopython=True)
    def soc(charging_eff, battery_capacity, soc_init, consumption, charging_cap, t):
        '''
        state of charge of battery
        '''
        soc = np.empty(consumption.shape)
        for i in range(soc.shape[0]):
            if i == 0:
                zero = soc_init
                current_soc = zero - consumption[i]/battery_capacity + charging_cap[i]*t*charging_eff/battery_capacity
                if current_soc > 1:
                    soc[i] = 1
                else:
                    soc[i] = current_soc
            else:
                zero = soc[i-1]
                current_soc = zero - consumption[i]/battery_capacity + charging_cap[i]*t*charging_eff/battery_capacity
                if current_soc > 1:
                    soc[i] = 1
                else:
                    soc[i] = current_soc
        return soc

    def testing_soc(self):
        self.failed_chrg = self.dt[self.dt['soc'] < self.soc_min].copy()
        if self.failed_chrg.empty:
            if self.dt['soc'].iloc[-1] >= self.soc_init:
                self.soc_end = round(self.dt['soc'].iloc[-1], 3)
                print('soc_init:', round(self.soc_init, 3), '--> soc_end:', self.soc_end)
                self.success = 'True'
                self.ready = True
            else:
                self.drivlist = self.dt[self.dt['state'] == 'driving'].index.to_list()[::-1]
                self.len = len(self.dt)
                for ix in self.drivlist:
                    self.dt.loc[ix, 'consumption'] = 0.0
                    self.drawing_soc()
                    if self.dt['soc'].iloc[-1] >= self.soc_init:
                        break
                self.new_len = len(self.dt[:ix])
                self.proportion_ts_modified = round(self.new_len/self.len, 3)
                if self.dt['soc'].iloc[-1] >= self.soc_init:
                    self.stored_n += 1
                    self.stored_success_prop.append(self.proportion_ts_modified)
                    self.stored_success.append(self.dt.copy())
                    if self.stored_n == 3:
                        self.dt = self.stored_success[max(enumerate(self.stored_success_prop), key=lambda tup: tup[1])[0]].copy()
                        self.proportion_ts_modified = max(enumerate(self.stored_success_prop), key=lambda tup: tup[1])[1]
                        self.success = str(self.proportion_ts_modified)
                        self.ready = True
                        print('Consumption set zero for the last trips. Time steps share:', max(enumerate(self.stored_success_prop), key=lambda tup: tup[1])[1])
                        self.soc_end = round(self.dt['soc'].iloc[-1], 3)
                        print('soc_init:', round(self.soc_init, 3), '--> soc_end:', self.soc_end)

        if not self.ready:
            if self.n % 40 == 0:
                print('still in while loop after ', self.n, ' iterations. Battery may be small, or few charging points available...')
            if self.n % 160 == 0:
                if self.battopt:
                    print('Change battery capacity from {} kWh to {} kWh'.format(self.battery_capacity, self.battopt[0]))
                    self.battery_capacity = self.battopt[0]
                    self.battopt.remove(self.battopt[0])
                else:
                    self.success = 'Faulty'  # save anyway but it must be verified
                    self.name = self.name + '_FAIL'
                    print(" ----- !!! UNSUCCESSFUL profile creation !!! ----- please check this '{}', it may need to increase battery capacity or soc init is too low".format(self.name))
                    self.ready = True

    def run(self):
        '''
        No input required.
        Once it finishes the following attributes can be called.
        Attributes:
            'kind',
            'input',
            'chargingdata',
            'battery_capacity',
            'charging_eff',
            'soc_init',
            'soc_min',
            'storage_altern',
            'profile',
            'timeseries',
            'success',
            'name',
            'proportion_ts_modified'
        '''
        self.initial_conf()
        self.battopt = self.storage_altern[:]
        self.battopt.sort()
        self.ready = False
        self.proportion_ts_modified = 1.0
        self.stored_success = []
        self.stored_success_prop = []
        self.stored_n = 0
        self.n = 0
        self.df.loc[:, 'dayhrs'] = self.df['hr'] % 24
        self.df.loc[:, 'consumption'] = self.df['distance']*self.energy_consumption
        while True:
            self.db = self.df.copy()
            self.db.loc[:, 'charging_point'] = self.df['state'].apply(lambda state: self.ChooseChargingPoint(state))
            self.db.loc[:, 'charging_cap'] = self.db['charging_point'].apply(lambda charging_point: self.capacity_charging_point[charging_point])
            self.fill_rows()
            self.drawing_soc()
            self.testing_soc()
            if self.ready:
                break
            else:
                self.n += 1
        self.profile = self.dt[['hh', 'state', 'distance', 'consumption', 'charging_point', 'charging_cap', 'soc']].copy()
        self.timeseries = add_column_datetime(self.profile.copy(), self.totalrows, self.refdate, self.t)

        to_rem = list(self.__dict__.keys())[:]

        keep_attr = [
                    'kind',
                    'input',
                    'energy_consumption',
                    'chargingdata',
                    'battery_capacity',
                    'charging_eff',
                    'soc_init',
                    'soc_min',
                    'soc_end',
                    'storage_altern',
                    'profile',
                    'timeseries',
                    'success',
                    'name',
                    'proportion_ts_modified'
                    ]

        for r in keep_attr:
            if r in to_rem:
                to_rem.remove(r)
        for attr in to_rem:
            self.__dict__.pop(attr, None)
        del to_rem
        print('Profile done: ' + self.name)

    def save_profile(self, folder, description=' '):
        '''
        folder: string, where the files will be stored. Folder is created in case it does not exist.
        description: string
        '''
        self.description = description
        os.makedirs(folder, exist_ok=True)
        filepath = os.path.join(folder, self.name + '.pickle')
        with gzip.open(filepath, 'wb') as datei:
            pickle.dump(self.__dict__, datei)
        print('=== profile saved === : ' + filepath)
