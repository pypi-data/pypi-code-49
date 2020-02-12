import os
import pathlib
import asyncclick as click
from asyncclick.core import Context
from pangeamt_tea.project.config import Config
from pangeamt_tea.project.project import (
    Project,
    ProjectAlreadyExistsException,
    ProjectNotFoundException,
)
from pangeamt_tea.project.workflow.workflow import Workflow
from pangeamt_tea.project.workflow.workflow import WorkflowAlreadyExists

# from pangeamt_tea.project.train.train import train as model_trainer
from pangeamt_nlp.processor.processor_factory import ProcessorFactory
from pangeamt_nlp.translation_model.translation_model_factory import (
    TranslationModelFactory,
)


@click.group(invoke_without_command=True)
@click.pass_context
async def tea(ctx: Context):
    pass


# New Project
@tea.command()
@click.option("--customer", "-c", help="Customer name")
@click.option("--src_lang", "-s", help="Source language")
@click.option("--tgt_lang", "-t", help="Target language")
@click.option("--flavor", "-f", default=None, help="Flavor")
@click.option("--version", "-v", default=1, type=click.INT, help="Version")
@click.option(
    "--dir",
    "-d",
    "parent_dir",
    default=None,
    help="Directory where the project is created",
)
async def new(
    customer: str,
    src_lang: str,
    tgt_lang: str,
    flavor: str,
    version: int,
    parent_dir: str,
):

    parent_dir = parent_dir if parent_dir is not None else os.getcwd()
    parent_dir = pathlib.Path(os.path.abspath(parent_dir))

    try:
        Project.new(
            customer,
            src_lang,
            tgt_lang,
            parent_dir,
            version=version,
            flavor=flavor,
        )
    except (ProjectAlreadyExistsException, ProjectNotFoundException) as e:
        click.echo(f"Error: {e}")


@tea.group()
@click.pass_context
async def config(ctx: Context):
    pass


# Add processors
@config.command()
@click.option("--project", "-p", "project_dir")
@click.pass_context
def show(ctx: Context, project_dir: str):
    if project_dir is None:
        project_dir = os.getcwd()
    project_dir = pathlib.Path(project_dir)

    try:
        Config.show(project_dir)

    except ProjectNotFoundException as e:
        click.echo(f"Error: {e}")


# Add tokenizer
@config.command()
@click.option(
    "--src",
    "-s",
    help="Source tokenizer",
    type=click.Choice(["moses", "mecab"], case_sensitive=False),
)
@click.option(
    "--tgt",
    "-t",
    help="Target tokenizer",
    type=click.Choice(["moses", "mecab"], case_sensitive=False),
)
@click.option("--project", "-p", "project_dir")
@click.pass_context
def tokenizer(ctx: Context, src: str, tgt: str, project_dir: str):
    ctx.ensure_object(dict)

    if project_dir is None:
        project_dir = os.getcwd()
    project_dir = pathlib.Path(project_dir)

    try:
        Config.add_tokenizer(src, tgt, project_dir)

    except ProjectNotFoundException as e:
        click.echo(f"Error: {e}")


# Add truecaser
@config.command()
@click.option("--src", "-s", help="Source truecaser", is_flag=True)
@click.option("--tgt", "-t", help="Target truecaser", is_flag=True)
@click.option("--project", "-p", "project_dir")
@click.pass_context
def truecaser(ctx: Context, src: bool, tgt: bool, project_dir: str):
    ctx.ensure_object(dict)
    if project_dir is None:
        project_dir = os.getcwd()
    project_dir = pathlib.Path(project_dir)

    try:
        Config.add_truecaser(src, tgt, project_dir)

    except ProjectNotFoundException as e:
        click.echo(f"Error: {e}")


# Add processors
@config.command()
@click.option(
    "--set",
    "-s",
    help="List of processors separated by semicolons with arguments separated by "
    'commas.\n i.e. "processor1, arg1, arg2; processor2;"',
)
@click.option("--list", "-l", help="List available processors", is_flag=True)
@click.option("--project", "-p", "project_dir")
@click.pass_context
def processors(ctx: Context, set: str, list: bool, project_dir: str):
    if list:
        print()
        print("### List of available processors:\n")
        all_processors = ProcessorFactory.get_available()
        for name in all_processors.keys():
            print(" -  ", name)
            print(
                "     -  Description training:"
                f"{all_processors[name].DESCRIPTION_TRAINING}"
            )
            print(
                "     -  Description decoding:"
                f"{all_processors[name].DESCRIPTION_DECODING}"
            )
        print()
        return

    if project_dir is None:
        project_dir = os.getcwd()
    project_dir = pathlib.Path(project_dir)

    try:
        Config.add_processors(set, project_dir)
    except ProjectNotFoundException as e:
        click.echo(f"Error: {e}")


