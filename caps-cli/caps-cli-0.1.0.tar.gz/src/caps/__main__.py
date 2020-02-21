import configparser
import logging
import os
import sys
from pathlib import Path
import json

import click

import semver

import caps
from caps import _utils, _metadata_schema, _transform_data

__DEFAULT_CAPS_CLI_CREDENTIALS_FILE__ = "~/.caps-cli/credentials"


@click.group()
@click.option("--verbose", "-v", default=0, count=True)
def cli(verbose):
    _utils.init_logger()
    lv = ".".join(_utils.get_latest_version().split(".")[:3])
    cv = ".".join(caps.__version__.split(".")[:3])

    if semver.compare(lv, cv) > 0:
        click.secho(
            f"""WARNING: You are using caps-cli version {caps.__version__}, however version {lv} is available.
You should consider upgrading via the 'pip install --upgrade caps' command.""",
            fg="yellow",
        )


@cli.command(short_help="Show caps-cli version.")
def version(debug=False):
    click.echo(f"{Path(sys.argv[0]).name} v{caps.__version__}")

@cli.command(short_help="Create an empty JSON template to fill the data to be inserted in Model Catalog")
@click.option(
    "--inputs",
    "-i",
    type=int,
    default=0,
)
@click.option(
    "--outputs",
    "-o",
    type=int,
    default=0,
)
@click.option(
    "--parameters",
    "-p",
    type=int,
    default=0,
)
def initialize(inputs = 0, outputs = 0, parameters = 0):

    with open("./files/initialize_schema.json", "r") as fp:
        json_obj = json.load(fp)

    template_obj = {}
    if inputs > 0:
        template_obj["hasInput"] = []
        for _ in range(inputs):
            template_obj["hasInput"].append(json_obj["schema"]["DatasetSpecification"])
    
    if outputs > 0:
        template_obj["hasOutput"] = []
        for _ in range(outputs):
            template_obj["hasOutput"].append(json_obj["schema"]["DatasetSpecification"])
    
    if parameters > 0:
        template_obj["hasParameter"] = []
        for _ in range(parameters):
            template_obj["hasParameter"].append(json_obj["schema"]["Parameter"])
    
    try:
        with open("./insertion_template.json", "w") as fp:
            fp.write(json.dumps(template_obj))
        
        logging.info("Generated the insertion template file in the root directory")
    except Exception as e:
        logging.error(str(e))

@cli.command(short_help="Transform the input YAML into a Valid JSON for posting the file to Model Catalog")
@click.argument("yaml_file_path", default=None, type=str)
def push(yaml_file_path):
    transformed_json = _transform_data.create_json(yaml_file_path)
    logging.info(json.dumps(transformed_json))

@cli.command(short_help="Validate the JSON obtained after creating one")
@click.argument("metadata_file_path", default=None, type=str)
def validate(metadata_file_path):
    _metadata_schema.validate_file(metadata_file_path)

