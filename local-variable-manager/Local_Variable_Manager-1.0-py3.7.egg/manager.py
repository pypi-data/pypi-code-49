# Build-In Modules
import os
import shutil
from shutil import copyfile
from distutils.dir_util import copy_tree
from pathlib import Path
import base64

# 3rd Party Modules
from cryptography.fernet import Fernet
import pyperclip

# Global Variables
ROOT = os.getenv("HOME")
TEMP_FOLDER = ROOT + "/.lvm/"
TEMP_EXPOSED_FOLDER = ROOT + "/.exposed/"


def generateKey():
    """
    Method to generate a encryption key
    """
    try:
        key = Fernet.generate_key()
        updateClipboard(f"export LVMANAGER_PW={str(key)[2:-1]}")
        print(f"Key: {key}")
        print("Export command copied to clipboard. Save this value!")
        return True
    except Exception as e:
        print(f"Something went wrong\nException: {e}")
        return False

def add(file_path, name, encrypt):
    """
    Method to add file LVM

    :param boolean encrypt: Flag to indicate if we should encrypt
    :param String file_path: Path to file
    :param String name: Name of project or file thats been passed in
    :return: Flag to indicate if we are successful
    :rtype boolean:
    """
    absPathToFile = str(Path(file_path).absolute())

    # Check if our file exists
    if not os.path.isfile(file_path):
        print(f"[Error] File {file_path} does not exists!")
        return False

    # Check if we have the file extension
    if "." not in file_path:
        print(f"[Warning] No extension in file_path!")

    try:
        with open(absPathToFile, "rb") as open_file:
            file_data = open_file.read()
        # Encrypt our file
        if encrypt:
            if os.getenv('LVMANAGER_PW') and encrypt:
                key = os.getenv('LVMANAGER_PW')
            else:
                key = ""
            encryption_client = Fernet(bytes(key, "utf-8"))

            encrypted_data = encryption_client.encrypt(file_data)
        else:
            encrypted_data = file_data
        # Write our file to our .lvm/ directory
        paths = name.split('/')
        verify_paths(paths)
        with open(TEMP_FOLDER + '/' + name + Path(file_path).suffix, "wb") as file:
            file.write(encrypted_data)
        return True
    except Exception as e:
        print(f"[Error] Exception: {e}")
        return False

def verify_paths(paths, exposed=False):
    """
    Helper to verify paths

    :param list paths: Sub-folder we should be looking at
    :param boolean exposed: If True verify through .exposed
    """
    if not exposed:
        index = TEMP_FOLDER
    else:
        index = TEMP_EXPOSED_FOLDER
    if len(paths) > 1:
        for path in paths[:-1]:
            index = os.path.join(index, f"{path}")
            if not os.path.isdir(index):
                # Create directories if they don't exists
                os.mkdir(index)

def delete(name):
    """
    Delete a stored project/value

    :param String name: Name of project/file to be deleted
    :return: Flag to indicate if we are successful
    :rtype boolean:
    """
    absPathToVal = str(Path(f"{TEMP_FOLDER}/{name}").absolute())

    # Check if it is a dir/project
    if os.path.isdir(absPathToVal):
        if confirm(name):
            if confirm(name, really=True):
                # Delete the folder
                shutil.rmtree(absPathToVal)
                return True
        else:
            return False
    # Loop to get the file extension and then delete the value
    file_extension = getFileExtension(name)
    if confirm(f"{name} [Type: {file_extension}]"):
        # We found the file, add its extension
        os.remove(absPathToVal + file_extension)
        return True
    else:
        return False

    # Always return false just in case we failed along the way
    return False

def getFileExtension(name):
    """
    Helper function to getFileExtension

    :param String name: Name of the value we're deleting
    :return: File Extension
    :rtype String:
    """
    parent_folder = str(Path(f"{TEMP_FOLDER}/{name}").parent.absolute())
    name_split = name.split('/')
    for file in os.listdir(parent_folder):
        split_file = file.split(".")
        if split_file[0] in name_split:
                return Path(file).suffix

