"""Timezones: Fun for everyone."""

import datetime

from clockifyclient.models import ClockifyDatetime


def now_local():
    """The datetime now, time zone aware for local timezone

    For marking log messages. By default python datetimes are tz naive"""
    return as_local(datetime.datetime.now())


def as_local(datetime_in):
    return ClockifyDatetime(datetime_in).datetime_local
