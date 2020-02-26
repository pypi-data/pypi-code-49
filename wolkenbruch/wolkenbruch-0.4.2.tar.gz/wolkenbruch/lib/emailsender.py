#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Copyright (C) 2019 Christoph Fink, University of Helsinki
#
#   This program is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation; either version 3
#   of the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, see <http://www.gnu.org/licenses/>.

""" Sends e-mails (convenience wrapper around `smtplib` and `email.message` """


import email.message
import smtplib


__all__ = [
    "EMailSender"
]


class EMailSender:
    """ Sends e-mails

        Args:
            from_addr:  Sender address
            to_addr:    Receiver address
            subject:    Subject line
            body:       e-mail text
            smtp_host:  host name/ip address to use as an SMTP server,
                        can contain port in the form [host]:[port]
            smtp_user:  SMTP user name if authentication required
            smtp_password: SMTP password if authentication required
            starttls:   use TLS (default: True)
    """

    def __init__(
            self,
            from_addr="",
            to_addr="",
            subject="",
            body="",
            smtp_host="",
            smtp_user="",
            smtp_password="",
            starttls=True,
            *args,
            **kwargs
    ):
        """
            Sends e-mails

            Args:
                from_addr:  Sender address
                to_addr:    Receiver address
                subject:    Subject line
                body:       e-mail text
                smtp_host:  host name/ip address to use as an SMTP server,
                            can contain port in the form [host]:[port]
                smtp_user:  SMTP user name if authentication required
                smtp_password: SMTP password if authentication required
                starttls:   use TLS (default: True)
        """
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.body = body

        self.smtp_host = smtp_host
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password
        self.starttls = starttls

    def send_message(self):
        """ Sends a message to `to_addr` """
        with smtplib.SMTP(self.smtp_host) as smtp:
            if self.starttls:
                smtp.starttls()
            if (
                    self.smtp_user != "" and
                    self.smtp_password != ""
            ):
                smtp.login(
                    self.smtp_user,
                    self.smtp_password
                )

            message = email.message.EmailMessage()
            message["From"] = self.from_addr
            message["To"] = self.to_addr
            message["Subject"] = self.subject
            message.set_content(self.body)

            smtp.send_message(message)
