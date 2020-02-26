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

  This is the About Dialog.
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from ad1459 import __version__, __license__


class AboutDialog(Gtk.AboutDialog):

    def __init__(self):
        super().__init__()

        self.set_program_name('AD1459')
        self.set_logo_icon_name('in.donotspellitgav.Ad1459')
        self.set_version(__version__.__version__)
        self.set_website('https://github.com/g4vr0che/ad1459')
        self.set_website_label('github.com/g4vr0che/ad1459')
        self.set_copyright('Copyright ©2019-2020 Gaven Royer et al')
        self.set_license(__license__.__license__)
        self.set_wrap_license(True)
        self.set_authors(
            [
                'Gaven Royer'
            ]
        )
