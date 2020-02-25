import requests
from xml.etree import ElementTree as ET
import re
import pandas as pd
from datetime import datetime
from datetime import timedelta
import ast


def get_devices(user, password):
    url = 'http://mgrvde1/AbacusWebService/ServiceSystem.asmx'

    # GET DEVICES LIST
    # API Call
    devices = requests.get(url + '/getApplicList' +
                           '?user=' + user +
                           '&pwd=' + password)

    # Parse Data
    device_data = ET.fromstring(devices.content)

    # Get Full List of Devices
    device_list = []
    for node in device_data:
        device = {'ID': node.attrib.get('ID'),
                  'Name': node.attrib.get('Name'),
                  'UId': node.attrib.get('UId')}
        device_list.append(device)

    return device_list


def get_carpark_list(user, password):
    url = 'http://mgrvde1/AbacusWebService/ServiceSystem.asmx'

    # GET DEVICES LIST
    # API Call
    xml = requests.get(url + '/getCarparkState' +
                       '?user=' + user +
                       '&pwd=' + password +
                       '&carparkNo=0')

    # Parse Data
    carpark_data = ET.fromstring(xml.content)

    # Get Full List of Carpark Numbers
    carpark_list = []

    for node in carpark_data:
        carpark = {}
        for item in list(node):
            tag = re.sub(r'{.*?}', '', item.tag).replace('Carpark', '')
            carpark[tag] = item.text
        carpark_list.append(carpark)

    return carpark_list


def get_occupancy(user, password, park_number):
    url = 'http://mgrvde1/AbacusWebService/ServiceSystem.asmx'

    if isinstance(park_number, list):
        carpark_counts = []

        for x in park_number:
            if x['Number'] != '99' and x['Number'] != '20000':
                xml = requests.get(url + '/getCarparkCounter' +
                                   '?user=' + user +
                                   '&pwd=' + password +
                                   '&system=1&carparkNo=' + x['Number'])

                # Parse Data
                carpark_data = ET.fromstring(xml.content)

                # Get Full List of Devices
                carpark = {'Lot': x['Name']}
                for node in carpark_data:
                    tag = re.sub(r'{.*?}', '', node.tag)
                    carpark[tag] = node.text
                carpark_counts.append(carpark)

    else:
        # GET DEVICES LIST
        # API Call
        xml = requests.get(url + '/getCarparkCounter' +
                           '?user=' + user +
                           '&pwd=' + password +
                           '&system=1&carparkNo=' + park_number)

        # Parse Data
        carpark_data = ET.fromstring(xml.content)

        # Get Full List of Devices
        carpark_counts = []
        carpark = {}
        for node in carpark_data:
            tag = re.sub(r'{.*?}', '', node.tag)
            carpark[tag] = node.text
        carpark_counts.append(carpark)

    carpark_counts = pd.DataFrame(carpark_counts)

    carpark_counts['Available'] = ((pd.to_numeric(carpark_counts['MaxCarparkFull']) +
                                    pd.to_numeric(carpark_counts['MaxCarparkFullWithReservation']))
                                   - pd.to_numeric(carpark_counts['CurrentCarparkFullTotal']))

    carpark_counts = carpark_counts.rename(columns={'Lot': 'Lot Name',
                                                    'CurrentCarparkFullTotal': 'Total',
                                                    'CurrentCarparkFullWithReservation': 'Contract',
                                                    'CurrentCarparkFullWithoutReservation': 'Transient'})

    carpark_counts = pd.melt(carpark_counts,
                             id_vars='Lot Name',
                             value_vars=['Total', 'Contract', 'Transient', 'Available'],
                             var_name='Parker Type',
                             value_name='Count')

    carpark_counts['Date'] = pd.to_datetime(datetime.strftime(datetime.now(), '%Y-%m-%d %H:00:17'))

    carpark_counts['Data Source'] = 'Designa'

    carpark_counts = carpark_counts[['Date',
                                     'Data Source',
                                     'Lot Name',
                                     'Parker Type',
                                     'Count']]

    return carpark_counts


