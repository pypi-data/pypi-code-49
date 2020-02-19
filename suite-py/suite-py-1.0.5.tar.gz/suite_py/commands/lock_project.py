# -*- coding: utf-8 -*-
import sys
import requests

from suite_py.lib.handler.captainhook_handler import CaptainHook
from suite_py.lib.logger import Logger

logger = Logger()


def entrypoint(project, action, timeout):
    lock = CaptainHook()
    if timeout:
        lock.set_timeout(timeout)
    if action in ["lock", "l"]:
        try:
            req = lock.lock_project(project)
            handle_request(req)
            logger.info(f"Bloccato deploy su staging del progetto {project}")
        except requests.exceptions.Timeout:
            logger.warning("Richiesta a Captainhook in timeout. Prova con suite-py --timeout=60 lock-project lock")
            sys.exit(1)
    elif action in ["unlock", "u"]:
        try:
            req = lock.unlock_project(project)
            handle_request(req)
            logger.info(f"Abilitato deploy su staging del progetto {project}")
        except requests.exceptions.Timeout:
            logger.warning("Richiesta a Captainhook in timeout. Prova con suite-py --timeout=60 lock-project unlock")
            sys.exit(1)
    else:
        logger.warning("Non ho capito che cosa devo fare")
        sys.exit(-1)


def handle_request(request):
    if request.status_code == 401:
        logger.error("Impossibie contattare captainhook, stai usando la VPN?")
        sys.exit(-1)
    if request.status_code == 500:
        logger.error(
            "Si è verificato un errore su captainhook. Chiedi ai devops di verificare (X_X)"
        )
        sys.exit(-1)
    if request.status_code != 200:
        logger.error("Qualcosa è andato storto durante la richiesta.")
        sys.exit(-1)

    return True
