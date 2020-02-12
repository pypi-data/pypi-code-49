from camembert import Bri


def create_index(args):
    b = Bri(args.bam_file)
    b.create()


def get_read(args):
    b = Bri(args.bam_file)
    b.load()
    for read in b.get(args.read_name):
        print(read.to_string())


def main():
    import argparse
    parser = argparse.ArgumentParser('Wrapper of bri (BAM Read Index) created by Jared Simpson. '
                                     'https://github.com/jts/bri')

    command_parsers = parser.add_subparsers(title='Available subcommands',
                                            dest='command',
                                            description='For detailed subcommand help run: <subcommand> -h.')

    index_parser = command_parsers.add_parser('index', help='Create read index for Bam file')
    index_parser.add_argument('bam_file')
    index_parser.set_defaults(func=create_index)

    get_parser = command_parsers.add_parser('get', help='Fetch a read from Bam file')
    get_parser.add_argument('bam_file')
    get_parser.add_argument('read_name')
    get_parser.set_defaults(func=get_read)

    args = parser.parse_args()

    try:
        args.func(args)
    except AttributeError:
        parser.print_help()
        parser.exit()


if __name__ == '__main__':
    main()
