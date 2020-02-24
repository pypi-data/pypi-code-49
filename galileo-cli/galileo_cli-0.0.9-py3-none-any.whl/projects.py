import click
import pandas
from galileo_sdk import GalileoSdk
from halo import Halo


def projects_cli(main, galileo: GalileoSdk):
    @main.group()
    def projects():
        pass

    @projects.command()
    @click.argument("index", type=int, required=False)
    @click.option(
        "-i",
        "--id",
        type=str,
        multiple=True,
        help="Filter by project id, can provide multiple options.",
    )
    @click.option(
        "-n",
        "--name",
        type=str,
        multiple=True,
        help="Filter by project name, can provide multiple options.",
    )
    @click.option(
        "-u",
        "--userid",
        type=str,
        multiple=True,
        help="Filter by userids, can provide multiple options.",
    )
    @click.option("--page", type=int, help="Filter by page number.")
    @click.option(
        "--items", type=int, help="Filter by number of items in the page.",
    )
    @click.option('-n', '--head', type=int, help="Number of items to display.")
    def ls(index, id, name, userid, page, items, head):
        """
        List all projects.
        """
        spinner = Halo("Retrieving information", spinner="dot").start()
        self = galileo.profiles.self()
        spinner.stop()
        spinner = Halo("Retrieving your projects", spinner="dot").start()
        userid += (self["userid"],)
        r = galileo.projects.list_projects(
            ids=list(id),
            names=list(name),
            user_ids=list(userid),
            page=page,
            items=items,
        )

        if not r["projects"]:
            spinner.stop()
            click.echo("No project matches that query.")
            return

        if isinstance(index, int):
            projects_ls = galileo.projects.list_projects(
                ids=list(id),
                names=list(name),
                user_ids=list(userid),
                page=page,
                items=items,
            )["projects"][index]
        else:
            projects_ls = galileo.projects.list_projects(
                ids=list(id),
                names=list(name),
                user_ids=list(userid),
                page=page,
                items=items,
            )["projects"]

        projects_df = pandas.json_normalize(projects_ls)
        projects_df['creation_timestamp'] = pandas.to_datetime(projects_df.creation_timestamp)
        projects_df = projects_df.sort_values(by="creation_timestamp", ascending=False)
        projects_df = projects_df[
            [
                "id",
                "name",
                "description",
                "source_storage_id",
                "source_path",
                "destination_storage_id",
                "destination_path",
                "creation_timestamp",
            ]
        ]

        spinner.stop()

        if head:
            click.echo(projects_df.head(head))
        else:
            click.echo("(Displaying only first 30 items)\n")
            click.echo(projects_df.head(30))

    @projects.command()
    @click.option(
        "-n", "--name", prompt="Name of project", required=True, help="Name of project."
    )
    @click.option(
        "-d",
        "--description",
        prompt="Description of project",
        required=True,
        help="Description of project.",
    )
    def create(name, description):
        """
        Create a project to start running a job.
        """
        project = galileo.projects.create_project(name, description)["project"]
        project_df = pandas.json_normalize(project)
        project_df = project_df[
            [
                "id",
                "name",
                "description",
                "source_storage_id",
                "source_path",
                "destination_storage_id",
                "destination_path",
                "user_id",
                "creation_timestamp",
            ]
        ]
        click.echo(project_df)

    @projects.command()
    @click.option("-p", "--pid", prompt="Project ID", required=True, help="Project ID.")
    @click.option(
        "-d",
        "--dir",
        prompt="Directory to upload",
        required=True,
        help="Path of directory you want to upload.",
    )
    @click.option(
        "-n",
        "--name",
        prompt="Name of directory",
        required=True,
        help="Name of the directory.",
    )
    def upload(pid, dir, name):
        """
        Upload a directory to a project.
        """
        if galileo.projects.upload(pid, dir, name):
            click.echo(f"Uploaded directory {dir} into project {pid}.")

    @projects.command()
    @click.option("-p", "--pid", prompt="Project ID", required=True)
    @click.option("-s", "--sid", prompt="Station ID", required=True)
    @click.option("-m", "--mid", prompt="Machine ID")
    def run(pid, sid, mid):
        """
        Start running a job on a machine or station.
        """
        if mid:
            if galileo.projects.run_job_on_machine(pid, sid, mid):
                click.echo(f"Started running job in project {pid} on machine {mid}.")
        else:
            if galileo.projects.run_job_on_station(pid, sid):
                click.echo(f"Started running job in project {pid} on station {sid}.")
