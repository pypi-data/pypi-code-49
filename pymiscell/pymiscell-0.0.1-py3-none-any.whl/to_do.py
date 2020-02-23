"""Functions to configure R packages within a Python 3 environment.

Developed by Rodrigo Rivero.
https://github.com/rodrigo1392

"""

from rpy2.robjects.packages import importr

utils = importr('utils')
utils.install_packages('rsm')

def check_corrupted_videos(root_path, extensions):
    """Check video files to detect corrupted ones.

    Filter files by given `extensions`, searching recursively in the
    `root_path`.

    Parameters
    ----------
    root_path : Path
        Starting path, to be searched recursively.
    extensions : list of str
        Video file extensions to look for.

    Returns
    -------
    int
        Amount of good files found.
    int
        Amount of corrupted files found.
    """
    # Report software versions.
    print("Python version:", sys.version)
    print("CV2:   ", cv2.__version__)

    # Gather video files paths and prepare list for progress bar.
    files_paths = []
    for extension in extensions:
        files_paths.extend(list_files_with_extension(root_path, extension))

    # Iterate on video files path, trying to open them, catching errors
    # and counting good files.
    files_paths = tqdm.tqdm(files_paths)
    good_files_counter = 0
    for filename in files_paths:
        try:
            vid = cv2.VideoCapture(filename)
            if not vid.isOpened():
                print('FILE NOT FOUND:' + filename)
                raise NameError('File not found')
        except cv2.error:
            print('error:' + filename)
            print("cv2.error:")
        else:
            good_files_counter += 1
    bad_files = len(files_paths) - good_files_counter

    print("Good files:", good_files_counter)
    print("Bad files:", bad_files)
    return good_files_counter, bad_files# -*- coding: utf-8 -*-

