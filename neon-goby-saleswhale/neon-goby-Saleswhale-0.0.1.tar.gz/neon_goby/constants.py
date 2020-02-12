import re

# Plain email format
PREPENDED_TEXT = [
    re.compile(r"^Sender [^\r\n]+\r\nTo: [^\r\n]+\r\n(?:CC: .*\r\n)?")
]

# Plain text quote indicators
QUOTED_EMAILS = [
    re.compile(r"On .+, <.+@.+\.\w+> wrote:"),
    re.compile(r"From: .+ <.+@.+\.\w+>"),
    re.compile(r"On .+, [^\n\r]+ wrote:"),
    re.compile(r"From: .+[\n\r]+Sent: .+[\n\r]+To:", flags=re.MULTILINE),
    re.compile(r"From: .+[\n\r]+Date: .+[\n\r]+To:", flags=re.MULTILINE)
]

# Entity patterns
EMAIL_MATCHER = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-\.]+\.[a-zA-Z0-9]+"

# Outlook quote tags
HTML_QUOTES = [
    re.compile(r"(?ms)<[^>]*appendonsend.*"),
    re.compile(r"(?ms)<[^>]*[dD]iv[rR]ply[fF]wd[mM]sg.*"),
]

PHONE_MATCHERS = "|".join([
    r"\+?\(?\d{2}\)? ?\d{4} ?\d{4}",
    r"\d{4} ?\d{4}",
    r"\+?\(?\d{2}\)? ?\d{4} ?\d{4}",
    r"\+?\d{2} ?\(?\d{2,4}\)? ?\d{2,4} ?\-?\d{2,4} ?\d{0,2}"
])

WEB_MATCHERS = "|".join([
    r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
    r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
])

ENTITIES = [
    [re.compile(EMAIL_MATCHER), ' <email> '],
    [re.compile(PHONE_MATCHERS), ' <phone> '],
    [re.compile(WEB_MATCHERS), ' <web> '],
]

REPLACEMENTS = [
    [re.compile(r"\d"), '9'], # Replace all digits
]

SPACES = [re.compile(r"[ \t]+")]

GREETINGS = [
    'dear', 'hi', 'hello', 'greetings', 'to whom', 'for whom', 'good', 'hey'
]
