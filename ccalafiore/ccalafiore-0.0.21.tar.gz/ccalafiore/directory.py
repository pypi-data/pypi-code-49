from os.path import dirname as os_path_dirname


def n_directories_up(directory, n=1):
    
    while n > 0:
        directory = os_path_dirname(directory)
        n -= 1

    return directory
