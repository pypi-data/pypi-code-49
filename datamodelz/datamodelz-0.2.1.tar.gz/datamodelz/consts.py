# metadata fields
from datetime import timedelta

from dateutil.relativedelta import relativedelta

id_string = "id"
calculated_string = "calculated"
frequency_string = "frequency"
chunks_string = "chunks"  # TODO: update after system update
min_value_string = "minValue"
max_value_string = "maxValue"
start_time_string = "startTime"
is_integer_string = "isInteger"
delay_string = "delay"
name_string = "name"

# frequencies
instant_string = "instant"
daily_string = "daily"
weekly_string = "weekly"
monthly_string = "monthly"
quarterly_string = "quarterly"
annually_string = "annually"

# Note: slight differences in days when using: 30, 90, etc. days versus 1 month, 3 months, and 13 weeks.
# 90 days ~ 3 months ~ 13 weeks (which is 91 days)
frequency_to_delta = {
    instant_string: relativedelta(seconds=+1),
    daily_string: relativedelta(days=+1),
    weekly_string: relativedelta(weeks=+1),  # unused
    monthly_string: relativedelta(months=+1),
    quarterly_string: relativedelta(months=+3),
    annually_string: relativedelta(years=+1),  # unused
}

frequency_to_timedelta = {
    instant_string: timedelta(seconds=+1),
    daily_string: timedelta(days=+1),
    weekly_string: timedelta(weeks=+1),  # unused
    monthly_string: timedelta(days=30),
    quarterly_string: timedelta(weeks=13),
    annually_string: timedelta(weeks=52),  # unused
}

frequencies = [k for k in frequency_to_delta]
