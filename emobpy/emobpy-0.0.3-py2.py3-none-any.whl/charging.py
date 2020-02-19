import pandas as pd
import numpy as np
import uuid
import os
import pickle
import gzip
from numba import jit


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


@jit(nopython=True)
def is_between(t, time_range):
    if time_range[1] < time_range[0]:
        return t >= time_range[0] or t <= time_range[1]
    return time_range[0] <= t <= time_range[1]


def add_column_datetime(df, totalrows, reference_date, t):
    fr = {1: 'H', 0.5: '30min', 0.25: '15min'}
    freq = fr[t]
    start_date = pd.to_datetime(reference_date)
    drange = pd.date_range(start_date, periods=totalrows, freq=freq)
    df = pd.DataFrame(df.values, columns=df.columns, index=drange)
    df = df.rename_axis('date').copy()
    return df


class Charging:
    """
    self.__init__(input)
    self.loadScenario(DataBase)
    self.setSubScenario(option)
    self.run()
    self.save_profile(folder, description=' ')
    """

    def __init__(self, input):
        '''
        input: string. File name of input.
        '''
        self.kind = 'charging'
        self.input = input
        self.change_battery_cap = False  # in case the battery capacity has been changed and then it differs from availability profile
        self.pointmissing = False  # in case of subscenario A2BatpPoint is selected
        self.success = False

    def loadScenario(self, DataBase):
        '''
        DataBase of object DataBase. see example,
        eg. manager = DataBase()
            "manager" is a class instance that contains the profiles
        '''
        if DataBase.db[self.input]:
            if DataBase.db[self.input]['kind'] == 'availability':
                self.profile = DataBase.db[self.input]['profile'].copy()
                self.capacity_charging_point = DataBase.db[self.input]['chargingdata']['capacity_charging_point']
                self.points = list(self.capacity_charging_point.keys())
                self.states = list(set(self.profile.loc[:, 'state']))
                self.battery_capacity = DataBase.db[self.input]['battery_capacity']
                self.charging_eff = DataBase.db[self.input]['charging_eff']
                self.soc_init = DataBase.db[self.input]['soc_init']
                self.soc_min = DataBase.db[self.input]['soc_min']
            else:
                raise ValueError('The charging availability profile {} can not be found in the database'.format(self.input))

            if DataBase.db[DataBase.db[self.input]['input']]['kind'] == 'driving':
                self.t = DataBase.db[DataBase.db[self.input]['input']]['t']
                self.totalrows = DataBase.db[DataBase.db[self.input]['input']]['totalrows']
                self.refdate = DataBase.db[DataBase.db[self.input]['input']]['refdate']
            else:
                raise ValueError('The driving profile {} can not be found in the database'.format(self.input))
        else:
            raise ValueError('The charging availability profile {} can not be found in the database'.format(self.input))

    def setSubScenario(self, option):
        '''
        options: string, 'immediate',  'balanced',  'from_22_to_6_at_home'.
        '''
        self.option = option

    def run(self):
        '''
        No input required.
        Once it finishes the following attributes can be called.
        Attributes:
                    'kind',
                    'input',
                    'change_battery_cap',
                    'pointmissing',
                    'success',
                    'option',
                    'profile',
                    'timeseries',
                    'name'
        '''
        self.name = self.input + '_' + self.option + '_' + uuid.uuid4().hex[0:5]
        if self.option == 'immediate':
            self.numpy_array2 = self.profile[['consumption', 'charging_cap']].values.T
            self.results = self.immediate(self.charging_eff, self.battery_capacity, self.soc_init, *self.numpy_array2, self.t)
            self.profile.loc[:, 'actual_soc'] = self.results[0]
            self.profile.loc[:, 'charge_battery'] = self.results[1]
            self.profile.loc[:, 'charge_grid'] = self.results[2]
        elif self.option == 'balanced':
            self.numpy_array3 = self.profile[['state', 'consumption', 'charging_cap']].values.T
            self.arraystringstate = self.numpy_array3[0]
            self.arraycodestate = np.array([self.states.index(s) for s in self.arraystringstate])
            self.arrayconsumption = self.numpy_array3[1].astype(np.float64)
            self.arraychargingcap = self.numpy_array3[2].astype(np.float64)
            self.results = self.balanced(self.charging_eff, self.battery_capacity, self.soc_init, self.arraycodestate, self.arrayconsumption, self.arraychargingcap, self.t)
            self.profile.loc[:, 'actual_soc'] = self.results[0]
            self.profile.loc[:, 'charge_battery'] = self.results[1]
            self.profile.loc[:, 'charge_grid'] = self.results[2]
        elif set(['from', 'to', 'at']).issubset(self.option.split('_')):  # eg. 'from_22_to_6_at_home'
            self.op_list = [int(s) if RepresentsInt(s) else s for s in self.option.split('_')]
            self.from_ = self.op_list[1]
            self.to_ = self.op_list[3]
            self.point = self.op_list[5]

            self.numpy_array4 = self.profile[['state', 'consumption', 'charging_cap', 'hh']].values.T
            self.arraystringstate = self.numpy_array4[0]
            self.arraycodestate = np.array([self.states.index(s) for s in self.arraystringstate])
            self.drivingcode = self.states.index('driving')
            try:
                self.pointcode = self.states.index(self.point)
            except ValueError:
                self.pointmissing = True
                self.success = False
                print('Charging point "{}" is not in "{}". Availability profile: {}'.format(self.point, ' - '.join(self.states), self.input))
                self.clean()
                return None
            self.arrayconsumption = self.numpy_array4[1].astype(np.float64)
            self.arraychargingcap = self.numpy_array4[2].astype(np.float64)
            self.hh = self.numpy_array4[3].astype(np.float64)
            self.results = self.A2BatPoint(self.from_,
                                           self.to_,
                                           self.pointcode,
                                           self.drivingcode,
                                           self.charging_eff,
                                           self.battery_capacity,
                                           self.soc_init,
                                           self.arraycodestate,
                                           self.arrayconsumption,
                                           self.arraychargingcap,
                                           self.hh,
                                           self.t)
            self.profile.loc[:, 'actual_soc'] = self.results[0]
            self.profile.loc[:, 'charge_battery'] = self.results[1]
            self.profile.loc[:, 'charge_grid'] = self.results[2]
            self.profile.loc[:, 'omit'] = self.results[3]
        else:
            raise ValueError('Select a valid option')
        self.check_success()
        self.timeseries = add_column_datetime(self.profile.copy(), self.totalrows, self.refdate, self.t)
        if self.pointmissing:
            self.name = self.name + '_FAIL'
        self.clean()
        print('Profile done: ' + self.name)
        return None

    @staticmethod
    @jit(nopython=True)
    def immediate(charging_eff, battery_capacity, soc_init, consumption, charging_cap, t):
        soc = np.empty(consumption.shape)
        battery = np.empty(consumption.shape)
        grid = np.empty(consumption.shape)
        rows = soc.shape[0]
        for i in range(rows):
            if i == 0:
                zero = soc_init
                current_soc = zero - consumption[i]/battery_capacity + charging_cap[i]*t*charging_eff/battery_capacity
                if current_soc > 1:
                    soc[i] = 1
                    battery[i] = charging_cap[i]*t*charging_eff - (current_soc-1)*battery_capacity
                    grid[i] = charging_cap[i]*t - (current_soc-1)*battery_capacity/charging_eff
                else:
                    soc[i] = current_soc
                    battery[i] = charging_cap[i]*t*charging_eff
                    grid[i] = charging_cap[i]*t
            else:
                zero = soc[i-1]
                current_soc = zero - consumption[i]/battery_capacity + charging_cap[i]*t*charging_eff/battery_capacity
                if current_soc > 1:
                    soc[i] = 1
                    battery[i] = charging_cap[i]*t*charging_eff - (current_soc-1)*battery_capacity
                    grid[i] = charging_cap[i]*t - (current_soc-1)*battery_capacity/charging_eff
                else:
                    soc[i] = current_soc
                    battery[i] = charging_cap[i]*t*charging_eff
                    grid[i] = charging_cap[i]*t
        return [soc, battery, grid]

    @staticmethod
    @jit(nopython=True)
    def balanced(charging_eff, battery_capacity, soc_init, state, consumption, charging_cap, t):
        soc = np.empty(consumption.shape)
        battery = np.empty(consumption.shape)
        grid = np.empty(consumption.shape)
        soc_ahead = np.empty(consumption.shape)
        rows = soc.shape[0]
        i = 0
        while i < rows:
            if i == 0:
                zero = soc_init
            else:
                zero = soc[i-1]
            if charging_cap[i]*t > 0:
                j = i
                cero = zero
                while state[j] == state[i]:
                    current_soc = cero - consumption[j]/battery_capacity + charging_cap[j]*t*charging_eff/battery_capacity
                    if current_soc > 1:
                        soc_ahead[j] = 1
                    else:
                        soc_ahead[j] = current_soc
                    j += 1
                    cero = current_soc
                k = j - i  # lengh in the same state, this will help to jump the queue
                if np.any(soc_ahead[i:j] == 1):
                    soc_diff = 1 - zero
                    delta_charging = soc_diff*battery_capacity/charging_eff/k
                    cero = zero
                    for m in range(i, j):
                        current_soc = cero - consumption[m]/battery_capacity + delta_charging*charging_eff/battery_capacity
                        if current_soc > 1:
                            soc[m] = 1
                            battery[m] = delta_charging*charging_eff - (current_soc-1)*battery_capacity
                            grid[m] = delta_charging - (current_soc-1)*battery_capacity/charging_eff
                        else:
                            soc[m] = current_soc
                            battery[m] = delta_charging*charging_eff
                            grid[m] = delta_charging
                        cero = current_soc
                    i = m
                else:
                    cero = zero
                    for m in range(i, j):
                        current_soc = cero - consumption[m]/battery_capacity + charging_cap[m]*t*charging_eff/battery_capacity
                        if current_soc > 1:
                            soc[m] = 1
                            battery[m] = charging_cap[m]*t*charging_eff - (current_soc-1)*battery_capacity
                            grid[m] = charging_cap[m]*t - (current_soc-1)*battery_capacity/charging_eff
                        else:
                            soc[m] = current_soc
                            battery[m] = charging_cap[m]*t*charging_eff
                            grid[m] = charging_cap[m]*t
                        cero = current_soc
                    i = m
            else:  # if charging capacity is zero
                current_soc = zero - consumption[i]/battery_capacity  # when only consumption may ocur then soc cannot be > 1, ovoid that statement
                soc[i] = current_soc
                battery[i] = 0
                grid[i] = 0
            i += 1
        return [soc, battery, grid]

    @staticmethod
    @jit(nopython=True)
    def A2BatPoint(from_, to_, point, driving, charging_eff, battery_capacity, soc_init, state, consumption, charging_cap, hr, t):
        soc = np.empty(consumption.shape)
        battery = np.empty(consumption.shape)
        grid = np.empty(consumption.shape)
        soc_ahead = np.empty(consumption.shape)
        preferenceignore = np.zeros(consumption.shape)
        rows = soc.shape[0]
        i = 0
        while i < rows:  # code 1
            if i == 0:
                zero = soc_init
            else:
                zero = soc[i-1]
            if (state[i] == point) | (preferenceignore[i] == 1) | (state[i] == driving):
                if (is_between(np.mod(hr[i], 24), (from_, to_))) | (preferenceignore[i] == 1) | (state[i] == driving):
                    j = i
                    cero = zero
                    negative = False
                    while state[j] == state[i]:  # code 2
                        current_soc = cero - consumption[j]/battery_capacity + charging_cap[j]*t*charging_eff/battery_capacity
                        if current_soc <= 0:
                            negative = i  # index when negative while driving
                        if current_soc > 1:
                            soc_ahead[j] = 1
                        else:
                            soc_ahead[j] = current_soc
                        j += 1
                        cero = current_soc
                    if negative:
                        cap = 0.01 + zero - current_soc
                        n = i
                        imagsoc = 0
                        while cap > imagsoc:  # code 3
                            n -= 1
                            imagsoc += charging_cap[n]*t*charging_eff/battery_capacity
                            cap += consumption[n]/battery_capacity
                        p = n
                        while state[p] == state[n]:  # code 4
                            p -= 1
                            if p < 0:
                                break  # p=-1
                        for idx in range(p+1, negative):
                            preferenceignore[idx] = 1
                        i = p + 1
                        continue
                    k = j - i  # lengh in the same state, this will help to jump the queue
                    if np.any(soc_ahead[i:j] == 1):
                        soc_diff = 1 - zero
                        delta_charging = soc_diff*battery_capacity/charging_eff/k
                        cero = zero
                        for m in range(i, j):
                            current_soc = cero - consumption[m]/battery_capacity + delta_charging*charging_eff/battery_capacity
                            if current_soc > 1:
                                soc[m] = 1
                                battery[m] = delta_charging*charging_eff - (current_soc-1)*battery_capacity
                                grid[m] = delta_charging - (current_soc-1)*battery_capacity/charging_eff
                            else:
                                soc[m] = current_soc
                                battery[m] = delta_charging*charging_eff
                                grid[m] = delta_charging
                            cero = current_soc
                        i = m
                    else:
                        cero = zero
                        for m in range(i, j):
                            current_soc = cero - consumption[m]/battery_capacity + charging_cap[m]*t*charging_eff/battery_capacity
                            if current_soc > 1:
                                soc[m] = 1
                                battery[m] = charging_cap[m]*t*charging_eff - (current_soc-1)*battery_capacity
                                grid[m] = charging_cap[m]*t - (current_soc-1)*battery_capacity/charging_eff
                            else:
                                soc[m] = current_soc
                                battery[m] = charging_cap[m]*t*charging_eff
                                grid[m] = charging_cap[m]*t
                            cero = current_soc
                        i = m
                else:
                    current_soc = zero - consumption[i]/battery_capacity
                    soc[i] = current_soc
                    battery[i] = 0
                    grid[i] = 0
            else:
                current_soc = zero - consumption[i]/battery_capacity
                soc[i] = current_soc
                battery[i] = 0
                grid[i] = 0
            i += 1
        return [soc, battery, grid, preferenceignore]

    def check_success(self):
        if self.profile['actual_soc'].min() >= self.soc_min:
            consT = round(self.profile['consumption'].sum(), 2)
            chrgT = round(self.profile['charge_battery'].sum(), 2)
            stoI = round(self.battery_capacity*self.soc_init, 2)
            stoE = round(self.battery_capacity*self.profile['actual_soc'].values[-1], 2)
            balT = round(stoI + chrgT - consT - stoE, 2)
            if balT != 0.0:
                print('Balance:', balT, '   Consumption:', consT, 'charge_battery:', chrgT, 'sto_init:', stoI, 'sto_end:', stoE)
            self.success = True
        else:
            self.success = False

    def changeBatteryCapacity(self, new_capacity):
        self.change_battery_cap = True
        self.battery_capacity = new_capacity

    def clean(self):
        to_rem = list(self.__dict__.keys())[:]
        keep_attr = [
                    'kind',
                    'input',
                    'change_battery_cap',
                    'pointmissing',
                    'success',
                    'option',
                    'profile',
                    'timeseries',
                    'name'
                    ]
        for r in keep_attr:
            if r in to_rem:
                to_rem.remove(r)
        for attr in to_rem:
            self.__dict__.pop(attr, None)
        del to_rem

    def save_profile(self, folder, description=' '):
        '''
        folder: string, where the files will be stored. Folder is created in case it does not exist.
        description: string
        '''
        self.description = description
        info = self.__dict__
        os.makedirs(folder, exist_ok=True)
        filepath = os.path.join(folder, self.name + '.pickle')
        with gzip.open(filepath, 'wb') as datei:
            pickle.dump(info, datei)
        del info
        print('File saved : ' + filepath)
        return None
