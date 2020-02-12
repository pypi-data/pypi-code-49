# -*- coding: utf-8 -*-
import sys

from suite_py.lib.handler.captainhook_handler import CaptainHook
from suite_py.lib.logger import Logger

logger = Logger()


def entrypoint(project, action, timeout):
    lock = CaptainHook()
    if timeout:
        lock.set_timeout(timeout)
    if(action in ['lock', 'l']):
        req = lock.lock_project(project)
        handle_request(req)
        logger.info(
            'Bloccato deploy su staging del progetto {}'.format(project))
    elif(action in ['unlock', 'u']):
        req = lock.unlock_project(project)
        handle_request(req)
        logger.info(
            'Abilitato deploy su staging del progetto {}'.format(project))
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
