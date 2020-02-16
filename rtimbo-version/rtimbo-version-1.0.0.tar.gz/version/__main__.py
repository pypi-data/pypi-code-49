import argparse
from .helpers import compare

def main():
    """Runs program as an executable.
    Reads two versions from the command line arguments
    and returns whether the first version is
    greater(1), equal(0), or less than(-1)
    the second version passed.
    """    
    parser = argparse.ArgumentParser(
        prog="Version Comparator",
        description="Given two versions v1 and v2, checks if v1 is greater than (1), equal(0), or less than(-1) v2")

    parser.add_argument('v', nargs='*', help="Versions to be compared.")

    args = parser.parse_args()

    if len(args.v) == 0:
        v1 = input()
        v2 = input()
        
        ans = compare(v1, v2)
        print(ans)
    else:
        if len(args.v) != 2:
            print("Please pass 2 version numbers.")
            return
        v1 = args.v[0]
        v2 = args.v[1]
        
        ans = compare(v1, v2)
        print(ans)

if __name__ == "__main__":
    main()