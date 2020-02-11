import subprocess


def replace_all(name: str, value: str, file: str = 'local'):
    subprocess.run(['git', 'config', '--' + file, name, value], check=True, stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE, encoding='utf-8', universal_newlines=True)


def get(name: str, file: str = 'local'):
    res = subprocess.run(['git', 'config', '--' + file, name], check=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, encoding='utf-8', universal_newlines=True)
    return res.stdout.rstrip('\n')


def version():
    res = subprocess.run(['git', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         encoding='utf-8', universal_newlines=True)
    return res.stdout.rstrip('\n')
