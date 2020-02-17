# Copyright (C) 2019  Nexedi SA and Contributors.
#                     Romain Courteaud <romain@nexedi.com>
#
# This program is free software: you can Use, Study, Modify and Redistribute
# it under the terms of the GNU General Public License version 3, or (at your
# option) any later version, as published by the Free Software Foundation.
#
# You can also Link and Combine this program with other software covered by
# the terms of any of the Free Software licenses or any of the Open Source
# Initiative approved licenses and Convey the resulting work. Corresponding
# source of such a combination shall include the source code for all other
# software used.
#
# This program is distributed WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See COPYING file for full licensing terms.
# See https://www.nexedi.com/licensing for rationale and options.

import peewee
from playhouse.sqlite_ext import SqliteExtDatabase
import datetime
from playhouse.migrate import migrate, SqliteMigrator


class LogDB:
    def __init__(self, sqlite_path):
        self._db = SqliteExtDatabase(
            sqlite_path, pragmas=(("journal_mode", "WAL"), ("foreign_keys", 1))
        )
        self._db.connect()

        class BaseModel(peewee.Model):
            class Meta:
                database = self._db

        # This store the start, stop, loop time of the bot
        # All other tables point to it to be able to group some info
        class Status(BaseModel):
            text = peewee.TextField()
            timestamp = peewee.TimestampField(
                primary_key=True,
                # Store millisecond resolution
                resolution=6,
                # date is in UTC
                utc=True,
                default=datetime.datetime.utcnow,
            )

        # Store the configuration modification
        class ConfigurationChange(BaseModel):
            status = peewee.ForeignKeyField(Status)
            parameter = peewee.TextField(index=True)
            value = peewee.TextField()

            class Meta:
                primary_key = peewee.CompositeKey("status", "parameter")
                # indexes = (
                # create a unique on from/to/date
                # (('status', 'parameter'), True),
                # )

        # Store the configuration modification
        class PlatformChange(BaseModel):
            status = peewee.ForeignKeyField(Status)
            parameter = peewee.TextField(index=True)
            value = peewee.TextField()

            class Meta:
                primary_key = peewee.CompositeKey("status", "parameter")

        # Store remote network status
        class NetworkChange(BaseModel):
            status = peewee.ForeignKeyField(Status)
            ip = peewee.TextField()
            transport = peewee.TextField()
            port = peewee.IntegerField()
            state = peewee.TextField()

            class Meta:
                primary_key = peewee.CompositeKey(
                    "status", "ip", "transport", "port"
                )

        class DnsChange(BaseModel):
            status = peewee.ForeignKeyField(Status)
            resolver_ip = peewee.TextField()
            domain = peewee.TextField()
            rdtype = peewee.TextField()
            response = peewee.TextField()

            class Meta:
                primary_key = peewee.CompositeKey(
                    "status", "resolver_ip", "domain", "rdtype"
                )

        class SslChange(BaseModel):
            status = peewee.ForeignKeyField(Status)
            ip = peewee.TextField()
            port = peewee.IntegerField()
            hostname = peewee.TextField()
            sha1_fingerprint = peewee.TextField(null=True)
            not_before = peewee.TimestampField(null=True, utc=True)
            not_after = peewee.TimestampField(null=True, utc=True)
            subject = peewee.TextField(null=True)
            issuer = peewee.TextField(null=True)

            class Meta:
                primary_key = peewee.CompositeKey(
                    "status", "ip", "port", "hostname"
                )

        class HttpCodeChange(BaseModel):
            status = peewee.ForeignKeyField(Status)
            ip = peewee.TextField()
            url = peewee.TextField()
            status_code = peewee.IntegerField()
            total_seconds = peewee.FloatField(default=0)

            class Meta:
                primary_key = peewee.CompositeKey("status", "ip", "url")

        self.Status = Status
        self.ConfigurationChange = ConfigurationChange
        self.PlatformChange = PlatformChange
        self.NetworkChange = NetworkChange
        self.DnsChange = DnsChange
        self.HttpCodeChange = HttpCodeChange
        self.SslChange = SslChange

    def createTables(self):
        # http://www.sqlite.org/pragma.html#pragma_user_version
        db_version = self._db.pragma("user_version")
        expected_version = 3
        if db_version != expected_version:
            with self._db.transaction():

                if db_version == 0:
                    # version 0 (no table)
                    self._db.create_tables(
                        [
                            self.Status,
                            self.ConfigurationChange,
                            self.HttpCodeChange,
                            self.NetworkChange,
                            self.PlatformChange,
                            self.DnsChange,
                        ]
                    )

                if db_version <= 1:
                    # version 1 without SSL support
                    self._db.create_tables([self.SslChange])

                if (0 < db_version) and (db_version <= 2):
                    # version 2 without the http total_seconds column
                    migrator = SqliteMigrator(self._db)
                    migrate(
                        migrator.add_column(
                            "HttpCodeChange",
                            "total_seconds",
                            self.HttpCodeChange.total_seconds,
                        )
                    )

                if db_version >= expected_version:
                    raise ValueError("Can not downgrade SQLite DB")

                self._db.pragma("user_version", expected_version)

    def close(self):
        self._db.close()
