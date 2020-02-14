import os


def src_dir():
    utils_dir_ = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(utils_dir_)


def project_dir():
    src_dir_ = src_dir()
    return os.path.dirname(src_dir_)


def resource_dir():
    src_dir_ = src_dir()
    return os.path.join(src_dir_, 'resources')
