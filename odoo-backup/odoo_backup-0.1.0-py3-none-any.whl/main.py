import click
from models import Server
import os
from config import DATA_DIR
from server import create_server


if not os.path.isdir(os.path.join(DATA_DIR)):
    os.mkdir(os.path.join(DATA_DIR))


@click.group()
def cli():
    """Simple Odoo backup manager"""
    pass


@cli.command()
def list():
    """Lists all available servers"""
    for server in Server.all():
        print(f"{server.name} ({server.ip})")


@cli.command()
@click.argument('server_name')
def check(server_name):
    """Checks a server (or all servers) connection and available backups"""
    if server_name == "all":
        for server in Server.all():
            server.check()
    else:
        Server.get(server_name).check()


@cli.command()
@click.argument('server_name')
@click.option('--database', default='all', help="database to backup")
def backup(server_name, database):
    """Backups a server (or all servers) databases (on only one using --database option)"""
    if server_name == "all":
        for server in Server.all():
            server.backup_all()
    else:
        server = Server.get(server_name)
        if database != "all":
            server.backup(database)
        else:
            server.backup_all()


@cli.command()
@click.argument('server_name')
@click.argument('database')
@click.option('--backup-date', default='latest', help='backup date (latest, oldest or yyyy-mm-dd format')
def download(server_name, database, backup_date):
    """Provides an URL to download specified backup"""
    server = Server.get(server_name)
    if database not in server.bases:
        print(f"Database {server_name}:{database} doesn't exist in config file.")
        exit(0)
    file_name = server.get_backup_name(database, backup_date)
    if file_name is None:
        print(f'Unable to find {server_name}:{database}:{backup_date} backup.')
        exit(0)
    print('[ INFO ] Setting up web server for backup file download. Please use CTRL+C after downloading.')
    server = create_server(server_name=server_name, database=database, file_name=file_name)
    server.run()


if __name__ == "__main__":
    cli()
