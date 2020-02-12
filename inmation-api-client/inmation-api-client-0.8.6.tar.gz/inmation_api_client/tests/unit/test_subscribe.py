import asyncio
import time
import unittest
from random import randint

from inmation_api_client.model import Item, ItemValue, SubscriptionType
from .base import TestBase

TEST_VALUE = randint(1, 1000)
VALUE = None


async def unsubscribe_from_data_changes(client, sItem):
    await client.WriteAsync(ItemValue(sItem, TEST_VALUE))
    await asyncio.sleep(1.5)
    await client.UnsubscribeAsync(Item(sItem), SubscriptionType.DataChanged)


class TestSubscribe(TestBase):
    def setUp(self):
        self.item_name = 'SubscribeItem'
        self.item = self.path + '/' + self.item_name

        self.items = [Item(self.item)]

        self.client.Mass([{
            'path': self.item,
            'operation': 'UPSERT',
            'class': 'HolderItem',
            'ObjectName': self.item_name,
            'ArchiveOptions.StorageStrategy': True
        }])

    @unittest.skip
    def test_can_subscribe(self):
        def on_data_changed(*args):
            global VALUE
            items = args[1]
            if items and isinstance(items, list):
                VALUE = items[0]['v']

        self.client.OnDataChanged(on_data_changed)

        self.client.RunAsync([
            self.client.SubscribeAsync(Item(self.item), SubscriptionType.DataChanged),
            unsubscribe_from_data_changes(self.client, self.item)
        ])

        sleep_time = 0.2
        cnt = 0
        max_cnt = 30 / sleep_time  # wait max for x seconds
        while VALUE is None:
            cnt += 1
            if cnt > max_cnt:
                break
            time.sleep(sleep_time)
        self.assertEqual(VALUE, TEST_VALUE)
