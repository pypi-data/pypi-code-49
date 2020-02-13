from . import rule
from .field import Field, StringField, BoolField, EnumField, IntField, DateField, BigIntField
from .consts import frequencies, id_string, calculated_string, frequency_string, min_value_string, max_value_string, \
    start_time_string, is_integer_string, delay_string, chunks_string


class TimeseriesMetadataField(Field):
    """
        Company Domain - I think we should take this from mainDomain. Each company should have one
        Ticker - do we use ticker/exchange directly to pull data? I thought we use EOD?
        Exchange - do we use ticker/exchange directly to pull data? I thought we use EOD?
        EOD ticker - should be exactly one. Flag cases of missing and multiple. All companies should have.
        Linkedin URL - should be exactly one, or in rare cases missing. Flag cases of missing and multiple. MOST companies should have.
        Indeed URL - should be exactly one, or in rare cases missing. Flag cases of missing and multiple.
        Comparably URL - should be exactly one, but will be missing for MANY companies. Flag cases of missing and multiple.
        Marketbeat URL - should be exactly one, or in rare cases missing. Flag cases of missing and multiple. MOST companies should have.
        Yahoo Finance URL - Is this for ESG? So only relevant for s&p500? or we need it for other things as well?
        Twitter - not too sure actually. I think should be one.
        Facebook - not too sure actually. I think should be one.
    """
    def __init__(self):
        super().__init__()
        self.name = "timeseries"
        self.value = {}

        self.id = StringField(id_string)
        self.calculated = BoolField(calculated_string)
        self.frequency = EnumField(frequency_string, frequencies)  # Check for daily, etc. more than/ less than daily -> gaps
        self.chunks = EnumField(chunks_string, frequencies)  # Used for recent data
        self.min_value = IntField(min_value_string)  # done
        self.max_value = IntField(max_value_string)  # done
        self.start_time = DateField(start_time_string)  # done
        self.is_integer = BoolField(is_integer_string)  # done
        self.delay = BigIntField(delay_string)  # goes w/ frequency. If delay =week and frequency=daily then last value should be a week ago.
        self.fields = [self.id, self.calculated, self.frequency, self.min_value, self.max_value,
                       self.start_time, self.is_integer, self.delay]
        self.rules = [rule.has_field(x.name) for x in self.fields]

    def set(self, value):
        self.value = value
        self.run_rules()
        if self.errors:  # checks for field names in value (type: dict)
            return self.errors
        self.set_fields(self.fields)
        return self.errors
