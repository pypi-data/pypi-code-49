# from snakypy.utils import decorators
from snakypy.ansi import NONE, FG, BG, SGR


def attr_foreground_background_sgr(*args):
    """
    Checks if the attributes of the functions that the foreground
    and background parameters are in accordance with their respective class.

    Arguments:
        args {str} -- It receives a certain number of arguments with an ansi code value.
    """
    if args[0] and args[0] not in FG.__dict__.values():
        msg = 'Attribute invalid in parameter "foreground". Must receive from FG class.'
        raise AttributeError(msg)
    if args[1] and args[1] not in BG.__dict__.values():
        msg = 'Attribute invalid in parameter "background". Must receive from BG class.'
        raise AttributeError(msg)
    if args[2] and args[2] not in SGR.__dict__.values():
        msg = 'Attribute invalid in parameter "sgr". Must receive from SGR class.'
        raise AttributeError(msg)


# @decorators.use_unix_system
def printer(*args, foreground='', background='', sgr='',
            sep=' ', end='\n', file=None, flush=False):
    """A function that allows you to print colored text on the terminal.

    >>> from snakypy import printer, FG, BG, SGR
    >>> printer('Hello, World!', foreground=FG.BLACK, background=BG.WHITE, sgr=SGR.UNDERLINE)
    >>> printer('Hello, World!', foreground=FG.MAGENTA, sgr=SGR.UNDERLINE)

    Keyword Arguments:
        **foreground {str}** -- This named argument should optionally receive \
                            an object of class "snakypy.ansi.FG" for the foreground \
                            color of the text. This object will be text with ansi code. \
                            (default: '')

        **background {str}** -- This named argument should optionally receive \
                            an object of class "snakypy.ansi.BG" for the background \
                            color of the text. This object will be text with ansi code. \
                            (default: '')

        **sgr {str}** -- This named argument should optionally receive \
                     an object of class "snakypy.ansi.SGR" for the effect \
                     of the text. This object will be text with ansi code. \
                     (default: '')

        **sep {str}** -- Separator between printer function objects. (default: {' '}) \

        **end {str}** -- Responsible for skipping a line after printing is finished. \
                         (default: '[bar]n')
    """

    attr_foreground_background_sgr(foreground, background, sgr)

    lst = []
    for i in range(len(args)):
        lst.append(args[i])
    text = ' '.join(map(str, lst))

    return print(f'{NONE}{sgr}{foreground}{background}{text}{NONE}',
                 sep=sep, end=end, file=file, flush=flush)


# @decorators.use_unix_system
def entry(text, *, foreground='', background='', sgr='', jump_line='\n> '):
    """
    This function is derived from the input, but with the option of
    coloring it and some different formatting.
    Note: If you use Windows, the coloring option will not work.

    >>> from snakypy import entry, FG
    >>> entry("What's your name?", foreground=FG.QUESTION)
    >>> entry("What's your name?", foreground=FG.BLUE)
    >>> entry("What's your name?", foreground=FG.GREEN)

    Arguments:
        **text {object}** -- Argument must receive an object

    Keyword Arguments:

        **foreground {str}** -- This named argument should optionally receive \
                            an object of class "snakypy.ansi.FG" for the foreground \
                            color of the text. This object will be text with ansi code. \
                            (default: '')

        background {str} -- This named argument should optionally receive \
                            an object of class "snakypy.ansi.BG" for the background \
                            color of the text. This object will be text with ansi code. \
                            (default: '')

        **sgr {str}** -- This named argument should optionally receive \
                         an object of class "snakypy.ansi.SGR" for the effect \
                         of the text. This object will be text with ansi code. \
                         (default: '')

        **jump_line {str}** -- Named argument that makes the action of skipping a line \
                           and adding a greater sign to represent an arrow. You change \
                           that argument to your liking. (default: '[bar]n> ') \

    """

    attr_foreground_background_sgr(foreground, background, sgr)

    try:
        return input(f'{NONE}{sgr}{foreground}{background}{text}{jump_line}{NONE}')
    except KeyboardInterrupt:
        print(f'\n{FG.WARNING} Aborted by user.{NONE}')


def pick_options(title, options, answer, *, colorful=False, index=False):
    if not colorful:
        FG.QUESTION = ''
        FG.GREEN = ''
        FG.MAGENTA = ''
        FG.CYAN = ''
        FG.ERROR = ''
        FG.WARNING = ''

    printer(title, '(Ctrl+C to Cancel)', foreground=FG.QUESTION)
    count = 1
    for option in options:
        print(f'{FG.GREEN}[{count}] {FG.MAGENTA}{option}{NONE}')
        count += 1
    try:
        pos = int(input(f'{FG.CYAN}{answer} {NONE}')) - 1
        assert pos > -1
        if index:
            return pos, options[pos].lower()
        return options[pos].lower()
    except Exception:
        printer('Option invalid!', foreground=FG.ERROR)
        return False
    except KeyboardInterrupt:
        printer('Canceled by user.', foreground=FG.WARNING)
        return


