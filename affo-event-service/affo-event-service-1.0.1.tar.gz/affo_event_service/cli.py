from flask_script import Manager

from .application import create_app
from .extensions import clickhouse

app = create_app()

db_command = Manager(usage="Perform database migrations")

manager = Manager(app)
manager.add_command("db", db_command)


@db_command.command
def upgrade():
    clickhouse.migrate("affo_event_service.migrations")


if __name__ == "__main__":
    manager.run()
