import asyncio

import pyconsoler
from pyconsoler.output import print_waiting_countdown

if __name__=="__main__":
    loop= asyncio.get_event_loop()

    loop.run_until_complete(print_waiting_countdown(2,clear=True))
    print("done")