import textwrap

FILE_PATH_HELP = "Path to file relative to the current working directory."

TEMPLATE_VARIABLE_PREFIX_HELP = textwrap.dedent(
    """
        Template variables will be nested in this namespace when rendering; e.g:

        {{ <template_variable_prefix>.your_template_variable }}
    """
)
