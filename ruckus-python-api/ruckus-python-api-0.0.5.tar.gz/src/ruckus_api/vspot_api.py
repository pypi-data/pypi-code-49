from .base import VSpotBase
from .decorators import returns_json, returns_gen, retry_on_processing, throw_for
from .exceptions import WaitForProcess, Unauthorized


DATE_FORMAT = '%Y-%m-%d'

class VSpotClient(VSpotBase):
    '''
    Documentation: https://18.228.238.187/api_explorer
    '''

    def email_login(self, email, password):
        d = self.api_keys(email, password)
        self.apikey = d.get('api_key')
        self._set_auth()
        self.role = d.get('role')
        return d

    @returns_json
    @throw_for(401, Unauthorized)
    def api_keys(self, email, password):
        data = {
                'email': email,
                'password': password,
                }
        return self.post(self.endpoint('api_keys.json'), data=data)

##### VENUES #####

    @returns_json
    def venues(self):
        '''
        Return JSON containing a list of all location IDs
        -------------------------------
        Name                   | Type
        -------------------------------
        venue_id               | string
        name                   | string
        exterior_thumbnail_url | string
        Example:
        [{
            'venue_id': 'mambo01',
            'name': 'mambo01',
            'exterior_thumbnail_url': 'https://18.228.238.187/venues/mambo01/files/exterior_thumbnail.png'
        }]
        '''
        return self.get(self.endpoint('venues.json'))

    @returns_json
    def venue(self, venue_id):
        '''
        Return JSON containing a data for one venue_id
        -
        Required: venue_id
        -----------------------------
        Name               | Type
        -----------------------------
        venue_id           | string
        name               | string
        exterior_image_url | string
        street_address     | string
        locality           | string
        region             | string
        postal_code        | string
        country_name       | string
        coordinates        | array
        ---|0              | position
           ---|time_zone_id| string
        -----------------------------
        Example:
        {
            'venue_id': 'mambo01',
             'name': 'mambo01',
             'exterior_image_url': 'https://18.228.238.187/venues/mambo01/files/exterior_image.png',
             'street_address': 'Rua São José ',
             'locality': 'Rio de Janerio',
             'region': 'Rio de Janeiro',
             'postal_code': '20010-020',
             'country_name': 'Brazil',
             'coordinates': [-22.906079, -43.17678],
             'time_zone_id': 'America/Sao_Paulo'
        }
        '''
        return self.get(self.endpoint('venues/{}.json', venue_id))

##### RADIO MAPS #####
    @returns_json
    def radio_maps(self, venue_id):
        '''
        Return radio map
        -
        Required: venue_id
        -------------------------
        Name            | Type
        -------------------------
        name            | string
        production      | boolean
        start_timestamp | string
        end_timestamp   | string
        -------------------------
        Example:
        [{
            'name': '1_0_0',
            'production': True,
            'start_timestamp': '2020-01-07T00:00:00-02:00',
            'end_timestamp': None
        }]

        '''
        return self.get(self.endpoint('venues/{}/radio_maps.json', venue_id))

    @returns_json
    def radio_map(self, venue_id, name):
        '''
        REQUIRED: venue_id and name
        -------------------------
        Name            | Type
        -------------------------
        name            | string
        production      | boolean
        start_timestamp | string
        end_timestamp   | string
        -------------------------
        Example:
        {
            'name': '1_0_0',
             'production': True,
             'start_timestamp': '2020-01-07T00:00:00-02:00',
             'end_timestamp': None,
             'width': 1889.0,
             'height': 856.0,
             'scale': 10,
             'floors': [{'number': 1,
               'display_name': 'Andar Mambo WiFi',
               'map_image_url': 'https://18.228.238.187/venues/mambo01/radio_maps/1_0_0/files/floor_1.png',
               'inside_image_url': 'https://18.228.238.187/venues/mambo01/radio_maps/1_0_0/files/floor_1_inside.png',
               'zone_maps': [
                            ]
                        }]
        }
        '''
        return self.get(self.endpoint('venues/{}/radio_maps/{}.json', venue_id, name))

