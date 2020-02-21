"""Remove duplicated log entries keeping only most recent unique user messages.

Reason:
To avoid many entries of the same text in the database,
and to increase the log query speed, we need to delete all
rows with the same hash except the latest one.

Revision ID: 213f246e1490
Revises: 45546b047abe

"""
from alembic import op
import sqlalchemy as sa

from rasax.community.database.conversation import MessageLog

# revision identifiers, used by Alembic.
revision = "213f246e1490"
down_revision = "45546b047abe"
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)
    delete_duplicate_hash_logs(session)


def delete_duplicate_hash_logs(session: sa.orm.Session) -> None:
    message_logs = session.query(MessageLog).order_by(MessageLog.time.desc()).all()

    unique_logs_hash = set()

    for log in message_logs:
        if log.hash in unique_logs_hash:
            # delete older log
            session.delete(log)
        else:
            unique_logs_hash.add(log.hash)

    session.commit()
