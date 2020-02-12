from . import core
from sys import stdin
import yaml
from pkg_resources import resource_listdir
import os

key_crhost = 'crhost'
key_project = 'project'
key_image= 'image'
key_version= 'version'
key_service= 'k8s_service'


project_configs = {
    key_crhost : 'host for container registry',
    key_project: 'gcloud project',
    key_image: 'docker image name',
    key_version: 'version',
    key_service: 'k8s service name',
}


def help():
    print('''config or init a project
    config:
        nb project config
        NOTE: pls make sure you are running this at project root path
        as .nb.yaml file will be generated in here.
        You will be asked to configure typical nb project properties,
        don't worry in case some values are entered incorrectly,
        you could always edit .nb.yaml file after this step.
    init:
        nb project init python
        only init python project is supported currently. will create src folder with cython and uwsgi configs.
    ''')
    core.exit('')

def load(check=True):
    c = {}
    for k in project_configs:
        if k not in c:
            c[k] = '' 
    try:
        with open('.nb.yaml','r') as f:
            l = yaml.load(f,Loader=yaml.BaseLoader)
            if l is not None:
                c = l
            if check:
                for k in project_configs:
                    if k not in c or len(c[k]) == 0:
                        core.exit('config:{0} not found'.format(k))
            return c
    except EnvironmentError:
        if check:
            core.exit('.nb.yaml not found in current path. maybe try nb project config?')
        return c

def do_version():
    core.cd_project_root()
    c = load()
    if key_version not in c:
        core.exit('project version config not found')
    v = c[key_version] 
    user = input('current verison :{0}, update to ?'.format(v)).strip()
    items = user.split('.')
    if len(items) != 3:
        core.exit('invalid version number. pls use major.minor.build')
    if user != v:
        cmd = "sed -e 's/appVersion: {0}/appVersion: {1}/' -i chart/Chart.yaml".format(v,user)
        print(cmd)
        r,o = core.shell(cmd)
        if r != 0:
            core.exit('failed to update chart/Chart.yaml')
        cmd = "sed -e 's/version: {0}/version: {1}/' -i .nb.yaml".format(v,user)
        print(cmd)
        r,o = core.shell(cmd)
        if r != 0:
            core.exit('failed to update .nb.yaml')
    core.exit('version number updated.')

def do_config():
    print('config project')
    c = load(check=False)
    if key_project not in c or c[key_project] == '':
        print('project configure not found, trying to retrive from gcloud sdk')
        g = core.parse_gcloud()
        c[key_project] = g['project']
    if key_crhost not in c or c[key_crhost] == '':
        c[key_crhost] = 'asia.gcr.io'
    for k in project_configs:
        if k not in c:
            c[k] = ''
        atleast_once = True
        while len(c[k]) == 0 or atleast_once:
            atleast_once=False
            user = input('{0}? or use [{1}]'.format(project_configs[k],c[k])).strip()
            if len(user) == 0 and len(c[k]) != 0:
                # so we keep the original value
                break
            c[k] = user
    with open('.nb.yaml', 'w') as f:
        f.write(yaml.dump(c))    
    print('.nb.yaml configured')        

def do_init(args):
    if os.path.exists('src'):
        print('path src exists, skip creating')
    else:
        which = 'python'
        if len(args) == 0:
            user = input('shall I setup a {0} template?[y/n]'.format(which)).lower()
            if user in ['y','yes','yeah']:
                print('setting up python src folder')
                r,o = core.shell('tar zxvf {0}/python.tgz'.format(core.get_resources_path()),stdout=True)
                if r ==0:
                    print('finished setup')
                else:
                    print('something wrong while setting up python src')
                r,o = core.shell('cp {0}/Dockerfile .'.format(core.get_resources_path()))
                if r == 0:
                    print('successfully created Dockerfile')
    if os.path.exists('chart'):
        print('path chart exists, skip creating')
    else:
        p = load()
        service = p[key_service]
        if service == '':
            core.exit('service name config not found. maybe you have not run nb project config?')
        r,o=core.shell('helm create {0}'.format(service)) 
        if r!= 0:
            core.exit('helm creating failed. maybe you have not configured helm properly?')
        print('helm chart creation done. renaming')
        r,o = core.shell('mv {0} chart'.format(service))
        if r == 0:
            print('renaming done. chart path is ready')
        

def handle(args):
    if len(args) == 0:
        help()
    cmd = args[0]
    if 'config'.find(cmd) == 0:
        do_config()
    elif 'init'.find(cmd) == 0:
        do_init(args[1:])
    elif 'version'.find(cmd) == 0:
        do_version()
        
