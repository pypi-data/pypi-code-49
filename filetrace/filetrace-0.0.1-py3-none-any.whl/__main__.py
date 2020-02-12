from .tracer import FileRunTracer
from .cli import parse_cmd_line


def main():
    options, args = parse_cmd_line()
    FileRunTracer(args, {}).run()


if __name__ == "__main__":
    main()
