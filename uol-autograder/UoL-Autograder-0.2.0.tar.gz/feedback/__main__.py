import argparse
from . import run_test
from .util import save_feedback_file


parser = argparse.ArgumentParser(description="General puprose test evaluator")
parser.add_argument('tested_file', type=str, help="file to be tested")
parser.add_argument('config_file', type=str, help="config for the test")
parser.add_argument('--result_file', '-f', type=str, default="result.json", help="output file name")
parser.add_argument('--clear_cache', '-x', action="store_true", help="Remove all cached contents")
parser.add_argument('--verbose', '-v', action="store_true", help="Enable extra console logging")

# Primary entry point, with argument processing
def main():
    args = parser.parse_args()
    result = run_test(args.tested_file, args.config_file, {"clear_cache": args.clear_cache, "verbose": args.verbose})
    save_feedback_file(result, args.result_file, args.verbose)


if __name__ == "__main__":      # Run main if ran directly
    main()