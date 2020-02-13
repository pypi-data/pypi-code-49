from os.path import isfile as os_path_isfile
from time import sleep


def wait_downloading(directory_saved_as, max_seconds_wait=60):

    wait = True
    downloaded = False
    seconds_wait = 0
    while wait:
        if os_path_isfile(directory_saved_as):
            wait = False
            downloaded = True

        wait = wait and (seconds_wait < max_seconds_wait)
        sleep(1)
        seconds_wait += 1
            
    return downloaded
