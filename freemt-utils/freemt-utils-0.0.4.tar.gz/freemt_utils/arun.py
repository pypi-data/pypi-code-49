'''
https://stackoverflow.com/questions/55590343/asyncio-run-or-run-until-complete
'''

import sys
import asyncio


def arun(awt):
    ''' arun awaitable'''
    if sys.version_info >= (3, 7):
        return asyncio.run(awt)  # pylint: disable=no-member

    # Emulate asyncio.run() on older versions
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()

    try:
        return loop.run_until_complete(awt)
    except (KeyboardInterrupt, SystemExit):
        pass
    # finally:
        # loop.close()
        # asyncio.set_event_loop(None)
