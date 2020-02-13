#!/usr/bin/env python
import click
import actions
from .auth import run as get_api_instance
from sys import argv

@click.command(help="- Read the most recent status updates from your timeline")
@click.option('--count', default=5, help="Number of tweets you want to read")
def read(count):
    api = get_api_instance()
    actions.read(api, count)

@click.command(help="- Read your chat with some user")
@click.argument('user')
def chat(user):
    api = get_api_instance()
    actions.chat(api, user)

@click.command(help="- Tweet something!")
@click.argument('content')
def post(content):
    api = get_api_instance()
    actions.post(api, content)

@click.command(help="- Send a direct message to an user")
@click.argument('user')
@click.argument('content')
def dm(user, content):
    api = get_api_instance()
    actions.dm(api, user, content)

@click.command(help="- Search for tweets")
@click.argument('query')
@click.option('--count', default=5, help="Number of tweets you want to read")
def search(query, count):
    api = get_api_instance()
    actions.search(api, user, content)

@click.command(help="- Search for an user")
@click.argument('query')
@click.option('--count', default=5, help="Number of users you want to see")
def user(query, count):
    api = get_api_instance()
    actions.user(api, user, content)

@click.group(commands={"chat": chat, "dm": dm, "post": post, "read": read, "search": search, "user": user})
def cli():
    pass

if __name__ == '__main__':
    cli()