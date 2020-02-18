import os
from dataclasses import dataclass
from pathlib import Path
from typing import NoReturn

from botox import Injector

from watermill.message_brokers.json_file_message_broker import JsonFileMessageBroker
from watermill.mill import WaterMill


class QuantityCalculator:
    def __init__(self):
        self.quantity = 0

    def add(self, quantity: int):
        self.quantity += quantity


@dataclass(frozen=True, eq=True)
class GoodsItem:
    title: str
    quantity: int
    price: int


def sum_good_quantities(goods_item: GoodsItem, side_effect: QuantityCalculator) -> NoReturn:
    side_effect.add(goods_item.quantity)


def single_stream_example():
    injector = Injector()
    injector.prepare(QuantityCalculator, QuantityCalculator())

    message_broker = JsonFileMessageBroker({
        GoodsItem: Path(os.path.join(os.path.dirname(__file__), 'samples/goods.json'))
    })

    mill = WaterMill(
        broker=message_broker,
        process_func=sum_good_quantities,
        stream_cls=GoodsItem,
        injector=injector
    )
    mill.run()

    calc = injector.deliver(QuantityCalculator)
    assert calc.quantity == 8


if __name__ == "__main__":
    single_stream_example()
