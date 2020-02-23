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


def format_str(source, line_length, target_version, skip_string_normalization):
    lines = []
    for line in source.split("\n"):
        lines.append(line.rstrip("\n"))

    min_indent = line_length
    for line in lines:
        if line:  # blank lines can be dedented indefinitely
            min_indent = min(min_indent, nr_of_space_prefix(line))

    hunk = dedent_lines(lines, min_indent)

    mode = black.FileMode(
        line_length=line_length - min_indent,
        is_pyi=True,
        string_normalization=not skip_string_normalization,
        target_versions={black.TargetVersion[target_version.upper()]},
    )
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
    argparser.add_argument(
        "-t",
        "--target-version",
        type=str,
        choices=["py27", "py33", "py34", "py35", "py36", "py37", "py38"],
        default="py36",
        help="Python versions that should be supported by Black's output.",
    )
    argparser.add_argument(
        "-S",
        "--skip-string-normalization",
        action="store_true",
        default=False,
        help="Don't normalize string quotes or prefixes.",
    )
    return argparser.parse_args()


def main():
    args = parse_args()
    source = args.SOURCE
    if not source:
        import sys

        with sys.stdin:
            source = sys.stdin.read()

    format_str(
        source,
        args.line_length,
        args.target_version,
        args.skip_string_normalization,
    )


if __name__ == "__main__":
    main()
