from galileo_sdk import GalileoSdk
import pandas
import click
import datetime


def jobs_cli(main, galileo: GalileoSdk):
    @main.group()
    def jobs():
        """
        See all jobs, manage the state of a job, or download your results.
        """
        pass

    @jobs.command()
    @click.argument("index", type=int, required=False)
    @click.option(
        "-i",
        "--id",
        type=str,
        multiple=True,
        help="Filter by job id, can provide multiple options.",
    )
    @click.option(
        "-r",
        "--receiver",
        type=str,
        multiple=True,
        help="Filter by receiver id, can provide multiple options.",
    )
    @click.option(
        "-s",
        "--sid",
        type=str,
        multiple=True,
        help="Filter by station id, can provide multiple options.",
    )
    @click.option(
        "--status",
        type=str,
        multiple=True,
        help="Filter by status, can provide multiple options.",
    )
    @click.option(
        "--page", type=int, multiple=True, help="Filter by page.",
    )
    @click.option(
        "--items", type=int, multiple=True, help="Filter by items per page.",
    )
    def ls(index, id, receiver, sid, status, page, items):
        """
        List all jobs.
        """

        r = galileo.jobs.list_jobs(
            jobids=list(id),
            receiverids=list(receiver),
            stationids=list(sid),
            statuses=list(status),
            page=page,
            items=items,
        )

        if not r["jobs"]:
            click.echo("No job matches that query.")
            return

        if isinstance(index, int):
            jobs_list = r["jobs"][index]
        else:
            jobs_list = r["jobs"]

        jobs_df = pandas.json_normalize(jobs_list)
        jobs_df.time_created = jobs_df.time_created.map(
            lambda x: datetime.datetime.fromtimestamp(x)
        )
        jobs_df.last_updated = jobs_df.last_updated.map(
            lambda x: datetime.datetime.fromtimestamp(x)
        )
        jobs_df.total_runtime = jobs_df.total_runtime.map(lambda x: x / 60)
        jobs_df = jobs_df[
            [
                "jobid",
                "stationid",
                "receiverid",
                "name",
                "total_runtime",
                "status",
                "time_created",
                "last_updated",
            ]
        ]
        click.echo(jobs_df)

    @jobs.command()
    @click.option(
        "-j", "--jobid", type=str, prompt="Job ID", required=True, help="Job id.",
    )
    def request_stop(jobid):
        """
        Request to stop a job.
        """
        jobs_list = galileo.jobs.request_start_job(jobid)["job"]
        jobs_df = pandas.json_normalize(jobs_list)
        jobs_df.time_created = jobs_df.time_created.map(
            lambda x: datetime.datetime.fromtimestamp(x)
        )
        jobs_df.last_updated = jobs_df.last_updated.map(
            lambda x: datetime.datetime.fromtimestamp(x)
        )
        jobs_df = jobs_df[
            [
                "jobid",
                "stationid",
                "receiverid",
                "name",
                "total_runtime",
                "status",
                "time_created",
                "last_updated",
            ]
        ]
        click.echo(jobs_df)

    @jobs.command()
    @click.option(
        "-j", "--jobid", type=str, prompt="Job ID", required=True, help="Job id.",
    )
    def request_pause(jobid):
        """
        Request to pause a job.
        """
        jobs_list = galileo.jobs.request_start_job(jobid)["job"]
        jobs_df = pandas.json_normalize(jobs_list)
        jobs_df.time_created = jobs_df.time_created.map(
            lambda x: datetime.datetime.fromtimestamp(x)
        )
        jobs_df.last_updated = jobs_df.last_updated.map(
            lambda x: datetime.datetime.fromtimestamp(x)
        )
        jobs_df = jobs_df[
            [
                "jobid",
                "stationid",
                "receiverid",
                "name",
                "total_runtime",
                "status",
                "time_created",
                "last_updated",
            ]
        ]
        click.echo(jobs_df)

    @jobs.command()
    @click.option(
        "-j", "--jobid", type=str, prompt="Job ID", required=True, help="Job id.",
    )
    def request_start(jobid):
        """
        Request to start a job.
        """
        jobs_list = galileo.jobs.request_start_job(jobid)["job"]
        jobs_df = pandas.json_normalize(jobs_list)
        jobs_df.time_created = jobs_df.time_created.map(
            lambda x: datetime.datetime.fromtimestamp(x)
        )
        jobs_df.last_updated = jobs_df.last_updated.map(
            lambda x: datetime.datetime.fromtimestamp(x)
        )
        jobs_df = jobs_df[
            [
                "jobid",
                "stationid",
                "receiverid",
                "name",
                "total_runtime",
                "status",
                "time_created",
                "last_updated",
            ]
        ]
        click.echo(jobs_df)

    @jobs.command()
    @click.option(
        "-j", "--jobid", type=str, prompt="Job ID", required=True, help="Job id.",
    )
    @click.option(
        "-p",
        "--path",
        type=str,
        prompt="Path (where results will be stored)",
        required=True,
        help="The path where the job results will be downloaded to.",
    )
    def download_results(jobid, path):
        """
        Download results of job when finished.
        """
        r = galileo.jobs.download_job_results(jobid, path)
        if r:
            click.echo(f"Downloading results into directory '{path}' ...")
