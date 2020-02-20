import os
import shutil


def copy_files(listOfFiles, destination):
    filesCount = 0
    if not os.path.isdir(destination):
        os.makedirs(destination)
    for file in listOfFiles:
        if os.path.isfile(file):
            shutil.copy(file, destination)
            filesCount += 1
    return filesCount
