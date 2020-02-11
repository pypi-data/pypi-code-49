import pkg_resources,os
from . import pkg_info

def get_filepath(fn):
    fn=os.path.join('data',fn)
    return pkg_resources.resource_filename('wpkit',fn)
def get_data(fn):
    fn = os.path.join('data', fn)
    fn=pkg_resources.resource_filename('wpkit',fn)
    with open(fn,'r',encoding='utf-8') as f:
        return f.read()
def get_pkg_tree():
    dir=pkg_info.pkg_dir
    from wpkit.basic import dir_tree
    return dir_tree(dir)
def get_resource_tree():
    dir = pkg_info.pkg_data_dir
    from wpkit.basic import dir_tree
    return dir_tree(dir)