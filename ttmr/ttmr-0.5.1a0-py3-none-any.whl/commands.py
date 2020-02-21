import threading
from datetime import datetime
from functools import wraps
from sqlalchemy import desc
from tabulate import tabulate
from ttmr.console import Console, GREEN, RED, BLACK, BG_WHITE
from ttmr.db import Database, load_incidences, regex_factory
from ttmr.gui import option_input, date_input, number_input, duration_input, show_timer
from ttmr.ui import (
    text_input,
    default_text_input,
)
from . import database
from ttmr.util import add_table_border


def db_session(func):

    @wraps(func)
    def _db_session(cfg):
        Session = database.init(cfg.db_path)
        cfg.db = Session()

        try:
            return func(cfg)
        finally:
            cfg.db.close()

    return _db_session


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
        new_category = database.Category(name=category_text)
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

    categories = conf.db.query(database.Category).all()

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
        project = database.Project(type=prj_type, number=prj_num, name=prj_desc)
        conf.db.add(project)
        conf.db.commit()
    except Exception as ex:
        Console.write(RED)
        Console.writeline("Update error. Incicent was not saved.")
        Console.clear_formating()
        return

    Console.write(GREEN)
    Console.write("New incident saved!")
    Console.clear_formating()
    Console.newline()

@db_session
def list_projects(conf):
    projects = conf.db.query(database.Project).all()

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
def time_entry(conf):
    """Creates a new entry. When doing so it ends the current entry
    (if there is one) and records its duration.

    When the new entry is created, the entries timer is displayed.

    """
    # fetch working data
    categories = conf.db.query(database.Category).all()
    projects = conf.db.query(database.Project).all()

    now = datetime.now()
    today = datetime(
        now.year,
        now.month,
        now.day
    )
    current_hour = now.hour if now.hour < 7 else 7
    current_minute = now.minute if now.hour < 7 else 0

    query = conf.db.query(database.Entry).filter(database.Entry.timestamp >= today)

    query = query.order_by(desc(database.Entry.timestamp))
    last_entry = query.first()

    # get inputs
    category = option_input("Category", categories)
    project = option_input("Project", projects)

    note = text_input("Notes")
    timestamp = date_input("Date")  # , timezone=conf.timezone)

    elapsed_time = 0

    prev_timestamp = last_entry.timestamp if last_entry else datetime(
        today.year,
        today.month,
        today.day,
        current_hour,
        current_minute,
        0
    )

    elapsed_time = timestamp - prev_timestamp

    duration = duration_input("Duration", str(int(elapsed_time.total_seconds() / 60)))

    entry = database.Entry(
        category=category,
        project=project,
        note=note,
        timestamp=timestamp,
        duration=duration
    )

    conf.db.add(entry)
    conf.db.commit()

    print()

    show_timer(timestamp)


@db_session
def list_entries(conf):
    entries = conf.db.query(database.Entry).all()

    Console.write(BG_WHITE)
    Console.write(BLACK)

    table = tabulate(
        [(e.category.name, e.project.identifier, e.note, e.timestamp, e.duration) for e in entries],
        headers=("CATEGORY", "PROJECT", "NOTE", "TIMESTAMP", "DURATION"),
        numalign="decimal",
    )
    Console.write(add_table_border(table))
    Console.newline()
    Console.clear_formating()