def get_events(user, password, start=None):
    url = 'http://mgrvde1/AbacusWebService/ServiceSystem.asmx'

    xml = requests.get(url + '/getEventLastNumber' +
                       '?user=' + user +
                       '&pwd=' + password +
                       '&system=1')

    event_number = int(ET.fromstring(xml.content).text)

    if start == None:

        events = []

        more_events = True

        while more_events == True:
            xml = requests.get(url + '/getEventInfo' +
                               '?user=' + user +
                               '&pwd=' + password +
                               '&system=1' +
                               '&eventNo=' + str(event_number))

            event_data = ET.fromstring(xml.content)

            if len(event_data) > 0:
                event = {}
                for node in event_data:
                    tag = re.sub(r'{.*?}', '', node.tag)
                    event[tag] = node.text
                events.append(event)
            else:
                more_events = False

            event_number -= 1

    else:

        events = []

        while event_number >= start:
            xml = requests.get(url + '/getEventInfo' +
                               '?user=' + user +
                               '&pwd=' + password +
                               '&system=1' +
                               '&eventNo=' + str(event_number))

            event_data = ET.fromstring(xml.content)

            event = {}
            for node in event_data:
                tag = re.sub(r'{.*?}', '', node.tag)
                event[tag] = node.text
            events.append(event)

            event_number -= 1

    return events


def get_entries(user, password, start=None):
    url = 'http://mgrvde1/AbacusWebService/ServiceSystem.asmx'

    xml = requests.get(url + '/getEventLastNumber' +
                       '?user=' + user +
                       '&pwd=' + password +
                       '&system=1')

    event_number = int(ET.fromstring(xml.content).text)

    if start == None:

        events = []

        more_events = True

        while more_events == True:
            xml = requests.get(url + '/getEventInfo' +
                               '?user=' + user +
                               '&pwd=' + password +
                               '&system=1' +
                               '&eventNo=' + str(event_number))

            event_data = ET.fromstring(xml.content)

            if len(event_data) > 0:
                event = {}
                for node in event_data:
                    tag = re.sub(r'{.*?}', '', node.tag)
                    event[tag] = node.text
                if event['Event_tcc_type'] == 1:
                    events.append(event)
            else:
                more_events = False

            event_number -= 1

    else:

        events = []

        while event_number >= start:
            xml = requests.get(url + '/getEventInfo' +
                               '?user=' + user +
                               '&pwd=' + password +
                               '&system=1' +
                               '&eventNo=' + event_number)

            event_data = ET.fromstring(xml.content)

            event = {}
            for node in event_data:
                tag = re.sub(r'{.*?}', '', node.tag)
                event[tag] = node.text
            if event['Event_tcc_type'] == 1:
                events.append(event)

            event_number -= 1

    return events


def get_exits(user, password, start=None):
    url = 'http://mgrvde1/AbacusWebService/ServiceSystem.asmx'

    xml = requests.get(url + '/getEventLastNumber' +
                       '?user=' + user +
                       '&pwd=' + password +
                       '&system=1')

    event_number = int(ET.fromstring(xml.content).text)

    if start is None:

        events = []

        more_events = True

        while more_events == True:
            xml = requests.get(url + '/getEventInfo' +
                               '?user=' + user +
                               '&pwd=' + password +
                               '&system=1' +
                               '&eventNo=' + str(event_number))

            event_data = ET.fromstring(xml.content)

            if len(event_data) > 0:
                event = {}
                for node in event_data:
                    tag = re.sub(r'{.*?}', '', node.tag)
                    event[tag] = node.text
                if event['Event_tcc_type'] == 2:
                    events.append(event)
            else:
                more_events = False

            event_number -= 1

    else:

        events = []

        while event_number >= start:
            xml = requests.get(url + '/getEventInfo' +
                               '?user=' + user +
                               '&pwd=' + password +
                               '&system=1' +
                               '&eventNo=' + event_number)

            event_data = ET.fromstring(xml.content)

            event = {}
            for node in event_data:
                tag = re.sub(r'{.*?}', '', node.tag)
                event[tag] = node.text
            if event['Event_tcc_type'] == 2:
                events.append(event)

            event_number -= 1

    return events


def get_counters(user, password):
    url = 'http://mgrvde1/AbacusWebService/ServiceSystem.asmx'

    xml = requests.get(url + '/getUkkCounter' +
                       '?user=' + user +
                       '&pwd=' + password)

    counter_data = ET.fromstring(xml.content)

    counters = []

    counter = {}
    for node in counter_data:
        tag = re.sub(r'{.*?}', '', node.tag)
        counter[tag] = node.text
    counters.append(counter)

    return counters


