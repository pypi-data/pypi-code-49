#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pybuildit.lib import *
from pybuildit.const import *
import sys,math
from pprint import pprint

# ノイジーなので2分探索やめておく

def _cost(buildit, devId, cur, x, span_ms = 1000):

    buildit.set_calibration_data(devId, x)

    buildit.set_ref_current(devId, cur)
    time.sleep(span_ms/1000)
    vplus = buildit.query_servo_status(devId).velocity()
    buildit.set_ref_current(devId, 0)
    buildit.wait_until(devId, lambda s,q:abs(q.velocity()) < 10)

    buildit.set_ref_current(devId, -cur)
    time.sleep(span_ms/1000)
    vminus = buildit.query_servo_status(devId).velocity()
    buildit.set_ref_current(devId, 0)
    buildit.wait_until(devId, lambda s,q:abs(q.velocity()) < 10)

    if vplus <= 0 or vminus >= 0:
        print(x, vplus, vminus, "N/A")
        return math.inf
    elif abs(vplus + vminus) > 3000:
        print(x, vplus, vminus, 'N/A')
        return math.inf
    else:
        ret = 100000 / abs(vplus - vminus)
        print(x, vplus, vminus, ret)
        return  ret


def calibrate(buildit, devId, current=2000, span_ms=1000):
    """

    キャリブレーションを行う

    Parameters
    ----------
    devId : int
        デバイスID
    current: int
        指令電流値
    """

    lastcalib = buildit.get_calibration_data(devId)
    print("last-calib: {}, current: {}, span-ms: {}" .format(lastcalib, current, span_ms))

    # rough search

    resolution = 256
    rough_skip = 16

    assert(resolution % rough_skip == 0)

    buildit.force_ready(devId)
    buildit.set_ref_current(devId, 0)

    rough_search_result = []

    for x in range(0, resolution, rough_skip):
        rough_search_result.append((x, _cost(buildit, devId, current, x, span_ms)))

    rough_best = sorted(rough_search_result, key= lambda a : a[1])[0]

    #pprint(candidates)
    rough_best_idx = rough_best[0]
    rough_best_val = rough_best[1]

    if rough_best_val == math.inf:
        sys.exit("candidates are not found")

    start_idx = (rough_best_idx - rough_skip) % resolution
    fine_search_result = []

    for i in range(2*rough_skip):
        idx = (start_idx + i) % resolution
        fine_search_result.append((idx, _cost(buildit, devId, current, idx, span_ms)))

    best = sorted(fine_search_result, key= lambda a : a[1])[0]

    print("result: {} => {}".format(lastcalib, best))

    buildit.set_calibration_data(devId, best[0])

    buildit.stop(devId)
    buildit.hold(devId)

