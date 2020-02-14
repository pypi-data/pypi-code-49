import pytest
from main.utility_functions import get_exchange_data, recalculate_casino_bot_sell_price


def test_exchange_data():
    result = get_exchange_data('binance', 'TRX/BNB', '1d')
    assert len(result['candle_data']) == 500
    assert result['ticker']
    assert result['trades']


def test_recalculate_casino_bot_sell_price():
    with pytest.raises(Exception):
        assert recalculate_casino_bot_sell_price(0, 0, 0, 0, 0, 0)

    assert round(recalculate_casino_bot_sell_price(0, 0, 1, 1, 0, 0)) == 1
    assert round(recalculate_casino_bot_sell_price(0, 0, 1, 1000, 0.1, 0.05)) == 1150
    assert round(recalculate_casino_bot_sell_price(1, 10, 2, 5, 0.1, 0), 1) == 7.3
