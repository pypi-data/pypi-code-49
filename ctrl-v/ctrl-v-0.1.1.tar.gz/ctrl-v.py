import click
from ctrlv_client.app import create_app, db
# Models have to be imported here
# Otherwise tables won't be created, dropped
from ctrlv_client.app.models import Snippet, Tag, SnippetTag
from sqlalchemy import event
from waitress import serve
from werkzeug.security import generate_password_hash
import json
import os
import logging

# Waiterss server logging
logger = logging.getLogger('waitress')
logger.setLevel(logging.ERROR)

# Needed Files
# populate.json contains the initial populate data
data_dir = os.path.join(
    os.path.dirname(__file__),
    'ctrlv_client'
)
populate_file = os.path.join(data_dir, "populate.json")
# site conifg file used for password protection
site_config_file = os.path.join(data_dir, "site-config.json")

# SnippetTag will only be created after Tag and Snippets
@event.listens_for(SnippetTag.__table__, 'after_create')
# *args, **kwargs
# TypeError: create_snippets() got an unexpected keyword argument 'checkfirst'
# https://github.com/sqlalchemy/sqlalchemy/issues/2206
def create_snippets(*args, **kwargs):
    with open(populate_file, "r") as jsonFile:
        populate_data = json.load(jsonFile)
        for snippet in populate_data['snippets']:
            new_snippet = Snippet(
                    snippet_title=snippet['title'],
                    snippet_text=snippet['text']
            )
            db.session.add(new_snippet)
            for tag in snippet['tags']:
                new_tag = Tag(tag_name=tag)
                db.session.add(new_tag)
                db.session.flush()
                new_snippet_tag = SnippetTag(
                    tag_id=new_tag.tag_id,
                    snippet_id=new_snippet.snippet_id
                )
                db.session.add(new_snippet_tag)
        db.session.commit()


@click.group(invoke_without_command=True)
@click.pass_context
@click.option(
    '--host', default='127.0.0.1',
    help='Host to use while running server',
    type=click.STRING
)
@click.option(
    '--port', default=5000,
    help='Port to use while running server',
    type=click.INT
)
def cli(ctx, host, port):
    # Runs if the tool is called without a command
    if ctx.invoked_subcommand is None:
        app = create_app('production')
        # Only created if it does not exist
        with app.app_context():
            db.create_all()
        serve(app, host=host, port=port)


@click.command()
@click.option(
    '--env', default='development',
    help='Environment to use while running server',
    type=click.STRING
)
@click.option(
    '--port', default=5000,
    help='Port to use while running server',
    type=click.INT
)
@click.option(
    '--host', default='127.0.0.1',
    help='Host to use while running server',
    type=click.STRING
)
def runserver(env, port, host):
    app = create_app(env)
    app.run(host=host, port=port)


@click.command()
@click.option(
    '--env', default='development',
    help='Environment to use while creating DB',
    type=click.STRING
)
def initdb(env):
    ''' Create the SQL DB '''
    with create_app(env).app_context():
        db.create_all()


@click.command()
@click.option(
    '--env', default='development',
    help='Environment to use while dropping DB',
    type=click.STRING
)
def dropdb(env):
    ''' Reset the SQL DB '''
    with create_app(env).app_context():
        db.drop_all()


@click.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
def protect(username, password):
    try:
        with open(site_config_file, "r") as jsonFile:
            site_config = json.load(jsonFile)
    except FileNotFoundError:
        site_config = {}
    site_config["username"] = username
    site_config["password_hash"] = generate_password_hash(password)
    json.dump(site_config, open(site_config_file, "w"))
    click.echo("Your site is now protected.")


@click.command()
def removeprotect():
    if os.path.isfile(site_config_file):
        os.remove(site_config_file)
    click.echo("Protection is removed.")


cli.add_command(runserver)
cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(protect)
cli.add_command(removeprotect)


def main():
    cli()


if __name__ == "__main__":
    main()
