##############################################################################
#
# Copyright (c) 2002 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################

from email.encoders import encode_7or8bit
from email.encoders import encode_base64
from email.encoders import encode_quopri
from email.mime.application import MIMEApplication
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import BytesIO
from io import StringIO

import six

from DocumentTemplate._DocumentTemplate import render_blocks
from DocumentTemplate.DT_String import String
from DocumentTemplate.DT_Util import Eval
from DocumentTemplate.DT_Util import ParseError
from DocumentTemplate.DT_Util import parse_params


if six.PY2:
    outfile = BytesIO
else:
    outfile = StringIO
TYPE_CLASSES = {
    'text': MIMEText,
    'image': MIMEImage,
    'audio': MIMEAudio,
    'application': MIMEApplication,
}
ENCODINGS = {
    '7bit': encode_7or8bit,
    '8bit': encode_7or8bit,
    'base64': encode_base64,
    'quoted-printable': encode_quopri,
}


class MIMEError(Exception):
    """MIME Tag Error"""


class MIMETag(object):
    """ The dtml-mime tag """

    name = 'mime'
    blockContinuations = ('boundary',)
    encode = None

    def __init__(self, blocks, encoding=None):
        self.encoding = encoding
        self.sections = []
        self.multipart = 'mixed'

        for tname, args, section in blocks:
            if tname == 'mime':
                args = parse_params(args, type=None, type_expr=None,
                                    disposition=None, disposition_expr=None,
                                    encode=None, encode_expr=None, name=None,
                                    name_expr=None, filename=None,
                                    filename_expr=None, cid=None,
                                    cid_expr=None, charset=None,
                                    charset_expr=None, skip_expr=None,
                                    multipart=None)
                self.multipart = args.get('multipart', 'mixed')
            else:
                args = parse_params(args, type=None, type_expr=None,
                                    disposition=None, disposition_expr=None,
                                    encode=None, encode_expr=None, name=None,
                                    name_expr=None, filename=None,
                                    filename_expr=None, cid=None,
                                    cid_expr=None, charset=None,
                                    charset_expr=None, skip_expr=None)

            if 'type_expr' in args:
                if 'type' in args:
                    raise ParseError('dtml-mime: type and type_expr given')
                args['type_expr'] = Eval(args['type_expr'])
            elif 'type' not in args:
                args['type'] = 'application/octet-stream'

            if 'disposition_expr' in args:
                if 'disposition' in args:
                    raise ParseError(
                        'dtml-mime: disposition and disposition_expr given')
                args['disposition_expr'] = Eval(args['disposition_expr'])
            elif 'disposition' not in args:
                args['disposition'] = ''

            if 'encode_expr' in args:
                if 'encode' in args:
                    raise ParseError('dtml-mime: encode and encode_expr given')
                args['encode_expr'] = Eval(args['encode_expr'])
            elif 'encode' not in args:
                args['encode'] = 'base64'

            if 'name_expr' in args:
                if 'name' in args:
                    raise ParseError('dtml-mime: name and name_expr given')
                args['name_expr'] = Eval(args['name_expr'])
            elif 'name' not in args:
                args['name'] = ''

            if 'filename_expr' in args:
                if 'filename' in args:
                    raise ParseError(
                        'dtml-mime: filename and filename_expr given')
                args['filename_expr'] = Eval(args['filename_expr'])
            elif 'filename' not in args:
                args['filename'] = ''

            if 'cid_expr' in args:
                if 'cid' in args:
                    raise ParseError('dtml-mime: cid and cid_expr given')
                args['cid_expr'] = Eval(args['cid_expr'])
            elif 'cid' not in args:
                args['cid'] = ''

            if 'charset_expr' in args:
                if 'charset' in args:
                    raise ParseError(
                        'dtml-mime: charset and charset_expr given')
                args['charset_expr'] = Eval(args['charset_expr'])
            elif 'charset' not in args:
                args['charset'] = 'us-ascii'  # Default for text parts

            if 'skip_expr' in args:
                args['skip_expr'] = Eval(args['skip_expr'])

            if args['encode'] not in ENCODINGS:
                raise MIMEError('An unsupported encoding was specified in tag')

            self.sections.append((args, section.blocks))

    def render(self, md):
        outer = MIMEMultipart(self.multipart)

        for (args, blocks) in self.sections:
            if 'skip_expr' in args and args['skip_expr'].eval(md):
                continue

            if 'type_expr' in args:
                typ = args['type_expr'].eval(md)
            else:
                typ = args['type']

            if 'disposition_expr' in args:
                disposition = args['disposition_expr'].eval(md)
            else:
                disposition = args['disposition']

            if 'encode_expr' in args:
                encode = args['encode_expr'].eval(md)
            else:
                encode = args['encode']

            if 'filename_expr' in args:
                filename = args['filename_expr'].eval(md)
            else:
                filename = args['filename']

            if 'cid_expr' in args:
                cid = args['cid_expr'].eval(md)
            else:
                cid = args['cid']

            if 'charset_expr' in args:
                charset = args['charset_expr'].eval(md)
            else:
                charset = args['charset']

            maintype, subtype = [x.lower() for x in typ.split('/')]
            if maintype not in TYPE_CLASSES:
                maintype = 'application'
                subtype = 'octet-stream'

            klass = TYPE_CLASSES.get(maintype, MIMEApplication)
            data = render_blocks(blocks, md)

            if maintype == 'text':
                inner = klass(data, _subtype=subtype, _charset=charset)
            else:
                inner = klass(data, _subtype=subtype,
                              _encoder=ENCODINGS.get(encode))

            if cid:
                inner.add_header('Content-ID', '<%s>' % cid)

            if disposition:
                if filename:
                    inner.add_header('Content-Disposition',
                                     '%s;\n filename="%s"' % (disposition,
                                                              filename))
                else:
                    inner.add_header('Content-Disposition', disposition)

            outer.attach(inner)

        return outer.as_string()

    __call__ = render


String.commands['mime'] = MIMETag
