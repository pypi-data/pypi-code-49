from filetrace.tracer import FileRunTracer
from .cli import parse_cmd_line
from .rootfs import create_tar, extract_tar, create_config_json


class FILETRACER_OPTIONS:
    output = "/dev/null"
    live = False
    exclude = None


def main():
    options, args = parse_cmd_line()
    output_dir = args[0]
    command_args = args[1:]
    file_list = FileRunTracer(FILETRACER_OPTIONS, command_args).run()
    tar_file_name = create_tar(file_list)
    bundle_dir = extract_tar(tar_file_name, output_dir, options.force)
    create_config_json(bundle_dir, command_args)
    print(bundle_dir)


if __name__ == "__main__":
    main()
