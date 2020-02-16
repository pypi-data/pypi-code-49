#!/usr/bin/env python
# -*- coding: utf-8 -*-

from statsd import StatsClient
import socket

Stats = None
try:
    #TODO make a configuration
    Stats = StatsClient(host='172.22.9.157', port=9125, prefix='pipline')
except (socket.gaierror, ImportError) as e:
    log.warning("Could not configure StatsClient: ", e)



