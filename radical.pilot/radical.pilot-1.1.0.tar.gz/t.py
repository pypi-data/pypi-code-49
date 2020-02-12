#!/usr/bin/env python

import sys

import radical.pilot as rp


# ------------------------------------------------------------------------------
#
if __name__ == '__main__':


    try:
        s = rp.Session()
    except:
        sys.stdout.write('============= main\n')
        sys.stdout.flush()
        raise


# ------------------------------------------------------------------------------

