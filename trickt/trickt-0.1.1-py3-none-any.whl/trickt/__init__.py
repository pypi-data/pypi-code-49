"""Search data for obfuscation and trickiness."""

__version__ = "0.1.1"


import argparse
import base64
import binascii
import re
import urllib.parse


REGEX_CHR_STRING = br"(chr\(.+chr\([0-9]+\))"
REGEX_CHR_CODE = br"([0-9]+)"
REGEX_ESCAPED_CHARACTERS_STRING = br"(\\[xu].+\\[xu][0-9a-fA-F]+)"
REGEX_ESCAPED_CHARACTERS_CHAR = br"(\\[xu][0-9a-zA-Z]{2,4})"
_REGEX_B64_STRING = br"([0-9a-zA-Z\+\\]{%s,}[=]{0,2})"
REGEX_B64_STRING = _REGEX_B64_STRING % br"32"
REGEX_URL_ENCODED = br"^.*%[0-9a-fA-F]{2}.*$"


# Compile the defaults regular expressions for speed
COMPILED_CHR_STRING = re.compile(REGEX_CHR_STRING)
COMPILED_CHR_CODE = re.compile(REGEX_CHR_CODE)
COMPILED_ESCAPED_CHARACTERS_STRING = re.compile(REGEX_ESCAPED_CHARACTERS_STRING)
COMPILED_ESCAPED_CHARACTERS_CHAR = re.compile(REGEX_ESCAPED_CHARACTERS_CHAR)
COMPILED_B64_STRING = re.compile(REGEX_B64_STRING)
COMPILED_URL_ENCODED = re.compile(REGEX_URL_ENCODED)


##########################################
## Functions to find trickiness in data ##
##########################################


def url_encoded(content, encoding="utf-8", string_regex=COMPILED_URL_ENCODED, **kwargs):
    """Decodes url encoded strings"""
    try:
        url_encoded = string_regex.search(content).group()
    except AttributeError:
        return []
    unquoted = urllib.parse.unquote(url_encoded.decode(encoding))
    return [unquoted.encode(encoding).strip()]


def code_point(
    content, string_regex=COMPILED_CHR_STRING, char_regex=COMPILED_CHR_CODE, **kwargs
):
    """Return strings converted from code points.

    Ex: String 'chr(104) . chr(101) . chr(108) . chr(108) . chr(111)'
    would be converted to 'hello'."""

    found = []
    matches = string_regex.findall(content)
    for match in matches:
        code_points = char_regex.findall(match)
        found.append(
            b"".join([bytes(chr(int(c)), "utf-8") for c in code_points]).strip()
        )
    return found


def escaped_characters(
    content,
    string_regex=COMPILED_ESCAPED_CHARACTERS_STRING,
    char_regex=COMPILED_ESCAPED_CHARACTERS_CHAR,
    **kwargs,
):
    """Return strings converted from escaped unicode characters or
    escaped hex characters."""

    found = []
    matches = string_regex.findall(content)
    for match in matches:
        escaped_chars = br"".join(char_regex.findall(match))
        bytes_ = escaped_chars.decode("unicode-escape").encode("latin1")
        found.append(bytes_.strip())
    return found


def base64_decode(
    content, string_regex=COMPILED_B64_STRING, minimum_length=None, **kwargs
):
    """Return strings converted from base64 encoded strings.

    Ex: 'aGVsbG93b3JsZAo=' would be returned as 'helloworld'

    Since the regex for base64 could match long words or strings,
    the default is to only attempt decoding strings that appear to be
    Base64 strings and are 32 characters in length or more. You can
    override this by passing in 'minimum_length'.

    #NOTE: Minimum length does include padding in the calculation.

    Note that you take a performance hit using the 'minimum_length'
    key word argument as it is complied with each execution of the
    function. Keeping track of your own compiled regex and passing
    in the compiled version yourself (so you can use it more than
    once) is much faster."""

    if minimum_length is not None:
        _interpol = _REGEX_B64_STRING % str(minimum_length).encode("utf-8")
        string_regex = re.compile(_interpol)
    found = []
    matches = string_regex.findall(content)
    for match in matches:
        try:
            b64 = base64.b64decode(match)
        except binascii.Error:
            continue
        else:
            found.append(b64.strip())
    return found


# Map trick name to function
BAG_O_TRICKS = {
    "url_encoded": url_encoded,
    "code_point": code_point,
    "escaped_characters": escaped_characters,
    "base64": base64_decode,
}


