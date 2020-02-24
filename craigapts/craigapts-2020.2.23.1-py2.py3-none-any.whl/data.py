#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

def craigslists():
    """Load 'craigslists' dataset, containing info for CL's US boards.

    Data source: https://gitlab.com/everetr/craig-sites

    See `data.py` source code for exact filename.
    """
    return pd.read_csv(
        ("https://gitlab.com/everetr/craig-sites/-/raw/master/"
         "craigslists_2020-02-22_19-35-35.csv")
    )
