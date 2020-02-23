"""Functions to manage os files and Path objects.

Intended to be used within a Python 3 environment.
Developed by Rodrigo Rivero.
https://github.com/rodrigo1392

"""

# Flexibility for python 2.x
try:
    import configparser
except ImportError:
    import ConfigParser as configparser
try:
    from pathlib import Path
except ImportError:
    pass
import ast
import os
import shutil

from . import strings_tools as st


def create_non_existent_folder(folder_path):
    """Create a folder if it does not exist yet.

    Parameters
    ----------
    folder_path : Path
        Path of folder to verify/create.

    Returns
    -------
    Path
        Path of verified/created folder.
    """
    # Normalize input path and attempt to create folder. If it already
    # exists, do nothing.
    folder_path = Path(folder_path)
    try:
        folder_path.mkdir()
        print(str(folder_path), 'folder created')
        return folder_path
    except FileExistsError:
        return folder_path


def extract_config_from_cfg(cfg_path):
    """Extract input data from *.cfg file.

    Parameters
    ----------
    cfg_path : Path
        Config file to read from.

    Returns
    -------
    dict
        Config keywords: python objects pairs.
    """
    # Start parser engine and read cfg file.
    cfg = configparser.ConfigParser()
    cfg.read(cfg_path)

    # Gather all input variables and merge them in one dict.
    input_data = ({k.lower(): v for k, v in cfg.items(i)}
                  for i in cfg.sections())
    config_dict = {}
    for i in input_data:
        config_dict.update(i)

    # Try to convert variables to Python objects.
    output_data = {}
    for k, value in config_dict.items():
        try:
            output_data[k] = ast.literal_eval(value)
        except SyntaxError:
            output_data[k] = value
        except TypeError:
            output_data[k] = value
    return output_data


def find_file(root_path, searched_file, recursively=False):
    """Find instances of file, searching in a folder system.

    Parameters
    ----------
    root_path : Path
        Top level folder, start search here.
    searched_file : str
        Name of searched file.
    recursively : bool, optional
        If True, search folders recursively. Default is False.

    Returns
    -------
    list
        Full Paths of `searched_file` instances.
    False
        If file is not found.
    """
    # List all files in root and extract searched file path.
    paths_list = list_files(root_path, True, recursively)
    file_path = [i for i in paths_list if str(i.name) == searched_file]
    if not file_path:
        print('File not found')
        return False
    return file_path


def generate_folder_walker(root_path, level=1):
    """Create generator that walks a folder recursively.

    Parameters
    ----------
    root_path : Path
        Top level folder, start search here.
    level : int
        Amount of levels to walk for.

    Yields
    ------
    Path
        Paths of accessed folders.
    """
    root_path = root_path.rstrip(os.path.sep)
    assert os.path.isdir(root_path)
    num_sep = root_path.count(os.path.sep)
    for root, dirs, files in os.walk(root_path):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]


def list_files(root_path, full_path=True, recursively=True):
    """List all files paths in a folder.

    Parameters
    ----------
    root_path : Path
        Top level folder, start search here.
    full_path : bool, optional
        If True, gets Full Path of files, instead of just files names.
    recursively : bool, optional
        If True, search folders recursively. Default is False.

    Returns
    -------
    List
        Paths of all existing files.
    """
    root_path = Path(root_path)

    # List files with or without recursion.
    if recursively:
        paths_list = [f for f in root_path.rglob("*") if f.is_file()]
    else:
        paths_list = [f for f in root_path.iterdir() if f.is_file()]
    if not full_path:
        paths_list = [f.name for f in paths_list]

    # Try to sort files by digits
    try:
        return st.sort_strings_by_digit(paths_list)
    except IndexError:
        return paths_list


def list_files_with_extension(root_path, extension, full_path=True,
                              recursively=True):
    """List all files paths in a folder, filtered by a given suffix.

    Parameters
    ----------
    root_path : Path
        Top level folder, start search here.
    extension : str
        Extension of files to list.
    full_path : bool, optional
        If True, gets Full Path of files, instead of just files names.
    recursively : bool, optional
        If True, search folders recursively. Default is False.

    Returns
    -------
    List
        Paths of filtered files.
    """
    # List all files in root and filter them by extension.
    paths_list = list_files(root_path, full_path, recursively)
    paths_list = [i for i in paths_list if
                  i.suffix == '.' + extension.replace('.', '')]
    return paths_list


