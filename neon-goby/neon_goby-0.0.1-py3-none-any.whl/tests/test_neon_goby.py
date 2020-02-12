import os
import sys
import unittest
import re

import time

from neon_goby import NeonGoby

class NeonGobyTest(unittest.TestCase):
  def test_simple_body(self):
    message = self._get_email('email_basic')

    parsed_message = NeonGoby.parse(message)
    self.assertEqual(1, len(parsed_message))
    self.assertEqual(
      parsed_message[0],
      "You should check it out that i have been supporting your company for the past few years"
    )

  def test_outlook_quote_stripping(self):
    message = self._get_email('email_with_outlook_quote')

    parsed_message = NeonGoby.parse(message)
    self.assertEqual(1, len(parsed_message))
    self.assertEqual(
      parsed_message[0],
      "You should check it out that i have been supporting your company for the past few years"
    )

  def test_gmail_quote_stripping(self):
    message = self._get_email('email_with_gmail_quote')

    parsed_message = NeonGoby.parse(message)
    self.assertEqual(1, len(parsed_message))
    self.assertEqual(
      parsed_message[0],
      "You should check it out that i have been supporting your company for the past few years"
    )
  
  def test_style_stripping(self):
    message = self._get_email('email_with_styles')

    parsed_message = NeonGoby.parse(message)
    self.assertEqual(1, len(parsed_message))
    self.assertEqual(
      parsed_message[0],
      "I am interested"
    )

  def _get_email(self, name):
      """ Return email as text
      """
      with open('tests/emails/%s.html' % name) as f:
          text = f.read()
      return text
