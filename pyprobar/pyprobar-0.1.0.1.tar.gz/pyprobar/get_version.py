import os
import pyprobar.version as version
NAME = 'pyprobar'
def get_version(update=False):
    v= version.version
    if update:
        v += 1
        with open(os.path.join(NAME,'version.py'),'w') as fo:
            fo.write('version= '+ str(v))
    return '.'.join(list(str(v)))

