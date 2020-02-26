import pandas as pd

from features_factory.input_features import DateTimeInputFeature, FloatInputFeature
# --- input data
from features_factory.one_component_features import OneComponentFeature
from features_factory.stack import Stack
from features_factory.two_component_features import TwoComponentFeature, DurationFeature

"""
INPUT:

   shipment_timestamp  delivery_timestamp  distance_in_m
0 2018-01-18 08:00:00 2018-01-18 18:00:00       750000.0
1 2018-01-18 08:00:00 2018-01-18 20:00:00       750000.0
2 2018-01-18 08:00:00 2018-01-18 21:00:00       750000.0
3 2018-01-18 08:00:00 2018-01-19 08:00:00       750000.0
4 2018-01-18 08:00:00 2018-01-19 12:00:00       750000.0
"""
input_df = pd.DataFrame({'shipment_timestamp': pd.to_datetime(['2018-01-18 08:00']*5),
                         'delivery_timestamp': pd.to_datetime(['2018-01-18 18:00',
                                                               '2018-01-18 20:00',
                                                               '2018-01-18 21:00',
                                                               '2018-01-19 08:00',
                                                               '2018-01-19 12:00']),
                         'distance_in_m': [750000.]*5})

# --- declare the input features
shipment = DateTimeInputFeature('shipment_timestamp')
delivery = DateTimeInputFeature('delivery_timestamp')
distance = FloatInputFeature('distance_in_m')

# --- verify that the input data are ok
# create a stack with the input features
input_features = Stack([shipment, delivery, distance])
# verify the data
error = input_features.verify(input_df)
ie = error.get_input_data_error()

if ie.has_missing_columns():
    print('missing columns: {}'.format(ie.get_missing_columns()))

if ie.has_columns_with_nan():
    print('columns with nan: {}'.format(ie.get_columns_with_nan()))

if ie.has_columns_with_wrong_format():
    print('columns with wrong format: {}'.format(ie.get_columns_with_wrong_format()))

# --- declare the distance feature, that converts the units from meters to kilometers
distance_km = OneComponentFeature('distance_in_km', distance, lambda x: x / 1000)

# --- declare the trip duration feature
duration = DurationFeature('duration_in_h', start_time_feat=shipment, end_time_feat=delivery, units='hours')

# --- declare the speed feature
speed = TwoComponentFeature('average_speed', distance_km, duration, lambda r: r[0] / r[1])

# --- declare a construction stack
stack = Stack([speed]).with_dependencies()
# and verify that there are no problems
error = stack.verify(input_df)
if not error.is_empty():
    print('there is a problem...')

# --- insert the speed feature in the df, including the _dependencies (distance_in_km and duration_in_h)
output_df = stack.insert_into(input_df)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(output_df)

"""
OUTPUT:

   shipment_timestamp  delivery_timestamp  distance_in_m  duration_in_h  distance_in_km  average_speed
0 2018-01-18 08:00:00 2018-01-18 18:00:00       750000.0           10.0           750.0      75.000000 
1 2018-01-18 08:00:00 2018-01-18 20:00:00       750000.0           12.0           750.0      62.500000 
2 2018-01-18 08:00:00 2018-01-18 21:00:00       750000.0           13.0           750.0      57.692308 
3 2018-01-18 08:00:00 2018-01-19 08:00:00       750000.0           24.0           750.0      31.250000 
4 2018-01-18 08:00:00 2018-01-19 12:00:00       750000.0           28.0           750.0      26.785714
"""
