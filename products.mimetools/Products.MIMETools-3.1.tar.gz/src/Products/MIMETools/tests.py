##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################

import base64
import email
import unittest

import six

from DocumentTemplate.DT_Util import ParseError


class MimeTest(unittest.TestCase):

    def _getTargetClass(self):
        from Products.MIMETools import MIMETag
        return MIMETag.MIMETag

    def _makeOne(self, blocks=[]):
        klass = self._getTargetClass()
        return klass(blocks)

    def _decode64(self, text):
        if six.PY3 and isinstance(text, str):
            text = text.encode('utf-8')
        try:
            return base64.decodebytes(text)
        except AttributeError:
            return base64.decodestring(text)

    @property
    def doc_class(self):
        from DocumentTemplate.DT_HTML import HTML
        return HTML

    def test_registered(self):
        klass = self._getTargetClass()
        from DocumentTemplate.DT_String import String
        self.assertTrue('mime' in String.commands)
        self.assertTrue(String.commands['mime'] is klass)

    def test_init(self):
        tag = self._makeOne()
        self.assertEqual(tag.sections, [])

    def test_render(self):
        tag = self._makeOne()
        result = tag.render(md={})
        self.assertIn('MIME-Version: 1.0', result)
        self.assertIn('Content-Type: multipart/mixed;', result)

    def test_call(self):
        tag = self._makeOne()
        result = tag(md={})
        self.assertIn('MIME-Version: 1.0', result)
        self.assertIn('Content-Type: multipart/mixed;', result)

    def test_text(self):
        html = self.doc_class(
            '<dtml-mime type="text/html" charset="utf-8">'
            '<b>I am BOLD</b>'
            '<dtml-boundary type="text/plain">'
            'Just plain text'
            '<dtml-boundary type="text/css" disposition="attachment" '
            '               filename="my.css" name="my" charset="iso8859-1" '
            '               cid="CID">'
            'All bells and whistles'
            '<dtml-boundary skip_expr="1==1">'
            'You cannot see me'
            '</dtml-mime>')

        msg = email.message_from_string(html(md={}))
        self.assertTrue(msg.is_multipart())

        parts = msg.get_payload()
        self.assertEqual(len(parts), 3)

        part1 = parts[0]
        self.assertFalse(part1.is_multipart())
        self.assertEqual(part1['Content-Type'],
                         'text/html; charset="utf-8"')
        self.assertEqual(part1['MIME-Version'], '1.0')
        self.assertEqual(part1['Content-Transfer-Encoding'], 'base64')
        self.assertEqual(self._decode64(part1.get_payload()),
                         b'<b>I am BOLD</b>')

        part2 = parts[1]
        self.assertFalse(part2.is_multipart())
        self.assertEqual(part2['Content-Type'],
                         'text/plain; charset="us-ascii"')
        self.assertEqual(part2['MIME-Version'], '1.0')
        self.assertEqual(part2['Content-Transfer-Encoding'], '7bit')
        self.assertEqual(part2.get_payload(), 'Just plain text')

        part3 = parts[2]
        self.assertFalse(part3.is_multipart())
        self.assertEqual(part3['Content-Type'],
                         'text/css; charset="iso8859-1"')
        self.assertEqual(part3['MIME-Version'], '1.0')
        self.assertEqual(part3['Content-Transfer-Encoding'], 'base64')
        self.assertEqual(part3['Content-ID'], '<CID>')
        self.assertEqual(part3['Content-Disposition'],
                         'attachment;\n filename="my.css"')
        self.assertEqual(self._decode64(part3.get_payload()),
                         b'All bells and whistles')

    def test_other(self):
        html = self.doc_class(
            '<dtml-mime>'
            '<b>I am BOLD</b>'
            '<dtml-boundary type="dont/know">'
            'Just plain text'
            '<dtml-boundary type="application/js" disposition="attachment" '
            '               filename="my.js" name="my" '
            '               encode="quoted-printable" cid="CID">'
            'All bells and whistles'
            '</dtml-mime>')

        msg = email.message_from_string(html(md={}))
        self.assertTrue(msg.is_multipart())

        parts = msg.get_payload()
        self.assertEqual(len(parts), 3)

        part1 = parts[0]
        self.assertFalse(part1.is_multipart())
        self.assertEqual(part1['Content-Type'],
                         'application/octet-stream')
        self.assertEqual(part1['MIME-Version'], '1.0')
        self.assertEqual(part1['Content-Transfer-Encoding'], 'base64')
        self.assertEqual(self._decode64(part1.get_payload()),
                         b'<b>I am BOLD</b>')

        part2 = parts[1]
        self.assertFalse(part2.is_multipart())
        self.assertEqual(part2['Content-Type'], 'application/octet-stream')
        self.assertEqual(part2['MIME-Version'], '1.0')
        self.assertEqual(part2['Content-Transfer-Encoding'], 'base64')
        self.assertEqual(self._decode64(part2.get_payload()),
                         b'Just plain text')

        part3 = parts[2]
        self.assertFalse(part3.is_multipart())
        self.assertEqual(part3['Content-Type'], 'application/js')
        self.assertEqual(part3['MIME-Version'], '1.0')
        self.assertEqual(part3['Content-Transfer-Encoding'],
                         'quoted-printable')
        self.assertEqual(part3['Content-ID'], '<CID>')
        self.assertEqual(part3['Content-Disposition'],
                         'attachment;\n filename="my.js"')
        self.assertEqual(part3.get_payload(),
                         'All=20bells=20and=20whistles')

    def test_bad_encoding(self):
        from .MIMETag import MIMEError
        broken = '<dtml-mime type="image/jpg" encode="foo"></dtml-mime>'
        html = self.doc_class(broken)
        with self.assertRaises(MIMEError) as cm:
            html()
        self.assertIn('unsupported encoding', str(cm.exception))

    def test_forbidden_combined_attributes(self):
        broken = '<dtml-mime type="x" type_expr="y"></dtml-mime>'
        html = self.doc_class(broken)
        with self.assertRaises(ParseError) as cm:
            html()
        self.assertIn('type and type_expr given', str(cm.exception))

        broken = ('<dtml-mime disposition="x" '
                  'disposition_expr="y"></dtml-mime>')
        html = self.doc_class(broken)
        with self.assertRaises(ParseError) as cm:
            html()
        self.assertIn('disposition and disposition_expr given',
                      str(cm.exception))

        broken = '<dtml-mime encode="x" encode_expr="y"></dtml-mime>'
        html = self.doc_class(broken)
        with self.assertRaises(ParseError) as cm:
            html()
        self.assertIn('encode and encode_expr given', str(cm.exception))

        broken = '<dtml-mime name="x" name_expr="y"></dtml-mime>'
        html = self.doc_class(broken)
        with self.assertRaises(ParseError) as cm:
            html()
        self.assertIn('name and name_expr given', str(cm.exception))

        broken = '<dtml-mime filename="x" filename_expr="y"></dtml-mime>'
        html = self.doc_class(broken)
        with self.assertRaises(ParseError) as cm:
            html()
        self.assertIn('filename and filename_expr given', str(cm.exception))

        broken = '<dtml-mime cid="x" cid_expr="y"></dtml-mime>'
        html = self.doc_class(broken)
        with self.assertRaises(ParseError) as cm:
            html()
        self.assertIn('cid and cid_expr given', str(cm.exception))

        broken = '<dtml-mime charset="x" charset_expr="y"></dtml-mime>'
        html = self.doc_class(broken)
        with self.assertRaises(ParseError) as cm:
            html()
        self.assertIn('charset and charset_expr given', str(cm.exception))


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MimeTest))
    return suite
