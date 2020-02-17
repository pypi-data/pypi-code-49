import json
import os
from dataclasses import dataclass
from pathlib import Path

from watermill.message_brokers.json_file_message_broker import JsonFileMessageBroker
from watermill.mill import WaterMill


@dataclass(frozen=True, eq=True)
class GoodsItem:
    title: str
    quantity: int
    price: int


@dataclass(frozen=True, eq=True)
class UpdatedGoodsItem:
    title: str
    quantity: int
    price: int


def update_goods_price(goods_item: GoodsItem) -> UpdatedGoodsItem:
    return UpdatedGoodsItem(
        title=goods_item.title,
        quantity=goods_item.quantity,
        price=int(goods_item.price * 1.1)
    )


def single_stream_example_with_result():
    input_file_name = os.path.join(os.path.dirname(__file__), 'samples/goods.json')
    output_file_name = '/tmp/updated-goods.json'

    message_broker = JsonFileMessageBroker({
        GoodsItem: Path(input_file_name),
        UpdatedGoodsItem: Path(output_file_name),
    })

    mill = WaterMill(
        broker=message_broker,
        process_func=update_goods_price,
        stream_cls=GoodsItem,
    )
    mill.run()

    with open(input_file_name, 'r') as input_file:
        input_items = json.load(input_file)

    with open(output_file_name, 'r') as result_file:
        updated_items = json.load(result_file)

    print(f'Input stream:   \n{json.dumps(input_items, sort_keys=True)}')
    print(f'Result stream:  \n{json.dumps(updated_items, sort_keys=True)}')


if __name__ == "__main__":
    single_stream_example_with_result()
