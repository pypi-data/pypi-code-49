#!python

# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import click
import sys

from zabbix_sys import get_platform, get_logger, get_config, print_json
from zabbix_sys.svc.mysql import MySQL
from zabbix_sys.svc.nginx import Nginx
from zabbix_sys.svc.rabbitmq import RabbitMQ
from yaml import MarkedYAMLError


@click.group()
@click.pass_context
def cli(ctx):

    system = get_platform()
    config = None

    if not system:
        print("Current platform not supported")
        sys.exit(1)

    try:
        config = get_config()
    except MarkedYAMLError:
        sys.exit(1)
    except Exception:
        pass

    logger = get_logger(config=config)

    ctx.obj = {
        'system': system,
        'config': config,
        'logger': logger
    }

# MySQL ###########################################################################################


@cli.command(name='lld.mysql.master')
@click.pass_context
def lld_mysql(ctx):
    print_json(MySQL(cfg=ctx.obj['config'], logger=ctx.obj['logger']).lld())


@cli.command(name='lld.mysql.slave')
@click.pass_context
def lld_mysql(ctx):
    print_json(MySQL(cfg=ctx.obj['config'], logger=ctx.obj['logger']).lld())


@cli.command(name='lld.mysql.server')
@click.pass_context
def lld_mysql(ctx):
    print_json(MySQL(cfg=ctx.obj['config'], logger=ctx.obj['logger']).lld())


@cli.command(name='raw.mysql.config')
@click.pass_context
def raw_mysql_config(ctx):
    print_json(MySQL(cfg=ctx.obj['config'], logger=ctx.obj['logger']).raw_config())


@cli.command(name='raw.mysql.master')
@click.pass_context
def raw_mysql_master(ctx):
    print_json(MySQL(cfg=ctx.obj['config'], logger=ctx.obj['logger']).raw_master())


@cli.command(name='raw.mysql.slave')
@click.pass_context
def raw_mysql_slave(ctx):
    print_json(MySQL(cfg=ctx.obj['config'], logger=ctx.obj['logger']).raw_slave())


@cli.command(name='raw.mysql.status')
@click.pass_context
def raw_mysql_status(ctx):
    print_json(MySQL(cfg=ctx.obj['config'], logger=ctx.obj['logger']).raw_status())


# Nginx ###########################################################################################


@cli.command(name='lld.nginx.status')
@click.pass_context
def lld_nginx(ctx):
    print_json(Nginx(cfg=ctx.obj['config'], logger=ctx.obj['logger']).lld_status())


@cli.command(name='raw.nginx.status')
@click.pass_context
def raw_nginx(ctx):
    print_json(Nginx(cfg=ctx.obj['config'], logger=ctx.obj['logger']).raw_status())


# RabbitMQ ########################################################################################


@cli.command(name='lld.rabbitmq.exchanges')
@click.pass_context
def lld_rabbitmq_exchanges(ctx):
    print_json(RabbitMQ(cfg=ctx.obj['config'], logger=ctx.obj['logger']).lld_exchanges())


@cli.command(name='lld.rabbitmq.queues')
@click.pass_context
def lld_rabbitmq_queues(ctx):
    print_json(RabbitMQ(cfg=ctx.obj['config'], logger=ctx.obj['logger']).lld_queues())


@cli.command(name='lld.rabbitmq.server')
@click.pass_context
def lld_rabbitmq_server(ctx):
    print_json(RabbitMQ(cfg=ctx.obj['config'], logger=ctx.obj['logger']).lld_server())


@cli.command(name='lld.rabbitmq.shovels')
@click.pass_context
def lld_rabbitmq_shovels(ctx):
    print_json(RabbitMQ(cfg=ctx.obj['config'], logger=ctx.obj['logger']).lld_shovels())


@cli.command(name='raw.rabbitmq.exchanges')
@click.argument("vhost", required=True)
@click.argument("exchange_name", required=True)
@click.pass_context
def raw_rabbitmq_exchanges(ctx, vhost, exchange_name):
    print_json(RabbitMQ(cfg=ctx.obj['config'], logger=ctx.obj['logger']).raw_exchanges(
        vhost=vhost, exchange_name=exchange_name
    ))


@cli.command(name='raw.rabbitmq.queues')
@click.argument("vhost", required=True)
@click.argument("queue", required=True)
@click.pass_context
def raw_rabbitmq_queues(ctx, vhost, queue):
    print_json(RabbitMQ(cfg=ctx.obj['config'], logger=ctx.obj['logger']).raw_queues(
        vhost=vhost, queue=queue
    ))


@cli.command(name='raw.rabbitmq.server')
@click.pass_context
def raw_rabbitmq_server(ctx):
    print_json(RabbitMQ(cfg=ctx.obj['config'], logger=ctx.obj['logger']).raw_server())


@cli.command(name='raw.rabbitmq.shovels')
@click.argument("vhost", required=True)
@click.argument("shovel_name", required=True)
@click.pass_context
def raw_rabbitmq_shovels(ctx, vhost, shovel_name):
    print_json(RabbitMQ(cfg=ctx.obj['config'], logger=ctx.obj['logger']).raw_shovels(
        vhost=vhost, shovel_name=shovel_name
    ))


if __name__ == "__main__":
    cli()