def pick(title, options: list, *,
         answer='Answer:',
         index=False,
         colorful=False):
    """Function that creates a menu of options in the terminal.

    >>> from snakypy import pick
    >>> title = 'What is your favorite programming language?'
    >>> options = ['C', 'C++', 'Java', 'Javascript', 'Python', 'Ruby']
    >>> pick(title, options)

    **output:**

    .. code-block:: shell

        What is your favorite programming language? (Ctrl+C to Cancel)
        [1] C
        [2] C++
        [3] Java
        [4] Javascript
        [5] Python
        [6] Ruby
        Answer: 5
        'python'

    Arguments:
        **title {str}** - You should receive a text that will be the \
                       title or the question with meaning in the alternatives.

        **options {list}** - You should receive a list with certain elements \
                          that will be part of the menu options.

    Keyword Arguments:
        **answer {str}** -- The text that will be shown before entering the answer. \
                        You can change to your language. (default: {'Answer:'})

        **index {bool}** -- This argument for True, will return a tuple, where element 0, \
                        will be the index of the option that the user chose, and \
                        element 1 of the tuple, will be the name of the choice option. \
                        Remember that the indexing of the menu is not the same as the \
                        list of options because it starts with zero (0). \
                        (default: {False})

        **colorful {bool}** -- If it has True, the menu color will be active, but it only \
                           works if it is on a UNIX system, as the color uses Ansi Color. \
                           If have Windows, no effect will appear. \
                           (default: {False})
    """

    if not type(options) is list:
        raise TypeError('You must enter a list in the argument: options')

    if len(title) == 0:
        raise TypeError('The title cannot contain an empty element. Approached.')

    for option in options:
        if len(option) == 0:
            raise TypeError('The list cannot contain an empty element. Approached.')

    try:
        while True:
            option = pick_options(title,
                                  options,
                                  answer=answer,
                                  index=index,
                                  colorful=colorful)
            if option or option is None:
                break
        return option
    except Exception:
        raise Exception('An unexpected error occurs when using pick')


def billboard(text, foreground='', background='', ret_text=False):
    """
    Creates a Billboard in the terminal.

    >>> from snakypy.console import billboard
    >>> from snakypy import FG, BG
    >>> billboard('Hello, Snakypy!')
    >>> billboard('Hello, Snakypy!', foreground=FG.BLUE, background=BG.WHITE)

    Arguments:
        **text {str}** -- Any text must be informed.

    Keyword Arguments:
        **foreground {str}** -- This named argument should optionally receive \
                            an object of class "snakypy.ansi.FG" for the foreground \
                            color of the text. This object will be text with ansi code. \
                            (default: '')

        **background {str}** -- This named argument should optionally receive \
                            an object of class "snakypy.ansi.BG" for the background \
                            color of the text. This object will be text with ansi code. \
                            (default: '')

        **ret_text {bool}** -- Receives a Boolean value. If the value is True, it will only \
                               return the text. If the value is False, it will resume printing.

    Returns:
        **[str]** -- The text informed in billboard form.
    """
    import pyfiglet
    import snakypy

    banner = pyfiglet.figlet_format(text)
    if ret_text:
        return banner
    return snakypy.printer(banner, foreground=foreground, background=background)


# --------------------------------------------
# Function that does not use pyfliglet package
# --------------------------------------------
# def billboard(text, foreground='', background=''):
#     from snakypy.utilities.utilities import is_tool
#     from shutil import which
#     from snakypy.console import cmd
#
#     if which('figlet') is not None:
#         return cmd(f'figlet {text}', verbose=True)
#     return print(text)


def cmd(command, *args, shell=True, universal_newlines=True, ret=False, verbose=False):
    """
    Function that uses the subprocess library with Popen.
    The function receives a command as an argument and shows
    execution in real time.

    >>> from snakypy.console import cmd
    >>> command = 'git clone https://github.com/snakypy/snakypy.git'
    >>> cmd(command, verbose=True)

    Arguments:
        **command {str}** -- Must inform the command to be executed.

    Keyword Arguments:
        **shell {bool}** -- Receives a Boolean value. If it has False, the command must be \
                        in list where the command space is split. \
                        **E.g:** ['ls', '/bin']. \
                        If the value is True, the command can be stored in a string \
                        normal. **E.g:** 'ls /bin'

        **ret {bool}** -- The default value is False, however if it is set to True it will \
                      return a code status of the command output, where the code 0 (zero), \
                      is output without errors. \

        **verbose {bool}** -- The default value is False, if you change it to True, the command \
                          will show in real time the exit at the terminal, if there is an exit. \
    """
    from subprocess import Popen, PIPE

    process = Popen(command, shell=shell, stdout=PIPE,
                    universal_newlines=universal_newlines)
    if verbose:
        for line in iter(process.stdout.readline, ''):
            print(NONE, *args, line.rstrip(), NONE)
    if ret:
        r = process.poll()
        return r


