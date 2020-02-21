def main():
    try:
        from lib5c import __version__ as version
    except ImportError:
        try:
            from setuptools_scm import get_version
            version = get_version(root='..', relative_to=__file__)
        except ImportError:
            raise ValueError('please install either lib5c or setuptools_scm')
    print(version)


if __name__ == '__main__':
    main()
