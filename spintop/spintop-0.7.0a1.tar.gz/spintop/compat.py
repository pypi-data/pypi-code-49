import pkgutil

version_file_content = pkgutil.get_data('spintop.compat', 'VERSION' )
VERSION = version_file_content.decode().strip()
    
def format_exception(e):
    return e.__class__.__name__ + ': ' + str(e)