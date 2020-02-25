import os
import guang.version as version

def get_version(update=False):
    v= version.version
    if update:
        v += 1
        with open(os.path.join('guang','version.py'),'w') as fo:
            fo.write('version= '+ str(v))
    return '.'.join(list(str(v)))

