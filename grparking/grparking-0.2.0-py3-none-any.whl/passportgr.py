from datetime import datetime
import math
import requests
import pandas as pd
from datetime import timedelta

def get_sessions(start, end, passport_key):

    start_date        = datetime.strptime(start, '%m/%d/%Y %H:%M:%S')
    end_date          = datetime.strptime(end, '%m/%d/%Y %H:%M:%S')

    if end_date > datetime.now():
        end_date      = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 23, 59, 59)

    days_query        = (end_date - start_date).days
    if days_query <= 25:
        url           = 'https://ppprk.com/apps/v7/server/opmgmt/api/partner_index.php/getsettledtransaction' \
                        '?apiKey=' + passport_key + \
                        '&startdate=' + start + \
                        '&enddate=' + end
        passport_data = requests.get(url)
        passport_data = passport_data.json()
        passport_data = pd.DataFrame(passport_data['parkers'])
    else:
        passport_data         = pd.DataFrame()
        total_queries         = math.ceil(days_query/25)
        end_date              = datetime.strftime(start_date + timedelta(days=25), '%m/%d/%Y 23:59:59')
        start_date            = datetime.strftime(start_date, '%m/%d/%Y 00:00:00')
        i = 0
        while i <= total_queries:
            url               = 'https://ppprk.com/apps/v7/server/opmgmt/api/partner_index.php/getsettledtransaction' \
                                '?apiKey=834356a06f8b4fca905c65a42c7f0bb3' \
                                '&startdate=' + start_date + \
                                '&enddate=' + end_date
            passport_response = requests.get(url).json()
            passport_data     = pd.concat([passport_data,
                                          pd.DataFrame(passport_response['parkers'])],
                                          sort=True)
            print('Query ' + str(i+1) + ' of ' + str(total_queries + 1) + ' completed.')
            start_date        = (datetime
                                 .strftime(datetime
                                           .strptime(start_date,
                                                     '%m/%d/%Y %H:%M:%S') + timedelta(days=30),
                                           '%m/%d/%Y 00:00:00')
                                 )
            end_date          = (datetime
                                 .strftime(datetime
                                           .strptime(end_date,
                                                     '%m/%d/%Y %H:%M:%S') + timedelta(days=30),
                                           '%m/%d/%Y 23:59:59')
                                 )
            if datetime.strptime(start_date, '%m/%d/%Y %H:%M:%S') >= datetime.strptime(end, '%m/%d/%Y %H:%M:%S'):
                break

            if datetime.strptime(end_date, '%m/%d/%Y %H:%M:%S')   >= datetime.strptime(end, '%m/%d/%Y %H:%M:%S'):
                end_date = end

            i += 1

    return passport_data


def passport_transforms(passport_data, space_data):

    ### SESSION ID
    passport_data['Session ID'] = 'MOTU-' + passport_data['recordid'].astype('str')

    ### SESSION START
    passport_data['Session Start'] = pd.to_datetime(passport_data['entrytime'])

    ### SESSION END
    passport_data['Session End'] = pd.to_datetime(passport_data['exittime'])

    ### SESSION START HOUR
    passport_data['Session Start Hour'] = pd.to_datetime(passport_data['Session Start'].dt.strftime('%Y-%m-%d %H:00:00'))

    ### COMPARISON DATE
    passport_data['Years Ago']       = datetime.now().year - passport_data['Session Start'].dt.year

    years_ago = list(passport_data['Years Ago'].unique())

    passport_data['Comparison Date'] = None

    for number in years_ago:
        if datetime.now().year - 1 % 4 == 0:
            passport_data.loc[passport_data['Years Ago'] == number, 'Comparison Date'] = pd.to_datetime((passport_data['Session Start'] - timedelta(days=int(number) + 1))
                                                                                                        + pd.DateOffset(years=number))
        else:
            passport_data.loc[passport_data['Years Ago'] == number, 'Comparison Date'] = pd.to_datetime((passport_data['Session Start'] - timedelta(days=int(number)))
                                                                                                        + pd.DateOffset(years=number))

    # Replace Previous Years' Dates with Current Year for Comparison
    passport_data['Comparison Date'] = pd.to_datetime(passport_data['Comparison Date'].dt.strftime('%Y-%m-%d %H:00:00'))

    ### YEAR
    passport_data['Year'] = None
    passport_data.loc[passport_data['Session Start'].dt.year == datetime.now().year, 'Year'] = 'This Year'
    passport_data.loc[(passport_data['Session Start'].dt.year < datetime.now().year) &
                      (passport_data['Session Start'].dt.year > datetime.now().year - 2), 'Year'] = 'Last Year'
    passport_data.loc[passport_data['Session Start'].dt.year <= datetime.now().year - 2, 'Year'] = pd.to_numeric(datetime.now().year - passport_data['Session Start'].dt.year).astype('str') + ' Years Ago'

    ### DURATION IN MINUTES
    passport_data = passport_data.rename(columns={'parkingdurationinmins': 'Duration in Minutes'})

    ### FEE IN CENTS
    passport_data = passport_data.rename(columns={'total_net_revenue': 'Fee in Cents'})

    ### PAYMENT TYPE
    passport_data = passport_data.rename(columns={'billingtype': 'Payment Type'})

    ### RATE NAME
    passport_data['Rate Name'] = passport_data['rate_name'].str.replace(r'(?<=Max).*', '')

    ### ZONE TYPE
    passport_data['Zone Type'] = passport_data['zonetype'].str.replace('license pl', 'License Plate')
    passport_data['Zone Type'] = passport_data['Zone Type'].str.replace('space base', 'Space Based')

    ### ZONE NUMBER
    passport_data['Zone Number'] = pd.to_numeric(passport_data['zonenumber']).astype('Int64').astype('str')

    ### SPACE NUMBER
    # Remove License Plate Numbers from Data
    passport_data.loc[passport_data['spacenumber'].str.contains('[\D+]', na=False), 'spacenumber'] = None

    # Format as String
    passport_data['Space Number'] = pd.to_numeric(passport_data['spacenumber']).astype('Int64').astype('str')

    ### DATA SOURCE
    passport_data['Data Source'] = 'MOTU'

    ### SPACE COORDINATES
    # Build Space Number-Coordinates Dictionary
    space_coord = pd.read_csv(space_data)

    space_coord = dict(zip(space_coord['space_id'].loc[space_coord['space_id'].notna()].astype('Int64').astype('str'),
                           space_coord['the_geom'].loc[space_coord['space_id'].notna()]))

    # Map Space Coordinates by Space Number
    passport_data['Space Coordinates'] = passport_data['Space Number'].map(space_coord)

    # Set Empty Coordinates to Blank Strings
    passport_data.loc[passport_data['Space Coordinates'].isna(), 'Space Coordinates'] = ''

    # Format Coordinates for Socrata
    passport_data['Space Coordinates'] = passport_data['Space Coordinates'].astype(str).str.replace('POLYGON \(\(','MULTIPOLYGON (((')
    passport_data['Space Coordinates'] = passport_data['Space Coordinates'].astype(str).str.replace('\)\)', ')))')

    ### PAYSTATION OR PARKER ID
    passport_data['Paystation or Parker ID'] = passport_data['parkerentryid'].astype(str)

    # Drop Unneeded Columns
    passport_data = passport_data[['Session ID',
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

    passport_data = passport_data.drop_duplicates()

    return passport_data