def get_payments(user, password, stop=None):
    url = 'http://mgrvde1/AbacusWebService/ServiceSystem.asmx'

    # Set Stop to Zero if no value entered
    if stop is None:
        stop = 0

    # Get Payment Numbers
    xml = requests.get(url + '/getPaymentLastNumber' +
                       '?user=' + user +
                       '&pwd=' + password +
                       '&system=1')

    start = int(ET.fromstring(xml.content).text)

    payments = []

    while start > stop:
        xml = requests.get(url + '/getPaymentInfo' +
                           '?user=' + user +
                           '&pwd=' + password +
                           '&system=1' +
                           '&eventNo=' + str(start))

        payment_data = ET.fromstring(xml.content)

        if len(payment_data) > 0:

            payment = {'payment_number': payment_data.items()[1][1]}

            for node in payment_data:
                tag = re.sub(r'{.*?}', '', node.tag)
                payment[tag] = node.text
            payments.append(payment)

        start -= 1

    return payments


def sessions_transforms(sessions, ramps, access_path, lanes_path):
    # Format Carpark Dictionary
    carparks = {}
    for line in ramps:
        carparks[line['Number']] = line['Name']

    # Format Access Group Dictionary
    with open(access_path, 'r') as file:
        groups = ast.literal_eval(file.read())

    # Format Lanes Dictionary
    with open(lanes_path, 'r') as file:
        lanes = ast.literal_eval(file.read())

    # SESSION ID
    sessions['Session ID'] = 'DE-' + sessions['payment_number'].astype(str)

    # CARD OR TICKET NUMBER
    sessions['Card or Ticket Number'] = sessions['Qtg_tic_iso']

    # LOT NAME
    sessions['Lot Name'] = sessions['Qtg_ph_num'].map(carparks)

    # ACCESS GROUP
    sessions['Access Group'] = pd.to_numeric(sessions['Qtg_tcc_num']).astype('Int64').map(groups)
    sessions.loc[sessions['Access Group'].isna(), 'Access Group'] = 'Transient'

    # LANE
    sessions['Lane'] = pd.to_numeric(sessions['Qtg_tcc_num']).astype('Int64').map(lanes)

    # REVENUE
    sessions['Revenue'] = pd.to_numeric(sessions['Qtg_bet_brutto']) / 100

    # DURATION
    sessions['Duration'] = (pd.to_datetime(sessions['Qtg_tic_time']) - pd.to_datetime(sessions['Qtg_ein_dat'])).astype(
        'timedelta64[m]')

    # All Date Columns
    # SESSION START
    sessions['Session Start'] = pd.to_datetime(sessions['Qtg_ein_dat'])

    # SESSION END
    sessions['Session End'] = pd.to_datetime(sessions['Qtg_tic_time'])

    # SESSION START HOUR
    sessions['Session Start Hour'] = pd.to_datetime(sessions['Session Start'].dt.strftime('%Y-%m-%d %H:00:00'))

    # COMPARISON DATE
    # Set Relative Dates
    # This Year
    this_start = datetime(datetime.now().year, 1, 1, 0, 0, 0)
    this_end = datetime(datetime.now().year, 12, 31, 23, 59, 59)

    # Last Year
    if datetime.now().year - 1 % 4 == 0:
        last_start = this_start - timedelta(days=363)
        last_end = this_end - timedelta(days=363)
    else:
        last_start = this_start - timedelta(days=364)
        last_end = this_end - timedelta(days=364)

    # Initially Set Year Filter Column to Number of Years Ago
    sessions['Year'] = this_start.year - sessions['Session Start'].dt.year

    # Determine Number of Unique Years in Dataset
    years_ago = sessions['Year'].unique()

    # COMPARISON DATE
    sessions['Comparison Date'] = sessions['Session Start Hour']

    for number in years_ago:
        if number > 0:
            # Check is Current Year is Leap Year and Set Dates Accordingly
            if datetime.now().year - 1 % 4 == 0:
                sessions.loc[sessions['Year'] == number, 'Comparison Date'] = sessions[
                                                                                  'Session Start Hour'] + timedelta(
                    days=364 - int(number))
            else:
                sessions.loc[sessions['Year'] == number, 'Comparison Date'] = sessions[
                                                                                  'Session Start Hour'] + timedelta(
                    days=365 - int(number))

    # YEAR
    sessions.loc[this_start.year - sessions['Session Start'].dt.year == 0, 'Year'] = 'This Year'
    sessions.loc[this_start.year - sessions['Session Start'].dt.year == 1, 'Year'] = 'Last Year'
    sessions.loc[this_start.year - sessions['Session Start'].dt.year > 1, 'Year'] = str(
        this_start.year - sessions['Session Start'].dt.year) + ' Years Ago'

    sessions.loc[sessions['Session Start'] < datetime.strftime(this_start, '%Y-%m-%d %H:%M:%S'), 'Year'] = 'Last Year'
    sessions.loc[sessions['Session Start'] < datetime.strftime(last_start, '%Y-%m-%d %H:%M:%S'), 'Year'] = str(
        sessions['Year']) + ' Years Ago'

    # DATA SOURCE
    sessions['Data Source'] = 'Designa'

    # PARKER TYPE
    sessions['Parker Type'] = 'Transient'
    sessions.loc[sessions['Qtg_tic_iso'].str.contains('EM', na=False), 'Parker Type'] = 'Contractor'

    # COORDINATES
    sessions['Coordinates'] = None

    # REMOVE/ORDER COLUMNS TO MATCH SOCRATA DATASET
    sessions = sessions[['Session ID',
                         'Card or Ticket Number',
                         'Lot Name',
                         'Access Group',
                         'Lane',
                         'Revenue',
                         'Duration',
                         'Comparison Date',
                         'Session Start Hour',
                         'Session Start',
                         'Session End',
                         'Data Source',
                         'Parker Type',
                         'Year',
                         'Coordinates']]

    return sessions


