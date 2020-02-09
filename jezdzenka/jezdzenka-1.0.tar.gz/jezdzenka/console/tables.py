from prettytable import PrettyTable

from jezdzenka.database import collection
from jezdzenka.translation import _


def show_in_table_normal(rows):
    rows = sorted(rows, key=lambda row: row['relevant_date'], reverse=True)
    table = PrettyTable()
    table.field_names = ["#", "Description", "Operator", "Date"]
    for row in rows:
        table.add_row([row.doc_id, row['description'], row['organization'], row['relevant_date']])
    table.align = 'l'
    print(table)


def show_in_table_verbose(rows):
    rows = sorted(rows, key=lambda row: row['relevant_date'], reverse=True)
    table = PrettyTable()
    table.field_names = ["#", "Description", "Operator", "Date", "Tags", "Operator's id"]
    for row in rows:
        table.add_row(
            [row.doc_id, row['description'], row['organization'], row['relevant_date'], row['tags'], row['id']])
    table.align = 'l'
    print(table)


def info_in_table(element_id):
    element = collection.get_object_by_id(element_id)
    table = PrettyTable()
    table.field_names = ["Parameter", "Value"]
    for key, data in element.items():
        table.add_row([_(key), type_handling(key, data)])
    table.align = 'l'
    print(table)


def type_handling(key, data):
    if key == 'type':
        return _(data.value)
    else:
        return data