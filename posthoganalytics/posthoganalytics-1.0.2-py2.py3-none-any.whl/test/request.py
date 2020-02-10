from datetime import datetime, date
import unittest
import json
import requests

from posthoganalytics.request import post, DatetimeSerializer


class TestRequests(unittest.TestCase):

    def test_valid_request(self):
        res = post(batch=[{
            'distinct_id': 'distinct_id',
            'event': 'python event',
            'type': 'track'
        }])
        self.assertEqual(res.status_code, 200)

    def test_invalid_request_error(self):
        self.assertRaises(Exception, post, 'testsecret',
                          'https://t.posthog.com', False, '[{]')

    def test_invalid_host(self):
        self.assertRaises(Exception, post, 'testsecret',
                          't.posthog.com/', batch=[])

    def test_datetime_serialization(self):
        data = {'created': datetime(2012, 3, 4, 5, 6, 7, 891011)}
        result = json.dumps(data, cls=DatetimeSerializer)
        self.assertEqual(result, '{"created": "2012-03-04T05:06:07.891011"}')

    def test_date_serialization(self):
        today = date.today()
        data = {'created': today}
        result = json.dumps(data, cls=DatetimeSerializer)
        expected = '{"created": "%s"}' % today.isoformat()
        self.assertEqual(result, expected)

    def test_should_not_timeout(self):
        res = post(batch=[{
            'distinct_id': 'distinct_id',
            'event': 'python event',
            'type': 'track'
        }], timeout=15)
        self.assertEqual(res.status_code, 200)

    def test_should_timeout(self):
        with self.assertRaises(requests.ReadTimeout):
            post(batch=[{
                'distinct_id': 'distinct_id',
                'event': 'python event',
                'type': 'track'
            }], timeout=0.0001)
