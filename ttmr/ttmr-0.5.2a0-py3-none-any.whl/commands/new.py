from ..console import GREEN
from ..console import RED
from ..console import Console
from ..gui import number_input
from ..ui import default_text_input
from ..ui import text_input
from ..util import regex_factory
from ..database import Category
from ..database import Entry
from ..database import Project
from .util import db_session


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
