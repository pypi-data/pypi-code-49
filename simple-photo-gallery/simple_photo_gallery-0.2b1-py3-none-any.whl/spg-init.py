import argparse
import logging
import simplegallery.gallery as gallery


logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(levelname)-6s %(message)s')


def parse_args():
    parser = argparse.ArgumentParser(description='Initializes a new gallery')

    parser.add_argument('--force',
                        dest='force',
                        action='store_true',
                        help='Overrides existing config files')

    return parser.parse_args()


def main():
    args = parse_args()

    print('Hello!')

    #gallery.create_gallery('.', 'gallery.json', args.force)


if __name__ == "__main__":
    main()
