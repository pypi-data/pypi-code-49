import pandas as pd
import numpy as np
from collections import Counter
import operator
import uuid
import os
import copy
from .constants import OPERATORS, WEEKS, TIME_FREQ, RULE, GROUPID
import pickle
import gzip
from numba import jit

# TODO:
#   - improve distance selection, currently only destination cares


def cmp(arg1, op, arg2):
    ops = {'<': operator.lt,
           '<=': operator.le,
           '==': operator.eq,
           '!=': operator.ne,
           '>=': operator.ge,
           '>': operator.gt}
    operation = ops.get(op)
    return operation(arg1, arg2)


@jit(nopython=True)
def firstpair_arg(np_pairs, np_pair):
    '''
    returns an integer or None. The integer represents index where the pair is located in the array of pairs.
    Only works for numpy arrays in form of list of pairs.
    This is a special implementation for NUMBA.
    '''
    memory = []
    n = np.int32(0)
    for i, j in zip(np_pairs[:, 0], np_pairs[:, 1]):
        if (i == np_pair[0]) & (j == np_pair[1]):
            memory.append(n)
        n += np.int32(1)
    return np.array(memory, dtype=np.int32)


@jit(nopython=True)
def rand_choice_nb(arr, prob):
    """
    :param arr: A 1D numpy array of values to sample from.
    :param prob: A 1D numpy array of probabilities for the given samples.
    :return: A random sample from the given array with a given probability.
    """
    return arr[np.searchsorted(np.cumsum(prob), np.random.rand(), side="right")]


def days_week_sequence(reference_date, weeks):
    '''
    this determines the day of the week of the reference date and sets the day-sequence
    '''
    df = pd.DataFrame({'ref_dates': [reference_date]})
    df['ref_dates'] = pd.to_datetime(df['ref_dates'])
    df['day_of_week'] = df['ref_dates'].dt.day_name()
    day_of_week = df['day_of_week'].values[0]
    for key, val in weeks.items():
        if val['day'] == day_of_week:
            day_numb = key
    sequence = [k % 7 for k in range(day_numb, 7+day_numb)]
    return sequence


def add_column_datetime(df, totalrows, reference_date, t):
    fr = {1: 'H', 0.5: '30min', 0.25: '15min'}
    freq = fr[t]
    start_date = pd.to_datetime(reference_date)
    drange = pd.date_range(start_date, periods=totalrows, freq=freq)
    df = pd.DataFrame(df.values, columns=df.columns, index=drange)
    df = df.rename_axis('date').copy()
    return df


