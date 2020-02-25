import codecs
import os
import re
import sqlite3
from sqlite3 import IntegrityError

from ttmr.domain import ViewEntry
from ttmr.util import DB_TIMESTAMP
from ttmr.util import find_data_file
from ttmr.util import replace_bad_char

codecs.register_error("replace", replace_bad_char)


def fetch_sql(sqlfile):
    with open(find_data_file(sqlfile), "r") as fh_:
        return fh_.read()


FMTS = {
    "INC": "{}{:0>8}",
    "WO": "{}{:0>9}",
    "FY16": "{}-{:0>6}",
    "FY17": "{}-{:0>6}",
    "FY18": "{}-{:0>6}",
    "FY19": "{}-{:0>6}",
    "FY20": "{}-{:0>6}",
}


def fmt_inc(typ, number):
    """
    INC00000000
    WO000000000
    FY18-000000
    """
    return FMTS[typ].format(typ, number)


class Database(object):
    def __init__(self, dbfile, dt):
        self.dbfile = dbfile
        self.dt = dt

    def __enter__(self):
        self.conn = sqlite3.connect(self.dbfile)
        self.csr = self.conn.cursor()
        return self

    @property
    def version(self):
        return sqlite3.sqlite_version

    def initialize(self):
        sql = fetch_sql("INITIALIZE.sql")
        self.csr.executescript(sql)

    def select(self, sql, parms=None):
        try:
            if parms:
                self.csr.execute(sql, parms)
            else:
                self.csr.execute(sql)
            return self.csr.fetchall()
        except IntegrityError as ex:
            raise ex

    def fetch_last_record(self, table):
        sql = "SELECT * FROM {} ORDER BY ID DESC LIMIT 1;"
        self.csr.execute(sql.format(table))
        return self.csr.fetchone()

    def execute(self, sql, parms, raise_errors=False):
        try:
            self.csr.execute(sql, parms)
        except IntegrityError as ex:
            print(parms["number"], ex)
            if raise_errors:
                raise ex

    def commit(self):
        self.conn.commit()

    def __exit__(self, *args):
        self.conn.close()

    def record_category(self, *data):
        self.execute(self.new_category_sql, data)
        self.commit()

    def fetch_category(self):
        return self.select(u"SELECT ID, NAME FROM CATEGORY WHERE ACTIVE = 1;")

    def record_incident(self, *data):
        # input data
        typ, num, name = data
        timestamp = self.dt.current_timestamp().format(DB_TIMESTAMP)
        parms = {
            "typ": typ,
            "number": num,
            "name": name,
            "active": 1,
            "persist": 0,
            "created": timestamp,
            "modified": timestamp,
        }

        self.execute(fetch_sql("INSERT-INCIDENT.sql"), parms)
        self.commit()
        return self.csr.rowcount

    def fetch_incidents(self):
        return self.select(u"SELECT ID, NAME FROM VIEW_INCIDENTS;")

    def deactivate_incident(self, inc_id):
        parms = {"id": inc_id}
        self.execute(
            ("UPDATE INCIDENT SET ACTIVE = 0 " "WHERE ID = :id AND PERSISTANT <> 1;"),
            parms,
        )
        self.commit()
        return self.csr.rowcount

    def fetch_last_entry(self):
        sql = u"SELECT * FROM VIEW_ENTRY ORDER BY ENTRY_ID DESC LIMIT 1;"
        self.csr.execute(sql)
        row = self.csr.fetchone()
        if not row:
            return row
        return ViewEntry(*row)

    def record_category(self, *data):
        self.execute(fetch_sql("INSERT-CATEGORY.sql"), data, raise_errors=True)
        self.commit()

    def record_entry(self, *data):
        category, incident, notes, timestamp, duration = data
        created = self.dt.current_timestamp().format(DB_TIMESTAMP)
        parms = {
            "category": category,
            "incident": incident,
            "note": notes,
            "timestamp": timestamp.format(DB_TIMESTAMP),
            "duration": duration,
            "created": created,
            "modified": created,
        }
        self.execute(fetch_sql("INSERT-ENTRY.sql"), parms, raise_errors=True)
        self.commit()

    def update_entry(self, *data):
        _id, category, incident, notes, timestamp = data
        modified = self.dt.current_timestamp().format(DB_TIMESTAMP)
        parms = {
            "id": _id,
            "category": category,
            "incident": incident,
            "note": notes,
            "timestamp": timestamp.format(DB_TIMESTAMP),
            "modified": modified,
        }
        self.execute(fetch_sql("UPDATE-ENTRY.sql"), parms, raise_errors=True)
        self.commit()

    def fetch_todays_entry_summary(self):
        sql = u"SELECT * FROM VIEW_CURRENT_TIME_SUMMARY"
        self.csr.execute(sql)
        return self.csr.fetchone()

    def fetch_weekly_totals(self, start_date, end_date):
        sql = fetch_sql("SELECT-WEEK-SUMMARY.sql")
        rows = self.select(sql, parms={"startdate": start_date, "enddate": end_date})
        return rows

    def fetch_entry_view(self, day):
        sql = fetch_sql("SELECT-ENTRY-VIEW.sql")
        rows = self.select(sql, parms={"day": day})
        return [ViewEntry(*r).to_view() for r in rows]

    def update_entry_duration(self, entry_id, duration):
        created = self.dt.current_timestamp().format(DB_TIMESTAMP)
        sql = fetch_sql("UPDATE-ENTRY-DURATION.sql")
        self.execute(
            sql, {"dur": duration, "id": entry_id, "mod": created}, raise_errors=True
        )
        self.commit()


