"""Some utils to help with python versions compatibility or with inspection.
"""
import inspect
import sys
import textwrap

IS_PYTHON2 = sys.version.startswith('2.')


def get_args_spec(func):  # pragma: nocover
    """
    :type func: callable
    :rtype: list[str]
    """
    is_partial = hasattr(func, 'func') and hasattr(func, 'args')

    args = list()
    if IS_PYTHON2 and not is_partial:
        # pylint: disable=deprecated-method
        args.extend(inspect.getargspec(func).args)
    elif IS_PYTHON2 and is_partial:
        # pylint: disable=deprecated-method
        args.extend(inspect.getargspec(func.func).args[len(func.args):])
    else:
        args.extend(
            inspect.getfullargspec(func).args  # pylint: disable=no-member
        )
    return args


def _wrap_function_with_additional_arguments(func, arguments):
    """
    :param func: function to wrap with additional arguments
    :param arguments: arguments to add if they are not already received in func
    :type arguments: set[str]
    :rtype: callable
    """
    args = get_args_spec(func)
    additional_args = list(arguments - set(args))
    call_args = args + additional_args
    wrapper_body = textwrap.dedent(
        """
        def _call_wrapper_{name}({args}):
            return func({call_args})
        """.format(
            name=func.__name__,
            args=', '.join(call_args),
            call_args=', '.join('{0}={0}'.format(a) for a in args)
        )
    )
    context = {"func": func}
    exec(wrapper_body, context)  # pylint: disable=exec-used
    return context["_call_wrapper_{}".format(func.__name__)]
