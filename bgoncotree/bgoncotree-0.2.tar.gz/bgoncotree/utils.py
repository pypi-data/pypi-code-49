import gzip


def open_read(file):
    if file.endswith('.gz'):
        return gzip.open(file)
    else:
        return open(file)
