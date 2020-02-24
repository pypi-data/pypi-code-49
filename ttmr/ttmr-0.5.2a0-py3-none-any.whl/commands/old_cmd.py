from functools import wraps

from sqlalchemy import desc

from ttmr.console import BG_WHITE
from ttmr.console import BLACK
from ttmr.console import GREEN
from ttmr.console import RED
from ttmr.console import Console
from ttmr.db import Database
from ttmr.db import load_incidences
from ttmr.db import regex_factory
from ttmr.ui import _date_input
from ttmr.ui import _option_input
from ttmr.ui import bool_input
from ttmr.ui import date_input
from ttmr.ui import default_text_input
from ttmr.ui import duration_input
from ttmr.ui import number_input
from ttmr.ui import option_input
from ttmr.ui import show_timer
from ttmr.ui import text_input
from ttmr.util import add_table_border

from . import database


def db_session(func):
    @wraps(func)
    def _db_session(cfg):
        Session = database.init(cfg._dbfile)
        cfg._db = Session()

        try:
            return func(cfg)
        finally:
            cfg._db.close()

    return _db_session


def display_config(conf):
    Console.write(str(conf))


def load(conf):
    load_incidences(conf)


def new_incident(conf):
    subject_text = text_input("Email Subject")

    parse_incident_id = regex_factory(
        (
            r"^.*(?P<type>WO|INC|CRQ|FY\d\d)"
            r"0*(?P<number>[0-9]\d+) "
            r".*Description: "
            r"(?P<description>.+)"
            r"(\d+ [KMG]B|\d+:\d\d [AP]M).*$"
        )
    )

    incident_id = parse_incident_id(subject_text) or {}

    Console.newline()
    Console.newline()

    inc_type = default_text_input("Type", incident_id.get("type", "WO"))
    inc_num = number_input("Number", incident_id.get("number", ""))
    inc_desc = default_text_input("Desc", incident_id.get("description", ""))

    Console.newline()

    with Database(conf.sqlite, conf.dt) as db:
        row_update = db.record_incident(inc_type, inc_num, inc_desc)

    if row_update != 1:
        Console.write(RED)
        Console.writeline("Update error. Incicent was not saved.")
        Console.clear_formating()
        return

    Console.write(GREEN)
    Console.write("New incident saved!")
    Console.clear_formating()
    Console.newline()


@db_session
def new_category(conf):
    category_text = text_input("Category")

    Console.newline()
    Console.newline()

    try:
        new_category = database.Category(name=category_text)
        conf._db.add(new_category)
        row_update = conf._db.commit()

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
def _new_incident(conf):
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
        conf._db.add(project)
        conf._db.commit()
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
def _time_entry(conf):
    """Creates a new entry. When doing so it ends the current entry
    (if there is one) and records its duration.

    When the new entry is created, the entries timer is displayed.

    """
    # fetch working data
    categories = conf._db.query(database.Category).all()
    projects = conf._db.query(database.Project).all()

    query = conf._db.query(database.Entry)

    query = query.order_by(desc(database.Entry.timestamp))
    last_entry = query.first()

    # get inputs
    category = _option_input("Category", categories)
    project = _option_input("Project", projects)

    note = text_input("Notes")
    timestamp = _date_input("Date", conf.dt)
    #  duration = duration_input("Duration")

    # calculate duration of last entry
    #  last_entry_id, last_entry_dur = conf.dt.get_duration(last_entry, timestamp)

    entry = database.Entry(
        category=category,
        project=project,
        note=note,
        timestamp=timestamp,
        duration=duration,
    )

    conf._db.add(entry)
    conf._db.commit()

    if last_entry:
        # calculate duration
        # update last entry
        pass

    show_timer(timestamp, conf.dt)


def time_entry(conf):
    """Creates a new entry. When doing so it ends the current entry
    (if there is one) and records its duration.

    When the new entry is created, the entries timer is displayed.

    """
    # fetch working data
    with Database(conf.sqlite, conf.dt) as db:

        categories = db.fetch_category()
        incidents = db.fetch_incidents()
        last_entry = db.fetch_last_entry()

    # get inputs
    category = _option_input("Category", categories)
    incident = _option_input("Incident", incidents)

    notes = text_input("Notes")
    timestamp = date_input("Date", conf.dt)
    duration = duration_input("Duration")

    # calculate duration of last entry
    last_entry_id, last_entry_dur = conf.dt.get_duration(last_entry, timestamp)

    with Database(conf.sqlite, conf.dt) as db:
        db.record_entry(category, incident, notes, timestamp, duration)
        if last_entry_id:
            db.update_entry_duration(last_entry_id, last_entry_dur)

    show_timer(timestamp, conf.dt)


