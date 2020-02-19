from infi.clickhouse_orm import migrations
from affo_event_service.models.event import Event

operations = [
    migrations.CreateTable(Event),
]
