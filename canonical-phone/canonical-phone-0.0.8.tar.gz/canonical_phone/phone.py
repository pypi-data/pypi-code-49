import re
import logging

logger = logging.getLogger()


def canonical_number(phone_no, has_country_code=False):
    """
    Convert given phone number to phone number used by system
    :param phone_no: mobile number
    :return: system mobile number
    """
    if not phone_no:
        return
    phone_no = re.sub(r'[^0-9\-]', '', phone_no)
    phone_no = phone_no.replace("-", "$", 1)
    phone_no = phone_no.replace("-", "")
    phone_no = phone_no.replace("$", "-", 1)
    phone_regex_with_cc_unkown = re.compile(r'^\+?62-?0?(?P<ph1>[1-9]\d{7,14})$'
                                            r'|^0?(?P<ph2>[1-9]\d{7,14})$'
                                            r'|^\+?(?P<cc>[1-9]\d{0,2})-?(?P<ph3>[1-9]\d{7,11})$')
    phone_regex_with_cc = re.compile(r'^\+?(?P<cc>[1-9]\d{0,1})-?(?P<ph1>[1-9]\d{7,14})$')
    use_regex = phone_regex_with_cc_unkown
    if has_country_code:
        use_regex = phone_regex_with_cc
    m = use_regex.match(phone_no)
    if m:
        country_code = m.group('cc') or '62'
        ph_no = m.group('ph1') or m.group('ph2') or m.group('ph3')
        final_phone_no = country_code + "-" + ph_no
    else:
        return
    logger.info("%s -> %s", phone_no, final_phone_no)
    return final_phone_no
