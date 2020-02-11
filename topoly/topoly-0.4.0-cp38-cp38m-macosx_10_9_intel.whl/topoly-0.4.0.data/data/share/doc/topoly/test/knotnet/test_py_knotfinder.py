#!/usr/bin/python3
import os

import pytest
from topoly.topoly_knot import find_knots

in_file = '2efv_A'
out_file = '/tmp/2efv_A_knot.out'

@pytest.mark.cuda
def test_find_knots():
    ret = find_knots(in_file.encode('utf-8'), out_file.encode('utf-8'), 2)
    print(str(ret))
    assert abs(os.path.getsize(out_file) < os.path.getsize(in_file)) < 2000
