import argparse

from yanf.yanflib.formatter import NotebookFormatter


def main():
    parser = argparse.ArgumentParser(description='Formatter for Python Jupyter Notebooks.')
    parser.add_argument('file')
    args = parser.parse_args()

    formatter = NotebookFormatter(args.file, 'pep8')
    formatter.format().write()
    exit(0)


if __name__ == '__main__':
    main()
