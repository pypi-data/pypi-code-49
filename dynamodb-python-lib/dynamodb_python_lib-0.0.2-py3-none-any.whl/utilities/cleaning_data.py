import re
import calendar


def execute(text: str) -> str:
    odd_chars = r"[^a-zA-Z0-9_\d\s:,.@()/':;?!^#$%*+=\[\]\\|<>\"&~`{}-]+"
    found_odd_chars = re.search(odd_chars, text)
    if found_odd_chars:
        return text

    regex_string = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    replace_word = "EMAIL_ADDRESS"
    text = re.sub(regex_string, replace_word, text)

    regex_string = r"([0-9]{4}[-\.\s]?){3}[0-9]{4}|([0-9]{4}[-\.\s]?){3}[0-9]{3}|[0-9]{3}([-\.\s]?[0-9]{4}){3}"
    replace_word = "CC_NUMBER"
    text = re.sub(regex_string, replace_word, text)

    regex_string = r"(\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4})"
    replace_word = "PHONE_NUMBER"
    text = re.sub(regex_string, replace_word, text)

    regex_string = r"([0-9][-\.]?){8,13}"
    replace_word = "ITINERARY"
    text = re.sub(regex_string, replace_word, text)

    months = calendar.month_name[1:]
    months.extend(calendar.month_abbr[1:])
    month_lower = [x.lower() for x in months]
    months.extend(month_lower)
    months = "|".join([month for month in months])

    regex_date_dd_MMM_yyyy = r"(\d{1,2}([th,st,rd,nd]{2})*)[ /.-](?:%s)([ /.-]\d{2,4})*" % months
    regex_date_MMM_dd_yyyy = r"(?:%s)[ /.-](\d{1,2}([th,st,rd,nd]{2})*)([ /.-]\d{2,4})*" % months
    regex_date_dd_mm_yyyy = r"(\d{1,2}([th,st,rd,nd]{2})*)[/.-](\d{1,2}([th,st,rd,nd]{2})*)[/.-](\d{0,4})"
    regex_date_dd_mm = r"(\d{1,2}([th,st,rd,nd]{2})*)[/.-](\d{1,2}([th,st,rd,nd]{2})*)"
    regex_date_day = r"(\d{1,2}([th,st,rd,nd]{2}))"
    regex_month = r"(?:%s)" % months
    regex_date = [regex_date_dd_MMM_yyyy, regex_date_MMM_dd_yyyy, regex_date_dd_mm_yyyy,
                  regex_date_dd_mm, regex_date_day, regex_month]

    regex_string = '|'.join(regex_date)
    replace_word = "DATE"
    text = re.sub(regex_string, replace_word, text)

    regex_string = r"(([0-9][\.,]?))+"
    replace_word = "NUMBER"
    text = re.sub(regex_string, replace_word, text)

    return text