def list_files_with_substring(root_path, input_string, full_path=True,
                              recursively=True):
    """List all files paths in a folder, filtered by given substring.

    Parameters
    ----------
    root_path : Path
        Top level folder, start search here.
    input_string : str
        String to filter paths by.
    full_path : bool, optional
        If True, gets Full Path of files, instead of just files names.
    recursively : bool, optional
        If True, search folders recursively. Default is False.

    Returns
    -------
    List
        Paths of filtered files.
    """
    # List all files in root and filter them by substring.
    paths_list = list_files(root_path, full_path, recursively)
    paths_list = [i for i in paths_list if input_string in i.name]
    return paths_list


def manage_old_version_file(file_path):
    """Avoid file overwriting, managing 'old' version of it.

    Algorithm looks for and 'old_' version of `file_path` in its same
    directory. If it finds it, returns a copy of it, if not, creates a
    copy of `file_path` as 'old_' version, setting it as the new backup
    file. This allows to have a backup of `file_path` available.

    Parameters
    ----------
    file_path : Path
        Path of file of interest.

    Returns
    -------
    Path
        Path of file that can be safely modified.
    """
    # Set old version file path
    file_path = Path(file_path)
    old_version_file = modify_filename_in_path(file_path,
                                               added='old_',
                                               prefix=True)

    # If old version exists, create a copy without prefix and return
    # that path. If not, create a copy with prefix and set it as the
    # new backup file.
    if old_version_file.exists():
        shutil.copy(str(old_version_file), str(file_path))
        output = file_path
    elif Path(file_path).exists():
        shutil.copy(file_path, old_version_file)
        output = file_path

    # Report if no file was found
    else:
        print(Path(file_path).name, 'FILE NOT FOUND IN', str(file_path.parent))
        output = None
    return output


def modify_filename_in_path(file_path, new_name=None, added=None,
                            prefix=False):
    """Modify file name of a given full path.

    The algorithm considers three types of modifications:
    - Full file name replace.
    - Adding of prefix or suffix to file name.
    - Combination of former two.

    Parameters
    ----------
    file_path : Path
        Full Path of file name to be modified.
    new_name : str, optional
        If given, replace file name with it.
    added : str, optional
        If given, add to file name as prefix or suffix
    prefix : bool, optional
        If True, add `added` as prefix. Otherwise, add it as suffix.

    Returns
    -------
    Path
        Modified full Path.
    """
    # Normalize input to Path object and build new file name.
    file_path = Path(file_path)
    if new_name is None:
        new_name = file_path.stem
    if added is not None:
        if prefix:
            new_name = added + new_name
        else:
            new_name = new_name + added
    output = Path(file_path.parent, new_name).with_suffix(file_path.suffix)
    return output


def renumber_file(file_path, delta):
    """Modify a file name adding a number to the last digit found in it.

    Parameters
    ----------
    file_path : Path
        Path of file to be renamed.
    delta : int
        Number to be add to the last digit found in file name.

    Returns
    -------
    Path
        Full Path of new file name.
    """
    # Normalize input to Path object and extract original number
    file_path = Path(file_path)
    number = st.extract_number_from_str(file_path)

    # Rename file
    output_path = str(file_path).replace(str(number), str(number + delta))
    file_path.rename(output_path)
    return output_path


def save_files_list_2txt(root_path, txt_path=None, full_path=False,
                         recursively=False):
    """Save all files paths in a folder to a txt file.

    Parameters
    ----------
    root_path : Path
        Top level folder, start search here.
    txt_path : Path, optional
        Path of txt file. If not defined, create it in current folder.
    full_path : bool, optional
        If True, gets Full Path of files, instead of just files names.
    recursively : bool, optional
        If True, search folders recursively. Default is False.

    Returns
    -------
    Path
        Path of txt file.
    """
    # Set default output file and normalize input suffix
    if not txt_path:
        txt_path = Path(root_path, 'files_list')
    txt_path = txt_path.with_suffix('.txt')

    # List all files in root and save to output txt
    paths_list = list_files(root_path, full_path, recursively)
    with open(txt_path, 'w+') as file_out:
        file_out.write('\n'.join(paths_list))
    return txt_path


def size_folder(root_path=None, recursively=True):
    """Calculate the size of a given folder in MB.

    Parameters
    ----------
    root_path : Path, optional
        Folder to find the size of. If None given, size current folder.
    recursively : bool, optional
        If True, consider sub-folders recursively. Default is False.

    Returns
    -------
    float
        Size of folder in MB.
    """
    # List all files in root folder and sum their stats
    if root_path is None:
        root_path = Path.cwd()
    paths_list = list_files(root_path, True, recursively)
    return round(sum(f.stat().st_size for f in paths_list) / (1024*1024), 3)
