import re
import email
import hashlib
from email_master.util import EmailParser, EmailUtil, EmailAttachment, EmailAttachmentList
from email_master.compat import base64_decode, base64_encode, base64_decode_to_bytes, to_unicode

import six
if six.PY2:
    from HTMLParser import HTMLParser
    from types import StringTypes
elif six.PY3:
    from html.parser import HTMLParser
    StringTypes = str
    unicode = to_unicode


class EMLParser(EmailParser):
    def __init__(self, email_data, filename="unknown.eml", ignore_errors=False, exclude_attachment_extensions=None):
        super(EMLParser, self).__init__(email_data,
                                        filename=filename,
                                        ignore_errors=ignore_errors,
                                        exclude_attachment_extensions=exclude_attachment_extensions)
        if six.PY3:
            self.msg = email.message_from_bytes(base64_decode_to_bytes(email_data))
        else:
            self.msg = email.message_from_string(base64_decode(email_data))

        self.seen_attachment_hashes = []  # Class-global list to keep track of which attachments have been processed

    def get_cc(self):
        return self.msg["cc"]

    def get_bcc(self):
        return self.msg["bcc"]

    def get_raw_content(self):
        if six.PY2:
            return self.msg.as_string()
        else:
            charsets = self.msg.get_charsets()
            for charset in charsets:
                to_try = EmailUtil.validate_charset(charset)
                try:
                    return bytes(self.msg).decode(to_try, errors="replace")
                except:
                    continue

            # Can't figure out the encoding, try utf-8 with ignore, if that fails, it will raise exception
            return bytes(self.msg).decode("utf-8", errors="ignore")

    def get_raw_headers(self):
        return u"\n".join([u"{}: {}".format(unicode(h[0], "utf-8", "ignore"), unicode(h[1], "utf-8", "ignore")) for h in self.msg.items() or []])

    def get_sender(self):
        return EmailUtil.try_decode(self.msg['From']) or u""

    def get_reply_to(self):
        return EmailUtil.try_decode(self.msg["Reply-To"]) or u""

    def get_plaintext_body(self):
        if self.msg.is_multipart():
            for part in self.msg.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))
                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    return part.get_payload(decode=True).decode("utf-8", errors="replace")
        else:
            if self.msg.get_content_type() == "text/plain":
                return self.msg.get_payload(decode=True).decode("utf-8", errors="replace")

        return u""

    def get_html_body(self, decode_html=True):
        if self.msg.is_multipart():
            for part in self.msg.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))
                if ctype == 'text/html' and 'attachment' not in cdispo:
                    # Try decoding HTML Entities
                    body = part.get_payload(decode=True).decode('utf8', errors="replace")
                    if decode_html:
                        return HTMLParser().unescape(body) or u""
                    else:
                        return body or u""
        else:
            if self.msg.get_content_type() == "text/html":
                return self.msg.get_payload(decode=True).decode("utf-8", errors="replace")

        return u""

    def get_rtf_body(self):
        return u""  # Pretty sure EML files can't/shouldn't have rtf bodies

    def get_subject(self):
        return EmailUtil.try_decode(self.msg['Subject']) if self.msg['Subject'] else "(No Subject)"

    def get_type(self):
        return "EML"

    def get_date(self):
        return self.msg['Date'] or ""

    def get_recipients(self):
        return EmailUtil.try_decode(self.msg['To']) or ""

    def get_id(self):
        return self.msg['id'] or self.msg['Message-ID'] or ""

    def get_headers(self):
        parser = email.parser.HeaderParser()
        headers = parser.parsestr(self.get_raw_content()).items()
        return headers if headers else []

    def get_attachments(self):
        """
        Handle the attachments and return strings of 'attachments_md5', 'attachments_sha1' and 'attach_info', the hashed
        data of the attachments, where attach_info is the Content-Type and Content-Transfer-Encoding concatenated
        :return: dictionary with csv values
        """
        raw_attachments = self._organize_attachments(self.msg)
        attachments = EmailAttachmentList()

        for raw_attachment in raw_attachments:
            if six.PY3:
                filename = self._get_attachment_filename(raw_attachment[0], hashlib.md5(raw_attachment[1].encode()).hexdigest())
            else:
                filename = self._get_attachment_filename(raw_attachment[0], hashlib.md5(raw_attachment[1]).hexdigest())

            email_attachment = EmailAttachment(
                u" ".join([u"{}: {}".format(unicode(k, "utf-8", "ignore"), unicode(v, "utf-8", "ignore")) for k, v in raw_attachment[0].items()]),
                filename, raw_attachment[1])

            # Make sure that the attachments aren't the same as the html_body or plaintext_body
            email_attachment.raw_data = email_attachment.raw_data.decode("utf-8", errors="replace")
            bodies = (self.get_html_body(decode_html=False), self.get_plaintext_body(), self.get_rtf_body())
            if email_attachment.raw_data not in bodies:
                attachments.add_attachment(email_attachment)

        return attachments

    @staticmethod
    def _get_attachment_filename(attachment_headers, fallback_name):
        """
        Attempt to get the filename from the content-type information, otherwise just use the fallback name
        :param attachment_headers: List of headers for the attachment
        :param fallback_name: Name to use if we can't find a filename, will be prefixed with unknown-<name>
        :return: filename to use for the attachment
        """
        attachment_headers = {k.lower(): v for k, v in attachment_headers.items()}
        filename = "unknown-{}".format(fallback_name)
        if "content-location" in attachment_headers:
            filename = attachment_headers["content-location"]
        elif 'subject' in attachment_headers:
            filename = "{}.eml".format(attachment_headers['subject'])
        elif "content-type" in attachment_headers:
            properties = attachment_headers["content-type"].split(";")
            for prop in properties:
                prop = prop.strip()  # Strip \t from prop
                if prop.startswith("name") or prop.startswith("filename"):
                    # Split 'name="asdf.png"' into 'asdf.png'
                    fn = re.split("name=\"?", prop)
                    if len(fn) > 1:  # If split failed we can't determine filename
                        fn = fn[1]
                        if fn.endswith("\"") or fn.endswith("\'"):
                            filename = fn[:-1]  # Cut off trailing quote
                    break

        return EmailUtil.try_decode(filename)  # Try and decode filenames that are encoded with mime encoded-word syntax

    @staticmethod
    def _is_attachment(headers):
        """
        Check if a given payload is an attachment (or it's email body)
        Valid from https://www.w3.org/Protocols/rfc1341/5_Content-Transfer-Encoding.html
        :param headers:
        :return:
        """
        if "content-disposition" in headers:
            if headers["content-disposition"].startswith("attachment"):
                return True
        if "content-transfer-encoding" in headers:
            trans_enc = headers["content-transfer-encoding"].lower()
            if trans_enc in ("quoted-printable", "7bit", "8bit"):
                return False
            else:
                return True

    def _organize_attachments(self, eml_obj):
        """
        Organize and filter the attachment data
        :param eml_obj: email object to organize
        :return: List like [[headers, attachment], ...]
        """
        data = self._extract_attachments(eml_obj)  # Recursively extract attachments from EML
        data = filter(lambda x: bool(x), data)  # Filter out the None attachments
        return data

    def _parse_attachment(self, headers, attachment):
        """
        Take in a list of headers and a Message object, and pre-parse the attachment
        Returns None if it isn't an attachment
        :param headers: [(header1, value1), ...]
        :param attachment: Message object to parse
        :return: [{headers}, <attachment raw data>
        """
        lower_headers = {}
        for k, v in headers:
            lower_headers[k.lower()] = v
        if self._is_attachment(lower_headers):
            newdata = self._decode_payload(attachment)
            return [lower_headers, newdata]
        else:
            return None

    def _extract_attachments(self, eml_obj):
        """
        Recursively parse attachments from an email object, keeping track of parsed emails using
        self.seen_attachment_hashes

        :param eml_obj: Message object
        :return: [ [{headers}, <attachment raw data>], ...]
        """
        if hash(eml_obj) in self.seen_attachment_hashes:
            return []
        else:
            data = []
            payload = eml_obj.get_payload()
            # Very specific case of the attached email being an EML that has been parsed into an attachment
            if isinstance(payload, list) and len(payload) == 1 and isinstance(payload[0], email.message.Message)\
                    and isinstance(payload[0].get_payload(), StringTypes):
                attachment = payload[0]
                if not hash(attachment) in self.seen_attachment_hashes:
                    parent_headers = eml_obj.items()
                    child_headers = attachment.items()
                    combined_headers = []  # Combine headers to give us the most information about this possible attachment
                    combined_headers.extend(parent_headers)
                    combined_headers.extend(child_headers)
                    data.append(self._parse_attachment(combined_headers, attachment))
                    self.seen_attachment_hashes.append(hash(attachment))
            elif isinstance(payload, list):
                for attachment in payload:
                    if isinstance(attachment, email.message.Message):
                        # First condition checks whether the attachment is another email
                        # by checking original and new msg ids
                        msg_id = attachment.get('id') or attachment.get('Message-id')
                        if self.get_id() is not msg_id and msg_id is not None:
                            data.append([dict(attachment.items()), str(eml_obj)])
                        elif not hash(attachment) in self.seen_attachment_hashes:
                            data.extend(self._extract_attachments(attachment))
                            self.seen_attachment_hashes.append(hash(attachment))
                        else:
                            continue  # Skip, we've processed this before
                    else:
                        # This shouldn't be an attachment, but in case it is, add it and filter after
                        data.append(self._parse_attachment(eml_obj.items(), attachment))
            elif isinstance(payload, StringTypes):
                data.append(self._parse_attachment(eml_obj.items(), eml_obj))
            else:
                pass
                # Shouldn't ever be here!
        return data

    @staticmethod
    def _decode_payload(attachment):
        """
        Take a given email payload and get the raw unencoded data
        :param attachment: email attachment part
        :return:
        """
        data = attachment.get_payload()
        if data and isinstance(data[0], email.message.Message):
            data = data[0].get_payload()  # Email-ception

        if "content-transfer-encoding" in attachment:
            if attachment["Content-Transfer-Encoding"].lower() == "base64":
                try:
                    data = base64_encode(data)
                except TypeError:
                    data = base64_encode(data, altchars="-_")
        return data
