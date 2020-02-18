import os
import sys
from efdir import csv

# too complicated...
#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument('-cfg','--config', default="",help="dirs config files,.rst or .json")
#parser.add_argument('-dst','--destnation', default="",help="make-tree-dirs to ")
#args = parser.parse_args()

#emk.fmktree(args.config,args.destnation)


def main():
    src = sys.argv[1]
    print(csv.csv_wcols(src,from_file=True))
