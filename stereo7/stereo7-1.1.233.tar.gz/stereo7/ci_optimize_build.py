import os


def main(project, parser):
    if os.path.isfile('CI_optimize_build.py'):
        return 0 == os.system('python CI_optimize_build.py')
    return True
