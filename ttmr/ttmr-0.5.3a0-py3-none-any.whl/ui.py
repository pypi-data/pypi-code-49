import sys
#  import msvcrt
from datetime import datetime
from time import sleep

from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer
from prompt_toolkit.completion import Completion
from prompt_toolkit.validation import ValidationError
from prompt_toolkit.validation import Validator

from ttmr.console import Console
from ttmr.util import DEFAULT_TMSTP_FMT
from ttmr.util import Timer


class ObjectCompleter(Completer):
    def __init__(self, objects):

        self.objects = objects

    def get_completions(self, document, complete_event):

        word_before_cursor = document.get_word_before_cursor(WORD=False)
        word_before_cursor = word_before_cursor.lower()

        for o in self.objects:
            if o.name.lower().startswith(word_before_cursor):
                yield Completion(
                    o.name, -len(word_before_cursor), display_meta=str(o.id)
                )


def promptor(func):
    """Prompt decorator that provides a common format
    to a prompts query.

    """
    INPUT_REQUEST_FMT = u" {: >10}: "

    def _promptor(input_query, *args, **kwargs):
        query = INPUT_REQUEST_FMT.format(input_query)
        return func(query, *args, **kwargs)

    return _promptor


@promptor
def text_input(input_query, default=None):
    prmpt_opt = {}
    if default:
        prompt_opt["default"] = default
    return prompt(input_query, **prmpt_opt)


class OptionValidator(Validator):
    def __init__(self, options):
        super(OptionValidator, self).__init__()
        self.options = options

    def validate(self, document):
        if document.text not in self.options:
            raise ValidationError(message="Must select complete row", cursor_position=0)


@promptor
def option_input(input_query, options, default=None):
    option_dict = {name: id_ for id_, name in options}
    prompt_opt = {
        "completer": ObjectCompleter(options),
        "validator": OptionValidator(option_dict),
    }
    if default:
        prompt_opt["default"] = default
    text = prompt(input_query, **prompt_opt)
    return option_dict.get(text, text)


@promptor
def _option_input(input_query, options, default=None):
    option_dict = {e.name: e for e in options}
    prompt_opt = {
        "completer": ObjectCompleter(options),
        "validator": OptionValidator(option_dict),
    }
    if default:
        prompt_opt["default"] = default
    text = prompt(input_query, **prompt_opt)
    return option_dict.get(text, text)


class NumberValidator(Validator):
    def __init__(self, default, *args, **kwargs):
        super(NumberValidator, self).__init__(*args, **kwargs)
        self.translated_value = default

    def validate(self, document):
        text = document.text

        if text and not text.isdigit():
            i = 0

            for i, c in enumerate(text):
                if not c.isdigit():
                    break

            raise ValidationError(
                message="Duration must be a number!", cursor_position=i
            )

        self.translated_value = int(text) if text else 0


@promptor
def default_text_input(input_query, default):
    return prompt(input_query, default=default)


@promptor
def number_input(input_query, default):
    validator = NumberValidator(0)
    prompt(input_query, default=default, validator=validator)
    return validator.translated_value


@promptor
def duration_input(input_query):
    validator = NumberValidator(0)
    prompt(input_query, validator=validator)
    return validator.translated_value


class DateValidator(Validator):
    def __init__(self, dt):
        super(DateValidator, self).__init__()
        self.dt = dt

    def translate(self, input):
        try:
            self.translated_value = self.dt.parse_date_input(input)
        except Exception as ex:
            raise ValidationError(message=unicode(ex))

    def validate(self, document):
        self.translate(document.text)


@promptor
def date_input(input_query, dt, default=None):
    validator = DateValidator(dt)
    if not default:
        default = dt.current_timestamp().format(DEFAULT_TMSTP_FMT)
    prompt(input_query, default=default, validator=validator)
    return validator.translated_value


class _DateValidator(Validator):
    def __init__(self, dt):
        super().__init__()
        self.dt = dt

    def translate(self, input):
        try:
            self.translated_value = self.dt.parse_date_input(input)
        except Exception as ex:
            raise ValidationError(message=ex)

    def validate(self, document):
        self.translate(document.text)


@promptor
def _date_input(input_query, dt, default=None):
    validator = _DateValidator(dt)
    if not default:
        default = dt.to_str(datetime.now())
    prompt(input_query, default=default, validator=validator)
    return validator.translated_value


class BooleanValidator(Validator):
    def __init__(self, *args, **kwargs):
        super(BooleanValidator, self).__init__(*args, **kwargs)
        self.translated_value = False
        self.true_str = ("y", "yes", "true", "1")
        self.false_str = ("n", "", "no", "false", "0")

    def parse(self, input):
        if input in self.true_str:
            return True
        if input in self.false_str:
            return False
        raise ValidationError(message="Must enter valid reply.", cursor_position=0)

    def validate(self, document):
        self.translated_value = self.parse(document.text.lower())


@promptor
def bool_input(input_query):
    validator = BooleanValidator()
    prompt(input_query, validator=validator)
    return validator.translated_value


def show_timer(start_time, dt):
    """show_timer displays a timer incrementing clock in
    a HH:MM:SS format for the given start_time.

    The timer will continuously increment until the console
    registers a keyboard press.

    """
    DSPLY_FMT = u" {: >10}: {}  \n\n"
    timer = Timer(start_time, dt)

    def write_display():
        Console.write(DSPLY_FMT.format("Timer", timer.get_formatted_lapsed_time()))

    write_display()

    while True:
        sleep(1)
        Console.cursor_up()
        Console.cursor_up()
        Console.cursor_to_left_margin()
        Console.clear_line()
        write_display()
        # this only works on Windows.
        # kbhit returns True if the keyboard is struck.
        #  if msvcrt.kbhit():
        #      break
