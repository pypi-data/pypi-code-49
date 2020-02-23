#!/usr/bin/python3

import argparse
import re
from datetime import datetime
from signal import signal, SIGPIPE, SIG_DFL
from operator import itemgetter

signal(SIGPIPE, SIG_DFL)


def get_datetime(asctime):
    return datetime.strptime(asctime, "%Y-%m-%d %H:%M:%S,%f")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--pattern", help="datetime pattern", default=r"^[\d :-]{19},\d+"
    )
    parser.add_argument("log", nargs="+", type=argparse.FileType(), help="log files")
    return parser.parse_args()


def rows(f, datetime_pattern):
    non_match = 0
    last_row = ()
    for line_no, raw_line in enumerate(f, 1):
        line = raw_line.rstrip()
        match = datetime_pattern.search(line)
        if match:
            if last_row:
                yield last_row
            last_row = [match.group(1), line]
        else:
            non_match += 1
            if last_row != ():
                # only do it if last row had something
                last_row[1] = last_row[1] + "\n" + line
    else:
        if last_row:
            yield last_row


def print_formatted(start, end):
    duration = end["time"] - start["time"]
    print(
        "%s\t%0.03f"
        % (end["time"].strftime("%Y-%m-%d %H:%M:%S.%f"), duration.total_seconds())
    )


def indexed_rows(files, pattern):
    for f in files:
        for indexed_row in rows(f, pattern):
            yield indexed_row


def sorted_lines(files, pattern):
    for _, line in sorted(indexed_rows(files, pattern), key=itemgetter(0)):
        yield line


def main():
    args = parse_args()
    datetime_pattern = re.compile("(%s)" % args.pattern)
    for line in sorted_lines(args.log, datetime_pattern):
        print(line)
