import argparse


def print1():

    parser = argparse.ArgumentParser(description='This is describtion.')
    parser.add_argument('num', default=1, type=int, help="number")
    args = parser.parse_args()
    num = args.num
    print(num)