def entries_transforms(entries, ramps, access_path, lanes_path):
    # Format Carpark Dictionary
    carparks = {}
    for line in ramps:
        carparks[line['Number']] = line['Name']

    # Format Access Group Dictionary
    with open(access_path, 'r') as file:
        groups = ast.literal_eval(file.read())

    # Check for Exits in Dataset and Remove
    if 2 in entries['Event_tcc_type']:
        exits = entries.loc[entries['Event_tcc_type'] == 2]
        entries = entries.drop(index=exits.index)

    # ENTRY ID
    entries['Entry ID'] = 'DE-' + entries['Event_id'].astype(str)

    # CARD OR TICKET NUMBER
    entries['Card or Ticket Number'] = entries['Event_tic_iso']

    # LOT NAME
    entries['Lot Name'] = entries['Event_ph_num'].astype(str).map(carparks)

    # ACCESS GROUPS
    entries['Access Group'] = 'Transient'

    for key in groups.keys():
        entries.loc[entries['Event_ph_num'] == key, 'Access Group'] = entries['Tic_para2'].map(groups[key])

    # LANE
    with open(lanes_path, 'r') as file:
        lanes = ast.literal_eval(file.read())

    entries['Lane'] = entries['Tic_tcc_num'].map(lanes)

    # All Date Columns
    # ACTIVITY TIME
    entries['Activity Time'] = pd.to_datetime(entries['Event_time'])

    # ACTIVITY TIME HOUR
    entries['Activity Time Hour'] = pd.to_datetime(entries['Activity Time'].dt.strftime('%Y-%m-%d %H:00:00'))

    # COMPARISON DATE
    # Set Relative Dates
    # This Year
    this_start = datetime(datetime.now().year, 1, 1, 0, 0, 0)
    this_end = datetime(datetime.now().year, 12, 31, 23, 59, 59)

    # Last Year
    if datetime.now().year - 1 % 4 == 0:
        last_start = this_start - timedelta(days=363)
        last_end = this_end - timedelta(days=363)
    else:
        last_start = this_start - timedelta(days=364)
        last_end = this_end - timedelta(days=364)

    # Initially Set Year Filter Column to Number of Years Ago
    entries['Year'] = this_start.year - entries['Activity Time'].dt.year

    # Determine Number of Unique Years in Dataset
    years_ago = entries['Year'].unique()

    # COMPARISON DATE
    entries['Comparison Date'] = entries['Activity Time Hour']

    for number in years_ago:
        if number > 0:
            # Check is Current Year is Leap Year and Set Dates Accordingly
            if datetime.now().year - 1 % 4 == 0:
                entries.loc[entries['Year'] == number, 'Comparison Date'] = entries['Activity Time Hour'] + timedelta(
                    days=364 - int(number))
            else:
                entries.loc[entries['Year'] == number, 'Comparison Date'] = entries['Activity Time Hour'] + timedelta(
                    days=365 - int(number))

    # YEAR
    entries.loc[this_start.year - entries['Activity Time'].dt.year == 0, 'Year'] = 'This Year'
    entries.loc[this_start.year - entries['Activity Time'].dt.year == 1, 'Year'] = 'Last Year'
    entries.loc[this_start.year - entries['Activity Time'].dt.year > 1, 'Year'] = str(
        this_start.year - entries['Activity Time'].dt.year) + ' Years Ago'

    entries.loc[entries['Activity Time'] < datetime.strftime(this_start, '%Y-%m-%d %H:%M:%S'), 'Year'] = 'Last Year'
    entries.loc[entries['Activity Time'] < datetime.strftime(last_start, '%Y-%m-%d %H:%M:%S'), 'Year'] = str(
        entries['Year']) + ' Years Ago'

    # DATA SOURCE
    entries['Data Source'] = 'Designa'

    # PARKER TYPE
    entries['Parker Type'] = None
    entries.loc[entries['Event_tic_iso'].str.contains('PM', na=False), 'Parker Type'] = 'Transient'
    entries.loc[entries['Event_tic_iso'].str.contains('EM', na=False), 'Parker Type'] = 'Contractor'

    # COORDINATES
    entries['Coordinates'] = None

    ### REORDER AND DROP COLUMNS FOR IMPORT
    entries = entries[['Entry ID',
                       'Card or Ticket Number',
                       'Lot Name',
                       'Access Group',
                       'Lane',
                       'Comparison Date',
                       'Activity Time Hour',
                       'Activity Time',
                       'Data Source',
                       'Parker Type',
                       'Year',
                       'Coordinates']]

    return entries


