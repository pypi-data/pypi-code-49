#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from ..lib.handler.captainhook_handler import CaptainHook
from ..lib.logger import Logger
import sys

logger = Logger()
lock = CaptainHook()


def entrypoint(args):
    if(args.action in ['lock', 'l']):
        req = lock.lock_project(args.project)
        handle_request(req)
        logger.info(
            'Bloccato deploy su staging del progetto {}'.format(args.project))
    elif(args.action in ['unlock', 'u']):
        req = lock.unlock_project(args.project)
        handle_request(req)
        logger.info(
            'Abilitato deploy su staging del progetto {}'.format(args.project))
    else:
        logger.warning('Non ho capito che cosa devo fare')
        sys.exit(-1)


def handle_request(request):
    if request.status_code == 401:
        logger.error("Impossibie contattare captainhook, stai usando la VPN?")
        sys.exit(-1)
    if request.status_code == 500:
        logger.error("Si è verificato un errore su captainhook. Chiedi ai devops di verificare (X_X)")
        sys.exit(-1)
    if request.status_code != 200:
        logger.error("Qualcosa è andato storto durante la richiesta.")
        sys.exit(-1)

    return True
