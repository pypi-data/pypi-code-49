#!/usr/bin/env python3

class SOArecord:
    """
    https://www.ripe.net/publications/docs/ripe-203
    Just object for storing all fields, and parsed email
    """
    def __init__(self, mname, rname, parsed_email, serial, refresh, retry, expire, minimum):
        self.mname = mname

        self.rname = rname
        self.parsed_email = parsed_email

        self.serial = serial

        self.refresh = refresh
        self.retry = retry
        self.expire = expire
        self.minimum = minimum


def soa_parse(authority_data):
    """parse out data fields in SOA and best guess email address to object"""
    soa_data = authority_data.split(" ")

    try:
        mname = soa_data[0][:-1]

        rname = soa_data[1][:-1]
        parsed_email = email_from_soa(raw_email)

        serial = soa_data[2]

        refresh = soa_data[3]
        retry = soa_data[4]
        expire = soa_data[5]
        minimum = soa_data[6]

        return SOArecord(mname, rname, parsed_email, serial, refresh, retry, expire, minimum)

    except IndexError as e:
        print("error parsing SOA data field:\n" + repr(e))
        return None


def email_from_soa(soa_email_field):
    """
    parse email address from DNS SoA rname field
    best-guess: assumes email hostname is root name, not a subdomain
    may not be accurate if email hostname has multiple parts
    """
    email_parts = soa_email_field.rsplit(".", maxsplit=2)
    email_name = email_parts[0]

    email = email_name + "@" + ".".join(email_parts[1:])
    return email
