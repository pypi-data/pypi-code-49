"""Bruker operations module"""
import logging

from .util import set_nested_attr

log = logging.getLogger(__name__)

def parse_bruker_params(fileobj):
    """Parse the pv5/6 parameters file, extracting keys

    References:
        - ParaVision D12_FileFormats.pdf
        - JCAMP DX format: http://www.jcamp-dx.org/protocols/dxnmr01.pdf

    Arguments:
        fileobj (file): The file-like object that supports readlines, opened in utf-8
    """
    # pylint: disable=too-many-branches
    result = {}

    # Variable names are ##/##$
    # And are either =value, =< value >, or =() with value(s) following the next lines
    # $$ appear to be comments

    key = None
    value = ''

    for line in fileobj.readlines(): # pylint: disable=too-many-nested-blocks
        if line.startswith('$$'):
            continue

        try:
            if line.startswith('##'):
                if key:
                    result[key] = value

                # Parse parameter name
                key, _, value = line[2:].partition('=')
                key = key.lstrip('$') # Paravision uses private parameters prefixed with '$'
                value = value.strip()

                # Check value
                if value:
                    # Case 1: value is wrapped in brackets: < foo >
                    if value[0] == '<' and value[-1] == '>':
                        result[key] = value[1:-1].strip()
                        key = None
                        value = ''
                    elif value[0] == '(':
                        # Case 2: value is a structure
                        if ',' in value:
                            continue
                        # Case 3: value is size/dimensions, in which case we ignore it
                        value = ''
                        continue
                    else:
                        # Case 4: value is directly assigned
                        result[key] = value.strip()
                        key = None
                        value = ''
            elif key:
                line = line.strip()
                if line[0] == '<' and line[-1] == '>':
                    line = line[1:-1]

                if value:
                    value = value + ' '

                value = value + line
        except ValueError as exc:
            log.debug(f'Error processing bruker parameter line: {exc}')
            # Any error should just reset state
            key = None
            value = ''

    if key:
        result[key] = value

    return result

def extract_bruker_metadata_fn(filename, keys):
    """Create a function that will open filename and extract bruker parameters.

    Arguments:
        filename (str): The name of the file to open (e.g. subject)
        keys (dict): The mapping of src_key to dst where dst is a key or a function
            that returns a key and a value, given an input value.

    Returns:
        function: The function that will extract bruker params as metadata
    """
    def extract_metadata(_, context, walker, path):
        file_path = walker.combine(path, filename)
        log.debug(f'Attempting to import params from: {file_path}')

        try:
            with walker.open(file_path, mode='r', encoding='utf-8') as file_obj:
                params = parse_bruker_params(file_obj)

            for src_key, dst_key in keys.items():
                if src_key in params:
                    value = params[src_key]
                    if callable(dst_key):
                        ret = dst_key(value, path=file_path, context=context)
                        if ret:
                            dst_key, value = ret
                        else:
                            dst_key = None

                    if dst_key:
                        set_nested_attr(context, dst_key, value)
        except FileNotFoundError:
            log.info(f'No param file located at: {file_path}')
        except IOError as exc:
            log.error(f'Unable to process params file {file_path}: {exc}')

    return extract_metadata


if __name__ == '__main__':
    # pylint: disable=invalid-name
    import argparse
    parser = argparse.ArgumentParser(description='Read and print bruker parameters file')
    parser.add_argument('path', help='The path to the file to read')

    args = parser.parse_args()

    with open(args.path, 'r') as f:
        parse_result = parse_bruker_params(f)

    for result_key, result_value in parse_result.items():
        print(f'{result_key} = {result_value}')
