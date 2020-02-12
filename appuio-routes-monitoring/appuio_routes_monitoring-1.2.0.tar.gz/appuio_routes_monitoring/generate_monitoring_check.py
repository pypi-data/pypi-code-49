#!/usr/bin/python3

""" script to generate hieradata http monitoring check from appuio routes"""

import sys
import argparse
import subprocess
import logging
import yaml

LOG = logging.getLogger(__name__)


def get_appuio_object(cmd):
    """get a object from APPUiO and return it as yaml"""

    try:
        rval = subprocess.check_output(
            cmd,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )
        LOG.debug(
            'command "%s" completed with exit code "0" and output: "%s"',
            ' '.join(cmd),
            rval.strip().replace('\n', '; '),
        )
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(
            'command "%s" failed with exit code "%s" and output: "%s"' % (
                ' '.join(cmd),
                exc.returncode,
                exc.output.strip().replace('\n', '; '),
            )
        ) from None
    try:
        return yaml.safe_load(rval)['items']
    except yaml.YAMLError as exc:
        sys.exit('Could not parse routes: %s' % exc)


def get_routes_in_namespace(namespace):
    """ Get all routes in a namspace but ignore the ones with let's encrypt """
    return get_appuio_object([
        'oc',
        '-n', namespace,
        'get', 'route',
        '-l', 'acme.openshift.io/exposer!=true',
        '-o', 'yaml',
        ])


def get_routes(args):
    """ get routes from the openshift cluster """
    routes = []
    if args.projects == 'all':
        cmd = ['oc', 'get', 'project', '-o', 'yaml']
        projects = get_appuio_object(cmd)
        for project in projects:
            routes += get_routes_in_namespace(project['metadata']['name'])
        return routes

    for project in args.projects:
        routes += get_routes_in_namespace(project)
    return routes


def get_route_path(route):
    """ get route path"""
    route_path = route['spec'].get('path', '')

    return route_path


def has_annnotations(route):
    """ check if a route has annotations """
    if 'annotations' in route['metadata']:
        return True

    return False


def is_monitoring_enabled(route):
    """ check if monitoring is enabled """
    if not has_annnotations(route):
        return True

    annotations = route['metadata']['annotations']
    return annotations.get('monitoring/enabled', 'true')


def alert_customer(route):
    """ set alert customer if conditions are met """
    if not has_annnotations(route):
        return False

    annotations = route['metadata']['annotations']
    return annotations.get('monitoring/alert_customer', 'false')


def get_production_level(route):
    """ Set production level to 4 if annotations exists """
    if not has_annnotations(route):
        return None

    annotations = route['metadata']['annotations']
    if annotations.get('monitoring/alert_vshn', 'false') == 'true':
        return 4

    return None


def get_monitoring_path(route):
    """
    Set monitoring path.

    Defaults to '/'
    Is set to the route path if the route path is set, but monitoring/path is empty
    The monitoring/path annotation takes highest priority.
    """
    if not has_annnotations(route):
        return '/'

    annotations = route['metadata']['annotations']

    if annotations.get('monitoring/path'):
        return annotations.get('monitoring/path')

    if get_route_path(route):
        return get_route_path(route)

    return '/'


def get_route_name(route):
    """ The route name is the hostname + uri """
    route_path = get_route_path(route).rstrip('/')

    return route['spec']['host'] + route_path.replace('/', ':')


def build_hieradata(routes):
    """ build the hieradata based on the routes """
    hieradata = {}
    for route in routes:

        if not is_monitoring_enabled(route):
            continue

        hieradata[get_route_name(route)] = {
            'display_name': '{}{} on APPUiO in {}'.format(
                route['spec']['host'],
                get_route_path(route),
                route['metadata']['namespace']),
            'http_address': route['spec']['host'],
            'http_ssl': True,
            'http_uri': get_monitoring_path(route),
            'vars': {
                'alert_customer': alert_customer(route)
            }
        }

        if get_production_level(route):
            hieradata[route['spec']['host']]['production_level'] = get_production_level(
                route
            )

        if 'tls' not in route['spec']:
            hieradata[get_route_name(route)]['http_ssl'] = False

    return hieradata


def print_hieradata(hierakey, hieradata):
    """ print the hieradata yaml result """
    print(yaml.safe_dump({hierakey: hieradata}, default_flow_style=False))


def main():
    """ Generate hieradata code from APPUiO routes"""
    parser = argparse.ArgumentParser(
        description='generate hieradata from appuio routes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prog='appuio_routes_monitoring',
    )
    parser.add_argument(
        '-p', '--project', nargs='+',
        dest='projects', default='all'
    )
    parser.add_argument(
        '-k', '--key',
        dest='hierakey', default='profile_icinga2::hiera_httpchecks'
    )

    routes = get_routes(parser.parse_args())
    hieradata = build_hieradata(routes)
    print_hieradata(parser.parse_args().hierakey, hieradata)


if __name__ == '__main__':
    main()
