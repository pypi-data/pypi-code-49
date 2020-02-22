import argparse

import black


def nr_of_space_prefix(line):
    i = 0
    for c in line:
        if not c.isspace():
            break
        i += 1

    return i


def dedent_lines(lines, amount):
    new_lines = []
    for line in lines:
        if line and amount > len(line):  # blank line can always be dedented
            raise ValueError(
                'Cannot dedent line "%s" with %d chars' % (line, amount)
            )
        new_lines.append(line[amount:])
    return new_lines


def indent_lines(lines, amount):
    new_lines = []
    for line in lines:
        if line:
            new_lines.append(" " * amount + line)
        else:  # do not indent empty lines as that would become trailing space
            new_lines.append(line)

    return new_lines


def format_str(source, line_length):
    lines = []
    for line in source.split("\n"):
        lines.append(line.rstrip("\n"))

    min_indent = line_length
    for line in lines:
        if line:  # blank lines can be dedented indefinitely
            min_indent = min(min_indent, nr_of_space_prefix(line))

    hunk = dedent_lines(lines, min_indent)

    mode = black.FileMode(line_length=line_length - min_indent, is_pyi=True)
    formatted_hunk = black.format_str(src_contents="\n".join(hunk), mode=mode)

    formatted_lines = formatted_hunk.split("\n")
    formatted_lines = indent_lines(formatted_lines, min_indent)
    print("\n".join(formatted_lines))


def parse_args():
    argparser = argparse.ArgumentParser(
        usage="Apply the black code formatter for a piece of python source "
        "code"
    )
    argparser.add_argument(
        "SOURCE",
        help="The python source code to be formatted. "
        "If not provided then source is read from stdin.",
        nargs="?",
        default=None,
        type=str,
    )
    argparser.add_argument(
        "-l",
        "--line-length",
        type=int,
        default=88,
        help="How many characters per line to allow. [default: 88]",
    )
    return argparser.parse_args()


def main():
    args = parse_args()
    if not args.SOURCE:
        import sys

        with sys.stdin:
            source = sys.stdin.read()
        format_str(source, args.line_length)
    else:
        format_str(args.SOURCE, args.line_length)


if __name__ == "__main__":
    main()
