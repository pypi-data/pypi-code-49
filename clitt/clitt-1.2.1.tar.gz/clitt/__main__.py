#!/usr/bin/env python
import click
from .actions import read, chat, dm, post, user, search
from .auth import run as get_api_instance
from sys import argv

@click.command(help="- Read the most recent status updates from your timeline")
@click.option('--count', default=5, help="Number of tweets you want to read")
def command_read(count):
    api = get_api_instance()
    read(api, count)

@click.command(help="- Read your chat with some user")
@click.argument('user')
def command_chat(user):
    api = get_api_instance()
    chat(api, user)

@click.command(help="- Tweet something!")
@click.argument('content')
def command_post(content):
    api = get_api_instance()
    post(api, content)

@click.command(help="- Send a direct message to an user")
@click.argument('user')
@click.argument('content')
def command_dm(user, content):
    api = get_api_instance()
    dm(api, user, content)

@click.command(help="- Search for tweets")
@click.argument('query')
@click.option('--count', default=5, help="Number of tweets you want to read")
def command_search(query, count):
    api = get_api_instance()
    search(api, user, content)

@click.command(help="- Search for an user")
@click.argument('query')
@click.option('--count', default=5, help="Number of users you want to see")
def command_user(query, count):
    api = get_api_instance()
    user(api, user, content)

@click.group(commands={"chat": command_chat, "dm": command_dm, "post": command_post, "read": command_read, "search": command_search, "user": command_user,})
def cli():
    pass

if __name__ == '__main__':
    cli()