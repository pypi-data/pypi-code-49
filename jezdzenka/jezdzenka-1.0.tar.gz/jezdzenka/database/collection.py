from jezdzenka.application import app as jezdzenka
from tinydb import Query


def get_all():
    return jezdzenka.table.all()


def get_current():
    ticket = Query()
    return jezdzenka.table.search(ticket.archived == False)


def get_all_by_tag(all_tag):
    return jezdzenka.table.search(Query().tags.any(all_tag))


def get_all_by_year(all_years):
    years = [int(x) for x in all_years]
    return jezdzenka.table.search(Query().validation_date.date.year.one_of(years))


def get_filename_by_id(doc_id: int):
    return jezdzenka.table.get(doc_id=int(doc_id))['filename']


def get_object_by_id(doc_id: int):
    return jezdzenka.table.get(doc_id=int(doc_id))
