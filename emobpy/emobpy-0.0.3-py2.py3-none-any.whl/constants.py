OPERATORS = {'last_trip_to': "==",
             'first_trip_to': "==",
             'not_last_trip_to': "!=",
             'overall_min_time_at': ">=",
             'overall_max_time_at': "<=",
             'min_state_duration': ">=",
             'max_state_duration': "<=",
             'equal_state_and_destination': "=="
             }

WEEKS = {0: {'day': 'Sunday', 'week': 'weekend', 'day_code': 'sunday'},
         1: {'day': 'Monday', 'week': 'weekday', 'day_code': 'weekdays'},
         2: {'day': 'Tuesday', 'week': 'weekday', 'day_code': 'weekdays'},
         3: {'day': 'Wednesday', 'week': 'weekday', 'day_code': 'weekdays'},
         4: {'day': 'Thursday', 'week': 'weekday', 'day_code': 'weekdays'},
         5: {'day': 'Friday', 'week': 'weekday', 'day_code': 'weekdays'},
         6: {'day': 'Saturday', 'week': 'weekend', 'day_code': 'saturday'}
         }

TIME_FREQ = {1.0: {'f': 'H'}, 0.5: {'f': '30min'}, 0.25: {'f': '15min'}}

RULE = {'weekday':
            {'n_trip_out': [1],
             'max_same_trip_times': False,
             'last_trip_to':{'home':False,'errands':False,'escort':False,'shopping':False,'leisure':False,'workplace':False},
             'first_trip_to':{'home':False,'errands':False,'escort':False,'shopping':False,'leisure':False,'workplace':False},
             'not_last_trip_to':{'home':False,'errands':False,'escort':False,'shopping':False,'leisure':False,'workplace':False},
             'at_least_one_trip':{'home':False,'errands':False,'escort':False,'shopping':False,'leisure':False,'workplace':False},
             'overall_min_time_at':{'home':False,'errands':False,'escort':False,'shopping':False,'leisure':False,'workplace':False},
             'overall_max_time_at':{'home':False,'errands':False,'escort':False,'shopping':False,'leisure':False,'workplace':False},
             'min_state_duration':{'home':0.5,'errands':0.5,'escort':0.5,'shopping':0.5,'leisure':0.5,'workplace':0.5},
             'max_state_duration':{'home':False,'errands':False,'escort':False,'shopping':False,'leisure':False,'workplace':False},
             'equal_state_and_destination':{'home':True,'errands':True,'escort':True,'shopping':True,'leisure':True,'workplace':True}
            },
        'weekend':
            {'n_trip_out': [1],
             'max_same_trip_times': False,
             'last_trip_to':{'home':False,'errands':False,'escort':False,'shopping':False,'leisure':False,'workplace':False},
             'first_trip_to':{'home':False,'errands':False,'escort':False,'shopping':False,'leisure':False,'workplace':False},
             'not_last_trip_to':{'home':False,'errands':False,'escort':False,'shopping':False,'leisure':False,'workplace':False},
             'at_least_one_trip':{'home':False,'errands':False,'escort':False,'shopping':False,'leisure':False,'workplace':False},
             'overall_min_time_at':{'home':False,'errands':False,'escort':False,'shopping':False,'leisure':False,'workplace':False},
             'overall_max_time_at':{'home':False,'errands':False,'escort':False,'shopping':False,'leisure':False,'workplace':False},
             'min_state_duration':{'home':0.5,'errands':0.5,'escort':0.5,'shopping':0.5,'leisure':0.5,'workplace':0.5},
             'max_state_duration':{'home':False,'errands':False,'escort':False,'shopping':False,'leisure':False,'workplace':False},
             'equal_state_and_destination':{'home':True,'errands':True,'escort':True,'shopping':True,'leisure':True,'workplace':True}
            }
       }

GROUPID = {'freetime':1,'commuter':2}
