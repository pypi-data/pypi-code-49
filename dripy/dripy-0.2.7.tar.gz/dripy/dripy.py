"""Module for working with drilling data.

"""

import lasio

def las_to_excel(las_file_path : str):
    """Converts a .las file to a .xlsx file. Creates a .xlsx file with the same name (different extension) as the input file.
    
    Parameters
    ----------
    las_file_path : str
        Filepath to data in .las format

    """
    las = lasio.read(las_file_path, ignore_header_errors=True)
    las.to_excel(las_file_path.replace('.las', '.xlsx'))