class Mobility:
    def __init__(self):
        '''
        self.setParams(param)
        self.setStats(stat_ntrip, stat_dest, stat_km)
        self.setRules(rules)
        self.initial_conf() "optional" Useful to copy full rules dictionary
        self.run()
        self.save_profile(dir)
        '''
        self.kind = 'driving'

    def setParams(self, param):
        '''
        param: dictionary with parameters

        eg.
           {'person':'fulltime',
            'group':'commuter',
            'refdate':'01/01/2020',
            'energy_consumption': 0.18,
            'hours': 168,
            'timestep_in_hrs':0.5}

        '''
        self.per_str = param['person']
        self.refdate = param['refdate']
        self.hours = param['hours']
        self.t = param['timestep_in_hrs']
        self.g_type = param['group']
        self.energy_consumption = param['energy_consumption']

    def setStats(self, stat_ntrip, stat_dest, stat_km):
        self.df1 = stat_ntrip.copy()
        self.df2 = stat_dest.copy()
        self.df3 = stat_km.copy()

    def setRules(self, rules={}):
        self.rulen = rules
        if not rules:
            print('rules not provided, using default rules instead')

    def initial_conf(self):
        self.operators = OPERATORS
        self.weeks = WEEKS
        self.time_freq = TIME_FREQ

        self.numb_weeks = int(self.hours/7/24) + 1
        self.sequence = days_week_sequence(self.refdate, self.weeks)
        self.totalrows = self.hours/self.t

        if self.df2['time'].max() >= 24.0:
            raise Exception("replace 24 by 0 in time column of departure time - trip purpose probabilities, time should range between 0 and 23.99")
        self.stat = self.df2.copy()
        self.stat.loc[self.stat[self.stat['time'] < 3.0].index, 'time'] = self.stat[self.stat['time'] < 3.0]['time'] + 24.0  # this change enables to create day tours with returning time to "home" at the most just befor 3 am the next day.
        self.df2mod = self.stat.copy()

        self.states = list(set(self.df2mod[['purpose', self.per_str]].replace(0.0, np.nan).dropna(how='any', axis=0)['purpose'].to_list()))
        self.homeid = self.states.index('home')
        if self.g_type == 'commuter':
            self.workid = self.states.index('workplace')
        self.g_id = GROUPID[self.g_type]
        self.km_pairs = np.array(self.df3['km_range'].apply(lambda x: [int(i) for i in x.split('_')]).to_list())
        self.km_dest_array_code = self.df3.set_index('km_range')[self.states].T.values

        self.rules = {self.g_type: RULE}
        for week, dicts in self.rulen.items():
            for opt, stdict in dicts.items():
                if isinstance(stdict, list):
                    self.rules[self.g_type][week][opt] = stdict
                elif isinstance(stdict, int):
                    self.rules[self.g_type][week][opt] = stdict
                else:
                    for key, value in stdict.items():
                        self.rules[self.g_type][week][opt][key] = value
        self.name = self.per_str + '_' + 'W' + str(self.numb_weeks) + '_' + uuid.uuid4().hex[0:5]

    def group_trips_week(self):
        '''
        This function returns an integer that represents the number of trips to create a day tour. This value is obtained based on mobility statistics.
        df: pandas dataframe with probability distribution number of trips.
        cut: a python list with trip numbers to be dropped from the prob. distribution.
        group: (string) persons.
        week: (string) weekend or weekday.
        '''
        self.T = self.df1[self.df1['group'] == self.per_str].copy()
        self.idx_drop = self.T[self.T['trip'].isin(self.cut)].index.tolist()
        self.T.drop(self.idx_drop, axis=0, inplace=True)
        self.T.loc[:, self.weektype] = self.T[self.weektype]/self.T[self.weektype].sum()  # once the trip quantity in "cut" is removed from the probability distribution, normalization is implemented for the remaining trip quantities to add up 100% again.
        self.trips_list = self.T['trip'].values.tolist()
        self.trips_prob = self.T[self.weektype].values.tolist()
        self.Rnd_week_trips = np.random.choice(self.trips_list, p=self.trips_prob)  # Numpy function, that takes into account a list of options (trips quantities, eg: 0, 1, or 3 ...) and their corresponding probabilities to chose one option (eg: 2 trips for a day tour)

    def time_purpose_iter(self):
        """
        It returns a tuple with departure time and destination eg. (15,'home') for a trip.
        As the departure time and purpose of day trips can not be repeated once it has been selected for a trip,
        the departure time of every consecutive trip must be removed from the probability distribution of the next trip.
        While the trip purpose can repeat until a determined number of times, after that the purpose can be removed for the next trips of the day.
        df: it is a Dataframe with probability distributions. df must have columns with day_code, time, purpose, and group of persons.
        cutt: it is a list that contains the hours to be removed from the df.
        cutp: it is a list that contains the purpose trip of previous trips.
        group: string that refers to a group of persons where a probability distribution has to be considered.
        day: string refering to a weekday, saturday or sunday.
        """
        self.D = self.df2mod[self.df2mod['days'] == self.day].copy()  # a smaller table is obtained that only contains the probability distribution of a selected day.
        self.H = self.D[['time', 'purpose', self.per_str]].copy()
        self.idx_drop_ = self.H[self.H['time'].isin(self.cutt)].index.tolist()  # from the probability distribution table the index of the rows that are cutt list are stored in a list.
        self.H.drop(self.idx_drop_, axis=0, inplace=True)  # rows of table are removed.

        if self.rules[self.g_type][self.weektype]['max_same_trip_times']:
            self.presence = self.rules[self.g_type][self.weektype]['max_same_trip_times'] - 1  # number of times that a destination (purpose) can repeat, if 1 that means that no more that two trips in a particular day can go to the same destination at diferent time.
            if any(i > self.presence for i in list(Counter(self.cutp).values())):  # Counter is a function that counts the how many times the objects repeats in a list. Then the statement is True if one objects is highet than "presence"
                self.idx_drop__ = self.H[self.H['purpose'].isin([i for i, j in Counter(self.cutp).items() if j > self.presence])].index.tolist()  # row index of probability distribution is obtained where the purpose repeat in previous trips.
                self.H.drop(self.idx_drop__, axis=0, inplace=True)  # the repeated objects (porpuse) in previous trips are removed from the prob. distribution.

        self.H.loc[:, self.per_str] = self.H[self.per_str]/self.H[self.per_str].sum()  # the prob. distribution is normalized.
        self.lists = self.H[['time', 'purpose']].values.tolist()
        self.tuple_list = [tuple(i) for i in self.lists]
        self.tuple_prob = self.H[self.per_str].values.tolist()
        self.Rnd_trip = self.tuple_list[np.random.choice(len(self.tuple_list), p=self.tuple_prob)]  # selection of tuple (time,purpose) base on prob. distribution.

    def creation_unsorted_trips(self):
        '''
        It returns a unsorted time dataframe with trips. It includes number of trips, departure time, destination (purpose).
        trips: number of trips to create a tour later (tour: multiple trips).
        df: Dataframe with probability distributions. df must have columns with day_code, time,purpose,group of persons (is only used for time_purpose_iter() function).
        group: string that refers to a grop of persons where the probability distribution of the df to consider (is only used for time_purpose_iter() function).
        day: string refering to a weekday, saturday or sunday (it is only used for time_purpose_iter() function).
        '''
        self.wdc = pd.DataFrame()
        self.cutt = []
        self.cutp = []
        for trip in range(self.Rnd_week_trips):
            self.time_purpose_iter()  # for the first trip, time_list and purp_list are empty, but for the up comming trips the lists are filled with info of previous trips.
            self.time_purp_tuple = self.Rnd_trip
            self.wdc.loc[trip, 'trips'] = self.Rnd_week_trips
            self.wdc.loc[trip, 'departure'] = self.time_purp_tuple[0]
            self.wdc.loc[trip, 'purpose'] = self.time_purp_tuple[1]
            self.cutt.append(self.time_purp_tuple[0])  # adding to the lists the time and purpose of the current trip
            # This was tested, improves speed in 20% but cause distortion in patterns
            # if self.time_purp_tuple[0] - self.t >= 3:
            #     self.cutt.append(self.time_purp_tuple[0] - self.t)
            # if self.time_purp_tuple[0] + self.t < 27:
            #     self.cutt.append(self.time_purp_tuple[0] + self.t)
            self.cutp.append(self.time_purp_tuple[1])

    def creation_unsorted_trips_commuter(self):
        '''
        It returns a unsorted time dataframe with trips. It includes number of trips, departure time, destination (purpose).
        trips: number of trips to create a tour later (tour: multiple trips).
        df: Dataframe with probability distributions. df must have columns with day_code, time,purpose,group of persons (is only used for time_purpose_iter() function).
        group: string that refers to a grop of persons where the probability distribution of the df to consider (is only used for time_purpose_iter() function).
        day: string refering to a weekday, saturday or sunday (it is only used for time_purpose_iter() function).
        repeated: is a list of tuples with departure time and destination (purpose) of thoso trips that habe to be constant. eg: [(),()]
        '''
        self.cutt = []
        self.cutp = []
        self.wdc = pd.DataFrame()
        for idx, tup in enumerate(self.repeated):
            self.wdc.loc[idx, 'trips'] = self.Rnd_week_trips
            self.wdc.loc[idx, 'departure'] = tup[0]
            self.wdc.loc[idx, 'purpose'] = tup[1]
            self.cutt.append(tup[0])  # adding to the lists the time and purpose of the current trip
            # This was tested, improves speed in 20% but cause distortion in patterns
            # if tup[0] - self.t >= 3:
            #     self.cutt.append(tup[0] - self.t)
            # if tup[0] + self.t < 27:
            #     self.cutt.append(tup[0] + self.t)
            self.cutp.append(tup[1])

        if idx+1 < self.Rnd_week_trips:
            for trip in range(idx+1, self.Rnd_week_trips):
                self.time_purpose_iter()  # for the first trip, time_list and purp_list are empty, but for the up comming trips the lists are filled with info of previous trips.
                self.time_purp_tuple = self.Rnd_trip
                self.wdc.loc[trip, 'trips'] = self.Rnd_week_trips
                self.wdc.loc[trip, 'departure'] = self.time_purp_tuple[0]
                self.wdc.loc[trip, 'purpose'] = self.time_purp_tuple[1]
                self.cutt.append(self.time_purp_tuple[0])  # adding to the lists the time and purpose of the current trip
                # This was tested, improves speed in 20% but cause distortion in patterns
                # if self.time_purp_tuple[0] - self.t >= 3:
                #     self.cutt.append(self.time_purp_tuple[0] - self.t)
                # if self.time_purp_tuple[0] + self.t < 27:
                #     self.cutt.append(self.time_purp_tuple[0] + self.t)
                self.cutp.append(self.time_purp_tuple[1])

    def create_tour(self):
        '''
        This function creates a tour (trips in a day in time ascending order).
        Each row contains information of a trip, such as, "state", "departure", "last_departure","duration","equal"
        db: is a dataframe of unsorted trips
        start: indicate the last trip time of the previous tour.
        t: is a factor that indicates the fraction of an hour. eg. for 30min is 0.5

        TODO: - to edit the script to be able to model with 30 min or even for 15 min "df.loc[i, 'duration'] = row['departure'] - (prev_triptime+1)"
              - to add the last trip time in the return
        '''
        self.tour = self.wdc.sort_values('departure').reset_index(drop=True)  # trips are sorted according to time in ascending order
        self.state = copy.deepcopy(self.prev_dest)  # in the for loop the fist state is the last destination of previous day, then this variable is changed to the next possible stages
        self.prev_triptime = copy.deepcopy(self.start)  # in the for loop the ealiest trip has a previous trip time set at -1 (23hrs day before)
        for i, row in self.tour.iterrows():
            self.tour.loc[i, 'state'] = self.state  # 'state' column is added indicating the actual state before taking a new trip
            self.tour.loc[i, 'last_dep'] = self.prev_triptime  # 'last_dep' column is added indicating the previous departure time
            self.tour.loc[i, 'duration'] = row['departure'] - (self.prev_triptime+self.t)  # 'duration' column is added indicating the duration in hours in the actual state before taking the new trip
            self.tour.loc[i, 'equal'] = self.state == row['purpose']  # 'equal' column is added indicating if the actual trip has destination equal to its current status, if so new trips must be created
            self.state = row['purpose']
            self.prev_triptime = row['departure']  # the previous trip time is changed to be included in the next trip row.

    @staticmethod
    @jit(nopython=True)
    def init_edges_create(km_pairs, km_dest_array_code, destid):
        '''
        This function returns a dictionary that contains two edges as dictionary keys and distance traveled in km as dictionary values for edges 'home' to 'workplace' and 'workplace' to 'home'
        where the distance of these two edges is the same.
        df_dist: is a dataframe that contains probability distribution of distance for each destination (purpose)
        '''
        km_pair = rand_choice_nb(km_pairs, km_dest_array_code[destid])  # select a range of distances based on destinations and their probability distribution.
        kvalue = np.random.randint(low=km_pair[0]+1, high=km_pair[1]+1)  # it returns an integer from a list interval in uniform distribution. eg: "(10,20]" including right endpoint.
        return kvalue

    @staticmethod
    @jit(nopython=True)
    def add_distance_to_tour(edges, initedge, initedgekm, km_pairs, km_dest_array_code, tour_state_code, tour_purpose_code):
        '''
        This function returns a day tour with distance travelled for each trip by adding a new column to the DataFrame (df) with column title 'distance'.
        in order to make a consistent tour of trips. The distance travelled for each trip should be similar, although it depends on the trips topology.
        A simple rule has been programmed.
        df: is a dataframe that represents a day tour and contains trip information in each row. The information required is 'state' and 'purpose'.
        df_dist: is a dataframe that contains probability distribution of distance for each destination (purpose).
        hwh_edges: is a dictionary with home-workplace-home edges and distance.
        '''
        # this script creates inverted edge of all edges and remove the one that is repeated in the list of edges.
        tour = np.array(list(zip(tour_state_code, tour_purpose_code)))
        while True:
            memory = []
            distances = np.empty(tour_state_code.shape, dtype=np.int32)
            for ie in [initedge, initedge[::-1]]:
                indexes = firstpair_arg(tour, ie)
                if indexes.shape[0] > 0:
                    for idx in indexes:
                        if idx not in memory:
                            distances[idx] = np.int32(initedgekm)
                            memory.append(idx)

            for ii, jj in zip(edges[:, 0], edges[:, 1]):
                km_pair = rand_choice_nb(km_pairs, km_dest_array_code[jj])  # select a range of distances based on destinations and their probability distribution.
                kvalue = np.random.randint(low=km_pair[0]+1, high=km_pair[1]+1)  # it returns an integer from a list interval in uniform distribution. eg: "(10,20]" including right endpoint.
                for e in [np.array([ii, jj]), np.array([jj, ii])]:
                    indexes = firstpair_arg(tour, e)
                    if indexes.shape[0] > 0:
                        for idx in indexes:
                            if idx not in memory:
                                distances[idx] = np.int32(kvalue)
                                memory.append(idx)
            # TODO:
            # this must be improved, find another way to select distance for trips. Bearing in mind that overall travelled distance in a day are consistent for each trip.
            if distances.mean() + 0.5 >= distances.max() - distances.min():  # distance consistency check
                break
        return distances

    def MeetAllConditions(self):
        self.flag = False
        self.cause = ''
        for condition, op in self.operators.items():
            self.flag1 = False
            for state in self.states:
                if self.rules_[self.g_type][self.weektype][condition][state]:  # for any condition in Rules when False, it continues to the next state
                    if condition == 'last_trip_to':
                        if self.tour['purpose'].iloc[-1]:
                            if cmp(self.tour['purpose'].iloc[-1], op, state):
                                pass
                            else:
                                self.reason = copy.deepcopy(state)
                                self.flag1 = True
                                self.cause = 'last_trip_to ' + state
                                break
                    elif condition == 'first_trip_to':
                        if self.tour['purpose'].iloc[0]:
                            if cmp(self.tour['purpose'].iloc[0], op, state):
                                pass
                            else:
                                self.reason = copy.deepcopy(state)
                                self.flag1 = True
                                self.cause = 'first_trip_to ' + state
                                break
                    elif condition == 'not_last_trip_to':
                        if self.tour['purpose'].iloc[-1]:
                            if cmp(self.tour['purpose'].iloc[-1], op, state):
                                pass
                            else:
                                self.reason = copy.deepcopy(state)
                                self.flag1 = True
                                self.cause = 'not_last_trip_to ' + state
                                break
                    elif condition == 'min_state_duration' or condition == 'max_state_duration':
                        if not self.tour[self.tour['state'] == state]['duration'].empty:
                            self.dur_list = self.tour[self.tour['state'] == state]['duration'].values.tolist()
                            for dur in self.dur_list:
                                if cmp(dur, op, self.rules_[self.g_type][self.weektype][condition][state]):
                                    pass
                                else:
                                    self.reason = copy.deepcopy(state)
                                    self.flag1 = True
                                    self.cause = 'min_or_max_state_duration ' + state
                                    break
                        else:
                            if self.rules_[self.g_type][self.weektype]['at_least_one_trip'][state]:
                                self.reason = copy.deepcopy(state)
                                self.flag1 = True
                                self.cause = 'min_or_max_state_duration ' + state
                                break
                            else:
                                pass
                    elif condition == 'equal_state_and_destination':
                        if not self.tour[self.tour['state'] == state]['purpose'].str.contains(state, case=True, regex=True).any():
                            pass
                        else:
                            self.reason = copy.deepcopy(state)
                            self.flag1 = True
                            self.cause = 'equal_state_and_destination ' + state
                            break
                    elif condition == 'overall_min_time_at' or condition == 'overall_max_time_at':
                        if self.tour[self.tour['state'] == state].empty:
                            if self.rules_[self.g_type][self.weektype]['at_least_one_trip'][state]:
                                self.reason = copy.deepcopy(state)
                                self.flag1 = True
                                self.cause = 'overall_min_or_max_time_at ' + state
                                break
                            else:
                                pass
                        elif self.tour[self.tour['state'] == state]['duration'].sum() != 0:
                            if cmp(self.tour[self.tour['state'] == state]['duration'].sum(), op, self.rules_[self.g_type][self.weektype][condition][state]):
                                pass
                            else:
                                self.reason = copy.deepcopy(state)
                                self.flag1 = True
                                self.cause = 'overall_min_or_max_time_at ' + state
                                break
                        else:
                            self.reason = copy.deepcopy(state)
                            self.flag1 = True
                            self.cause = 'overall_min_or_max_time_at ' + state
                            break
            if self.flag1:
                self.flag = True
                break

    def select_tour(self):
        '''
        This function returns a day tour of trips that meets all the preset conditions defined in rules dict.
        The tour is created based on the three probability distribution that lead to determine amount of trips per day, destinations and distance.

        start: represents the departing hour of the last trip of the tour of the day before.
        df_trips,df_hr,df_dist: are the probability distributions.
        n_day: string of weekday, Saturday or Sunday.
        per_str: string of a group of person.
        g_dict: dictionary with group of person.
        week_dict: dictionary that contains days of the week, kind of weekday and a day code.
        states: a list that contains all the possible locations that a vehicle can be.
        rules: dictionary with constraints that the tour of trips has to meet to be selected.
        operators: a dictionary that represent equality or inequality operator that may apply depends on the constraint contained in rules dictionary. This operator compares values of trips in right hand side (RHS) with rules dict values in left hand side (LHS).
        hwh_edges: dictionary with home-work-home edges and distance.
        day_hrs: this variable represents the number of values in the column "time" of the time_purpose stats, in order to identify if 24 hour a day, or 48 of 30min or 96 for 15min
        '''
        self.day = self.weeks[self.n_day]['day_code']
        self.weektype = self.weeks[self.n_day]['week']
        self.cut = self.rules[self.g_type][self.weektype]['n_trip_out'][:]
        self.group_trips_week()
        if self.Rnd_week_trips != 0:
            self.rules_ = copy.deepcopy(self.rules)
            self.no_trip = False
            self.warningB = -1
            self.causes = []
            self.rate = {}
            self.flagiter = False
            while True:
                self.warningB += 1
                self.creation_unsorted_trips()
                self.create_tour()
                self.MeetAllConditions()
                if self.cause != '':
                    self.causes.append(self.cause)
                if self.flag:
                    self.ratesteps = 10
                    if self.warningB % self.ratesteps == 0:
                        self.counts = Counter(self.causes)
                        if self.warningB == 0:
                            pass
                        elif self.warningB == self.ratesteps:
                            self.countbefore = self.counts
                        else:
                            for k, v in self.counts.items():
                                if k in list(self.countbefore.keys()):
                                    self.rate[k] = (v - self.countbefore[k])/self.ratesteps
                                else:
                                    self.rate[k] = (v)/self.ratesteps
                            self.countbefore = self.counts
                            self.rate['days'] = self.days
                            self.rate['trips'] = self.Rnd_week_trips
                            self.rate['iter'] = self.warningB
                            os.makedirs(self.logdir, exist_ok=True)
                            self.logdf = self.logdf.append([self.rate], sort=False, ignore_index=True)
                            sortedcol = ['days', 'trips', 'iter']
                            cols = sortedcol + [col for col in self.logdf if col not in sortedcol]
                            self.logdf = self.logdf[cols]
                            self.logdf.to_csv(os.path.join(self.logdir, 'log.csv'), index=False)
                    if self.warningB >= 10*self.ratesteps and self.warningB % 200 == 10*self.ratesteps:
                        if not self.flagiter:
                            self.flagiter = True
                        print('   "select_tour" method in loop Nr. ' + str(self.warningB) + ' for day ' + str(self.days) + '. See log file ' + self.name)
                        self.rank = self.logdf[self.logdf['days'] == self.logdf['days'].iloc[-1]][-3:][[x for x in self.logdf.columns if x not in ['days', 'trips', 'iter']]].mean()
                        print('\n'.join(['       ' + x + ' uncompliance rate (last 30 iter)' for x in self.rank.nlargest(2).round(2).to_string().split('\n')]))
                    continue
                if self.flagiter:
                    print('   tour done')
                break

            self.tour_state_code = np.array([self.states.index(s) for s in self.tour['state'].to_list()])
            self.tour_purpose_code = np.array([self.states.index(s) for s in self.tour['purpose'].to_list()])
            self.edges = np.array(list(set(list(list(zip(self.tour_state_code, self.tour_purpose_code))))))  # create a list with all the edges identified in a tour of trips
            self.distances = self.add_distance_to_tour(self.edges, self.initedge, self.initedgekm, self.km_pairs, self.km_dest_array_code, self.tour_state_code, self.tour_purpose_code)
            self.tour.loc[:, 'distance'] = self.distances
            self.start = self.tour['departure'].iloc[-1] - 24.0
            self.prev_dst = copy.deepcopy(self.state)
        else:
            self.no_trip = True
            self.tour = False
            self.start -= 24
            self.prev_dst = copy.deepcopy(self.prev_dest)

    def select_tour_commuter(self):  # start,prev_dest,df_trips,df_hr,df_dist,n_day,per_str,g_dict,week_dict,states,operators,rules,hwh_edges,day_hrs,t,repeated
        '''
        This function returns a day tour of trips that meets all the preset conditions defined in rules dict.
        The tour is created based on the three probability distribution that lead to determine amount of trips per day, destinations and distance.

        start: represents the departing hour of the last trip of the tour of the day before.
        df_trips,df_hr,df_dist: are the probability distributions.
        n_day: string of weekday, Saturday or Sunday.
        per_str: string of a group of person.
        g_dict: dictionary with group of person.
        week_dict: dictionary that contains days of the week, kind of weekday and a day code.
        states: a list that contains all the possible locations that a vehicle can be.
        rules: dictionary with constraints that the tour of trips has to meet to be selected.
        operators: a dictionary that represent equality or inequality operator that may apply depends on the constraint contained in rules dictionary. This operator compares values of trips in right hand side (RHS) with rules dict values in left hand side (LHS).
        hwh_edges: dictionary with home-work-home edges and distance.
        day_hrs: this variable represents the number of values in the column "time" of the time_purpose stats, in order to identify if 24 hour a day, or 48 of 30min or 96 for 15min
        '''
        self.day = self.weeks[self.n_day]['day_code']
        self.weektype = self.weeks[self.n_day]['week']
        self.rem_trip = self.rules[self.g_type][self.weektype]['n_trip_out'][:]  # from rules dictionary the trips quantities to remove
        self.add_rem_trip = list(range(1, len(self.repeated)*2))
        self.rem_trip.extend(self.add_rem_trip)
        self.rem_trp = list(set(self.rem_trip))
        self.cut = copy.deepcopy(self.rem_trp)
        self.group_trips_week()
        if self.Rnd_week_trips != 0:
            self.no_trip = False
            self.warningC = 0
            self.hometime = 0
            self.rules_ = copy.deepcopy(self.rules)
            self.causes = []
            self.rate = {}
            self.flagrule1 = False
            self.flagrule2 = False
            self.flagiter = False
            while True:
                self.warningC += 1
                self.creation_unsorted_trips_commuter()
                self.create_tour()
                self.MeetAllConditions()
                if self.cause != '':
                    self.causes.append(self.cause)
                if self.flag:
                    self.ratesteps = 10
                    if self.warningC % self.ratesteps == 0:
                        self.counts = Counter(self.causes)
                        if self.warningC == 0:
                            pass
                        elif self.warningC == self.ratesteps:
                            self.countbefore = self.counts
                        else:
                            for k, v in self.counts.items():
                                if k in list(self.countbefore.keys()):
                                    self.rate[k] = (v - self.countbefore[k])/self.ratesteps
                                else:
                                    self.rate[k] = (v)/self.ratesteps
                            self.countbefore = self.counts
                            self.rate['days'] = self.days
                            self.rate['trips'] = self.Rnd_week_trips
                            self.rate['iter'] = self.warningC
                            os.makedirs(self.logdir, exist_ok=True)
                            self.logdf = self.logdf.append([self.rate], sort=False, ignore_index=True)
                            sortedcol = ['days', 'trips', 'iter']
                            cols = sortedcol + [col for col in self.logdf if col not in sortedcol]
                            self.logdf = self.logdf[cols]
                            self.logdf.to_csv(os.path.join(self.logdir, 'log.csv'), index=False)
                        # start commuter mod
                        if self.warningC >= 3*self.ratesteps and self.warningC % 3*self.ratesteps == 0:
                            self.exception = 'overall_min_or_max_time_at home'
                            self.cap = 0.32
                            if self.exception in self.logdf[self.logdf['days'] == self.logdf['days'].iloc[-1]][-3:].columns.tolist():
                                self.speed = self.logdf[self.logdf['days'] == self.logdf['days'].iloc[-1]][-3:].mean()[self.exception]
                                if not self.flagrule1:
                                    if self.speed > self.cap:
                                        self.tm = self.rules[self.g_type][self.weektype]['overall_min_time_at']['home']
                                        self.rules_[self.g_type][self.weektype]['overall_min_time_at']['home'] = self.tm/2  # here, the condiction is removed. This method is not efficient
                                        self.flagrule1 = True
                                        print('  Rules relaxed from %s hrs to %s hrs for "overall_min_time_at %s ". Uncompliance rate: %s' % (self.tm, self.tm/2, 'home', round(self.speed, 2)))
                                elif not self.flagrule2:
                                    if self.speed > self.cap:
                                        self.rules_[self.g_type][self.weektype]['overall_min_time_at']['home'] = False
                                        self.flagrule2 = True
                                        print('  Rules relaxed from %s hrs to %s. Uncompliance rate: %s' % (self.tm/2, 'False', round(self.speed, 2)))
                        # end commuter mod
                    if self.warningC >= 10*self.ratesteps and self.warningC % 200 == 10*self.ratesteps:
                        if not self.flagiter:
                            self.flagiter = True
                        print('   "select_tour commuter" method in loop Nr. ' + str(self.warningC) + ' for day ' + str(self.days) + '. See log file ' + self.name)
                        self.rank = self.logdf[self.logdf['days'] == self.logdf['days'].iloc[-1]][-3:][[x for x in self.logdf.columns if x not in ['days', 'trips', 'iter']]].mean()
                        print('\n'.join(['       ' + x + ' uncompliance rate (last 30 iter)' for x in self.rank.nlargest(2).round(2).to_string().split('\n')]))
                    continue
                if self.flagiter:
                    print('   tour done')
                break

            self.tour_state_code = np.array([self.states.index(s) for s in self.tour['state'].to_list()])
            self.tour_purpose_code = np.array([self.states.index(s) for s in self.tour['purpose'].to_list()])
            self.edges = np.array(list(set(list(list(zip(self.tour_state_code, self.tour_purpose_code))))))  # create a list with all the edges identified in a tour of trips
            self.distances = self.add_distance_to_tour(self.edges, self.initedge, self.initedgekm, self.km_pairs, self.km_dest_array_code, self.tour_state_code, self.tour_purpose_code)
            self.tour.loc[:, 'distance'] = self.distances
            self.start = self.tour['departure'].iloc[-1] - 24.0
            self.prev_dst = copy.deepcopy(self.state)
        else:
            self.no_trip = True
            self.tour = False
            self.start -= 24.0
            self.prev_dst = copy.deepcopy(self.prev_dest)
        # return (self.no_trip, df, start,prev_dst)

    def loadprofile(self, profilepath):
        self.profile = pd.read_csv(profilepath)

    def fill_rows(self):
        self.repeats = ['hr', 'state', 'weekday', 'person']
        self.fixed = ['distance', 'consumption']
        self.copied = ['departure', 'last_dep', 'purpose', 'duration']
        self.calc = ['dayhrs']
        self.same = []
        self.db = self.profile.copy()
        self.db.loc[:, 'dayhrs'] = self.db['hr'] % 24
        self.db.loc[:, 'consumption'] = self.db['distance']*self.energy_consumption
        self.timeseries = pd.DataFrame(columns=self.db.columns)
        self.timeseries.loc[:, 'hh'] = np.arange(0, self.hours, self.t)
        self.idx = self.timeseries[self.timeseries['hh'].isin(self.db['hr'].tolist())].index.tolist()
        self.mixed = self.repeats + self.fixed + self.copied
        for r in self.mixed:
            self.val = self.db[r].values.tolist()
            self.timeseries.loc[self.idx, r] = self.val
        self.timeseries.loc[self.totalrows-1, 'state'] = self.db['state'].iloc[-1]
        self.timeseries.loc[self.totalrows-1, 'hr'] = self.timeseries['hh'][self.totalrows-1]
        self.rp = self.timeseries[::-1].reset_index(drop=True)
        self.rp.loc[:, self.repeats] = self.rp[self.repeats].fillna(method='ffill')
        self.rp.loc[:, self.fixed] = self.rp[self.fixed].fillna(0)
        self.timeseries = self.rp[::-1].reset_index(drop=True)
        for sm in self.same:
            self.timeseries.loc[:, sm] = self.db[sm].values.tolist()[0]
        for cal in self.calc:
            self.timeseries.loc[:, cal] = self.timeseries['hh'].apply(lambda x: x % 24)
        self.timeseries = add_column_datetime(self.timeseries, self.totalrows, self.refdate, self.t)
        self.timeseries = self.timeseries[['state', 'distance', 'consumption']]

        # delete all unnecesary attributes
    def clean(self, keep_attr=None):
        to_rem = list(self.__dict__.keys())[:]
        if keep_attr is None:
            keep_attr = [
                    'kind',
                    'per_str',
                    'refdate',
                    'hours',
                    't',
                    'g_type',
                    'energy_consumption',
                    'df1',
                    'df2',
                    'df3',
                    'rulen',
                    'states',
                    'numb_weeks',
                    'totalrows',
                    'name',
                    'profile',
                    'timeseries'
                    ]
        for r in keep_attr:
            if r in to_rem:
                to_rem.remove(r)
        for attr in to_rem:
            self.__dict__.pop(attr, None)
        del to_rem

    def run(self):
        '''
        This function returns a driving profile. No input required.
        Once it finishes the following attributes can be called.
        Attributes:
                'kind',
                'per_str',
                'refdate',
                'hours',
                't',
                'g_type',
                'energy_consumption',
                'df1',
                'df2',
                'df3',
                'rulen',
                'states',
                'numb_weeks',
                'totalrows',
                'name',
                'profile',
                'timeseries'
        '''
        self.initial_conf()
        print('New profile running: ' + self.name)
        self.logdir = os.path.join('log', self.name)
        self.logdf = pd.DataFrame()
        self.start = -3
        self.flag = True
        self.days = -1
        self.prev_dest = 'home'  # it is the first state at the begining of the profile

        if self.g_type == 'commuter':
            self.initedge = np.array([self.states.index('home'), self.states.index('workplace')])
            self.initedgekm = self.init_edges_create(self.km_pairs, self.km_dest_array_code, self.states.index('workplace'))
            self.warningD = 0
            while True:
                self.warningD += 1
                if self.warningD % 100 == 0:
                    print('   "driving_profile_creation" method, loop in section "select_tour" not instatiated after %s iter. Many tours w/o trips to workplace' % self.warningD)
                self.n_day = 1
                self.select_tour()
                if not self.no_trip:
                    if not self.tour[self.tour['purpose'] == 'workplace'].empty:
                        break
            self.wpl = self.tour[self.tour['purpose'] == 'workplace']
            self.repeated = list(zip(self.wpl['departure'], self.wpl['purpose']))
            print(' Departure time to workplace set for commuter: ', self.repeated)
        elif self.g_type == 'freetime':
            self.n_day = 1
            self.day = self.weeks[self.n_day]['day_code']
            self.weektype = self.weeks[self.n_day]['week']
            self.cutt = []
            self.cutp = []
            while True:
                self.time_purpose_iter()
                if self.Rnd_trip[1] != 'home':
                    break

            self.initedge = np.array([self.states.index('home'), self.states.index(self.Rnd_trip[1])])
            self.initedgekm = self.init_edges_create(self.km_pairs, self.km_dest_array_code, self.states.index(self.Rnd_trip[1]))

        self.profile = pd.DataFrame()
        endflag = False
        lastflag = False
        for _ in range(self.numb_weeks):
            for n_day in self.sequence:
                self.n_day = n_day
                self.days += 1
                if self.weeks[self.n_day]['week'] == 'weekday' and self.g_type == 'commuter':
                    self.select_tour_commuter()
                else:
                    self.select_tour()
                self.prev_dest = copy.deepcopy(self.prev_dst)
                if not self.no_trip:
                    for _, row in self.tour.iterrows():
                        self.hr = row['departure'] + self.days*24.0 - self.t
                        if self.hr == self.hours-self.t:
                            self.profile.loc[self.hr, 'hr'] = self.hr
                            self.profile.loc[self.hr, 'state'] = row['state']
                            self.profile.loc[self.hr, 'departure'] = row['departure']
                            self.profile.loc[self.hr, 'last_dep'] = row['last_dep']
                            self.profile.loc[self.hr, 'purpose'] = row['purpose']
                            self.profile.loc[self.hr, 'duration'] = row['duration']
                            self.profile.loc[self.hr, 'weekday'] = self.weeks[self.n_day]['day']
                            self.profile.loc[self.hr, 'person'] = self.g_type
                            self.profile.loc[self.hr, 'distance'] = 0
                            endflag = True
                            break
                        elif self.hr > self.hours-self.t:
                            endflag = True
                            break
                        elif self.hr < self.hours-self.t:
                            self.profile.loc[self.hr, 'hr'] = self.hr
                            self.profile.loc[self.hr, 'state'] = row['state']
                            self.profile.loc[self.hr, 'departure'] = row['departure']
                            self.profile.loc[self.hr, 'last_dep'] = row['last_dep']
                            self.profile.loc[self.hr, 'purpose'] = row['purpose']
                            self.profile.loc[self.hr, 'duration'] = row['duration']
                            self.profile.loc[self.hr, 'weekday'] = self.weeks[self.n_day]['day']
                            self.profile.loc[self.hr, 'person'] = self.g_type
                            self.profile.loc[self.hr, 'distance'] = 0
                            # add driving in next row
                            self.profile.loc[self.hr+self.t, 'hr'] = self.hr + self.t
                            self.profile.loc[self.hr+self.t, 'state'] = 'driving'
                            self.profile.loc[self.hr+self.t, 'distance'] = row['distance']
                if endflag:
                    lastflag = True
                    break
            if lastflag:
                break
        if not self.profile.empty:
            if self.profile['hr'].iloc[-1] < self.hours-self.t:
                self.profile.loc[self.hours-self.t, 'hr'] = self.hours-self.t
                self.profile.loc[self.hours-self.t, 'state'] = self.prev_dest
                self.profile.loc[self.hours-self.t, 'distance'] = 0
            elif self.profile['state'].iloc[-1] == 'driving':
                self.profile.loc[self.hours-self.t, 'hr'] = self.hours-self.t
                self.profile.loc[self.hours-self.t, 'state'] = self.profile['state'].iloc[-2]
                self.profile.loc[self.hours-self.t, 'distance'] = 0
            self.fill_rows()
            self.clean()
        else:
            print('   Empty profile. Running again...   This occurs either high prob. of zero trips per day or/and few hours time series (couple of days)')
            self.clean(['kind', 'per_str', 'refdate', 'hours', 't', 'g_type', 'energy_consumption',
                        'df1', 'df2', 'df3', 'rulen', 'states', 'numb_weeks', 'totalrows', 'name'])
            self.run()
        print('Profile done: ' + self.name)

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
        print('=== profile saved: ' + filepath)