def credence(app_name, app_version, app_url, data: dict, foreground=''):
    """
    Print project development credits.

    >>> from snakypy.console import credence
    >>> data = {
        "credence": [
            {
                "my_name": "William Canin",
                "email": "example@domain.com",
                "website": "http://williamcanin.me",
                "locale": "Brazil - SP"
            },
            {
                "my_name": "Maria Canin",
                "email": "example@domain.com",
                "locale": "Brazil - SP"
            }
        ]
    }
    >>> credence('Snakypy', '0.1.0', 'https://github.com/snakypy/snakypy', data)

    **output:**

    .. code-block:: shell

        ---------------------------------------------------------
                       Snakypy - Version 0.1.0
        ---------------------------------------------------------

                              Credence:

                        My Name: William Canin
                      Email: example@domain.com
                   Website: http://williamcanin.me
                         Locale: Brazil - SP

                         My Name: Maria Canin
                      Email: example@domain.com
                         Locale: Brazil - SP

        ---------------------------------------------------------
                    Snakypy © 2020 - All Right Reserved.
                Home: https://github.com/snakypy/snakypy
        ---------------------------------------------------------

    Arguments:
        app_name {str} -- Put application name.

        app_version {str} -- Application version.

        app_url {str} -- Application or website url.

        data {dict} -- You must receive a dictionary containing a key called "credence".
                       E.g: data = {'credence': []}

    Keyword Arguments:
        **foreground {str}** -- This named argument should optionally receive \
                            an object of class "snakypy.ansi.FG" for the foreground \
                            color of the text. This object will be text with ansi code. \
                            (default: '')
    """

    from datetime import date

    try:

        if type(data) is not dict:
            msg = f'>>> The function "{credence.__name__}" ' \
                  'must take a dictionary as an argument.'
            raise Exception(msg)

        printer(f'{57 * "-"}'.center(75), foreground=foreground)
        printer(f'{app_name} - Version {app_version}'.center(70),
                foreground=foreground)
        printer(f'{57 * "-"}\n'.center(75), foreground=foreground)
        printer(f'Credence:\n'.center(70), foreground=foreground)
        for item in data['credence']:
            for key, value in item.items():
                printer(f'{key.title().replace("_", " ")}: {value}'.center(70),
                        foreground=foreground)
            print()
        printer(f'{57 * "-"}'.center(75), foreground=foreground)
        printer(f'{app_name} © {date.today().year} - All Right Reserved.'.center(70),
                foreground=foreground)
        printer(f'Home: {app_url}'.center(70), foreground=foreground)
        printer(f'{57 * "-"}'.center(75), foreground=foreground)
    except KeyError:
        msg = "The 'credence' key was not found." \
              "Enter a dictionary containing a 'credits' key."
        raise KeyError(msg)


def loading(set_time=0.030, bar=False, header='[Loading]', foreground=''):
    """Function will show animated logging in percentage and bar style.

    >>> from snakypy.console import loading
    >>> loading()

    Using bar instead of percentage and setting the time (Default: set_time=0.030):

    >>> loading(set_time=0.20, bar=True)

    Keyword Arguments:

        **set_time {float}** -- Time when the animation will last. (default: {0.030})

        **bar {bool}** -- If True, the animation will be barred and not percentage. (default: {False})

        **header {str}** -- Modifies the animation header (default: {'[Loading]'})
    """

    import time
    import sys

    # denying_win(foreground)
    printer(header, foreground=foreground)
    try:
        if bar:
            for i in range(0, 100):
                time.sleep(set_time)  # 5 seconds
                width = (i + 1) / 4
                bar = f"[{'#' * int(width)}{' ' * (25 - int(width))}]"
                sys.stdout.write(u"\u001b[1000D" + bar)
                sys.stdout.flush()
            print()
            return
        for i in range(0, 100):
            time.sleep(set_time)
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.flush()
            # time.sleep(0.1)
            sys.stdout.write(f'{str(i + 1)}%')
            sys.stdout.flush()
        print()
        return
    except KeyboardInterrupt:
        printer('\nCanceled by user.', foreground=FG.WARNING)
        return


__all__ = ['pick', 'entry', 'printer', 'billboard', 'cmd', 'credence', 'loading']
