import sys
import os
import argparse
import shutil
import re
import compileall
import zipfile

def compile():
    paths = sys.path # remove current directory
    paths.pop(0)
    for path in paths:
        if path:
            compileall.compile_dir(path, force=True, quiet=True)

def zip_dir(dir_path, zip_path):
    zipf = zipfile.ZipFile(zip_path, mode='w')
    len_dir_path = len(dir_path)
    for root, _, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, file_path[len_dir_path:])
    zipf.close()

def zip_dir_pyc(dir_path, zip_path):
    zipf = zipfile.ZipFile(zip_path, mode='w')
    len_dir_path = len(dir_path)
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.py'):
                continue
            else:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path:])
    zipf.close()

def convert():
    python_installation = os.path.dirname(sys.executable)
    
    if python_installation.lower().endswith('scripts'):
        script_dir = python_installation
    else:
        script_dir = os.path.join(python_installation, 'Scripts')
        
    for root, dirs, files in os.walk(script_dir):
        for filename in files:
            if filename.endswith('.exe'):
                filepath = os.path.join(root, files)
                replace_str = r'#!"{}"'.format(sys.executable)
                search_str = r'#!".*python\.exe"'.format(sys.executable)
                re.compile(search_str)
                file_h = open(filepath, "rb")
                content = file_h.read()
                file_h.close()
                content = re.sub(bytes(search_str, 'utf-8'), bytes(re.escape(replace_str), 'utf-8'), content)
                file_h = open(filepath, "wb")
                file_h.write(content)
                file_h.close()

def pack(dest, pyc_only):
    """dest (str): path for the zip. excluding the name
    """
    try:
        os.mkdir(dest)
    except FileExistsError:
        pass

    if pyc_only:
        compile()
    python_installation = os.path.dirname(sys.executable)
    filepath = os.path.join(dest, 'dist.zip')
    if not pyc_only:
        zip_dir(python_installation, filepath)
    else:
        zip_dir_pyc(python_installation, filepath)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='help to deploy your application in a standalone python environment')
    parser.add_argument('--dest', dest='dest', default=os.getcwd(), help='destination path of the zip path (not the filepath)')
    parser.add_argument('--pack', action='store_true', help='use this flag to pack into zip file')
    parser.add_argument('--convert', action='store_true', help='use this flag to convert scripts to use current python deployment')
    # parser.add_argument('--pyc-only', action='store_true', help='use this flag to only pack pyc files')
    args = parser.parse_args()
    if args.pack:
        pack(args.dest, False)
    elif args.convert:
        convert()
    else:
        print("please specify use mode (--pack or --convert).")
