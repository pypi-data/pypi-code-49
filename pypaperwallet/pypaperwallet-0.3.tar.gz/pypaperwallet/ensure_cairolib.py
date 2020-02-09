# [rights]  Copyright 2020 brianddk at github https://github.com/brianddk
# [license] Apache 2.0 License https://www.apache.org/licenses/LICENSE-2.0
# [repo]    https://github.com/brianddk/pypaperwallet
# [btc]     BTC-b32: bc1qwc2203uym96u0nmq04pcgqfs9ldqz9l3mz8fpj
# [tipjar]  https://gist.github.com/brianddk/3ec16fbf1d008ea290b0

from winreg import OpenKey, EnumKey, QueryValueEx, QueryInfoKey
from winreg import HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE
from os.path import exists, isdir, join
from os import listdir
from os import environ

cairo = 'libcairo-2.dll'

def find_msys2_cairo(cairo):
    swpath = r"Software\Microsoft\Windows\CurrentVersion\Uninstall"
    for root in [HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE]:
        with OpenKey(root, swpath) as swkey:
            keys, _, _ = QueryInfoKey(swkey)
            for i in range(0, keys):
                subpath = EnumKey(swkey, i)
                with OpenKey(root, swpath +"\\"+ subpath) as subkey:
                    try:
                        name, _ = QueryValueEx(subkey, 'DisplayName')
                        loc, _ = QueryValueEx(subkey, 'InstallLocation')
                        if name.startswith('MSYS2'):
                            dirs = [d for d in listdir(loc) if isdir(join(loc, d))]
                            for d in dirs:
                                libdir = join(loc, d, 'bin')
                                if exists(join(libdir, cairo)):
                                    return libdir
                    except:
                        pass
    return False

def in_path(cairo):
    for d in environ["PATH"].split(';'):
        if exists(join(d, cairo)):
            return True
    return False
    
if not in_path(cairo):
    libdir = find_msys2_cairo(cairo)
    if(libdir):
        environ["PATH"] += f";{libdir}"
        # print(f"added {libdir}")
    # else:
        # print("ERROR: cairolib not found")
# else:
    # print("cairo is in path")

# print("imported ensure")
