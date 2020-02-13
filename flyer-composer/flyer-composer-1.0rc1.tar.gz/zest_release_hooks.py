import subprocess
import sys
import os
import glob

def compile_message_catalogs(data):
    print("Compiling catalogs")
    subprocess.run([sys.executable, "setup.py", "compile_catalog", "--statistics"])
    print("Done")


def sign_release(data):
    "Sign the archive that will be uploaded to PYPI."
    # zest.releaser does a clean checkout where it generates tgz/zip in 'dist'
    # directory and those files will be then uploaded to pypi.
    dist_dir = os.path.join(data['tagdir'], 'dist')
    cmd = ['gpg', '--detach-sign', '--armor']
    codesigning_id = os.getenv("CODESIGNING_ID")
    if codesigning_id:
        print("Using gpg identity", codesigning_id, "for signing.")
        cmd.extend(['--local-user', codesigning_id])
    # Sign all files in the 'dist' directory.
    for f in list(os.listdir(dist_dir)):
        f = os.path.join(dist_dir, f)
        print('Signing file %s' % f)
        subprocess.run(cmd + [f])


def run_twine_check(data):
    import twine.cli
    dist_dir = os.path.join(data['tagdir'], 'dist')
    dist_files = list(glob.glob(os.path.join(dist_dir, "*")))
    twine.cli.dispatch(["check"] + dist_files)
