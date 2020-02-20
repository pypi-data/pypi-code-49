import pathlib
import os
import subprocess

def return_local_test_data(filename):
    """return_local_test_data returns the path to test data located in the tests/data directory."""
    current_path = pathlib.Path(__file__).parent.absolute()
    path = os.path.join(current_path, "data", filename)
    return path

def convert_to_json(filename):
    """convert_to_json converts a Markdown file to Pandoc's JSON format and returns the result."""
    cmd = ['pandoc', '-t', 'json', filename]
    process = subprocess.run(cmd, check=True, stdout=subprocess.PIPE)
    output = process.stdout.decode('utf-8')
    return output