def result_is_empty(result):
    """Return True/False if there are no results."""
    for trick in result:
        if trick != "url_encoded":
            if result[trick]:
                return False
    return True


def all(content, minimum_length=None, depth=0, parent_type=None, **kwargs):
    """Return a dictionary of results from all the tricks.

    This includes searching child values to make sure tricks aren't
    nested. For example, a string could be base64 encoded twice. Another
    example would be if a string of code points was base64 encoded."""

    result = {}
    for trick_name, trick in BAG_O_TRICKS.items():

        deobfuscated_strings = trick(content, minimum_length=minimum_length)
        result[trick_name] = []

        # Unquoting a string that doesn't need unquoting will return
        # the same string. We don't want to unquote a string forever.
        if (trick_name == "url_encoded") and (parent_type == "url_encoded"):
            continue

        for string_ in deobfuscated_strings:
            # Recursively look for more trickiness...
            child_result = all(
                string_,
                minimum_length=minimum_length,
                depth=(depth + 1),
                parent_type=trick_name,
            )

            _value = {
                "value": string_,
                "depth": depth,
                "child": child_result,
            }

            # There are plenty of benign strings that could be unurl_encoded.
            # If we tried to keep all of them, there would be too much
            # noise. So if the unurl_encoded value does not match any other
            # trick, then don't keep it for the output.
            if trick_name == "url_encoded" and result_is_empty(child_result):
                continue

            result[trick_name].append(_value)

    return result


#######################
## PRETTY CLI OUTPUT ##
#######################


class Term:
    PURPLE = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m"


def decode(content, encoding):
    """Return a decoded or original string"""
    if content is None:
        return content

    try:
        return content.decode(encoding)
    except Exception as e:
        print(f"{Term.YELLOW}!!! Unable to decode as '{encoding}': {e} !!!{Term.END}")
        return content


def print_lines(num, result, original=None, depth=0, pretty=False, encoding="utf-8"):
    """Recursively print results for current line number."""
    for trick_type, values in result.items():
        for value in values:
            print_line(
                num,
                trick_type,
                value["value"],
                original=original,
                depth=depth,
                pretty=pretty,
                encoding=encoding,
            )
            print_lines(
                num, value["child"], depth=(depth + 1), pretty=pretty, encoding=encoding
            )


def print_line(
    num, type_, content, original=None, depth=0, pretty=False, encoding="utf-8"
):
    """Print the current result."""

    if pretty:
        original = decode(original, encoding)
        content = decode(content, encoding)

    if depth == 0 and original:
        print(
            f"\n{Term.BOLD}{Term.GREEN}line {num}::{Term.PURPLE}original:> {Term.END} {original}"
        )

    # Indent if this is a nested result.
    offset = "    " * (depth + 1)
    print(
        f"{Term.BOLD}{Term.GREEN}{offset}|\n{offset}|--decoded_{Term.PURPLE}{type_}> {Term.END} {content}"
    )


#################
## CLI PROGRAM ##
#################


def parse_args():
    parser = argparse.ArgumentParser(description="Search data for bad guy trickiness.")
    parser.add_argument(
        "-m",
        "--minimum_length",
        default=None,
        help="Minimum length of Base64 match to decode. The higher the minimum, the less junk output Default is 32.",
    )
    parser.add_argument(
        "-p",
        "--pretty",
        action="store_true",
        help="Decode string and try to pretty print it.",
    )
    parser.add_argument(
        "-e",
        "--encoding",
        default="utf-8",
        help="Specify the encoding of the string. Default is 'utf-8'",
    )
    parser.add_argument("target", help="File path or a string to parse")

    return parser.parse_args()


def main():
    args = parse_args()

    target = [args.target.encode("utf-8")]
    startup_message = "Searching string for trickiness..."

    try:
        target = open(args.target, "rb")
    except OSError:
        # File name too long or file not found.
        # Assume target is just a string.
        pass
    else:
        startup_message = f"Searching file '{args.target}' for trickiness..."

    print(f"\n{Term.PURPLE}{startup_message}{Term.END}")

    for index, line in enumerate(target):
        result_dict = all(line, minimum_length=args.minimum_length)
        line_num = index + 1
        print_lines(
            line_num,
            result_dict,
            original=line,
            pretty=args.pretty,
            encoding=args.encoding,
        )

    if not isinstance(target, list):
        target.close()


if __name__ == "__main__":
    main()
    exit()
