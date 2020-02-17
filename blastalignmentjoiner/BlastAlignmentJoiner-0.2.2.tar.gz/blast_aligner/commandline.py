"""

"""

from blast_aligner.BlastResults import BlastResults
import os
import glob
import json

def process_dir(args):
    if os.path.isdir(args.dir):
        files = glob.glob(args.dir + os.path.sep + "*." + args.pattern)
        results = [BlastResults(b) for b in files]
        output = {}
        for res in results:
            output[res.sample] = res.results

        with open(args.output, 'w') as f:
            json.dump(output, f)
    else:
        raise NotADirectoryError


def process_file(args):
    try:
        blast = BlastResults(args.file)
        results = blast.results
        output = {blast.sample: results}
        with open(args.output, 'w') as f:
            json.dump(output, f)
    except Exception as e:
        print(e)

import argparse
#from blast_aligner.commandline import process_file, process_dir

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="The name of the output file", default="output.json")
parser.add_argument("-p", "--pattern", help="The pattern of suffixes to look for", default="blast")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", "--file", help="The file you want to process")
group.add_argument("-d", "--dir", help="The directory that contains the files you want to process")

args = parser.parse_args()

print(args)

def main():
    if args.dir:
        process_dir(args)
    elif args.file:
        process_file(args)
    else:
        parser.print_usage()
        parser.print_help()