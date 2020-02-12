import json
import os

from jinja2 import Environment, FileSystemLoader
from k9.core import last_word, namespace_exists, get_default_namespace, create_namespace, run_command

def helm_repo_add(repo_name: str, repo_url: str):
    """
    Adds the repository to the current kubernetes environment.

    :param repo_name: Local name of repository
    :param repo_url: URL of repository
    :return: output string on success, exception if failure.
    """
    return run_command('helm', 'repo', 'add', repo_name, repo_url)


def helm_repo_update():
    """
    Update the local copy of the repository with the current
    repository.

    :param repo_name:
    :return: output string on success, exception if failure.
    """
    return run_command('helm', 'repo', 'update')


def helm_repo_ls():
    """
    Lists available repositories.

    :return: Object derived from JSON output, exception on failure.
    """
    result = run_command('helm', 'repo', 'list', '-o', 'json')
    return json.loads(result.stdout)


def helm_repo_remove(repo_name: str):
    """
    Removes a repository.

    :param repo_name:
    :return: output string on success, exception if failure.
    """
    return run_command('helm', 'repo', 'remove', repo_name)


def helm_install(chart_name: str, params, release_name: str = None, debug = False, namespace: str = None):
    """
    Runs the Helm installation for the specified chart.   Before the chart
    is installed, the values file which should have the same name as the release_name
    will be evaluated with Jinja, using the parameters to build the new values file.

    The values file is written to the .output/{{release-name}}-values.yaml.

    Helm installation is run with this values.yaml file and on the
    default namespace set using set_default_namespace()

    :param chart_name: Name of Chart.
    :param params: Parameter values in a Dictionary used when pre-processing values.  If it is not a dictionary,
                   the vars() function is run on the object to create a dictionary.
    :param release_name: If None - release_name is defaulted to the last word in chart_name.  For example
           if chart_name is "stable/tomcat", the release_name is "tomcat".   Release name
           is also used to construct the charts values file in the following format:
           ./charts/{{release_name}}-values.yaml
    :param debug: If True, runs Helm with --debug and --dry-run, which will not actually run
                  and displays the chart values.  Default is False.
    :param namespace: Namespace to install the chart on. If None, we use the default namespace.
    :return: output string on success, exception if failure.

    """
    f = None

    try:
        if namespace is None:
            namespace = get_default_namespace()

        if not namespace_exists(namespace):
            create_namespace(namespace)

        if not isinstance(params, dict):
            params = vars(params)

        # setup release_name
        if release_name is None:
            release_name = last_word(chart_name)

        env = Environment(loader=FileSystemLoader('./charts/'))
        value_fn = f'{release_name}-values.yaml'

        if not os.path.exists(f'./charts/{value_fn}'):
            value_fn = f'{release_name}-values.yml'

        if not os.path.exists(f'./charts/{value_fn}'):
            print(f'values file not found: ./charts/{value_fn}')

        template = env.get_template(value_fn)
        template_body = template.render(params)

        if not os.path.exists('./.output'):
            os.mkdir('./.output')

        value_path = f'./.output/{value_fn}'
        f = open(value_path, 'w+')
        f.write(template_body)
        f.close()

        the_call = ['helm', 'install', '-n', namespace, '-f', value_path, release_name, chart_name]
        if debug:
            the_call.extend(['--debug', '--dry-run'])

        return run_command(*the_call)

    finally:
        if f is not None:
            f.close()


def helm_ls(namespace: str = None):
    """
    Lists all current helm installations.

    :param namespace: Namespace to list charts from. If None, we use the default namespace.
    :return: List of all helm installations.  Throws exception on error.

    Sample Output::

        [
            {"name":"tomcat",
            "namespace":"default",
            "revision":"1",
            "updated":"2019-12-10 18:28:43.753814 -0500 EST",
            "status":"deployed",
            "chart":"tomcat-0.4.0",
            "app_version":"7.0"}
        ]

    """

    if namespace is None:
        namespace = get_default_namespace()
    
    result = run_command('helm', '-n', namespace, 'ls', '-o', 'json')
    values = json.loads(result.stdout)
    return values


def helm_exists(release_name: str, namespace: str = None):
    """
    Returns true if the specified release_name exist.

    :param release_name: Name of release.
    :param namespace: Namespace to check for the chart in. If None, we use the default namespace.
    :return: True if found.
    """
    result = helm_ls(namespace)
    found = [
        release
        for release in result
        if release['name'] == release_name
    ]
    return len(found) > 0


def helm_uninstall(release_name: str, namespace: str = None):
    """
    Uninstalls the specified release.

    :param release_name: Name of the release you want to uninstall.
    :param namespace: Namespace to uninstall the chart from. If None, we use the default namespace.
    :return: Returns output value from uninstall process.  Otherwise throws exception.
    """
    if namespace is None:
        namespace = get_default_namespace()
    return run_command('helm', 'uninstall', '-n', namespace, release_name)
