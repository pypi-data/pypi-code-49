import csv
from pathlib import Path

import click

from boiler import BoilerSession, cli
from boiler.commands.utils import exit_with, handle_request_error
from boiler.definitions import CameraLocation, ReleaseBatches


def ingest_video(video_path: str, release_batch: str, session: BoilerSession):
    video_name = Path(video_path).stem

    r = session.get('video', json={'name': video_name})
    out = handle_request_error(r)
    if r.ok and len(out['response']):
        click.echo(f'name={video_name} already exists', err=True)
        return out
    elif not r.ok:
        click.echo(f'Could not query server for video={video_name}', err=True)
        return out

    data = {'video_name': video_name, 'release_batch': release_batch}
    r = session.post('video/name', json=data)
    out = handle_request_error(r)

    if r.ok:
        v = out['response']
        click.echo(f'id={v["id"]} created for name={video_name}', err=True)
        click.echo(f'sending name={video_name} id={v["id"]} to S3', err=True)
        # TODO: upload to s3
        return out
    else:
        click.echo(f'name={video_name} creation failed', err=True)
        return out


@click.group(name='video', short_help='ingest and query video')
@click.pass_obj
def video(ctx):
    pass


@video.command(name='get-bulk-csv-header')
def make_header():
    click.echo('local_file,release_batch')


@video.command(name='bulk-ingest', help='ingest videos from CSV file')
@click.option('--file', type=click.File(mode='r'), required=True, help='csv file')
@click.pass_obj
def bulk_ingest(ctx, file):
    reader = csv.DictReader(file)
    payloads = []
    successes = []
    failures = []
    for row in reader:
        try:
            payloads.append(dict(**row))
        except ValueError as err:
            failures.append(
                {'error': str(err), 'context': f'Failed to construct valid payload for video',}
            )
            click.echo(str(err), err=True)
    for p in payloads:
        result = ingest_video(p['video_path'], p['release_batch'], ctx['session'])
        if 'error' in result:
            failures.append(result)
        else:
            successes.append(result)

    exit_with({'error': failures, 'response': successes})


@video.command(name='search', help='search for video')
@click.option('--name', type=click.STRING)
@click.option('--gtag', type=click.STRING)
@click.option('--location', type=click.Choice([e.value for e in CameraLocation]))
@click.option('--frame-rate', type=click.FLOAT, default=None)
@click.option('--duration', type=click.FLOAT, default=None)
@click.option('--width', type=click.INT, default=None)
@click.option('--height', type=click.INT, default=None)
@click.pass_obj
def search(ctx, **kwargs):
    data = {}
    for key, value in kwargs.items():
        if value is not None:
            data[key] = value
    r = ctx['session'].get('video', params=data)
    exit_with(handle_request_error(r))


@video.command(name='add', help='ingest video into stumpf from file')
@click.option(
    '--video-path', type=click.Path(exists=True, dir_okay=False, resolve_path=True),
)
@click.option(
    '--release-batch', type=click.Choice([e.value for e in ReleaseBatches]), required=True
)
@click.pass_obj
def add(ctx, video_path, release_batch):
    exit_with(ingest_video(video_path, release_batch, ctx['session']))


cli.add_command(video)  # type: ignore
