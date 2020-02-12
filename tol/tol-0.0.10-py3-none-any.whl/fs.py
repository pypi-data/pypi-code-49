def mkdir(path, mode=None):
    return 'mkdir --parents {mode} {path}'.format(
        path=path,
        mode='--mode %s' % mode if mode else '')


def chown(user, path):
    return 'chown --recursive %s:%s %s' % (user, user, path)


def exists(path):
    return "test -e %s" % path


def by_timestamp(path, depth=1, type='f', name='*', long=False):
    """
    List files sorted by timestamp
    """
    return 'find {path} {mindepth} {maxdepth} {name} {type} | xargs {ls_cmd}'.format(
        path=path,
        mindepth='-mindepth %d' % depth,
        maxdepth='-maxdepth %d' % depth,
        name='-name "%s"' % name,
        type='-type %s' % type,
        ls_cmd='ls --directory -1t%s' % ('l' if long else ''))