def show_current_entry(conf):
    """Show the last or current entry and display it's timer.
    If there is no open entries, it shows nothing.

    """
    with Database(conf.sqlite, conf.dt) as db:
        last_entry = db.fetch_last_entry()

    if not last_entry or last_entry.minutes != 0:
        Console.write(RED)
        Console.writeline(" There are no active entries!")
        Console.clear_formating()
        return

    Console.write(str(last_entry))
    Console.newline()

    start_time = conf.dt.parse_date_input(last_entry.start_time)
    show_timer(start_time, conf.dt)


def edit_entry(conf):
    if not conf.cli_curr_obj:
        print("We don't have the selection feature built yet!")
        return

    with Database(conf.sqlite, conf.dt) as db:
        last_entry = db.fetch_last_entry()
        categories = db.fetch_category()
        incidents = db.fetch_incidents()

    # get inputs
    entry_id = last_entry.entry_id
    category = option_input("Category", categories, default=last_entry.category)
    incident = option_input("Incident", incidents, default=last_entry.incident)

    notes = text_input("Notes", default=last_entry.note)
    timestamp = date_input("Date", conf.dt, default=last_entry.start_time)

    do_update = bool_input("Proceed with update?")

    if not do_update:
        print("canceling update")
        return

    with Database(conf.sqlite, conf.dt) as db:
        db.update_entry(entry_id, category, incident, notes, timestamp)


def stop_entry(conf):
    """Ends the current entry (if there is one) and records its
    duration.

    """
    # fetch working data
    with Database(conf.sqlite, conf.dt) as db:
        last_entry = db.fetch_last_entry()

        if not last_entry:
            Console.write(RED)
            Console.writeline(" There are no entries!")
            return

        Console.writeline(str(last_entry))

        if last_entry.minutes > 0:
            Console.write(RED)
            Console.writeline(" Last entry already has a duration.")
            Console.clear_formating()
            return

        timestamp = date_input("End Date", conf.dt)
        duration = duration_input("Duration")

        # calculate duration of last entry
        last_entry_id, last_entry_dur = conf.dt.get_duration(last_entry, timestamp)

        # if we have a duration, then we override the calculated value
        if last_entry_id and duration:
            last_entry_dur = duration

        if last_entry_id:
            db.update_entry_duration(last_entry_id, last_entry_dur)


def summary(conf):
    """Displays a summary of the current days total time.

    """
    from tabulate import tabulate

    with Database(conf.sqlite, conf.dt) as db:
        row = db.fetch_todays_entry_summary()

    Console.write(BG_WHITE)
    Console.write(BLACK)
    Console.newline()

    table = tabulate(
        [row], headers=("DATE", "START", "END", "DURATION"), numalign="decimal"
    )
    Console.write(add_table_border(table))
    Console.newline()
    Console.clear_formating()


def weekly_summary(conf):
    """Displays a summary of times for a given range of days.

    """
    from tabulate import tabulate

    start_date = date_input("Start Date", conf.dt)
    end_date = date_input("End Date", conf.dt)

    with Database(conf.sqlite, conf.dt) as db:
        rows = db.fetch_weekly_totals(
            start_date.format("YYYY-MM-DD"), end_date.format("YYYY-MM-DD")
        )

    Console.write(BG_WHITE)
    Console.write(BLACK)

    table = tabulate(
        rows,
        numalign="decimal",
        headers=("INCIDENT", "TOTALS", "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"),
    )

    Console.write(add_table_border(table))
    Console.newline()
    Console.clear_formating()


def view(conf):
    from tabulate import tabulate

    today = conf.dt.current_timestamp().format("YYYY-MM-DD")
    with Database(conf.sqlite, conf.dt) as db:
        rows = db.fetch_entry_view(today)

    Console.write(BG_WHITE)
    Console.write(BLACK)
    table = tabulate(
        rows,
        headers=("TIMESTAMP", "MIN", "CATEGORY", "INCIDENT", "NOTES"),
        numalign="decimal",
    )
    Console.write(add_table_border(table))
    Console.newline()
    Console.clear_formating()
