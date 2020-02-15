from pathlib import Path
import click
from .models import Contacts, db
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

db.connect()
db.create_tables([Contacts])

@click.group()
def cli_contacts():
    pass

@cli_contacts.command()
@click.option('--name', help='Navn', prompt='Navn')
@click.option('--tlf', help='Telefonnummer', prompt='Telefonnr')
@click.option('--email', help='Email', prompt='Email')
@click.option('--arbejdsplads', help='Arbejdsplads', prompt='Arbejdsplads')
def create(name, tlf, email, arbejdsplads):
    '''
    Gemmer en ny kontakt i databasen.
    '''
    new_entry = Contacts(name=name, tlf=tlf, email=email, arbejdsplads=arbejdsplads)
    new_entry.save()
    click.echo(f'{new_entry.name} gemt!')
    
@cli_contacts.command()
@click.argument('id')
@click.confirmation_option(prompt='Er du sikker på, at du vil slette denne kontakt?')
def delete(id):
    '''
    Sletter en række med et givent id!

    Id kan findes i search med --show-id.
    '''
    try:
        row = Contacts.get(Contacts.id == id)
        row.delete_instance()
        click.echo(f'{row.name} slettet!')
    except:
        click.echo('Ingen række med det ID!')
        raise click.Abort()

@cli_contacts.command()
@click.argument('id')
@click.option('--name', default='', help='Nyt navn', prompt='Navn')
@click.option('--tlf', default='', help='Nyt telefonnummer', prompt='Telefonnr')
@click.option('--email', default='', help='Ny email', prompt='Email')
@click.option('--arbejdsplads', default='', help='Ny arbejdsplads', prompt='Arbejdsplads')
def update(id, name, tlf, email, arbejdsplads):
    '''
    Opdaterer en række med de givne informationer.

    ID kan findes i search.
    '''
    row = Contacts.get(Contacts.id == id)
    q = (Contacts.update({
        Contacts.name: row.name if name == '' else name,
        Contacts.tlf: row.tlf if tlf == '' else tlf,
        Contacts.email: row.email if email == '' else email,
        Contacts.arbejdsplads: row.arbejdsplads if arbejdsplads == '' else arbejdsplads,
    }).where(Contacts.id == id))
    q.execute()
    click.echo(f'{name} opdateret!')


@cli_contacts.command('search')
@click.argument('search_string')
@click.option('--id/--no-id', default=False, help='Vis ID eller ej')
def search_by_name(search_string, id):
    '''
    Søg efter kontakt.
    '''
    query = Contacts.select().where(Contacts.name ** f'%{search_string}%')
    if query.count() > 0:
        for person in query:
            if id == True:
                fid = click.style(str(person.id), fg='green', bold=True)
                click.echo(f'ID: {fid}')
            click.echo(f'Navn: {person.name}')
            click.echo(f'Tlf: {person.tlf}')
            click.echo(f'Email: {person.email}')
            click.echo(f'Arbjedssted: {person.arbejdsplads}')
            if query.count() > 1:
                afslut = click.style('----------', bold=True)
                click.echo(afslut)
    else:
        raise click.ClickException('Fandt ingen resultater!')

@cli_contacts.command()
@click.option('--id/--no-id', default=False, help='Vis ID eller ej')
def list_all(id):
    '''
    Viser en liste over alle kontakter.

    --show-id viser resultatets ID felt, som kan bruges til opdatering/sletning af data.
    '''
    for person in Contacts.select():
        if id:
            fid = click.style(str(person.id), fg='green', bold=True)
            click.echo(f'ID: {fid}')
        click.echo(f'Navn: {person.name}')
        click.echo(f'Tlf: {person.tlf}')
        click.echo(f'Email: {person.email}')
        click.echo(f'Arbjedssted: {person.arbejdsplads}')
        afslut = click.style('----------', bold=True)
        click.echo(afslut)

@cli_contacts.command()
# @click.confirmation_option('Er du sikker på, at du gerne vil tage backup af dine kontakter?')
def backup_db():
    '''
    Tager backup af databasen til en Google Drive konto!
    '''

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    db_path = Path.home() / '.contacts.db'

    db_file = drive.CreateFile({'mimetype': 'application/x-sqlite3'})
    db_file['title'] = db_path.name
    db_file.SetContentFile(db_path.__str__())
    db_file.Upload()
    click.echo('Dine kontakter er uploaded til din Google Drive!')
