#!/usr/bin/env python3

""" AD1459, an IRC Client

  Copyright ©2019-2020 by Gaven Royer

  Permission to use, copy, modify, and/or distribute this software for any
  purpose with or without fee is hereby granted, provided that the above
  copyright notice and this permission notice appear in all copies.

  THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH REGARD
  TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
  FITNESS. IN NO EVENT SHALL ISC BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
  CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
  DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
  ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
  SOFTWARE.

  A parser for IRC style tags.
"""

import logging
from urllib.parse import urlparse

class Parser:
    """ This is a text formatting helper class.

    It aids with IRC formatting as well as providing Pango markup to the 
    interface for label widgets.
    """

    formatting = {
        '\x02': ['b', '*'],
        #'\u0003': 'color',
        #'\u000F': 'clear',
        '\x1D': ['i', '_'],
        '\x1F': ['u', '-']
    }

    def __init__(self):
        self.log = logging.getLogger('ad1459.formatting')
    
    def format_text(self, text):
        for i in self.formatting:
            # text = text.replace(f'/{self.formatting[i][0]}', i)
            text = text.replace(f'/{self.formatting[i][1]}', i)
        return text
    
    def sanitize_message(self, message):
        """ Strips IRC formatting from a message to make it suitable for display
        outside of the client, e.g. in notifications.

        Arguments:
            message (str): The message to clean up.

        Returns:
            str: The cleaned message.
        """
        formatting_chars = [
            '\x02', # bold
            '\x1D', # italics
            '\x1F', # underline
            '\x1E', # strikethrough
            '\x11'
        ]

        for fchar in formatting_chars:
            message = message.replace(fchar, '')
        
        return message

    def parse_text(self, text):        
        # \u0002 bold
        # \u0003 colour
        # \u000F cancel all
        # \u001D italic
        # \u001F underline
        text = self.fix_markedup_tags(text)
        f_text = ''
        current_tags = []

        for char in text:
            if char in self.formatting:

                if not char in current_tags:
                    for tag in reversed(current_tags):
                        f_text = f'{f_text}</{self.formatting[tag][0]}>'

                    current_tags.append(char)
                    for tag in current_tags:
                        f_text = f'{f_text}<{self.formatting[tag][0]}>'

                else:
                    for tag in reversed(current_tags):
                        f_text = f'{f_text}</{self.formatting[tag][0]}>'

                    current_tags.pop()
                    for tag in current_tags:
                        f_text = f'{f_text}<{self.formatting[tag][0]}>'

            else: 
                f_text = f'{f_text}{char}'
        
        for tag in reversed(current_tags):
            f_text = f'{f_text}</{self.formatting[tag][0]}>'

        return f_text
    
    def hyperlinks(self, text):
        words = text.split()

        linked_words = []
        for word in words:
            stripped = word.replace('/u000A', '')
            scheme = urlparse(stripped).scheme
            if scheme == 'http' or scheme == 'https':
                paren = False
                if word.endswith(')'):
                    word = word.strip(')')
                    paren = True
                word = f'<a href="{stripped}">{word}</a>'
                if paren:
                    word = f'{word})'
            linked_words.append(word)
        return " ".join(linked_words)

    def fix_markedup_tags(self, text):
        mu_formatting = {
            '&#x2;': '\x02',
            #'\u0003': #'\u0003',
            #'\u000F': #'\u000F',
            '&#x1d;': '\x1D',
            '&#x1f;': '\x1F'
        }

        for i in mu_formatting:
            text = text.replace(i, mu_formatting[i])
        
        return text