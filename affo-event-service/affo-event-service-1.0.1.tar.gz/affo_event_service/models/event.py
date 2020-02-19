import enum

from infi.clickhouse_orm import models, fields, engines


class EventType(enum.Enum):
    pageview = 1
    event = 2
    transaction = 3
    revenue = 4


class Event(models.Model):
    t = fields.Enum8Field(EventType)
    tid = fields.StringField()
    cid = fields.NullableField(fields.UUIDField())
    cn = fields.StringField()
    cf1 = fields.NullableField(fields.StringField())
    cf2 = fields.NullableField(fields.StringField())
    cf3 = fields.NullableField(fields.StringField())
    cf4 = fields.NullableField(fields.StringField())
    cf5 = fields.NullableField(fields.StringField())

    dl = fields.NullableField(fields.StringField())
    dr = fields.NullableField(fields.StringField())
    uip = fields.NullableField(fields.StringField())
    utt = fields.NullableField(fields.StringField())
    ua = fields.NullableField(fields.StringField())

    # Event fields
    # (Required for event type)
    ec = fields.NullableField(fields.StringField())
    ea = fields.NullableField(fields.StringField())
    el = fields.NullableField(fields.StringField())
    ev = fields.NullableField(fields.Int64Field())

    # Transaction fields
    # (Required for transaction type)
    ti = fields.NullableField(fields.StringField())
    tr = fields.NullableField(fields.Decimal64Field(scale=6))

    # Revenue fields
    r = fields.NullableField(fields.Decimal64Field(scale=6))

    event_time = fields.DateTimeField()
    event_date = fields.DateField(materialized="toDate(event_time)")

    engine = engines.MergeTree("event_date", ("tid", "event_date"))

    @classmethod
    def table_name(cls):
        return "events"
