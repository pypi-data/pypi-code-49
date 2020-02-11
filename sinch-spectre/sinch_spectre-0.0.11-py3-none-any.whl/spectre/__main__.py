import click
from spectre import config

@click.group()
@click.option('--spectre-dir', default=None, help='Path to the spectre root directory (location of spectre config and target dir for generated files)')
def cli(spectre_dir):
    global CONFIG
    CONFIG = config.load(spectre_dir)
    pass

@click.group()
def generate():
    pass

@click.group(name='import')
def handle_import():
    pass

@click.command(name='mysql')
@click.argument('path')
def import_mysql(path):
    from spectre.importers import mysql
    mysql.import_mysql(CONFIG, path)

@click.command()
@click.argument('path')
def proto(path):
    from spectre.generation import proto
    proto.generate(CONFIG, path)


@click.command()
@click.argument('path')
@click.option('--spring-data', is_flag=True)
@click.option('--spring-web', is_flag=True)
def java(path, spring_data, spring_web):
    from spectre.generation import java
    options = { 'spring_data': spring_data, 'spring_web': spring_web }
    CONFIG.java_options = options
    click.echo(f'Generating java code from {path}')
    java.generate(CONFIG, path)

@click.command()
@click.argument('path')
def jhipster(path):
    from spectre.generation import jhipster
    click.echo(f'Generating jhipster entities from {path}')
    written = jhipster.generate(CONFIG, path)
    for path in written:
        click.echo(path)

if __name__== "__main__":
    cli.add_command(handle_import)
    cli.add_command(generate)
    handle_import.add_command(import_mysql)
    generate.add_command(java)
    generate.add_command(jhipster)
    generate.add_command(proto)
    cli()
