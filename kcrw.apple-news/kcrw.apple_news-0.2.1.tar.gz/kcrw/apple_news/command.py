#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Command-line tool for using the Apple News API"""
import click
import click_log
import glob
import json
import os
import six
from kcrw.apple_news.api import API, logger


click_log.basic_config(logger)


@click.group()
@click.pass_context
@click.option('-k', '--key_id', required=True,
              help='Apple News Acceess Key Id', type=str)
@click.option('-s', '--key_secret', required=True,
              help='Apple News Secret', type=str)
@click.option('-c', '--channel', required=True,
              help='Apple News Channel Id', type=str)
@click_log.simple_verbosity_option(logger)
def cli(ctx, key_id, key_secret, channel):
    """Make calls to the Apple News API.
       Requires an API Key Id, Key Secret, and a News Channel Id.
       These can be passed as commandline options or
       set as environment variables:

       APPLE_KEY_ID, APPLE_KEY_SECRET, APPLE_CHANNEL
    """
    click.echo('Initializing Apple News API')
    ctx.ensure_object(dict)
    ctx.obj['channel'] = channel
    ctx.obj['api'] = API(key_id, key_secret, channel)


@click.command()
@click.pass_context
def channel(ctx):
    """Fetch channel info"""
    channel = ctx.obj['channel']
    click.echo('Fetching Channel Info for channel: {}'.format(channel))
    api = ctx.obj['api']
    data = api.read_channel()
    click.echo('Received data:\n\n{}'.format(
        json.dumps(data, indent=True)
    ))


def read_article_dir(path):
    assets = {}
    metadata = None
    article = None
    filenames = glob.glob('%s/*' % path)
    for fname in filenames:
        base_name = os.path.basename(fname)
        if base_name.endswith('.json'):
            with open(fname) as f:
                data = json.load(f)
            if base_name == 'article.json':
                article = data
            elif base_name == 'metadata.json':
                metadata = data
        else:
            with open(fname, 'rb') as f:
                f_data = f.read()
                assets[base_name] = six.ensure_binary(f_data, 'utf8')

    return metadata, article, assets


@click.command()
@click.pass_context
@click.argument('article_content', type=click.Path(exists=True, dir_okay=True))
def create(ctx, article_content):
    """Create and upload an article from a folder of files"""
    channel = ctx.obj['channel']
    click.echo('Creating Article in Channel: {}'.format(channel))
    api = ctx.obj['api']
    metadata, article, assets = read_article_dir(article_content)
    data = api.create_article(article, metadata, assets)
    click.echo('Received data:\n\n{}'.format(
        json.dumps(data, indent=True)
    ))


@click.command()
@click.pass_context
@click.argument('identifier', type=str)
@click.argument('article_content', type=click.Path(exists=True, dir_okay=True))
def update(ctx, identifier, article_content):
    """Update an existing article by Id from a folder of files"""
    click.echo('Updating Article: {}'.format(identifier))
    api = ctx.obj['api']
    metadata, article, assets = read_article_dir(article_content)
    data = api.update_article(identifier, metadata, article, assets)
    click.echo('Received data:\n\n{}'.format(
        json.dumps(data, indent=True)
    ))


@click.command()
@click.pass_context
@click.argument('identifier', type=str)
def read(ctx, identifier):
    """Read information for a specific article by Id"""
    click.echo('Fetching Article Information: {}'.format(identifier))
    api = ctx.obj['api']
    data = api.read_article(identifier)
    click.echo('Received data:\n\n{}'.format(
        json.dumps(data, indent=True)
    ))


@click.command()
@click.pass_context
@click.argument('identifier', type=str)
def delete(ctx, identifier):
    """Delete a specific article by Id"""
    click.echo('Deleting Article Information: {}'.format(identifier))
    api = ctx.obj['api']
    data = api.delete_article(identifier)
    click.echo('Received data:\n\n{}'.format(
        json.dumps(data, indent=True)
    ))


cli.add_command(channel)
cli.add_command(create)
cli.add_command(update)
cli.add_command(read)
cli.add_command(delete)

if __name__ == '__main__':
    cli(auto_envvar_prefix='APPLE')  # pragma: no cover
