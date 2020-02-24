"""finds all import in jupyter notebook, check if they are alredy present if not then install it."""

__version__ = '1.0'

import re 
import sys
import json
import warnings
import pkgutil
import subprocess
import argparse
warnings.filterwarnings("ignore")

def run(fileName=None) :
    data = ''
    if fileName == None :
        print('No file name provided so exiting the program.')
    else :
        with open(fileName) as f :
            data = f.read()
        dic = json.loads(data)
        print(dic.keys())
        cells = dic['cells']
        import_set = set()
        for cell in cells :
            if cell['cell_type'] == "code" :
                txt_list = cell['source']
                for txt in txt_list :
                    if txt.startswith('from') :
                        import_set.add(re.search('from \w+',txt).group(0).split()[1])
                    elif txt.startswith('import') :
                        import_set.add(re.search('import \w+',txt).group(0).split()[1])
        print('package list to import '+str(import_set))

        # alternative to below solution is this python library. stdlib-list
        lib_set = set([ key.split('.')[0] for key in sys.modules if not key.startswith('_') ])
        pkg_util_set = set([ i[1] for i in pkgutil.iter_modules(None) ])
        lib_set = lib_set | pkg_util_set
        install_set = import_set-lib_set
        if len(install_set) == 0 :
            print('all packages are available so no package will be installed.')
        else :
            print('package list to install '+str(install_set))

            failed_list = []
            for package in install_set :
                try :
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                except subprocess.CalledProcessError : 
                    failed_list.append(package)

            if len(failed_list) == 0 :
                print('all packages installed successfully.')
            else :
                print('following packages failed to install. Please check and install them manually. '+str(failed_list))

if __name__ == '__jupyter_installer__' :
#def main(*args) :

    
    try :
        fileName=sys.argv[1]
    except IndexError :
        print('no file path found. So using test path. Please add command line argument to chech your file.')
        fileName = 'test.ipynb'
    run(fileName)

    # non working code find the bug later.
    # parser = argparse.ArgumentParser(description='Argument Parser.')
    # parser.add_argument('fileName', help="pass relative or absolute path of ipynb file.", default='test.ipynb', required=False)
    # args = parser.parse_args()
    # run(args.fileName)