import sys
from django.conf import settings


def common(template_name, *args):
    project_dir_name = getattr(settings, 'BASE_DIR', '').split('/')[-1]
    virtualenv = sys.executable.split('/bin')[0]
    python_interpreter = sys.executable

    return {
        'settings': settings,
        'project_dir_name': project_dir_name,
        'virtualenv': virtualenv,
        'python_interpreter': python_interpreter
    }