import argparse
import re
import sys

from .search import get_search_results
from .download import get_tube, get_streams
from .progress import set_progress_bar


def main():
    argparser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Simple YouTube Downloader'
    )
    argparser.add_argument(
        'keywords',
        help='Url 또는 검색어',
        nargs='*'
    )
    args = argparser.parse_args()

    results = get_search_results(args.keywords)
    print('=' * 120)
    for i, row in enumerate(results, 1):
        line = "{}. {}".format(i, row['title'])
        print(line)

    print('=' * 120)
    nlist = input('Input Your choices as seperate with comma: ')
    if not nlist:
        return

    nlist = nlist.split(',')
    nlist = list(map(int, nlist))

    for i, row in enumerate(results, 1):
        if i in nlist:
            tube = get_tube(row['link'])

            description = "Downloading {} from {}".format(
                tube.title, row['link'])
            print(description)

            streams = get_streams(tube, mime_type='audio/mp4')
            for stream in streams:
                set_progress_bar(stream)
                stream.download()


if __name__ == "__main__":
    main()
