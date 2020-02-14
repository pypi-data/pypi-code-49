# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tinvest']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6,<4.0', 'pydantic>=1.2,<2', 'requests>=2.22,<3.0']

setup_kwargs = {
    'name': 'tinvest',
    'version': '1.0.16',
    'description': 'Tinkoff Invest',
    'long_description': '# T-Invest\n\n[![Build Status](https://api.travis-ci.com/daxartio/tinvest.svg?branch=master)](https://travis-ci.com/daxartio/tinvest)\n[![PyPI](https://img.shields.io/pypi/v/tinvest)](https://pypi.org/project/tinvest/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tinvest)](https://www.python.org/downloads/)\n[![Codecov](https://img.shields.io/codecov/c/github/daxartio/tinvest)](https://travis-ci.com/daxartio/tinvest)\n[![GitHub last commit](https://img.shields.io/github/last-commit/daxartio/tinvest)](https://github.com/daxartio/tinvest)\n[![Tinvest](https://img.shields.io/github/stars/daxartio/tinvest?style=social)](https://github.com/daxartio/tinvest)\n\n```\npip install tinvest\n```\n\n```python\nimport asyncio\n\nimport tinvest\n\nTOKEN = "<TOKEN>"\n\nevents = tinvest.StreamingEvents()\n\n\n@events.candle()\nasync def handle_candle(\n    api: tinvest.StreamingApi, payload: tinvest.CandleStreamingSchema\n):\n    print(payload)\n\n\n@events.orderbook()\nasync def handle_orderbook(\n    api: tinvest.StreamingApi, payload: tinvest.OrderbookStreamingSchema\n):\n    print(payload)\n\n\n@events.instrument_info()\nasync def handle_instrument_info(\n    api: tinvest.StreamingApi, payload: tinvest.InstrumentInfoStreamingSchema\n):\n    print(payload)\n\n\n@events.error()\nasync def handle_error(\n    api: tinvest.StreamingApi, payload: tinvest.ErrorStreamingSchema\n):\n    print(payload)\n\n\n@events.startup()\nasync def startup(api: tinvest.StreamingApi):\n    await api.candle.subscribe("BBG0013HGFT4", "1min")\n    await api.orderbook.subscribe("BBG0013HGFT4", 5, "123ASD1123")\n    await api.instrument_info.subscribe("BBG0013HGFT4")\n\n\n@events.cleanup()\nasync def cleanup(api: tinvest.StreamingApi):\n    await api.candle.unsubscribe("BBG0013HGFT4", "1min")\n    await api.orderbook.unsubscribe("BBG0013HGFT4", 5)\n    await api.instrument_info.unsubscribe("BBG0013HGFT4")\n\n\nasync def main():\n    await tinvest.Streaming(TOKEN, state={"postgres": ...}).add_handlers(events).run()\n\n\nif __name__ == "__main__":\n    try:\n        asyncio.run(main())\n    except KeyboardInterrupt:\n        pass\n\n```\n\n```python\nimport tinvest\n\nTOKEN = "<TOKEN>"\n\nclient = tinvest.SyncClient(TOKEN)\napi = tinvest.PortfolioApi(client)\n\nresponse = api.portfolio_get()  # requests.Response\nif response.status_code == 200:\n    print(response.parse_json())  # tinvest.PortfolioResponse\n```\n\n```python\n# Handle error\n...\napi = tinvest.OperationsApi(client)\n\nresponse = api.operations_get("", "")\nif response.status_code != 200:\n    print(response.parse_error())  # tinvest.Error\n```\n\n```python\nimport asyncio\nimport tinvest\n\nTOKEN = "<TOKEN>"\n\nclient = tinvest.AsyncClient(TOKEN)\napi = tinvest.PortfolioApi(client)\n\n\nasync def request():\n    async with api.portfolio_get() as response:  # aiohttp.ClientResponse\n        if response.status == 200:\n            print(await response.parse_json())  # tinvest.PortfolioResponse\n\n\nloop = asyncio.get_event_loop()\nloop.run_until_complete(request())\n```',
    'author': 'Danil Akhtarov',
    'author_email': 'daxartio@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/tinvest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