##### LOCATIONS #####
    @returns_gen
    def locations_by_date(self, venue_id, date, macs=[], limit=''):
        '''
        REQUIRED: venue_id and date
        -----------------------------------------------------
        Name            | Example                   | Type
        -----------------------------------------------------
        mac             | B40C00000000              | String
        timestamp       | 2020-01-16T13:04:38-02:00 | String
        floor_number    | 0                         | Int
        x               | 0.0                       | Int
        y               | 0.0                       | Int
        located_inside  | False                     | Boolean
        zones           | []                        | Array
        -{zone_map_name |                           | String
          zone_name  }  |                           | String
        -----------------------------------------------------
        Example:
        {
            'mac': 'B40C00000000',
            'timestamp': '2020-01-16T13:04:38-02:00',
            'floor_number': 0,
            'x': 0.0,
            'y': 0.0,
            'located_inside': False,
            'zones': []
        }
        '''

        data = {
            'date': date.strftime(DATE_FORMAT),
            'limit': limit,
            'macs[]': macs
        }
        r = self.get(self.endpoint('venues/{}/locations/by_date.json', venue_id), params=data)
        return self.link_gen(r)

    @returns_json
    def locations_last_known(self, venue_id, seconds_ago=60, macs=[]):
        '''
        REQUIRED: venue_id
        -----------------------------------------------------
        Name            | Example                   | Type
        -----------------------------------------------------
        mac             | B40C00000000              | String
        timestamp       | 2020-01-16T13:04:38-02:00 | String
        floor_number    | 0                         | Int
        x               | 0.0                       | Int
        y               | 0.0                       | Int
        located_inside  | False                     | Boolean
        zones           | []                        | Array
        -{zone_map_name |                           | String
          zone_name  }  |                           | String
        -----------------------------------------------------
        Example:
        {
            'mac': 'B40C00000000',
            'timestamp': '2020-01-16T13:04:38-02:00',
            'floor_number': 0,
            'x': 0.0,
            'y': 0.0,
            'located_inside': False,
            'zones': []
        }
        '''
        data = {
            'macs[]': macs,
            'seconds_ago': seconds_ago
        }
        return self.get(self.endpoint('venues/{}/locations/last_known.json', venue_id), params=data)