def exits_transforms(exits, ramps, access_path, lanes_path):
    # Format Carpark Dictionary
    carparks = {}
    for line in ramps:
        carparks[line['Number']] = line['Name']

    # Format Access Group Dictionary
    with open(access_path, 'r') as file:
        groups = ast.literal_eval(file.read())

    # Check for Entries in Dataset and Remove
    if 1 in exits['Event_tcc_type']:
        entries = exits.loc[exits['Event_tcc_type'] == 1]
        exits = exits.drop(index=entries.index)

    # EXIT ID
    exits['Exit ID'] = 'DE-' + exits['Event_id'].astype(str)

    # CARD OR TICKET NUMBER
    exits['Card or Ticket Number'] = exits['Event_tic_iso']

    # LOT NAME
    exits['Lot Name'] = exits['Event_ph_num'].astype(str).map(carparks)

    # ACCESS GROUPS
    exits['Access Group'] = 'Transient'

    for key in groups.keys():
        exits.loc[exits['Event_ph_num'] == key, 'Access Group'] = exits['Tic_para2'].map(groups[key])

    # LANE
    with open(lanes_path, 'r') as file:
        lanes = ast.literal_eval(file.read())

    exits['Lane'] = exits['Tic_tcc_num'].map(lanes)

    # All Date Columns
    # Exit Time
    exits['Exit Time'] = pd.to_datetime(exits['Event_time'])

    # Exit Time HOUR
    exits['Exit Time Hour'] = pd.to_datetime(exits['Exit Time'].dt.strftime('%Y-%m-%d %H:00:00'))

    # COMPARISON DATE
    # Set Relative Dates
    # This Year
    this_start = datetime(datetime.now().year, 1, 1, 0, 0, 0)
    this_end = datetime(datetime.now().year, 12, 31, 23, 59, 59)

    # Last Year
    if datetime.now().year - 1 % 4 == 0:
        last_start = this_start - timedelta(days=363)
        last_end = this_end - timedelta(days=363)
    else:
        last_start = this_start - timedelta(days=364)
        last_end = this_end - timedelta(days=364)

    # Initially Set Year Filter Column to Number of Years Ago
    exits['Year'] = this_start.year - exits['Exit Time'].dt.year

    # Determine Number of Unique Years in Dataset
    years_ago = exits['Year'].unique()

    # COMPARISON DATE
    exits['Comparison Date'] = exits['Exit Time Hour']

    for number in years_ago:
        if number > 0:
            # Check is Current Year is Leap Year and Set Dates Accordingly
            if datetime.now().year - 1 % 4 == 0:
                exits.loc[exits['Year'] == number, 'Comparison Date'] = exits['Exit Time Hour'] + timedelta(
                    days=364 - int(number))
            else:
                exits.loc[exits['Year'] == number, 'Comparison Date'] = exits['Exit Time Hour'] + timedelta(
                    days=365 - int(number))

    # YEAR
    exits.loc[this_start.year - exits['Exit Time'].dt.year == 0, 'Year'] = 'This Year'
    exits.loc[this_start.year - exits['Exit Time'].dt.year == 1, 'Year'] = 'Last Year'
    exits.loc[this_start.year - exits['Exit Time'].dt.year > 1, 'Year'] = str(
        this_start.year - exits['Exit Time'].dt.year) + ' Years Ago'

    exits.loc[exits['Exit Time'] < datetime.strftime(this_start, '%Y-%m-%d %H:%M:%S'), 'Year'] = 'Last Year'
    exits.loc[exits['Exit Time'] < datetime.strftime(last_start, '%Y-%m-%d %H:%M:%S'), 'Year'] = str(
        exits['Year']) + ' Years Ago'

    # DATA SOURCE
    exits['Data Source'] = 'Designa'

    # PARKER TYPE
    exits['Parker Type'] = None
    exits.loc[exits['Event_tic_iso'].str.contains('PM', na=False), 'Parker Type'] = 'Transient'
    exits.loc[exits['Event_tic_iso'].str.contains('EM', na=False), 'Parker Type'] = 'Contractor'

    # COORDINATES
    exits['Coordinates'] = None

    ### REORDER AND DROP COLUMNS FOR IMPORT
    exits = exits[['Exit ID',
                   'Card or Ticket Number',
                   'Lot Name',
                   'Access Group',
                   'Lane',
                   'Comparison Date',
                   'Exit Time Hour',
                   'Exit Time',
                   'Data Source',
                   'Parker Type',
                   'Year',
                   'Coordinates']]

    return exits


