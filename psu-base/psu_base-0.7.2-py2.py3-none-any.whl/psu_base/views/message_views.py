# message_views.py
#
#   These are views that are used for sending messages to the user
#

from django.shortcuts import render
from psu_base.classes.Log import Log
import time

log = Log()


def messages(request):

    return render(
        request,
        '_components/messages.html',
        {'message_birth_date': int(time.time())}
    )
