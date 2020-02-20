from subprocess import run
from pathlib import Path

def install():
    run(['/bin/bash', Path(__file__).parent / 'ffmpeg.sh'])