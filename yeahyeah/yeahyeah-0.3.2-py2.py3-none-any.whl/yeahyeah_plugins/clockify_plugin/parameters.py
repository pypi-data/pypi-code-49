"""Custom click data types

"""
import datetime
import re

import click

from yeahyeah_plugins.clockify_plugin.time import now_local


class TimeParamType(click.ParamType):
    """A parameter to indicate the time. Time zone aware.

    Is either an absolute time like 14:54
    Or a relative time like +10 (in 10 minutes) or -2:30 (2 hours and 30 minutes ago)

    """

    name = "time"

    absolute_time = re.compile("^([0-9]+):([0-9]+)$")  # 14:23
    add_time_hour_min = re.compile("^\\+([0-9]+):([0-9]+)$")  # +2:13
    subtract_time_hour_min = re.compile("^-([0-9]+):([0-9]+)$")  # -1:45
    add_time_min = re.compile("^\\+([0-9]+)$")  # +10
    subtract_time_min = re.compile("^-([0-9]+)$")  # -18

    def convert(self, value, param, ctx):
        if not value:
            return None
        if self.absolute_time.match(value):
            hour, minute = self.absolute_time.match(value).groups()
            try:
                return now_local().replace(hour=int(hour), minute=int(minute))
            except ValueError as e:
                self.fail(f"Error: {e}", param, ctx)
        elif self.add_time_hour_min.match(value):
            hours, minutes = self.add_time_hour_min.match(value).groups()
            return now_local() + datetime.timedelta(
                hours=int(hours), minutes=int(minutes)
            )
        elif self.subtract_time_hour_min.match(value):
            hours, minutes = self.subtract_time_hour_min.match(value).groups()
            return now_local() - datetime.timedelta(
                hours=int(hours), minutes=int(minutes)
            )
        elif self.add_time_min.match(value):
            minutes = self.add_time_min.match(value).groups()[0]
            return now_local() + datetime.timedelta(minutes=int(minutes))
        elif self.subtract_time_min.match(value):
            minutes = self.subtract_time_min.match(value).groups()[0]
            return now_local() - datetime.timedelta(minutes=int(minutes))
        else:
            self.fail(
                "expected absolute time (e.g. 14:34) or time delta (e.g. -10, -2:30, +1:15). "
                f"Got {value} of type {type(value).__name__}",
                param,
                ctx,
            )


TIME = TimeParamType()
