"""Update DNS resource names

Revision ID: 8fef9c67eb44
Revises: add1e10105f5
Create Date: 2019-07-15 11:42:54.261235

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '8fef9c67eb44'
down_revision = 'add1e10105f5'


def upgrade():
    op.execute("UPDATE account_types SET account_type = 'DNS AXFR' WHERE account_type = 'DNS: AXFR'")
    op.execute("UPDATE account_types SET account_type = 'DNS CloudFlare' WHERE account_type = 'DNS: CloudFlare'")


def downgrade():
    op.execute("UPDATE account_types SET account_type = 'DNS: AXFR' WHERE account_type = 'DNS AXFR'")
    op.execute("UPDATE account_types SET account_type = 'DNS: CloudFlare' WHERE account_type = 'DNS CloudFlare'")