##### METRICS #####
    @returns_json
    @retry_on_processing
    @throw_for(202, WaitForProcess)
    def metrics_impressions(self, venue_id, start_date, end_date, granularity='daily', floor_number='', zone_map_name='', zone_name=''):
        '''
        Required: venue_id, start_date and end_date
        ---------------------------------------------
        Name            |   Format           | Type
        ---------------------------------------------
        venue_id        |   mambo01          | String
        start_date      |   YYYY-MM-DD       | String
        end_date        |   YYYY-MM-DD       | String
        granularity     |   daily or hourly  | String
        floor_number    |   0                | Int
        zone_map_name   |                    | String
        zone_name       |                    | String
        ---------------------------------------------
        Example:
        [
          {
            "timestamp": "string",
            "impressions": [
              {
                "x": 0,
                "y": 0,
                "count": 0,
                "located_inside": 0,
                "located_outside": 0
              }
            ]
          }
        ]
        '''
        assert start_date < end_date, 'Start date should be before end date'
        if floor_number or zone_map_name or zone_name:
            assert floor_number and zone_map_name and zone_name, 'floor_number, zone_map_name and zone_name must be used together'
        data = {
                'start_date': start_date.strftime(DATE_FORMAT),
                'end_date': end_date.strftime(DATE_FORMAT),
                'granularity': granularity,
                'floor_number': floor_number,
                'zone_map_name': zone_map_name,
                'zone_name': zone_name,
                }
        return self.get(self.endpoint('venues/{}/metrics/impressions.json', venue_id), params=data)

    @returns_json
    @retry_on_processing
    @throw_for(202, WaitForProcess)
    def metrics_unique_visitors(self, venue_id, start_date, end_date, granularity='daily', floor_number='', zone_map_name='', zone_name='', list_macs=False):
        '''
        Required: venue_id, start_date and end_date
        ---------------------------------------------
        Name            |   Format           | Type
        ---------------------------------------------
        venue_id        |   mambo01          | String
        start_date      |   YYYY-MM-DD       | String
        end_date        |   YYYY-MM-DD       | String
        granularity     |   daily or hourly  | String
        floor_number    |   0                | Int
        zone_map_name   |                    | String
        zone_name       |                    | String
        list_macs       |   true or false    | String
        ---------------------------------------------
        Example:
        [
          {
            "timestamp": "string",
            "unique_visitors": 0,
            "unique_macs": [
              "string"
            ]
          }
        ]
        '''
        assert start_date < end_date, 'Start date should be before end date'
        if floor_number or zone_map_name or zone_name:
            assert floor_number and zone_map_name and zone_name, 'floor_number, zone_map_name and zone_name must be used together'
        data = {
                'start_date': start_date.strftime(DATE_FORMAT),
                'end_date': end_date.strftime(DATE_FORMAT),
                'granularity': granularity,
                'list_macs': list_macs,
                'floor_number': floor_number,
                'zone_map_name': zone_map_name,
                'zone_name': zone_name,
                }
        return self.get(self.endpoint('venues/{}/metrics/unique_visitors.json', venue_id), params=data)

    @returns_json
    @retry_on_processing
    @throw_for(202, WaitForProcess)
    def metrics_average_dwell_time(self, venue_id, start_date, end_date, floor_number='', zone_map_name='', zone_name=''):
        '''
        Required: venue_id, start_date and end_date
        ---------------------------------------------
        Name            |   Format           | Type
        ---------------------------------------------
        venue_id        |   mambo01          | String
        start_date      |   YYYY-MM-DD       | String
        end_date        |   YYYY-MM-DD       | String
        floor_number    |   0                | Int
        zone_map_name   |                    | String
        zone_name       |                    | String
        ---------------------------------------------
        Example:
        [
          {
            "timestamp": "string",
            "average_dwell_time": 0
          }
        ]
        '''
        assert start_date < end_date, 'Start date should be before end date'
        if floor_number or zone_map_name or zone_name:
            assert floor_number and zone_map_name and zone_name, 'floor_number, zone_map_name and zone_name must be used together'
        data = {
                'start_date': start_date.strftime(DATE_FORMAT),
                'end_date': end_date.strftime(DATE_FORMAT),
                'floor_number': floor_number,
                'zone_map_name': zone_map_name,
                'zone_name': zone_name,
                }
        return self.get(self.endpoint('venues/{}/metrics/average_dwell_time.json', venue_id), params=data)

    @returns_json
    @retry_on_processing
    @throw_for(202, WaitForProcess)
    def metrics_dwell_time_distribution(self, venue_id, start_date, end_date, floor_number='', zone_map_name='', zone_name=''):
        '''
        Required: venue_id, start_date and end_date
        ---------------------------------------------
        Name            |   Format           | Type
        ---------------------------------------------
        venue_id        |   mambo01          | String
        start_date      |   YYYY-MM-DD       | String
        end_date        |   YYYY-MM-DD       | String
        floor_number    |   0                | Int
        zone_map_name   |                    | String
        zone_name       |                    | String
        ---------------------------------------------
        Example:
        [
          {
            "timestamp": "string",
            "dwell_time_distribution": {
              "1-5 mins": 0,
              "6-10 mins": 0,
              "11-30 mins": 0,
              "31-60 mins": 0,
              "> 60 mins": 0
            }
          }
        ]
        '''
        assert start_date < end_date, 'Start date should be before end date'
        if floor_number or zone_map_name or zone_name:
            assert floor_number and zone_map_name and zone_name, 'floor_number, zone_map_name and zone_name must be used together'
        data = {
                'start_date': start_date.strftime(DATE_FORMAT),
                'end_date': end_date.strftime(DATE_FORMAT),
                'floor_number': floor_number,
                'zone_map_name': zone_map_name,
                'zone_name': zone_name,
                }
        return self.get(self.endpoint('venues/{}/metrics/dwell_time_distribution.json', venue_id), params=data)

    @returns_json
    @retry_on_processing
    @throw_for(202, WaitForProcess)
    def metrics_new_vs_repeat(self, venue_id, start_date, end_date, floor_number='', zone_map_name='', zone_name=''):
        '''
        Required: venue_id, start_date and end_date
        ---------------------------------------------
        Name            |   Format           | Type
        ---------------------------------------------
        venue_id        |   mambo01          | String
        start_date      |   YYYY-MM-DD       | String
        end_date        |   YYYY-MM-DD       | String
        floor_number    |   0                | Int
        zone_map_name   |                    | String
        zone_name       |                    | String
        ---------------------------------------------
        Example:
        [
          {
            "timestamp": "string",
            "new_vs_repeat": {
              "New": 0,
              "Repeat": 0
            }
          }
        ]
        '''
        assert start_date < end_date, 'Start date should be before end date'
        if floor_number or zone_map_name or zone_name:
            assert floor_number and zone_map_name and zone_name, 'floor_number, zone_map_name and zone_name must be used together'
        data = {
                'start_date': start_date.strftime(DATE_FORMAT),
                'end_date': end_date.strftime(DATE_FORMAT),
                'floor_number': floor_number,
                'zone_map_name': zone_map_name,
                'zone_name': zone_name,
                }
        return self.get(self.endpoint('venues/{}/metrics/new_vs_repeat.json', venue_id), params=data)

    @returns_json
    @retry_on_processing
    @throw_for(202, WaitForProcess)
    def metrics_repeat_count(self, venue_id, start_date, end_date, floor_number='', zone_map_name='', zone_name=''):
        '''
        Required: venue_id, start_date and end_date
        ---------------------------------------------
        Name            |   Format           | Type
        ---------------------------------------------
        venue_id        |   mambo01          | String
        start_date      |   YYYY-MM-DD       | String
        end_date        |   YYYY-MM-DD       | String
        floor_number    |   0                | Int
        zone_map_name   |                    | String
        zone_name       |                    | String
        ---------------------------------------------
        Example:
        [
          {
            "timestamp": "string",
            "repeat_count": {
              "1 time": 0,
              "2-5 times": 0,
              "6-10 times": 0,
              "> 10 times": 0
            }
          }
        ]
        '''
        assert start_date < end_date, 'Start date should be before end date'
        if floor_number or zone_map_name or zone_name:
            assert floor_number and zone_map_name and zone_name, 'floor_number, zone_map_name and zone_name must be used together'
        data = {
                'start_date': start_date.strftime(DATE_FORMAT),
                'end_date': end_date.strftime(DATE_FORMAT),
                'floor_number': floor_number,
                'zone_map_name': zone_map_name,
                'zone_name': zone_name,
                }
        return self.get(self.endpoint('venues/{}/metrics/repeat_count.json', venue_id), params=data)

    @returns_json
    @retry_on_processing
    @throw_for(202, WaitForProcess)
    def metrics_days_since_last_visit(self, venue_id, start_date, end_date, floor_number='', zone_map_name='', zone_name=''):
        '''
        Required: venue_id, start_date and end_date
        ---------------------------------------------
        Name            |   Format           | Type
        ---------------------------------------------
        venue_id        |   mambo01          | String
        start_date      |   YYYY-MM-DD       | String
        end_date        |   YYYY-MM-DD       | String
        floor_number    |   0                | Int
        zone_map_name   |                    | String
        zone_name       |                    | String
        ---------------------------------------------
        Example:
        [
          {
            "timestamp": "string",
            "days_since_last_visit": {
              "1 day": 0,
              "2-7 days": 0,
              "8-30 days": 0,
              "> 30 days": 0
            }
          }
        ]
        '''
        assert start_date < end_date, 'Start date should be before end date'
        if floor_number or zone_map_name or zone_name:
            assert floor_number and zone_map_name and zone_name, 'floor_number, zone_map_name and zone_name must be used together'
        data = {
                'start_date': start_date.strftime(DATE_FORMAT),
                'end_date': end_date.strftime(DATE_FORMAT),
                'floor_number': floor_number,
                'zone_map_name': zone_map_name,
                'zone_name': zone_name,
                }
        return self.get(self.endpoint('venues/{}/metrics/days_since_last_visit.json', venue_id), params=data)

