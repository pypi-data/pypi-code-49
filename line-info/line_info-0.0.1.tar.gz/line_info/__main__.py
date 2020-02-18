import sys

from .line_info import get_line_info


def main():
    return get_line_info(*sys.argv[1:])


if __name__ == '__main__':
    main()
