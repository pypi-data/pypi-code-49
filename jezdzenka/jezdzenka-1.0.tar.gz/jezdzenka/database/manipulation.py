import os
import re
import json
import datetime
from zipfile import ZipFile

from jezdzenka.database import collection
from jezdzenka.application import app as jezdzenka


def move_file_to_app(information, file):
    directory = jezdzenka.configuration
    name, extension = os.path.splitext(file)
    new_name = information['relevant_date'].strftime("%Y%m%d%H%M%S") \
        + re.sub('[\W_]+', '', information['organization']) + '#' \
        + re.sub('[\W_]+', '', information['id']) + extension
    os.rename(file, os.path.join(directory, new_name))
    return new_name


def add_new_from_form(information, file):
    db = jezdzenka.table
    filename = move_file_to_app(information, file)
    # print(information['type'])
    information['filename'] = filename
    information['archived'] = False
    db.insert(information)


def remove_elements_by_ids(doc_ids):
    for doc_id in doc_ids:
        element = collection.get_object_by_id(int(doc_id))
        if os.path.exists(os.path.join(jezdzenka.configuration, element['filename'])):
            os.remove(os.path.join(jezdzenka.configuration, element['filename']))
        jezdzenka.table.remove(doc_ids=[int(doc_id)])


def move_to_archive(doc_ids):
    ids = [int(x) for x in doc_ids]
    jezdzenka.table.update({'archived': True}, doc_ids=ids)


def update_object(doc_id, element):
    jezdzenka.table.update(element, doc_ids=[int(doc_id)])


def datetime_export(o):
    if isinstance(o, datetime.datetime):
        return o.strftime("%Y-%m-%d %H:%M:%S")


def export(rows, zip_path):
    data_path = os.path.join(jezdzenka.configuration, "export_data.json")
    files_to_export = [os.path.join(jezdzenka.configuration, x['filename']) for x in rows]
    with open(data_path, 'w') as outfile:
        json.dump(rows, outfile, default=datetime_export, indent=4)
    with ZipFile(zip_path, 'w') as zip:
        zip.write(data_path, arcname=data_path.replace(jezdzenka.configuration, ''))
        for file_to_export in files_to_export:
            zip.write(file_to_export, arcname=file_to_export.replace(jezdzenka.configuration, ''))
    files_to_delete = [x.doc_id for x in rows]
    remove_elements_by_ids(files_to_delete)
    os.remove(data_path)