##### DEVICES

    def devices_find(self, venue_id, ip):
        '''
        Required: venue_id and ip
        --------------------------
        Name        | Type
        --------------------------
        mac         | String
        ip          | String
        Example:
        {
            "mac": "string",
            "ip": "string"
        }
        '''
        r = self.get(self.endpoint('venues/{}/devices/{}/find.json', venue_id, ip))
        return r.json()

    def devices_ip(self, venue_id, ip):
        '''
        Required: venue_id and ip
        --------------------------
        Name        | Type
        --------------------------
        mac         | String
        ip          | String
        Example:
        {
            "mac": "string",
            "ip": "string"
        }
        '''
        r = self.get(self.endpoint('venues/{}/devices/{}.json', venue_id, ip))
        return r.json()

##### beta

    @returns_json
    @retry_on_processing
    @throw_for(202, WaitForProcess)
    def metrics_consolidated(self, venue_id, start_date, end_date, floor_number='', zone_map_name='', zone_name=''):
        assert start_date < end_date, 'Start date should be before end date'
        if floor_number or zone_map_name or zone_name:
            assert floor_number and zone_map_name and zone_name, 'floor_number, zone_map_name and zone_name must be used together'

        data = {
                'start_date': start_date.strftime(DATE_FORMAT),
                'end_date': end_date.strftime(DATE_FORMAT),
                'floor_number': floor_number,
                'zone_map_name': zone_map_name,
                'zone_name': zone_name,
                }

        return self.get(self.endpoint('venues/{}/metrics/consolidated.json', venue_id), params=data)

    @returns_json
    def metrics_time_divisions(self, venue_id, start_date, end_date, granularity='daily'):
        data = {
                'start_date': start_date.strftime(DATE_FORMAT),
                'end_date': end_date.strftime(DATE_FORMAT),
                'granularity': granularity,
                }
        return self.get(self.endpoint('venues/{}/metrics/time_divisions.json', venue_id), params=data)

    @returns_json
    @retry_on_processing
    @throw_for(202, WaitForProcess)
    def metrics_heatmap(self, venue_id, start_date, end_date, time_division, granularity='daily', floor_number='', zone_map_name='', zone_name=''):
        data = {
                'start_date': start_date.strftime(DATE_FORMAT),
                'end_date': end_date.strftime(DATE_FORMAT),
                'granularity': granularity,
                'time_division': time_division,
                'floor_number': floor_number,
                'zone_map_name': zone_map_name,
                'zone_name': zone_name,
                }

        return self.get(self.endpoint('venues/{}/metrics/heatmap.json', venue_id), params=data)

    @returns_gen
    def metrics_heatmap_range(self, venue_id, start_date, end_date, granularity='daily', floor_number='', zone_map_name='', zone_name=''):
        time_divisions = self.metrics_time_divisions(venue_id, start_date, end_date, granularity)

        return ( self.metrics_heatmap(
                    venue_id,
                    start_date,
                    end_date,
                    t,
                    granularity,
                    floor_number,
                    zone_map_name,
                    zone_name)
                 for t in time_divisions
                )

    @returns_json
    def metrics_realtime_heatmap(self, venue_id, floor_number='', zone_map_name='', zone_name=''):
        '''
        {
            "timestamp": timestamp_iso,
            "heatmap_data": [
                {
                    "floor_number": int,
                    "floor_name": str,
                    "floor_map_url": url,
                    "floor_width": float,
                    "floor_height": float,
                    "floor_scale": int,
                    "located_inside": int,
                    "located_outside": int,
                    "floor_data": [
                        {
                            "x": float,
                            "y": float,
                            "count": int
                        }
                    ]
                }
            ]
        }
        '''
        if floor_number or zone_map_name or zone_name:
            assert floor_number and zone_map_name and zone_name, 'floor_number, zone_map_name and zone_name must be used together'

        data = {
            'floor_number': floor_number,
            'zone_map_name': zone_map_name,
            'zone_name': zone_name,
        }
        return self.get(self.endpoint('venues/{}/metrics/real_time_heatmap.json', venue_id), params=data)
