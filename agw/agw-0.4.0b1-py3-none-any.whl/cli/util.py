import sys
from pprint import pprint
from functools import wraps


def ctrl_exit(func):
    @wraps(func)
    def _ctrl_exit(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print("")
            print("\nexiting...\n")
            sys.exit()

    return _ctrl_exit


def output_final_status(kwarg_key, status_msg, object_builder):
    def _output_final_status(func):
        @wraps(func)
        def _output_final_status_(*args, **kwargs):
            kwargs[kwarg_key] = final_obj = object_builder()
            try:
                return func(*args, **kwargs)
            except KeyboardInterrupt as ex:
                if final_obj:
                    print("\n{status_msg}:\n")
                    pprint(final_obj)
                    print("*" * 60)
                raise ex

        return _output_final_status_

    return _output_final_status
