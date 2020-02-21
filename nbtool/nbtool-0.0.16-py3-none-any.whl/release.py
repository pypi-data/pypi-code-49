from . import core
from . import project
import yaml
from os import path
import sys

def help():
    print('''install/upgrade k8s deployment using helm chart.
release:
    nb release <namespace> [variation]
    variables:
    - namespace : k8s namespace for the release
    - variation : if not empty, release_name=release_name-variation''')       
    sys.exit(0)


def handle(args):
    core.cd_project_root()
    p = project.load()
    service = p[project.key_service]
    if len(args) == 0:
        print('namespace arg is not optional')
        help()
    namespace = args[0]
    release = service 
    variation = ''
    if len(args) > 1:
        variation = args[1]
        release = '{0}-{1}'.format(service,variation)
    print('releasing {0} to namespace {1}'.format(release,namespace))
    r,o = core.shell('helm list -n {0} | grep {1}'.format(namespace,release))

    with open('chart/Chart.yaml', 'r') as f:
        chart = yaml.load(f, Loader=yaml.BaseLoader)
        if 'appVersion' not in chart:
            core.exit('failed to detect appVersion setting from chart')
        if chart['appVersion'] != p[project.key_version]:
            core.exit('chart appVersion does not match project version setting, abort execution')
    
    helm_cmd = 'install'
 
    if len(o) > 0:
        print('release {0} found in namespace {1}'.format(release,namespace))
        helm_cmd = 'upgrade'
    if len(variation) > 0 and not path.exists('chart/{0}.yaml'.format(variation)):
        core.exit('chart/{0}.yaml not found. abort releasing'.format(variation))
    shell = 'helm {0} {1} chart -n {2} --values chart/{3}.yaml'.format(helm_cmd, release,namespace,variation)
    print(shell)
    r,o = core.shell(shell,stdout=True)

