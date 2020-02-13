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