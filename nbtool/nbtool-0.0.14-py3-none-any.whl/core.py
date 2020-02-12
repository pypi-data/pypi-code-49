import sys
import subprocess
import yaml
import traceback
from . import docker
from . import project
from . import freeze
from . import release
import os
from os import path

modules = {
    'docker': docker,
    'project':project ,
    'freeze':freeze,
    'release':release,
}

invoke_path = ''

def help(args):
     
    if len(args) == 0:
        print('''welcome to nbtool help!
nb project|docker|release|freeze  args... 
nb help <cmd> to view help info for individual cmd
        
[workdir]: nb will detect project root (where config file is stored) for most commands. 

[config file]: nb works with .nb.yaml at project root, `nb project config` will guide user to setup/update this file.

[gcloud project]: if not found in config file, nb will read `gcloud info` automatically and determine your current project.         

[directory structure]: nb assumes following project folder structure: see `nb project init`
.nb.yaml Dockerfile src chart README.md ... 
    src: contains all source code.
    chart: contains helm chart to release/upgrade the service. see `nb help relase`
''')
        sys.exit(0)
    elif args[0] in modules:
        modules[args[0]].help()
    else:
        exit('there is no help for command: {0}'.format(args[0]))

def check_tag():
    p = project.load()
    version = p[project.key_version]
    r,o = shell('git tag')
    if len(o) == 0:
       exit('no git tags found, aborting') 
    match = False
    for line in o.splitlines():
        line = line.strip().decode()
        if line == version:
            print('tag matching version:{0}'.format(line))
            match = True
            break
        else:
            print('tag:{0} not matching version:{1}'.format(line, version))
    return match

    

def get_resources_path():
    return os.path.join(invoke_path,'resources')

def shell(cmds, stdout=False):
    sto = None
    if not stdout:
        sto = subprocess.PIPE
    p = subprocess.Popen(cmds,stdout=sto,shell=True)
    (out,err) = p.communicate()
    return p.returncode,out

def exit(err):
    print(err, file=sys.stderr)
    sys.exit(1)

    
    sys.exit(0)

def parse_gcloud():
    gcloud = {}
    r,o = shell(['gcloud info'])
    if r != 0:
        exit('gcloud sdk not installed or configured properly')
    lines = o.splitlines()
    for line in lines:
        line = line.decode()
        if line.find('project:') != -1:
            p = line[line.find('[')+1:line.find(']')]
            if len(p) == 0:
                print('WARNING: gcloud has no project info, please try reconfigure gcloud')
            gcloud['project'] = p
            break
    return gcloud

def cd_project_root():
    ok = False
    while not ok:
        if path.abspath(os.curdir) == '/':
            exit('we failed to locate project root. maybe you have not run nb project config?')
        if not path.exists('.nb.yaml'):
            os.chdir(os.path.join(os.getenv('PWD'),'..'))
        else:
            break
    print('working at {0}'.format(path.abspath(os.curdir)))
    

if __name__ == '__main__':
    invoke_path = sys.argv[0]
    if len(sys.argv) == 1:
        help([])

    cmd = sys.argv[1]
    if cmd == 'help':
        help(sys.argv[2:])
    if cmd not in modules:
        exit('cmd {0} not supported yet'.format(cmd)) 
    try:
        modules[cmd].handle(sys.argv[2:])
    except Exception as e:
        print(e)
        traceback.print_exc(file=sys.stdout)
        exit('{0} cmd faied to run'.format(cmd))
    
        
    
