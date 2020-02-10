import os, sys
import subprocess
import shutil
import traceback

from aos.util import log, error, is_domestic

## Download externals
def check_download_require(require, config_file):
    """ Check download require """
    if not os.path.isfile(config_file):
        return False

    with open(config_file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if require == line:
                return True

    return False

def download_externals(externals, source_root, config_file):
    """ Download external repos """
    tmpdir = 'tmp_{0:02x}'.format(ord(os.urandom(1)))
    while os.path.isdir(tmpdir):
        tmpdir = 'tmp_{0:02x}'.format(ord(os.urandom(1)))

    try:
        os.mkdir(tmpdir)
    except:
        error("Can not create temp folder %s" % tmpdir)

    try:
        os.chdir(tmpdir)
        for key in externals:
            result = 0
            t = externals[key]
            name = t["name"]
            gittag = t["gittag"]
            destdir = t["destdir"]
            postscript = t["postscript"]
            require = t["require"]

            destdir = os.path.join(source_root, destdir)
            if os.path.exists(destdir):
                return

            # Don't download if require is not meet
            if require != "":
                if not check_download_require(require, config_file):
                    continue

            # domestic check takes a little bit long time,
            # so only do the check when really necessary
            giturl = t["giturl"]["github"]
            if is_domestic():
                if "gitee" in t["giturl"] and t["giturl"]["gitee"] != "":
                    giturl = t["giturl"]["gitee"]

            print('Downloading %s: %s -> %s ...' % (name, giturl, destdir))
            cmd = "git clone %s %s" % (giturl, name)
            if gittag != "":
                cmd = "git clone -b %s %s %s" % (gittag, giturl, name)

            result += subprocess.call(cmd, shell=True)
            if result > 0:
                print('git clone %s failed' % name)
                print('You can mannually try fix this problem by running:')
                print('    %s' % cmd)
                print('    mv %s %s && rm -rf %s' % (name, destdir, name))

            srcdir = name
            if os.path.exists(srcdir) == False:
                print('The folder %s is not exist' % (srcdir))
                result += 1

            if result == 0:
                if os.path.isfile(destdir):
                    os.remove(destdir)
                if os.path.isdir(destdir):
                    shutil.rmtree(destdir)
                if not os.path.isdir(os.path.dirname(destdir)):
                    os.makedirs(os.path.dirname(destdir))

                shutil.move(srcdir, destdir)
                print('Download %s succeed' % name)
            else:
                print('Download %s failed' % name)

            # Run post scripts
            ret = 0
            if postscript != "":
                cmd = "python %s/%s" % (source_root, postscript)
                ret += subprocess.call(cmd, shell=True)

            if ret > 0:
                print("Run post script failed: %s" % cmd)
    except:
        traceback.print_exc()
    finally:
        os.chdir('../')
        try:
            shutil.rmtree(tmpdir)
        except:
            print("Can not remove temp folder %s, please remove it manually" % tmpdir)

def install_externals(source_root, app_root=None):
    """ Download externals according to build/external_config.py """
    auto_dl = False
    externals = {}
    external_config = os.path.join(source_root, "build/external_config.py")
    if os.path.isfile(external_config):
        sys.path.append(os.path.dirname(external_config))
        try:
            import external_config as ec
        except:
            error("Import external configs failed")

        if ec.auto_download == "yes":
            auto_dl = True

        externals = ec.externals

    if not auto_dl:
        return

    build_config = os.path.join(source_root, ".config")
    if app_root:
        build_config = os.path.join(app_root, ".config")

    download_externals(externals, source_root, build_config)
