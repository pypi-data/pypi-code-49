#!/usr/bin/env python3

"""
db.py
This handels the interaction between reme and the database. It can convert
Entry objects to SQL statements and vice versa.
"""

import sqlite3
import logging
from datetime import datetime, timedelta
from entry import Entry, from_db
# import threading
# import time

###############################################################################
# TODO
# Add try blocks to all DB functions
# Add error recovery to all functions
# Add logging to all transactions
# Add a clean function that will remove entries that should have been executed
#   before the current timestamp
##############################################################################


class DB:
    """
    An object that handels interaction between reme and the DB
    """

    def __init__(self, db_path='reme.db'):
        try: 
            logging.debug(
                "db.py:__init__ - Attempting to establish a connection to the DB"
            )
            self.connection = sqlite3.connect(
                db_path, 
                detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES
            )
            logging.debug("db.py:__init__ - Connection established to DB")
            self.make_table()

        # TODO do better error handeling than this
        except Exception as e:
            logging.error("db.py:__init__ - {}".format(e))
            exit(3)

    # end __init__


    def make_table(self):
        """
        Creates the entry table if it does not already exist
        """
        try:
            for row in self.connection.execute(
                "select name from sqlite_master where type='table' \
                and name not like 'sqlite_%';"):

                if 'entries' in row:
                    logging.debug(
                        "db.py:make_table - Entries table already exists"
                    )
                    return True

            self.connection.execute(
                """
                CREATE TABLE entries (
                    uid INTEGER PRIMARY KEY AUTOINCREMENT,
                    msg TEXT NOT NULL,
                    users TEXT NOT NULL,
                    channel INTEGER NOT NULL,
                    created DATETIME,
                    executed DATETIME NOT NULL,
                    everyone INTEGER NOT NULL
                );
                """
            )

        except sqlite3.Warning:
            logging.error(
                "db.py:make_table [sqlite3.Warning] - Failed to execute the \
                entries table creation sql"
            )
            return False
        except sqlite3.OperationalError:
            logging.error(
                "db.py:make_table [sqlite3.OperationalError] - Failed to \
                create the entries table. Table might already exist"
            )

        logging.debug("db.py:make_table - New entries table created")
        return True

    def add_entry(self, entry: Entry) -> bool:
        """
        Insert an Entry object into the DB
        """
        try:
            self.connection.execute(
                """
                INSERT INTO entries(msg, users, channel, created, executed, everyone)
                VALUES(?, ?, ?, ?, ?, ?);
                """,
                (entry.msg, entry.users, entry.channel, entry.created, entry.executed, entry.everyone)
            )
            self.connection.commit()

        except sqlite3.Warning as e:
            logging.error(f"db.py:add_entry - Failed to add an entry to the DB | {e}")
            return False
        except Exception as e:
            logging.error(f"db.py:add_entry - An unknown error occured | {e}")
            return False

        logging.debug("db.py:add_entry - Added an entry to the DB")
        return True

    # end add_entry


    def close(self) -> bool:
        """
        Commits changes to the DB and closes the connection
        """
        # TODO:
        # Add error handeling and error logging
        logging.debug(
            "db.py:close - Starting to close the connection to the DB"
        )
        try:
            self.connection.commit()
            logging.debug("db.py:close - Commited transactions to the DB")
            self.connection.close()
            logging.debug("db.py:close - Connection to the DB has closed")

        except sqlite3.Warning as e:
            logging.error(
                "db.py:close - Error occured while trying to close the \
                connection to the DB | {}".format(e)
            )
            return False

        return True

    def collect(self, time: datetime) -> list:
        """
        Collects the entries from the DB
        :param timestamp datetime.datetime: A datetime to compare against the
        executed column
        :return list - The DB entries that match the given datetime
        """
        logging.debug(
            "db.py:collect - Collecting entries from the DB with datetime {}".format(time)
        )

        sql: str = f"SELECT * FROM entries WHERE executed='{time}'"
        try:
            entries: list = [from_db(row) for row in self.connection.execute(sql)]
            logging.debug(f"db.py:collect - {len(entries)} entries found with datetime {time}")
            return entries

        except sqlite3.ProgrammingError as e:
            logging.error(f"db.py:collect - There was an issue with the SQL statement | {e}")
            return []

        except sqlite3.DatabaseError as e:
            logging.error(f"db.py:collect - There was an issue with the Database | {e}")
            return []

        except sqlite3.Warning as e:
            logging.error(f"db.py:collect - Failed to retrieve entries from the DB for datetime: {time} | {e}")
            return []

        except Exception as e:
            logging.error(f"db.py:collect - An unknown error occurred | {e}")
            return []

    # end collect


    def commit(self):
        """
        Commit the database and log the results
        """
        try:
            self.connection.commit()
            logging.debug("db.py:commit - Transactions have been commited to the database")
        
        except sqlite3.Warning as e:
            logging.error(
                "db.py:commit - An error occured while trying to commit \
                transactions to the database | {}".format(e)
            )

    def remove(self, uid: int):
        """
        Remove entries from the DB
        """
        sql: str = f"DELETE FROM entries WHERE uid={uid}"
        try:
            logging.debug(f"db.py:remove - Attempting to remove row with UID: {uid}")
            self.connection.execute(sql)

        except sqlite3.Warning as e:
            logging.error(f"db.py:remove - Failed to remove row with UID: {uid} | {e}")
            return
        except Exception as e:
            logging.error(
                f"db.py:remove - An unknown error occurred while removing entry with UID: {uid} | {e}"
            )
            return

        logging.debug(f"db.py:remove - Entry with UID: {uid} has been removed")

    # end remove


    #TODO update to match the current schema 
    #TODO add performance metrics
    def gen_demo(self):
        """
        Creates dummy entries in the DB for testing purposes
        """

        # Create current time and floored to the given minute
        created = datetime.now().replace(second=0, microsecond=0)

        entries = [
            ("Take pizza out of oven", "Jason", created, created + timedelta(minutes=1)),
            ("Go to the store for milk", "Patrick", created, created + timedelta(minutes=2)),
            ("Do laundry", "Alex", created, created + timedelta(minutes=3)),
            ("Workout!", "JB", created, created + timedelta(minutes=4)),
            ("Walk around a little bit", "Alex", created, created + timedelta(minutes=5)),
            ("Smoke break!", "Alex", created, created + timedelta(minutes=5))
        ]

        for row in entries:
            self.connection.execute(
                """
                insert into entries(msg, users, attachments, created, executed)
                values (?, ?, ?, ?, ?);
                """,
                row
            )