def fetch_directory_incidences(conf):
    """Look for incidences from directory names.

    """
    reg = re.compile(
        (r"^(?P<type>WO|INC|CRQ)" r"0*(?P<number>[0-9]\d+) " r"?- ?(?P<name>.*)\w?$"),
        re.I,
    )

    if not os.path.exists(conf.project_dir):
        print("The project directory does not exist. Nothing to load.")
        return

    for entry in os.listdir(conf.project_dir):
        m = reg.match(entry)
        if m:
            g = m.groupdict()
            yield (g["type"], int(g["number"]), g["name"].strip())


def fetch_file_incidences(conf):
    """Look for incidences from a files content.

    """
    # get from list
    reg = re.compile((r"^(?P<type>WO|INC|CRQ|FY\d\d)" r"0*(?P<number>[0-9]\d+)$"), re.I)

    remedyfile = os.path.join(conf.project_dir, "remedy-tickets.txt")

    if not os.path.exists(remedyfile):
        print("Remedy file does not exist!")
        return

    with open(remedyfile) as fh_:
        lines = fh_.readlines()

    parse_incident_id = regex_factory(
        (r"^(?P<type>WO|INC|CRQ)" r"0*(?P<number>[0-9]\d+)$")
    )

    ilines = iter(lines)
    for line in ilines:
        g = parse_incident_id(line)
        if g:
            next(ilines)  # skip a line
            g["name"] = next(ilines).strip()
            yield (g["type"], int(g["number"]), g["name"].strip())


def load_incidences(conf):

    import pyperclip

    remedy_regex = "^(?P<type>(INC|WO))0*(?P<id>[1-9]\d+)[\r\n]+Mark Gemmill[\r\n]+^(?P<name>[^\r\n]+)[\r\n]?$"
    outlook_regex = "(?P<type>(INC|WO))0*(?P<id>[1-9]\d+).*Description: (?P<name>.+)$"
    er_regex = "(?P<type>FY\d\d)-0*(?P<id>[1-9]\d+)[^\r\n]*[\r\n]+^(?P<name>[^\r\n]+)[\r\n]+^Mark Gemmill"
    jira_regex = "(?P<type>(INC|WO|FY\d\d))[^\d]*0*(?P<id>[1-9]\d+) +(?P<name>[^\r\n]+)[\r\n]+^\S+"

    re_flags = re.M

    capture_list = [
        re.compile(remedy_regex, re_flags),
        re.compile(outlook_regex, re_flags),
        re.compile(er_regex, re_flags),
        re.compile(jira_regex, re_flags),
    ]

    def parse_from(regex, pasted):
        results = []
        for result in regex.finditer(pasted):
            d = result.groupdict()
            results.append((d["type"].upper(), d["id"], d["name"]))
        return results

    def parse_pasted():
        content = pyperclip.paste()
        for rx in capture_list:
            for result in parse_from(rx, content):
                yield result

    with Database(conf.sqlite, conf.dt) as db:
        print("loading....")

        for typ, num, nme in parse_pasted():
            print("  {} - {}".format(fmt_inc(typ, num), nme))
            try:
                db.record_incident(typ, num, nme)
            except Exception as ex:
                print(ex)
