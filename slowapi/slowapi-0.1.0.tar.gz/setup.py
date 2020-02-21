# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['slowapi']

package_data = \
{'': ['*']}

install_requires = \
['limits>=1.5,<2.0', 'redis>=3.4.1,<4.0.0']

setup_kwargs = {
    'name': 'slowapi',
    'version': '0.1.0',
    'description': 'A rate limiting extension for Starlette and Fastapi',
    'long_description': '# SlowApi\n\nA rate limiting library for Starlette and FastAPI adapted from [flask-limiter](http://github.com/alisaifee/flask-limiter).\n\nNote: this is alpha quality code still, the API may change, and things may fall apart while you try it.\n\n# Quick start\n\n## Starlette\n\n```python\n    from starlette.applications import Starlette\n    from slowapi import Limiter, _rate_limit_exceeded_handler\n\n    limiter = Limiter(key_func=get_remote_address)\n    app = Starlette()\n    app.state.limiter = limiter\n    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)\n\n    @limiter.limit("5/minute")\n    async def homepage(request: Request):\n        return PlainTextResponse("test")\n\n    app.add_route("/home", homepage)\n```\n\nThe above app will have a route `t1` that will accept up to 5 requests per minute. Requests beyond this limit will be answered with an HTTP 429 error, and the body of the view will not run.\n\n## FastAPI\n\n```python\n    from fastapi import FastAPI\n    from slowapi import Limiter, _rate_limit_exceeded_handler\n\n    limiter = Limiter(key_func=get_remote_address)\n    app = FastAPI()\n    app.state.limiter = limiter\n    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)\n\n    @app.get("/home")\n    @limiter.limit("5/minute")\n    async def homepage(request: Request):\n        return PlainTextResponse("test")\n```\n\nThis will provide the same result, but with a FastAPI app.\n\n# Features\n\nMost feature are coming from (will come from) FlaskLimiter and the underlying [limits](https://limits.readthedocs.io/).\n\nSupported now:\n- Single and multiple `limit` decorator on endpoint functions to apply limits\n- redis, memcached and memory backends to track your limits (memory as a fallback)\n- support for sync and async HTTP endpoints\n- Support for shared limits across a set of routes\n\n\n# Limitations and known issues\n\n  * There is no support for default limits yet (in other words, the only default limit supported is "unlimited")\n\n  * The `request` argument must be explicitly passed to your endpoint, or `slowapi` won\'t be able to hook into it. In other words, write:\n\n```python\n    @limiter.limit("5/minute")\n    async def myendpoint(request: Request)\n        pass\n```\n\nand not:\n\n```python\n    @limiter.limit("5/minute")\n    async def myendpoint()\n        pass\n```\n\n  * `websocket` endpoints are not supported yet.\n\n# Developing and contributing\n\nPRs are more than welcome! Please include tests for your changes :)\n\nThe package uses [poetry](https://python-poetry.org) to manage dependencies. To setup your dev env:\n\n```bash\n$ poetry install\n```\n\nTo run the tests:\n```bash\n$ pytest\n```\n\n# Credits\n\nCredits go to [flask-limiter](https://github.com/alisaifee/flask-limiter) of which SlowApi is a (still partial) adaptation to Starlette and FastAPI.\nIt\'s also important to mention that the actual rate limiting work is done be [limits](https://github.com/alisaifee/limits/), `slowapi` is just a wrapper around it.\n',
    'author': 'Laurent Savaete',
    'author_email': 'laurent@where.tf',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/laurents/slowapi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
