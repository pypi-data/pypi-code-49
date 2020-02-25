import os, pkg_resources, shutil

def create_schema_documentation(schema_string, output_folder, output_name):
    """
    Generates documentation for the provided LIXI schema. Documentation is based on a custom version of readthedocs [https://docs.readthedocs.io/en/rel/theme.html] theme.

    Args:
        schema_etree (:obj:`lxml.etree`, required): LIXI XML schema provided as string.
        output_folder (:obj:`str`, required): Path to write the produced lixi schema documentation to.
        outputname (:obj:`str`, required): Custom schema name used in namespace. Do .
            
    Returns:
        Outputs the custom documentation for a schema to the specified folder. 
    """
    
    def copytree(src, dst, symlinks=False, ignore=None):
        
        if os.path.exists(dst):
            shutil.rmtree(dst)
            os.mkdir(dst)
        else:    
            os.mkdir(dst)
        
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)    
    
    # First create the directory
    output_path = os.path.join(output_folder, output_name) 
    
    # Copy all documentation files from lib to provided path
    docs_location = pkg_resources.resource_filename(__name__, "documentation")
    copytree(docs_location, output_path)
    
    # Write data to file to display correct info
    data = "var schemaString = `" + schema_string + "`"
    writepath = os.path.join(output_path, 'js', 'LIXI-Master-Schema.js')
    with open(writepath, 'w') as file:
        data = file.write(data)
        
    return True
        
        