def occupancy_transforms(occupancy, ramps):
    # DATE
    occupancy['Date'] = datetime.strftime(datetime.now(), '%Y-%m-%d %H:00:00')

    # COMPARISON DATE
    # Set Relative Dates
    # This Year
    this_start = datetime(datetime.now().year, 1, 1, 0, 0, 0)
    this_end = datetime(datetime.now().year, 12, 31, 23, 59, 59)

    # Last Year
    if datetime.now().year - 1 % 4 == 0:
        last_start = this_start - timedelta(days=363)
        last_end = this_end - timedelta(days=363)
    else:
        last_start = this_start - timedelta(days=364)
        last_end = this_end - timedelta(days=364)

    # Initially Set Year Filter Column to Number of Years Ago
    occupancy['Year'] = this_start.year - occupancy['Exit Time'].dt.year

    # Determine Number of Unique Years in Dataset
    years_ago = occupancy['Year'].unique()

    # COMPARISON DATE
    occupancy['Comparison Date'] = occupancy['Exit Time Hour']

    for number in years_ago:
        if number > 0:
            # Check is Current Year is Leap Year and Set Dates Accordingly
            if datetime.now().year - 1 % 4 == 0:
                occupancy.loc[occupancy['Year'] == number, 'Comparison Date'] = occupancy['Exit Time Hour'] + timedelta(
                    days=364 - int(number))
            else:
                occupancy.loc[occupancy['Year'] == number, 'Comparison Date'] = occupancy['Exit Time Hour'] + timedelta(
                    days=365 - int(number))

    # YEAR
    occupancy.loc[this_start.year - occupancy['Exit Time'].dt.year == 0, 'Year'] = 'This Year'
    occupancy.loc[this_start.year - occupancy['Exit Time'].dt.year == 1, 'Year'] = 'Last Year'
    occupancy.loc[this_start.year - occupancy['Exit Time'].dt.year > 1, 'Year'] = str(
        this_start.year - occupancy['Exit Time'].dt.year) + ' Years Ago'

