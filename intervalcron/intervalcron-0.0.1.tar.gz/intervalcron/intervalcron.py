import datetime
from apscheduler.triggers.base import BaseTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger

class IntervalCronTrigger(BaseTrigger):
    """
    Triggers on specified intervals, based on cron.
    It is assumed, interval will be used for higher level fields and cron for lower level fields.
    
    Example: every 3 weeks on monday, every 3 months on 3rd friday

    NOTE: Not all supported fields in underlying triggers are supported in this trigger. Below are the only supported fields.

    :param int months: number of months to wait
    :param int weeks: number of weeks to wait
    :param int days: number of days to wait

    :param int|str day: day of the (1-31) or nth weekday (1st mon, 3rd fri,...)
    :param int|str day_of_week: number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)

    :param int|str hour: hour (0-23)
    :param int|str minute: minute (0-59)
    :param int|str second: second (0-59)

    :param datetime|str start_date: earliest possible date/time to trigger on (inclusive)
    :param datetime|str end_date: latest possible date/time to trigger on (inclusive)

    :param datetime.tzinfo|str timezone: time zone to use for the date/time calculations (defaults
        to scheduler timezone)

    :param int|None jitter: advance or delay the job execution by ``jitter`` seconds at most.
    """

    __slots__ = 'interval_trigger', 'cron_trigger', 'jitter'

    def __init__(self,
                 months=0, weeks=0, days=0,
                 day=None, day_of_week=None,
                 hour=None, minute=None, second=None,
                 start_date=None, end_date=None, timezone=None, jitter=None
                ):
        assert not (start_date is None)

        if months > 0:
            days = months * 30

        self.interval_trigger = IntervalTrigger(
            weeks=weeks, days=days, 
            start_date=start_date, end_date=end_date, timezone=timezone)

        self.cron_trigger = CronTrigger(
            day=day, day_of_week=day_of_week, 
            hour=hour, minute=minute, second=second, 
            start_date=start_date, end_date=end_date, timezone=timezone)

        # Jitter will be applied on final output
        self.jitter = jitter

    def get_next_fire_time(self, previous_fire_time, now):
        # Get interval next fire
        next_fire_time = self.interval_trigger.get_next_fire_time(now, now)
        
        # Get cron next fire
        # Not using previous fire time in cron
        cron_fire_time = self.cron_trigger.get_next_fire_time(None, next_fire_time)

        if not cron_fire_time is None:
            # Cron tends to go back in time, make sure it's after intervals next fire
            while cron_fire_time < next_fire_time:
                cron_fire_time = self.cron_trigger.get_next_fire_time(None, cron_fire_time + datetime.timedelta(milliseconds=1))
            # Update final next fire
            next_fire_time = cron_fire_time

        # Apply jitter
        return self._apply_jitter(next_fire_time, self.jitter, now)

    def __str__(self):
        return 'intervalcron[{}, {}]'.format(self.interval_trigger, self.cron_trigger)