# Add bpe
@config.command()
@click.option("--joint", "-j", help="Joint bpe process", is_flag=True)
@click.option(
    "--num_iterations", "-n", help="Number of iterations", type=click.INT
)
@click.option("--threshold", "-t", help="Threshold bpe", type=click.INT)
@click.option("--project", "-p", "project_dir")
@click.pass_context
def bpe(
    ctx: Context,
    joint: bool,
    num_iterations: int,
    threshold: int,
    project_dir: str,
):

    if project_dir is None:
        project_dir = os.getcwd()
    project_dir = pathlib.Path(project_dir)

    if threshold is None:
        threshold = 50

    try:
        Config.add_bpe(joint, num_iterations, threshold, project_dir)
    except ProjectNotFoundException as e:
        click.echo(f"Error: {e}")


# Add translation_model
@config.command()
@click.option("--name", "-n", help="Trainer name")
@click.option("--args", "-a", help="Arguments for the trainer")
@click.option("--list", "-l", help="List all available trainers", is_flag=True)
@click.option("--project", "-p", "project_dir")
@click.pass_context
def translation_model(
    ctx: Context, name: str, args: str, list: bool, project_dir: str,
):
    if list:
        print()
        print("### List of available trainers:\n")
        for name in TranslationModelFactory.get_available().keys():
            print(" -  ", name)
        print()
        return

    if project_dir is None:
        project_dir = os.getcwd()
    project_dir = pathlib.Path(project_dir)

    if args is None:
        translation_model = TranslationModelFactory.get_class(name)
        args = translation_model.DEFAULT

    try:
        Config.add_translation_model(name, args, project_dir)
    except ProjectNotFoundException as e:
        click.echo(f"Error: {e}")


# Add reset command
@tea.command()
@click.option("--section", "-s", help="Name of the section to reset")
@click.option("--project", "-p", "project_dir")
@click.pass_context
def reset(ctx: Context, section: str, project_dir: str):
    if project_dir is None:
        project_dir = os.getcwd()
    project_dir = pathlib.Path(project_dir)

    try:
        Config.reset_section(section, project_dir)
    except ProjectNotFoundException as e:
        click.echo(f"Error: {e}")


# Workflow group
@tea.group(invoke_without_command=True)
@click.option("--project", "-p", "project_dir")
@click.pass_context
async def workflow(ctx, project_dir):
    ctx.ensure_object(dict)
    if project_dir is None:
        project_dir = os.getcwd()
    project_dir = os.path.abspath(project_dir)
    project_dir = pathlib.Path(project_dir)
    ctx.obj["project"] = Project.load(project_dir)


# New workflow
@workflow.command()
@click.option("--force", "-f", default=False)
@click.pass_context
async def new(ctx: Context, force):
    """
    Init the workflow.
    """
    project = ctx.obj["project"]
    try:
        await Workflow.new(project, force)
    except WorkflowAlreadyExists as e:
        click.echo(f"Error: {e}")

    #    click.echo(ctx.obj["project"])
    click.echo("---> Done")


# Status workflow
@workflow.command()
@click.pass_context
async def status(ctx: Context):
    workflow = Workflow.load(ctx.obj["project"])
    workflow.show()


# Clean
@workflow.command()
@click.option(
    "--num_workers",
    "-n",
    type=click.INT,
    help="Max number of workers to be spawned.",
)
@click.pass_context
async def clean(ctx: Context, num_workers: int):
    if num_workers is None:
        raise ValueError(
            "Maximum number of workers not defined. i.e. clean -n 4"
        )

    workflow = Workflow.load(ctx.obj["project"])
    await workflow.run_stage("clean", num_workers)

    #    click.echo(ctx.obj["project"])
    click.echo("---> Done")


# Prepare
@workflow.command()
@click.option(
    "--num_workers",
    "-n",
    type=click.INT,
    help="Max number of workers to be spawned.",
)
@click.option(
    "--project",
    "-p",
    "project_dir",
    help="The project directory. Default: the current working directory",
)
@click.pass_context
async def prepare(ctx: Context, num_workers: int, project_dir: str):
    workflow = Workflow.load(ctx.obj["project"])
    await workflow.run_stage("prepare", num_workers)


# Train
@workflow.command()
@click.option(
    "--gpu",
    "-g",
    type=click.INT,
    help="The GPU where the model will be trained",
)
@click.option(
    "--project",
    "-p",
    "project_dir",
    help="The project directory. Default: the current working directory",
)
@click.pass_context
async def train(ctx: Context, gpu: int, project_dir: str):
    workflow = Workflow.load(ctx.obj["project"])
    await workflow.run_stage("train")


def main():
    tea(_anyio_backend="asyncio")  # or asyncio, or curio


class RequireOptionExpcetion(Exception):
    def __init__(self, command: str, variable: str):
        super().__init__(f"Error: {command} {variable} is required")


if __name__ == "__main__":
    main()
