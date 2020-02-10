import os
import datetime
import json
import csv

import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import sqlalchemy

##__________________________________________________________________||
db = SQLAlchemy()

##__________________________________________________________________||
def get_db_connection():
    if 'db_connection' not in g:
        g.db_connection = db.engine.connect()
    return g.db_connection

##__________________________________________________________________||
def close_db_connection(e=None):
    conn = g.pop('db_connection', None)
    if conn is not None:
        conn.close()

##__________________________________________________________________||
def init_app(app):
    db.init_app(app)
    app.cli.add_command(init_db_command)
    app.cli.add_command(dump_db_command)
    app.cli.add_command(import_csv_command)
    app.teardown_appcontext(close_db_connection)

##__________________________________________________________________||
def init_db():

    engine = db.engine
    metadata = MetaData()
    metadata.reflect(bind=engine)

    if metadata.tables:
        tbl_names = metadata.tables.keys()
        # ['maps', 'beams']

        tbl_names = ', '.join(['"{}"'.format(t) for t in tbl_names])
        # '"beams", "maps"'

        msg = "Dropped all tables: {}".format(tbl_names)

        metadata.drop_all(bind=engine)
        print(msg)

    if not db.Model.metadata.tables:
        msg = "No tables to be created are found!"
        print(msg)
        return

    tbl_names = db.Model.metadata.tables.keys()
    # ['maps', 'beams']

    tbl_names = ', '.join(['"{}"'.format(t) for t in tbl_names])
    # '"beams", "maps"'

    msg = "Created tables: {}".format(tbl_names)

    db.Model.metadata.create_all(engine)

    print(msg)

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

##__________________________________________________________________||
def get_all_db_content():
    # https://stackoverflow.com/questions/47307873/read-entire-database-with-sqlalchemy-and-dump-as-json
    engine = db.engine
    metadata = MetaData()
    metadata.reflect(bind=engine)
    ret = { }
    for tbl in metadata.sorted_tables:
        ret[tbl.name] = [dict(r) for r in engine.execute(tbl.select())]
    return ret

@click.command("dump-db")
@with_appcontext
def dump_db_command():
    db_content = get_all_db_content()

    click.echo(json.dumps(db_content, indent=2, default=str))
    # https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable

##__________________________________________________________________||
def import_csv(csvdir):
    metadata = MetaData()
    metadata.reflect(bind=db.engine)
    for tbl in metadata.sorted_tables:
        csv_filename = '{}.csv'.format(tbl.name)
        csv_path = os.path.join(csvdir, csv_filename)
        if os.path.exists(csv_path):
            import_csv_(tbl, csv_path)
            message = 'imported to "{}" from {}'.format(tbl.name, csv_path)
        else:
            message = 'skipped "{}". file not found: {}'.format(tbl.name, csv_path)
        print(message)

def import_csv_(tbl, csv_path):
    with open(csv_path, 'r') as f:
        rows = list(csv.reader(f))
    fields = rows[0]
    rows = rows[1:]
    data = [{f: convert_type(e, tbl.columns[f].type) for f, e in zip(fields, r)} for r in rows]
    ins = tbl.insert()
    connection = get_db_connection()
    connection.execute(ins, data)

def convert_type(str_, type_):
    if isinstance(type_, sqlalchemy.sql.sqltypes.DATE):
        if str_:
            return datetime.datetime.strptime(str_, "%Y-%m-%d").date()
        return None
    return str_

@click.command("import-csv")
@click.argument("csvdir")
@with_appcontext
def import_csv_command(csvdir):
    import_csv(csvdir)

##__________________________________________________________________||
