
dependencies=[
    'flask',
    'Flask-Cors',
    'fire',
    'dulwich',
    'wget',
    'request'
]
optional_dependencies=[
    'gitpython'
]
def install_requirements():
    import os
    for dep in dependencies:
        os.system('pip3 install %s'%(dep))
if __name__ == '__main__':
    install_requirements()
