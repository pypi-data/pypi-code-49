from datetime import datetime
from ..console import Console
from ..gui import date_input
from ..gui import duration_input
from ..gui import option_input
from ..gui import show_timer
from ..gui import bool_input
from ..gui import display_alert
from ..gui import display_message
from ..gui import clear_line
from ..ui import text_input
from ..database import Category
from ..database import Entry
from ..database import Project
from .util import db_session
from .util import new_session


def time_entry(conf, ui, end_entry=False):
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

    end_time = None
    duration = 0
    current_timestamp = datetime.now()
    last_entry = Entry.get_last(conf.db, current_timestamp)

    if end_entry:

        if not last_entry:
            last_entry = Entry.get_day_start_entry()

        if last_entry.end_time is not None:
            current_timestamp = last_entry.end_time

    if not end_entry and last_entry and last_entry.duration == 0:
        # if there is a pre-exiting entry that is not closed
        close_open_entry(conf.db, last_entry)

    # get inputs
    category, project, note, start_time = ui.fetch_entry_inputs(
        categories, projects, current_timestamp
    )

    # if this is an end entry...
    if end_entry:
        # TODO: it is a bit of a problem that we might be overriding the duration...
        # TODO: and that the duration is a captured value
        end_time, duration = ui.fetch_end_entry_inputs(start_time, current_timestamp)

    # create entry
    entry = Entry(
        category=category,
        project=project,
        note=note,
        start_time=start_time,
        end_time=end_time,
        duration=duration,
    )

    conf.db.add(entry)
    conf.db.commit()

    return entry.id

@db_session
def show_current_entry(conf):
    """Show the last or current entry and display it's timer.
    If there is no open entries, it shows nothing.

    """
    last_entry = Entry.get_last(conf.db, datetime.now())

    if not last_entry or last_entry.duration != 0:
        display_alert(" There are no active entries!")
        return

    display_message(str(last_entry))

    EntryUI.post_entry_timer(conf, "", last_entry.start_time, last_entry.id)


@db_session
def start_time_entry(cfg):
    entry_id = time_entry(cfg, EntryUI, end_entry=False)
    EntryUI.post_entry_timer(cfg, "Current Project Timer:", datetime.now(), entry_id)


@db_session
def stop_time_entry(cfg):
    entry_id = time_entry(cfg, EntryUI, end_entry=True)
    EntryUI.post_entry_timer(cfg, "Time since last completed entry::", datetime.now())


def close_open_entry(db, current_entry):

    clear_line()
    print("You have an open entry.")
    end_entry = bool_input("End the current entry?")
    if end_entry:
        current_entry.end()
        db.commit()

        Console.cursor_up()
        Console.cursor_to_left_margin()
        Console.clear_line()
        Console.cursor_up()
        Console.cursor_to_left_margin()
        Console.clear_line()

        return
    else:
        raise KeyboardInterrupt()


class EntryUI:
    @staticmethod
    def fetch_entry_inputs(categories, projects, last_end_time):
        category = option_input("Category", categories)
        project = option_input("Project", projects)
        note = text_input("Notes")
        start_time = date_input("Start Date", default=last_end_time)
        return category, project, note, start_time

    @staticmethod
    def fetch_end_entry_inputs(start_time, current_timestamp):
        end_time = date_input("End Date", default=current_timestamp)
        elapsed_time = 0
        elapsed_time = current_timestamp - start_time
        duration = duration_input(
            "Duration", str(int(elapsed_time.total_seconds() / 60))
        )
        return end_time, duration

    @staticmethod
    def post_entry_timer(cfg, msg, current_timestamp, current_entry_id=None):
        print()

        if current_entry_id:
            print(msg)
            try:
                show_timer(current_timestamp)
            except KeyboardInterrupt:
                clear_line()
                end_entry = bool_input("End the current entry?")
                if end_entry:
                    print("Closing current session...")
                    with new_session(cfg.db_path) as db:
                        current_entry = (
                            db.query(Entry)
                            .filter(Entry.id == current_entry_id)
                            .one_or_none()
                        )
                        current_entry.end()
                        db.commit()
        else:
            print(msg)
            show_timer(current_timestamp)
