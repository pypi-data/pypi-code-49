import time
import unittest
from datetime import datetime, timedelta

from inmation_api_client.model import Item, ItemValue, RawHistoricalDataQuery
from .base import TestBase


class TestReadRawHistoricalData(TestBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        date_format = '%Y-%m-%dT%H:%M:%S.000Z'
        now = datetime.now()

        start_time = (now + timedelta(-30)).strftime(date_format)
        end_time = now.strftime(date_format)

        item_name = 'ReadRawHistoricalDataItem'
        cls.item = cls.path + '/' + item_name
        cls.items = [Item(cls.item)]
        cls.queries = [
            RawHistoricalDataQuery(cls.items, start_time, end_time)
        ]

        cls.client.Mass([{
            'path': cls.item,
            'operation': 'UPSERT',
            'class': 'HolderItem',
            'ObjectName': item_name,
            'ArchiveOptions.StorageStrategy': True
        }])
        item_values = []
        for i in range(10):
            time.sleep(.1)
            item_values.append(ItemValue(cls.item, i))
        cls.client.Write(item_values)
        time.sleep(0.7)

    def test_can_read_raw_historical_data(self):
        res = self.client.ReadRawHistoricalData(self.queries)

        if res and 'error' in res.keys():
            print(res)

        self.assertEqual(res['code'], 200)

        values = res['data']['historical_data']['query_data'][0]['items'][0]['v']
        self.assertEqual(set(list(range(10))).issubset(values), True)

    def test_can_read_raw_historical_data_async(self):
        res = self.run_coro(
            self.client.ReadRawHistoricalDataAsync(self.queries))

        self.assertEqual(res['code'], 200)

        values = res['data']['historical_data']['query_data'][0]['items'][0]['v']
        self.assertEqual(set(list(range(10))).issubset(values), True)
