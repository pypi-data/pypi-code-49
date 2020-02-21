import sys
from . import core
from . import project

def help():
    print('''nb docker build
build:
    build docker image for the project and upload to configured cr.
    NOTE: the command will auto detect project root path (where .nb.yaml is stored)
    docker push will only happen when current git ref is tagged with value equal to version configured in .nb.yaml . you will see an error message telling you the push step has been skipped otherwise.''')
    sys.exit(0)


def handle(args):
    core.cd_project_root()
    if len(args) == 0:
        help()
    cmd = args[0]
    if 'build'.find(cmd) == 0:
        print('running docker build')
        p = project.load()
        version = p[project.key_version]
        crhost= p[project.key_crhost]
        image = p[project.key_image]
        prj = p[project.key_project]
        docker_tag = '{0}/{1}/{2}:{3}'.format(crhost,prj,image,version)
        shell_cmd = 'docker build -t {0} .'.format(docker_tag)
        print(shell_cmd)
        r,o = core.shell(shell_cmd, stdout=True)
        if r!=0:
            core.exit('error while building docker image')
        
        user = input('push {0}? y/n'.format(docker_tag)).strip()
        if user not in ['y','Y','yes','yeah']:
            core.exit('skipped pushing')
        print('pushing image')
        r,o = core.shell('docker push {0}'.format(docker_tag), stdout=True)
        if r == 0:
            print('pushing done')
        else:
            core.exit('something wrong happened')
        pass       
    else:
        core.exit('invalid command : {0}'.format(cmd))
        
