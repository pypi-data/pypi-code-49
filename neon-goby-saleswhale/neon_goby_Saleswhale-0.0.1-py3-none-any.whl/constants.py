import re

FILTERS = "\"_:.,?!$%&()*-/;=?@[\\]^`{|}~\r\t\n"

# Gmail/Outlook quote tags
HTML_QUOTES = [
    re.compile(r"(?ms)<[^>]*gmail_quote.*"),
    re.compile(r"(?ms)<[^>]*appendonsend.*"),
    re.compile(r"(?ms)<[^>]*[dD]iv[rR]ply[fF]wd[mM]sg.*"),
]

# Plain text quote indicators
QUOTED_EMAILS_MATCHER = re.compile('|'.join([
    r"^Sender [^\r\n]+\r\nTo: [^\r\n]+\r\n(?:CC: .*\r\n)?",
    r"^On .+, <.+@.+\.\w+> wrote:",
    r"^From: .+ <.+@.+\.\w+>",
    r"^On .+, [^\n\r]+ wrote:",
    r"^>.*",
    r"From: .+[\n\r]+Sent: .+[\n\r]+To:",
    r"From: .+[\n\r]+Date: .+[\n\r]+To:"
]))

# Entitiy patterns
_EMAIL = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-\.]+\.[a-zA-Z0-9]+"
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
    [re.compile(_EMAIL), ' <email> '],
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

FAREWELLS = [
    'all the best',
    'best regards',
    'best wishes',
    'best',
    'cheers',
    'kind regards',
    'regards',
    'sincerely',
    'speak to you soon',
    'yours faithfully',
    'yours sincerely',
    'yours truly',
    'yours',
    'warmest regards',
    'thank you',
    'many thanks and kind regards',
    'many thanks',
    'warm regards',
    'thanks & best regards',
    'thanks and regards',
    'thanks for your understanding and kind regards',
    'thanks',
    'mit freundlichen grüßen',
    'degards',
    'have a nice weekend',
    'with kind regards',
    'with best wishes',
    'with best regards',
    'with my best',
    'with warmest regards',
    'sent from my' # hack, should move to its own check
]

OOO_SUBJECTS = [
    'auto',
    # 'auto reply',
    # 'automatic reply',
    # 'automated reply',
    'away',
    'leave',
    'ooo',
    'out of office',
    'out of the office',
    'overseas',
    'public holiday',
    'travelling'
]

REPLIED_SUBJECT = re.compile(r"(?<![\w\d])[Rr][Ee](?![\w\d])")

TOPIC_RULES = [
    'soft_bounce',
    'meeting_request',
    'negative_intent',
    'not_good_time',
    'not_right_person',
    'ignore',
    'ooo',
    'positive_intent',
    'referral',
    'rfi',
    'other_solution',
    'negative_intent'
]
