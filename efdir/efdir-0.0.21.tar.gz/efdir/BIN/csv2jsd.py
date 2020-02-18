import os
import sys
from efdir import csv
import efuntool.efuntool as efun

# too complicated...
#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument('-cfg','--config', default="",help="dirs config files,.rst or .json")
#parser.add_argument('-dst','--destnation', default="",help="make-tree-dirs to ")
#args = parser.parse_args()

#emk.fmktree(args.config,args.destnation)


def main():
    src = sys.argv[1]
    cn0 = efun.dflt_sysargv("Name",2)
    cn1 = efun.dflt_sysargv("Template",3)
    print(csv.csv_wjsd(src,cn0,cn1))

