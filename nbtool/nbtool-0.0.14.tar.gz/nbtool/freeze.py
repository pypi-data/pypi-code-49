from . import core

def handle(args):    
    core.cd_project_root()
    core.shell('pip freeze | grep -vi uwsgi | grep -vi cython | grep -vi nbtool > src/docker_requirements.txt')
    core.shell('pip freeze > src/requirements.txt')
    
