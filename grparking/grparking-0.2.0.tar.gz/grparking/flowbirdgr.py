from datetime import datetime
import math
import requests
import pandas as pd
from io import StringIO
from datetime import timedelta
import time

def get_sessions(start, end):
    start_date = datetime.strptime(start, '%Y%m%d%H%M%S')
    end_date = datetime.strptime(end, '%Y%m%d%H%M%S')

    if end_date > datetime.now():
        end_date = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 23, 59, 59)
    days_query = (end_date - start_date).days

    if days_query < 6:
        fb_url = 'https://my.parkfolio.com/drdirect.php'
        fb_params = {'login': 'grandrapids_dr',
                     'password': 'yZ9kjPBKNHzxd2dx',
                     'report': 'transaction_history',
                     'startdate': start,
                     'enddate': end}
        fb_response_data = requests.post(fb_url, data=fb_params)
        flowbird_data = pd.read_csv(StringIO(fb_response_data.text))
        print('Query completed. ' + str(len(flowbird_data)) + ' rows of data pulled.')

    else:
        flowbird_data = pd.DataFrame()
        total_queries = math.ceil(days_query / 5)
        end_date = datetime.strftime(start_date + timedelta(days=5), '%Y%m%d235959')
        start_date = datetime.strftime(start_date, '%Y%m%d000000')

        i = 0
        while i <= total_queries:
            if i > 0:
                print('Waiting 70 seconds for next query to avoid API limits.')
                time.sleep(70)
            fb_url = 'https://my.parkfolio.com/drdirect.php'
            fb_params = {'login': 'grandrapids_dr',
                         'password': 'yZ9kjPBKNHzxd2dx',
                         'report': 'transaction_history',
                         'startdate': start_date,
                         'enddate': end_date}
            fb_response_data = requests.post(fb_url, data=fb_params)
            flowbird_data = pd.concat([flowbird_data,
                                       pd.read_csv(StringIO(fb_response_data.text))],
                                      sort=True,
                                      ignore_index=True
                                      )
            print('Query ' + str(i + 1) + ' of ' + str(total_queries + 1) + ' completed.')
            start_date = (datetime
                          .strftime(datetime
                                    .strptime(start_date,
                                              '%Y%m%d%H%M%S') + timedelta(days=5),
                                    '%Y%m%d000000')
                          )
            end_date = (datetime
                        .strftime(datetime
                                  .strptime(end_date,
                                            '%Y%m%d%H%M%S') + timedelta(days=5),
                                  '%Y%m%d235959')
                        )

            if datetime.strptime(start_date, '%Y%m%d%H%M%S') >= datetime.strptime(end, '%Y%m%d%H%M%S'):
                break

            if datetime.strptime(end_date, '%Y%m%d%H%M%S') >= datetime.strptime(end, '%Y%m%d%H%M%S'):
                end_date = end

            i += 1

    return flowbird_data


