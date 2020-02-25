"""Synchronous polling-based echo.

NOTE: this test is currently broken.
"""

# Builtins

# import cProfile  # for profiling
# import pstats  # for profiling
import time  # for testing

# Packages
from phylline.links.loopback import TopLoopbackLink

from phyllo.io.polling.stack import PollingPipelineBottomCoupler
from phyllo.protocol.application.stacks import make_minimal
from phyllo.protocol.communication import AutomaticStack
from phyllo.protocol.stacks import make_stack


def run(coupler, limit=None):
    """Repeatedly update the sender."""
    counter = 0
    start_time = time.time()
    coupler.update_clock()
    data = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x00'
    coupler.pipeline_one.send(data)
    try:
        while True:
            while coupler.pipeline_one.has_receive():  # application logic goes here
                coupler.update_clock()
                data = coupler.pipeline_one.receive()
                # print('Sending: {}'.format(data))
                counter += 1
                if counter % 2500 == 0:
                    print(
                        'Exchanged {} echoes so far ({:.4} echoes per second)'
                        .format(counter, counter / (time.time() - start_time))
                    )
                coupler.pipeline_one.send(data)  # just loopback manually
                if counter == limit:
                    raise KeyboardInterrupt
    except KeyboardInterrupt:
        pass
    print(
        'Exchanged {} echoes ({:.4} echoes per second)'
        .format(counter, counter / (time.time() - start_time))
    )
    print('Last data echoed: {}'.format(data))


def main():
    """Run loopback test."""
    coupler = PollingPipelineBottomCoupler(
        make_stack(application_stack=make_minimal),
        AutomaticStack(make_stack(), TopLoopbackLink())
    )
    print(coupler)
    run(coupler, 25000)
    print('Quitting!')


if __name__ == '__main__':
    # cProfile.run('main()', 'loopback_polling.profile')
    # p = pstats.Stats('loopback_polling.profile')
    # p.strip_dirs().sort_stats('cumulative').print_stats(30)
    main()