def confirm(name, really=False):
    """
    Helper function to deal with user confirming

    :param String name: Value we are deleting
    :param boolean really: Are you sure you want to delete this?
    :return: Flag to indicate if they confirmed
    :rtype: boolean
    """
    if not really:
        confirm = input(f"Are you sure you want to delete: {name}?\n"
                        f"Press y to confirm [must be lowercase]:")
    else:
        confirm = input(f"Are you REALLY SURE you want to delete: {name}?\n"
                        f"Press y to confirm [must be lowercase]:")
    if confirm == "y":
        return True
    else:
        return False

def setenv(project_name, name_of_env, encrypt, return_string=False):
    """
    Delete a stored project

    :param String project_name: Name of project/file to be used
    :param String name_of_env: Name of global variable to be used
    :param boolean encrypt: Flag to indicate if we should unencrypt
    :param boolean return_string: Return string instead of boolean
    :return: Flag to indicate if we are successful/clipboard string
    :rtype boolean/String:
    """
    absPathToVal = os.path.join(TEMP_FOLDER, project_name)
    newAbsPathToVal = os.path.join(TEMP_EXPOSED_FOLDER, project_name)

    if os.path.isdir(absPathToVal) and name_of_env == "":
        # Copy our folder to .exposed
        copy_tree(absPathToVal, newAbsPathToVal)
        # If its a dir connect the export's with a ;
        clipboard_string = ""
        for file in os.listdir(newAbsPathToVal):
            file_no_extension = os.path.splitext(file)[0]
            clipboard_string += setenv(project_name+file_no_extension, file_no_extension.upper(), encrypt, return_string=True) + ";"
        return updateClipboard(clipboard_string)

    elif name_of_env != "":
        file_extension = getFileExtension(project_name)
        with open(absPathToVal + file_extension, "rb") as file:
            # read the encrypted data
            encrypted_data = file.read()
        if encrypt:
            # Get our key
            if os.getenv('LVMANAGER_PW') and encrypt:
                key = os.getenv('LVMANAGER_PW')
            else:
                key = ""
            encryption_client = Fernet(bytes(key, "utf-8"))
            # Decrypt the data
            decrypted_data = encryption_client.decrypt(encrypted_data)
        else:
            decrypted_data = encrypted_data
        # If the file is .lvmanager, export the content of the file
        if file_extension == ".lvmanager":
            clipboard_string = f"export {name_of_env}=" + str(decrypted_data)[2:-1].replace('\\n', '')
        else:
            # Copy our file to .exposed
            verify_paths(project_name.split('/'), exposed=True)
            with open(newAbsPathToVal+file_extension, "wb") as file:
                file.write(decrypted_data)
            # Build our string to paste into clipboard
            new_path = os.path.join(TEMP_EXPOSED_FOLDER, f"{project_name}{file_extension}")
            clipboard_string = f"export {name_of_env}={new_path}"
        if return_string:
            return clipboard_string
        return updateClipboard(clipboard_string)

    print(f"[Error] No name for env provided for: {project_name}")
    return False

def updateClipboard(clipboard_string):
    """
    Update clipboard with string.
    Taken from: https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard-on-windows-using-python

    :param String clipboard_string: String we should copy to clipboard
    :return: Flag if we were successful
    """
    try:
        pyperclip.copy(clipboard_string)
        return True
    except:
        print(f"Could not update clipboard.\n{clipboard_string}\n")
        return False
def ls():
    """
    List out projects/values we have stored

    :return: Flag to indicate if we are successful
    :rtype boolean:
    """
    list_files(TEMP_FOLDER)
    return True

def list_files(startpath):
    """
    Helper function to list files
    Taken from: https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python

    :param String startpath: Start of root we should display
    """
    skip_first = False
    for root, dirs, files in os.walk(startpath):
        if not skip_first:
            skip_first = True
            continue
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
            # TODO: If we are at the end, show the file name my.key [main/project/my]

def cleanup():
    """
    Delete .exposed/ dir

    :return: Flag to indicate if we are successful
    :rtype boolean:
    """
    shutil.rmtree(os.path.join(TEMP_EXPOSED_FOLDER))
    return True