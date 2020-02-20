from subprocess import run
from pathlib import Path


def install():
    run(['/bin/bash', Path.cwd() / 'installers' / 'ffmpeg' / 'ffmpeg.sh'])