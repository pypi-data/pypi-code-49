#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Maxime “pep” Buquet <pep@bouah.net>
#
# Distributed under terms of the GPLv3 license.

"""
    OMEMO Plugin.
"""

import os
import asyncio
import logging
from typing import Dict, List, Optional

from poezio.plugin_e2ee import E2EEPlugin
from poezio.xdg import DATA_HOME
from poezio.tabs import ChatTab, DynamicConversationTab, StaticConversationTab, MucTab

from omemo.exceptions import MissingBundleException
from slixmpp import JID
from slixmpp.stanza import Message
from slixmpp.exceptions import IqError, IqTimeout
from slixmpp_omemo import PluginCouldNotLoad, MissingOwnKey, NoAvailableSession
from slixmpp_omemo import UndecidedException, UntrustedException, EncryptionPrepareException
import slixmpp_omemo

log = logging.getLogger(__name__)


class Plugin(E2EEPlugin):
    """OMEMO (XEP-0384) Plugin"""

    encryption_name = 'omemo'
    eme_ns = slixmpp_omemo.OMEMO_BASE_NS
    replace_body_with_eme = True
    stanza_encryption = False

    encrypted_tags = [
        (slixmpp_omemo.OMEMO_BASE_NS, 'encrypted'),
    ]

    # TODO: Look into blind trust stuff.
    # https://gist.github.com/mar-v-in/b683220a55bc65dcdafc809be9c5d0e4
    trust_states = {
        'accepted': {
            'verified',
            'accepted',
        }, 'rejected': {
            'undecided',
            'distrusted',
        },
    }
    supported_tab_types = (DynamicConversationTab, StaticConversationTab, MucTab)

    def init(self) -> None:
        super().init()

        self.info = lambda i: self.api.information(i, 'Info')

        data_dir = os.path.join(DATA_HOME, 'omemo', self.core.xmpp.boundjid.bare)
        os.makedirs(data_dir, exist_ok=True)

        try:
            self.core.xmpp.register_plugin(
                'xep_0384', {
                    'data_dir': data_dir,
                },
                module=slixmpp_omemo,
            ) # OMEMO
        except (PluginCouldNotLoad,):
            log.exception('And error occured when loading the omemo plugin.')

        asyncio.ensure_future(
            self.core.xmpp['xep_0384'].session_start(self.core.xmpp.boundjid)
        )

    def display_error(self, txt) -> None:
        self.api.information(txt, 'Error')

    def get_fingerprints(self, jid: JID) -> List[str]:
        devices = self.core.xmpp['xep_0384'].get_trust_for_jid(jid)

        # XXX: What to do with did -> None entries?
        # XXX: What to do with the active/inactive devices differenciation?
        # For now I'll merge both. We should probably display them separately
        # later on.
        devices['active'].update(devices['inactive'])
        return [
            slixmpp_omemo.fp_from_ik(trust['key'])
            for trust in devices['active'].values()
            if trust is not None
        ]

    def decrypt(self, message: Message, jid: Optional[JID], tab: ChatTab) -> None:

        if jid is None:
            self.display_error('Unable to decrypt the message.')
            return None

        body = None
        try:
            encrypted = message['omemo_encrypted']
            body = self.core.xmpp['xep_0384'].decrypt_message(
                encrypted,
                jid,
                # Always decrypt. Let us handle how we then warn the user.
                allow_untrusted=True,
            )
            body = body.decode('utf-8')
        except (MissingOwnKey,):
            # The message is missing our own key, it was not encrypted for
            # us, and we can't decrypt it.
            self.display_error(
                'I can\'t decrypt this message as it is not encrypted for me.'
            )
        except (NoAvailableSession,) as exn:
            # We received a message from that contained a session that we
            # don't know about (deleted session storage, etc.). We can't
            # decrypt the message, and it's going to be lost.
            # Here, as we need to initiate a new encrypted session, it is
            # best if we send an encrypted message directly. XXX: Is it
            # where we talk about self-healing messages?
            self.display_error(
                'I can\'t decrypt this message as it uses an encrypted '
                'session I don\'t know about.',
            )
        except (EncryptionPrepareException,):
            # Slixmpp tried its best, but there were errors it couldn't
            # resolve. At this point you should have seen other exceptions
            # and given a chance to resolve them already.
            self.display_error('I was not able to decrypt the message.')
        except (Exception,) as exn:
            self.display_error('An error occured while attempting decryption.\n%r' % exn)
            raise

        if body is not None:
            message['body'] = body

    async def encrypt(self, message: Message, jids: Optional[List[JID]], _tab) -> None:
        if jids is None:
            self.display_error('Unable to encrypt the message.')
            return None

        body = message['body']
        expect_problems = {}  # type: Optional[Dict[JID, List[int]]]

        while True:
            try:
                # `encrypt_message` excepts the plaintext to be sent, a list of
                # bare JIDs to encrypt to, and optionally a dict of problems to
                # expect per bare JID.
                #
                # Note that this function returns an `<encrypted/>` object,
                # and not a full Message stanza. This combined with the
                # `recipients` parameter that requires for a list of JIDs,
                # allows you to encrypt for 1:1 as well as groupchats (MUC).
                recipients = jids
                encrypt = await self.core.xmpp['xep_0384'].encrypt_message(
                    body,
                    recipients,
                    expect_problems,
                )
                message.append(encrypt)
                return None
            except UndecidedException as exn:
                # The library prevents us from sending a message to an
                # untrusted/undecided barejid, so we need to make a decision here.
                # This is where you prompt your user to ask what to do. In
                # this bot we will automatically trust undecided recipients.
                self.core.xmpp['xep_0384'].trust(exn.bare_jid, exn.device, exn.ik)
            # TODO: catch NoEligibleDevicesException
            except EncryptionPrepareException as exn:
                log.debug('FOO: EncryptionPrepareException: %r', exn.errors)
                for error in exn.errors:
                    if isinstance(error, MissingBundleException):
                        self.display_error(
                            'Could not find keys for device "%d" of recipient "%s". Skipping.' %
                            (error.device, error.bare_jid),
                        )
                        jid = JID(error.bare_jid)
                        device_list = expect_problems.setdefault(jid, [])
                        device_list.append(error.device)
            except (IqError, IqTimeout) as exn:
                self.display_error(
                    'An error occured while fetching information on a recipient.\n%r' % exn,
                )
                return None

        return None
