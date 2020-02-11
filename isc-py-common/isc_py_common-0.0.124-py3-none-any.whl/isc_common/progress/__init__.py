from contextlib import contextmanager

from django.conf import settings
from django.utils import timezone

from isc_common.auth.models.user import User
from isc_common.models.progresses import Progresses
from isc_common.ws.progressStack import ProgressStack


@contextmanager
def managed_progress(qty, user, id, message='Обработано позиций', title='Обработано позиций', props=0):
    progress = Progress(id=id, qty=qty, user=user, message=message, title=title, props=props)
    try:
        yield progress
    except Exception as ex:
        progress.close()
        raise ex
    finally:
        progress.close()


def clean_progresses():
    Progresses.objects.all().delete()


class Progress:
    progress = None

    def __init__(self, qty, user, id, message='Обработано позиций', title='Обработано позиций', props=0):
        self.message = message
        self.title = title
        self.props = props
        self.id = id

        if isinstance(user, int):
            self.user = User.objects.get(id=user)
        elif not isinstance(user, User):
            raise Exception(f'user must be User instance.')
        else:
            self.user = user
        self.qty = qty

        if self.qty > 0:
            channel = f'common_{self.user.username}'
            self.progress = ProgressStack(
                host=settings.WS_HOST,
                port=settings.WS_PORT,
                channel=channel,
                props=self.props,
                user_id=self.user.id
            )

            self.demand_str = f'<h3>{self.message}</h3>'

            self.progress.show(
                cntAll=qty,
                id=self.id,
                label_contents=self.demand_str,
                title=f'<b>{title}</b>',
            )

            self.progresses, created = Progresses.objects.get_or_create(
                id_progress=self.id,
                user=self.user,
                defaults=dict(
                    cnt=0,
                    label_contents=self.demand_str,
                    qty=self.qty,
                    message=self.message,
                    props=self.props,
                    title=self.title,
                    lastmodified=timezone.now()
                )
            )

        self.cnt = 0

    def check_4_exit(self):
        return Progresses.objects.filter(
            id_progress=self.id,
            user=self.user
        ).count() == 0

    def step(self):
        if self.progress != None:
            self.progress.setCntDone(self.cnt, self.id)
            self.cnt += 1
            self.progresses.cnt = self.cnt
            self.progresses.save()

    def setContentsLabel(self, content):
        if self.progress != None:
            self.progress.setContentsLabel(labelContents=content, id=self.id)
            self.progresses.labelContents = content
            self.progresses.save()

    def sendInfo(self, message):
        if self.progress != None:
            self.progress.sendInfo(message=message)

    def sendWarn(self, message):
        if self.progress != None:
            self.progress.sendWarn(message=message)

    def close(self):
        if self.progress != None:
            self.progress.close(self.id)
            self.progresses.delete()
