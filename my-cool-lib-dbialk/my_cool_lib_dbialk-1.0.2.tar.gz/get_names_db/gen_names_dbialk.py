import names
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--gender", help="set male or female")
args = parser.parse_args()

name = names.get_full_name(gender=args.gender)

print(name, len(name)-1)