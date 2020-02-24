import sys
import threading
from contextlib import contextmanager
from datetime import datetime
from functools import wraps

from sqlalchemy import desc
from tabulate import tabulate

from ttmr.console import BG_WHITE
from ttmr.console import BLACK
from ttmr.console import GREEN
from ttmr.console import RED
from ttmr.console import Console
from ttmr.db import Database
from ttmr.db import load_incidences
from ttmr.db import regex_factory
from ttmr.gui import date_input
from ttmr.gui import duration_input
from ttmr.gui import number_input
from ttmr.gui import option_input
from ttmr.gui import show_timer
from ttmr.ui import default_text_input
from ttmr.ui import text_input
from ttmr.util import add_table_border

from . import database
from .database import Category
from .database import Entry
from .database import Project
from .util import db_session
from .util import new_session


def display_config(conf):
    Console.write(str(conf))


def load(conf):
    load_incidences(conf)


@db_session
def new_category(conf):
    category_text = text_input("Category")

    Console.newline()
    Console.newline()

    try:
        new_category = Category(name=category_text)
        conf.db.add(new_category)
        row_update = conf.db.commit()

    except Exception as ex:
        Console.write(RED)
        Console.writeline("Update error. Category was not saved.")
        Console.clear_formating()
        return

    Console.write(GREEN)
    Console.write(f"New Category {category_text} saved!")
    Console.clear_formating()
    Console.newline()


@db_session
def list_categories(conf):

    categories = Category.get_all(conf.db)

    Console.write(BG_WHITE)
    Console.write(BLACK)

    table = tabulate(
        [(c.name, c.active, c.created, c.modified) for c in categories],
        headers=("CATEGORY", "ACTIVE", "CREATED", "MODIFED"),
        numalign="decimal",
    )
    Console.write(add_table_border(table))
    Console.newline()
    Console.clear_formating()


@db_session
def new_project(conf):
    subject_text = text_input("Project/Incident")

    parse_incident_id = regex_factory(
        (
            r"^.*(?P<type>WO|INC|CRQ|FY\d\d)-?"
            r"0*(?P<number>[0-9]\d+) "
            r"(?P<description>.+)$"
        )
    )

    incident_id = parse_incident_id(subject_text) or {}

    Console.newline()

    prj_type = default_text_input("Type", incident_id.get("type", "WO"))
    prj_num = number_input("Number", incident_id.get("number", ""))
    prj_desc = default_text_input("Desc", incident_id.get("description", ""))

    Console.newline()

    try:
        project = Project(type=prj_type, number=prj_num, name=prj_desc)
        conf.db.add(project)
        conf.db.commit()
    except Exception as ex:
        Console.write(RED)
        Console.writeline("Update error. Incicent was not saved.")
        Console.writeline(f"(Error: {ex})")
        Console.clear_formating()
        return

    Console.write(GREEN)
    Console.write("New incident saved!")
    Console.clear_formating()
    Console.newline()


@db_session
def list_projects(conf):
    projects = Project.get_all(conf.db)

    Console.write(BG_WHITE)
    Console.write(BLACK)

    table = tabulate(
        [(c.identifier, c.name, c.active, c.created, c.modified) for c in projects],
        headers=("IDENTIFIER", "NAME", "ACTIVE", "CREATED", "MODIFED"),
        numalign="decimal",
    )
    Console.write(add_table_border(table))
    Console.newline()
    Console.clear_formating()


@db_session
def start_day(conf):
    """
    Set the begging time of the day.

    """
    start_category = (
        conf.db.query(Category).filter(Category.name == "Day Start").one_or_none()
    )
    start_project = (
        conf.db.query(Project).filter(Project.name == "Day Start").one_or_none()
    )

    timestamp = datetime.now()

    entry = Entry(
        category=start_category,
        project=start_project,
        note="Day Start",
        timestamp=timestamp,
        duration=0,
    )

    conf.db.add(entry)
    conf.db.commit()

    print()

    show_timer(timestamp)


@db_session
def time_entry(conf, start_entry=False):
    """Creates a new entry. When doing so it ends the current entry
    (if there is one) and records its duration.

    When the new entry is created, the entries timer is displayed.

    The timer requires that there is a Day Start Entry.
    Day Start will have a start_time and end_time that are the same.

    There are 2 ways to create entries:

    1. as a ttmr start command:
        - this will open a new entry with a start time that is set
          automatically based on the end_time of the previous entry.
        - if there is no previous entry for the day, then it will use
          the default day's start time.
        - the window remains open with a time counter that explains
          this is the count on the current timer.
        - when you close the window, the end time will be set.

    2. as a ttmr end command:
        - this will open a new entry with a start that is set
          automatically based on the end_time of the previous entry.
        - if there is no previous entry for the day, then it will use
          the default day's start time.
        - this will also set the end time.
        - the window remains open with time counter

    """
    # fetch working data
    categories = Category.get_all(conf.db)
    projects = Project.get_all(conf.db)

    current_timestamp = datetime.now()

    last_entry = Entry.get_last(conf.db, today)

    if not last_entry:
        last_entry = Entry.get_day_start_entry()

    if last_entry.end_time is None:
        last_entry.end_time = current_timestamp

    # get inputs
    category = option_input("Category", categories)
    project = option_input("Project", projects)
    note = text_input("Notes")
    start_time = date_input("Start Date", default=last_entry.end_time)

    end_time = None
    duration = 0

    if not start_entry:
        end_time = date_input("End Date", default=current_timestamp)
        elapsed_time = 0
        elapsed_time = current_timestamp - start_time
        duration = duration_input(
            "Duration", str(int(elapsed_time.total_seconds() / 60))
        )

    # create entry
    entry = Entry(
        category=category,
        project=project,
        note=note,
        start_time=last_entry.end_time,
        end_time=current_end_time,
        duration=duration,
    )

    conf.db.add(entry)
    conf.db.commit()
    conf.db.close()

    current_entry_id = entry.id

    print()

    if start_entry:
        print("Current Entry Time:")
        try:
            show_timer(current_timestamp)
        except KeyboardInterrupt:
            print("Closing current session...")
            with new_session(cfg.db_path) as db:
                current_entry = (
                    db.query(Entry).filter(Entry.id == current_entry_id).one_or_none()
                )
                current_entry.end()
                db.commit()
    else:
        print("Time since last entry:")
        show_timer(current_timestamp)


def _list_entries(list_of_entries):
    entries = [
        (e.category.name, e.project.identifier, e.note, e.timestamp, e.duration)
        for e in list_of_entries
    ]

    total_minutes = int(sum([e[4] for e in entries]))

    entries.append(("", "", "", "", total_minutes))

    Console.write(BG_WHITE)
    Console.write(BLACK)

    table = tabulate(
        entries,
        headers=("CATEGORY", "PROJECT", "NOTE", "TIMESTAMP", "DURATION"),
        numalign="decimal",
    )
    Console.write(add_table_border(table))
    Console.newline()
    Console.clear_formating()


@db_session
def list_entries(conf):
    _list_entries(Entry.get_all(conf.db))


@db_session
def list_current_weeks_entries(conf):
    _list_entries(Entry.current_week(conf.db))
