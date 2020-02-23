from os import walk, remove
from os.path import join
from shutil import rmtree
from threading import Thread


def cleaner(directory, *file, level=None):
    """
    **DANGER!** A function for cleaning objects and folders on the system.

    Arguments:
        **directory {str}** -- Directory where are the files to be destroyed

        ***file** -- Enter an N file name number (Optional)

    Keyword Arguments:
        **level {int}** -- This option receives 3 values, they are: \

                           Value 0 = If this value is set, the function revokes the \
                           unitary file exclusion option, that is, this option will \
                           exclude all files at the root of the informed directory.

                           Value 1 = If this value is set, the function revokes the unitary \
                           file exclusion option as well, however, it will exclude all \
                           subdirectories of the root directory, except the files contained \
                           in the root.

                           Value None = If this value is set, the function must receive at least \
                           one file name to be deleted. Can pass as many files as you want.

                           (default: {None})

    """

    data = next(walk(directory))

    #: DANGER!
    if level == 0:
        for f in data[2]:
            remove(join(data[0], f))
        return 0

    #: DANGER!
    if level == 1:
        # r: root, r: directory, f: files
        for r, d, f in walk(directory, topdown=False):
            for item in d:
                t = Thread(target=rmtree(join(r, item)), args=())
                t.start()
        return 1

    try:
        if file:
            for f in file:
                remove(join(data[0], f))
            return
    except FileNotFoundError as err:
        msg = '>>> There was an error removing the files'
        raise FileNotFoundError(msg, err)


__all__ = ['cleaner']
