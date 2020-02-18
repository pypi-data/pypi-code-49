
import sys
from efdir import mktree as emk

# too complicated...
#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument('-cfg','--config', default="",help="dirs config files,.rst or .json")
#parser.add_argument('-dst','--destnation', default="",help="make-tree-dirs to ")
#args = parser.parse_args()

#emk.fmktree(args.config,args.destnation)

def main():
    if(sys.argv.__len__()==3):
        emk.fmktree(sys.argv[1],sys.argv[2])
    else:
        emk.fmktree(sys.argv[1],"./wkdir")
