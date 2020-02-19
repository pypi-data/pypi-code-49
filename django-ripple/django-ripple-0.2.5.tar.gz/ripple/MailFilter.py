
from django.conf import settings
from django.core import mail
from django.core.mail import send_mail, backends
from django.core.mail import EmailMultiAlternatives
import re
import logging

logger = logging.getLogger(__name__)

ALLOW_EXP = settings.EMAIL_ALLOW_EXP and [
    re.compile(e) for e in settings.EMAIL_ALLOW_EXP.split(' ')]
BLOCK_EXP = settings.EMAIL_BLOCK_EXP and [
    re.compile(e) for e in settings.EMAIL_BLOCK_EXP.split(' ')]


def filter_email(from_email, recipient_list):

    recp1 = []
    recp2 = []

    if settings.EMAIL_FORCE_SENDER:
        from_email = settings.EMAIL_FORCE_SENDER

    if from_email is None or from_email == "":
        from_email = settings.EMAIL_DEFAULT_SENDER
    if ALLOW_EXP and len(ALLOW_EXP) > 0:
        for r in recipient_list:
            append = False
            for e in ALLOW_EXP:
                if e and e.match(r):
                    append = True
            if append:

                recp1.append(r)
            else:
                logger.info('%s filtered by ALLOW_EXP: %s' %
                            (r, settings.EMAIL_ALLOW_EXP))

    else:
        recp1 = recipient_list

    if BLOCK_EXP and len(BLOCK_EXP) > 0:
        for r in recp1:
            block = False

            for e in BLOCK_EXP:
                if e and e.match(r):
                    block = True
            if not block:
                recp2.append(r)
            else:
                logger.info('%s blocked by BLOCK_EXP: %s' %
                            (r, settings.EMAIL_BLOCK_EXP))

    else:
        recp2 = recp1

    return from_email, recp2


def filtered_send_mail(
    subject,
    text_message,
    from_email,
    recipient_list,
    fail_silently=False,
    auth_user=None,
    auth_password=None,
    connection=None,
    html_message=None,
    sg_template_id=None,
    sg_context=None,
    sg_substitutions=None
):
    # TODO red attachments
    from_email, recp2 = filter_email(from_email, recipient_list)
    emails = []
    for to_email in recp2:
        # https://docs.djangoproject.com/en/2.2/topics/email/#sending-alternative-content-types
        email = EmailMultiAlternatives(
            subject, text_message, from_email, [to_email])
        if html_message:
            email.attach_alternative(html_message, 'text/html')

        if sg_template_id:
            email.template_id = sg_template_id

        if sg_context:
            email.dynamic_template_data = sg_context

        if sg_substitutions:
            email.substitutions = sg_substitutions

        emails.append(email)
    if len(emails):

        connection = mail.get_connection(fail_silently=fail_silently)
        connection.send_messages(emails)

        return emails
