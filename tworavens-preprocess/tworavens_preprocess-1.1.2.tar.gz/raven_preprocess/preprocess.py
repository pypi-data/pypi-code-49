"""Main module to call all sub modules"""
from os.path import abspath, dirname, join
import logging
import sys

CURRENT_DIR = dirname(abspath(__file__))
sys.path.append(dirname(CURRENT_DIR))

from raven_preprocess.preprocess_runner import PreprocessRunner
from raven_preprocess.basic_utils.basic_response import (ok_resp, err_resp)
from raven_preprocess.msg_util import msgt

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

INPUT_DIR = join(dirname(CURRENT_DIR), 'input')
OUTPUT_DIR = join(dirname(CURRENT_DIR), 'output')

def run_preprocess(input_file, output_filepath=None, old_format=False):
    """Main test run class for this module"""
    run_info = PreprocessRunner.load_from_file(input_file)

    if not run_info.success:
        msgt(run_info.err_msg)
        #print(err_resp(err_msg))
        return

    runner = run_info.result_obj

    runner.show_final_info(old_format=old_format)
    #return ok_resp(runner.get_final_json(indent=4))

    jstring = runner.get_final_json(indent=4, old_format=old_format)

    if output_filepath:
        try:
            open(output_filepath, 'w').write(jstring)
            msgt('file written: %s' % output_filepath)
        except OSError as os_err:
            msgt('Failed to write file: %s' % os_err)


def show_instructions():
    """show command line instructions"""
    info = """
--------------------------
preprocess a single file
--------------------------

# write output to screen
> python preprocess.py [input csv file] [--old-format]

# write output to screen and file
> python preprocess.py [input csv file] [output file name] [--old-format]

OR

# test input and output files
> python preprocess.py test

"""
    print(info)

if __name__ == '__main__':
    old_format = '--old-format' in sys.argv
    args = [x for x in sys.argv if x != '--old-format']
    if len(args) == 2:
        if args[1] == 'test':
            input_csv = join(INPUT_DIR, 'test_file_01.csv')
            output_file = join(OUTPUT_DIR, 'test_file_01_preprocess.json')
            run_preprocess(input_csv, output_file, old_format=old_format)
        else:
            run_preprocess(args[1], old_format=old_format)

    elif len(args) == 3:
        run_preprocess(args[1], args[2], old_format=old_format)
    else:
        show_instructions()