def flowbird_transforms(flowbird_data, meter_data, zone_data):

    ### SESSION ID
    flowbird_data['Session ID'] = 'FB-' + pd.to_numeric(flowbird_data['SYSTEM_ID']).astype('Int64').astype('str')

    ### SESSION START
    flowbird_data['Session Start'] = pd.to_datetime(flowbird_data['METER_DATE'], format='%Y-%m-%d %H:%M:%S.%f')

    ### SESSION END
    flowbird_data['Session End'] = pd.to_datetime(flowbird_data['END_DATE'], format='%Y-%m-%d %H:%M:%S.%f')

    ### YEAR
    flowbird_data['Year'] = None

    # Label This Year
    flowbird_data.loc[flowbird_data['Session Start'].dt.year == datetime.now().year, 'Year'] = 'This Year'

    # Label Last Year
    flowbird_data.loc[(flowbird_data['Session Start'].dt.year < datetime.now().year) &
                      (flowbird_data['Session Start'].dt.year > datetime.now().year - 2), 'Year'] = 'Last Year'

    # Label Years prior to Last Year
    flowbird_data.loc[flowbird_data['Session Start'].dt.year <= datetime.now().year - 2, 'Year'] = pd.to_numeric(
        datetime.now().year - flowbird_data['Session Start'].dt.year).astype('str') + ' Years Ago'

    ### DURATION IN MINUTES
    flowbird_data['Duration in Minutes'] = flowbird_data['TOTAL_DURATION'] / 60

    ### FEE IN CENTS
    flowbird_data['Fee in Cents'] = flowbird_data['AMOUNT'] * 100

    ### PAYMENT TYPE
    flowbird_data = flowbird_data.rename(columns={'PAYMENT_MEAN': 'Payment Type'})

    ### ZONE NUMBER
    # Get Meter-Zone Dictionary
    meter_numbers = pd.read_csv(meter_data)

    meter_zones = dict(zip(meter_numbers['meter_id'].loc[meter_numbers['meter_id'].notna()].astype('Int64'),
                           meter_numbers['zone_id'].loc[meter_numbers['meter_id'].notna()].astype('Int64')))

    flowbird_data['Zone Number'] = flowbird_data['CIRCUIT_DESC'].str.extract('(\d+)')

    flowbird_data.loc[~flowbird_data['CIRCUIT_DESC'].str.contains('Plate', na=False), 'Zone Number'] = flowbird_data[
        'METER_CODE'].astype('Int64').map(meter_zones).astype('Int64')

    ### RATE NAME
    # Read Zone-Rate Dictionary
    zones = pd.read_csv(zone_data)

    zone_rates = dict(zip(zones['Zone Number'],
                          zones['Rate Name']))

    # Map Rate Names by Zone
    flowbird_data['Rate Name'] = pd.to_numeric(flowbird_data['Zone Number']).astype('Int64').map(zone_rates)

    ### ZONE TYPE
    flowbird_data['Zone Type'] = None
    flowbird_data.loc[flowbird_data['CIRCUIT_DESC'].str.contains('Plate', na=False), 'Zone Type'] = 'License Plate'
    flowbird_data.loc[~flowbird_data['CIRCUIT_DESC'].str.contains('Plate', na=False), 'Zone Type'] = 'Space Based'

    ### SPACE NUMBER
    flowbird_data['Space Number'] = pd.to_numeric(flowbird_data['METER_CODE']).astype('Int64').astype('str')

    ### DATA SOURCE
    flowbird_data['Data Source'] = 'Flow Bird'

    ### SESSION START HOUR
    flowbird_data['Session Start Hour'] = pd.to_datetime(flowbird_data['Session Start'].dt.strftime('%Y-%m-%d %H:00:00'))
    flowbird_data.loc[(flowbird_data['Session Start'].dt.hour < 8) & (~flowbird_data['Rate Name'].str.contains('24', na=False)), 'Session Start Hour'] = flowbird_data['Session Start Hour'].dt.strftime('%Y-%m-%d 08:00:00')

    ### COMPARISON DATE
    flowbird_data['Years Ago'] = datetime.now().year - flowbird_data['Session Start'].dt.year
    years_ago = list(flowbird_data['Years Ago'].unique())

    flowbird_data['Comparison Date'] = None

    for number in years_ago:
        if datetime.now().year - 1 % 4 == 0:
            flowbird_data.loc[flowbird_data['Years Ago'] == number, 'Comparison Date'] = (flowbird_data[
                                                                                              'Session Start'] - timedelta(
                days=int(number) + 1)) + pd.DateOffset(years=number)
        else:
            flowbird_data.loc[flowbird_data['Years Ago'] == number, 'Comparison Date'] = (flowbird_data[
                                                                                              'Session Start'] - timedelta(
                days=int(number))) + pd.DateOffset(years=number)

    # Replace Previous Years' Dates with Current Year for Comparison
    flowbird_data['Comparison Date'] = pd.to_datetime(flowbird_data['Comparison Date']).dt.strftime('%Y-%m-%d %H:00:00')

    # Move Comparison Dates outside of 24 Hour Zones that Start before 8:00 am
    flowbird_data['Comparison Date'] = pd.to_datetime(flowbird_data['Comparison Date'])
    flowbird_data.loc[(flowbird_data['Session Start'].dt.hour < 8) & (~flowbird_data['Rate Name'].str.contains('24', na=False)), 'Comparison Date'] = flowbird_data['Comparison Date'].dt.strftime('%Y-%m-%d 08:00:00')

    ### SPACE COORDINATES
    # Read Space-Coordinates Dictionary
    meter_coord = dict(zip(meter_numbers['meter_id'].loc[meter_numbers['meter_id'].notna()].astype('Int64').astype('str'),
                           meter_numbers['the_geom'].loc[meter_numbers['meter_id'].notna()]))

    # Map Coordinates to Space Numbers
    flowbird_data['Space Coordinates'] = flowbird_data['Space Number'].map(meter_coord)

    # Set Missing Coordinates to Blank String
    flowbird_data.loc[flowbird_data['Space Coordinates'].isna(), 'Space Coordinates'] = ''

    # Format Coordinates for Socrata Import
    flowbird_data['Space Coordinates'] = flowbird_data['Space Coordinates'].astype(str).str.replace('POLYGON \(\(','MULTIPOLYGON (((')
    flowbird_data['Space Coordinates'] = flowbird_data['Space Coordinates'].astype(str).str.replace('\)\)', ')))')

    ### PAYSTATION OR PARKER ID
    flowbird_data['Paystation or Parker ID'] = flowbird_data['ZONE_ID'].astype(str)

    ### DROP UNNEEDED COLUMNS AND REORDER
    flowbird_data = flowbird_data[['Session ID',
                                   'Year',
                                   'Comparison Date',
                                   'Session Start Hour',
                                   'Session Start',
                                   'Session End',
                                   'Duration in Minutes',
                                   'Fee in Cents',
                                   'Payment Type',
                                   'Rate Name',
                                   'Zone Type',
                                   'Zone Number',
                                   'Space Number',
                                   'Data Source',
                                   'Space Coordinates',
                                   'Paystation or Parker ID']]

    # Drop Duplicates from overlapping Queries
    flowbird_data = flowbird_data.drop_duplicates()

    # Return Data
    return (flowbird_data)


def parse_spaces(spaces):
    fb_space_nums = {}
    for row in spaces:
        fb_space_nums[row] = (row
                              .replace(' INACTIVE', '')
                              .replace(' (INACTIVE)', '')
                              .replace('*', '')
                              .replace(' (Neops)', ''))
        sep_id = row.split('-')
        if len(sep_id) > 1:
            if sep_id[0].startswith('28'):
                if len(sep_id[1]) == 1:
                    fb_space_nums[row] = '2800' + sep_id[1]
                else:
                    fb_space_nums[row] = '280' + sep_id[1]
            elif sep_id[0].startswith('60'):
                if len(sep_id[1]) == 3:
                    fb_space_nums[row] = sep_id[0] + sep_id[1]
                elif len(sep_id[1]) == 2:
                    fb_space_nums[row] = sep_id[0] + '0' + sep_id[1]
                else:
                    fb_space_nums[row] = sep_id[0] + '00' + sep_id[1]
            else:
                fb_space_nums[row] = sep_id[0] + sep_id[1]
    return (spaces.map(fb_space_nums))