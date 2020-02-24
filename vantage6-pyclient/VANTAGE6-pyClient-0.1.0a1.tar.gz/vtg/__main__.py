import sys
import os
import json
import importlib

def dispatch_RPC(input_data, pkg=''):
    """Dispatch Remote Procedure Call."""
    if not input_data or (not 'method' in input_data):
        return ''

    input_ = json.loads(input_data)

    # 'method' is a required key
    methodname = f"RPC_{input_['method']}"

    # 'args' and 'kwargs' can be left out
    args = input_.get('args', [])
    kwargs = input_.get('kwargs', {})

    # The imported module is expected to contain all 'RPC_' methods.
    # Of course, they can be defined in separate files/packages, as long as they
    # are imported into the module's namespace.
    mod = importlib.import_module(pkg)

    func = getattr(mod, methodname)

    # The 'RPC_' function should return a (JSON) serializable result.
    result = func(*args, **kwargs)
    return json.dumps(result)

def docker_wrapper(PKG):
    """...."""
    # Database, input and output files ...
    DATABASE_URI = os.environ.get('DATABASE_URI')
    INPUT_FILE = '/app/input.txt'
    OUTPUT_FILE = '/app/output.txt'

    # Input/output defaults
    input_data = None
    output_data = ''

    # Get crackin'
    print(f'Using {DATABASE_URI} as database')

    # Load the input from disk
    print(f'Loading input from "{INPUT_FILE}"')

    try:
        with open(INPUT_FILE) as fp:
            input_data = fp.read()
    except Exception as e:
        print(f'Could not load input: {e}')

    # Do some dispatching ...
    output_data = dispatch_RPC(input_data, PKG)

    # Write output ...
    with open(OUTPUT_FILE, 'w') as fp:
        fp.write(output_data)

    # All done ...
    print('Done!')



# ------------------------------------------------------------------------------
# __main__
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    PKG = sys.argv[1]
    docker_wrapper(PKG)