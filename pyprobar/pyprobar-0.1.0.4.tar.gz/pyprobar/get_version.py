import os
import pyprobar.version as version

def get_version(update=False):
    v= version.version
    name = version.name
    if update:
        v += 1
        with open(os.path.join(version.name,'version.py'),'w') as fw:
            fw.write('version= '+ str(v)+'\n')
            fw.write(f"""name='{name}'""")
    return '.'.join(list(str(v)))

