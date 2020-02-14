import codecs
import os

import jinja2


def encode(input):
    return input, len(input)


def decode(input):
    code_string = codecs.decode(input)
    code_string = code_string + "\n"
    template = jinja2.Template(
        code_string,
        block_start_string="# {%",
        trim_blocks=True,
        lstrip_blocks=True,
    )
    context = os.environ
    rendered = template.render(**context)
    for i, line in enumerate(rendered.splitlines()):
        print(f"{i+1}: {line}")
    return rendered, len(input)


def search_function(name):
    if name == "jinja2":
        return codecs.CodecInfo(encode=encode, decode=decode)
