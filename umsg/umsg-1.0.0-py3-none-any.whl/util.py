# Copyright © 2020 R.A. Stern
# SPDX-License-Identifier: LGPL-3.0-or-later

import inspect



DEPTH = 2


# ------------------------------------------------------------------ Functions -
def _caller(root=False):
    depth = DEPTH

    # walk the stack, find the first ancestor that isn't us
    while True:
        try:
            s = inspect.stack()[depth]
            m = inspect.getmodule(s[0])
            depth += 1

            if not m.__name__.startswith('umsg.'):
                break
        except IndexError:
            break

    #if root:
    #    return m.__name__.split('.')[0]

    return m.__name__
