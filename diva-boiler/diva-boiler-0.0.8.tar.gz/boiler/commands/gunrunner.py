import click

from boiler import cli, KW18BaseName
from boiler.commands.utils import activity_types_from_file, exit_with, handle_request_error
from boiler.definitions import AnnotationVendors


@click.group(name='gunrunner', short_help='Manage transitions to gunrunner')
@click.pass_obj
def gunrunner(ctx):
    pass


@gunrunner.command(name='dispatch', help='Dispatch a set of activities to gunrunner')
@click.option('--video-name', type=click.STRING, help='video name in stumpf', required=True)
@click.option(
    '--vendor-name',
    type=click.Choice([e.value for e in AnnotationVendors]),
    help='vendor name in stumpf',
    required=True,
)
@click.option('--kw18', type=KW18BaseName(), help='basename of kw18 files', required=True)
@click.option('--activity-type-list', type=click.File(mode='r'), required=True)
@click.pass_obj
def dispatch(ctx, video_name, vendor_name, kw18, activity_type_list):
    # refactor
    for f in kw18.values():
        if f['file'] is None:
            f['model'] = {'id': None}
            continue
        f['file'].seek(0, 0)  # reset reader position after local deserialization
        payload = {'file': f['file']}
        r = ctx['session'].post('upload', files=payload)
        if r.status_code == 409:
            r.status_code = 201
        resp = handle_request_error(r)
        if r.status_code == 201:
            f['model'] = resp['response']
        else:
            exit_with(resp)

    data = {
        'video_name': video_name,
        'vendor_name': vendor_name,
        'kw18_geom_id': kw18['geom']['model']['id'],
        'kw18_types_id': kw18['types']['model']['id'],
        'kw18_activities_id': kw18['activities']['model']['id'],
        'kw18_regions_id': kw18['regions']['model']['id'],
        'activity_types': activity_types_from_file(activity_type_list),
    }
    r = ctx['session'].post('video-pipeline/gunrunner/dispatch', json=data)
    if not r.ok:
        exit_with(handle_request_error(r))
    else:
        resp = r.json()
        num_activity_types = len(resp['status_changes'])
        click.echo(f'transitioned {num_activity_types} activity types from audit to gunrunner.')


cli.add_command(gunrunner)
