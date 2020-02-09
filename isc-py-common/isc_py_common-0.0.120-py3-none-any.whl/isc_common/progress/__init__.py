from django.conf import settings

from isc_common.auth.models.user import User
from isc_common.ws.progressStack import ProgressStack


class Progress:
    progress = None
    def __init__(self, qty, user, id, message='Обработано позиций', title='Обработано позиций'):
        self.message = message
        self.title = title

        if isinstance(user, int):
            self.user = User.objects.get(id=user)
        elif not isinstance(user, User):
            raise Exception(f'user must be User instance.')
        else:
            self.user = user
        self.qty = qty

        if self.qty > 0:
            self.progress = ProgressStack(
                host=settings.WS_HOST,
                port=settings.WS_PORT,
                channel=f'common_{self.user.username}',
            )

            self.id_progress = f'document_{id}'
            demand_str = f'<h3>{self.message}</h3>'

            self.progress.show(
                title=f'<b>{title}</b>',
                label_contents=demand_str,
                cntAll=qty,
                id=self.id_progress
            )

        self.cnt = 0

    def step(self):
        if self.progress != None:
            self.progress.setCntDone(self.cnt, self.id_progress)
            self.cnt += 1

    def setContentsLabel(self, content):
        if self.progress != None:
            self.progress.setContentsLabel(labelContents=content, id=self.id_progress)

    def sendInfo(self, message):
        if self.progress != None:
            self.progress.sendInfo(message=message)

    def sendWarn(self, message):
        if self.progress != None:
            self.progress.sendWarn(message=message)

    def close(self):
        if self.progress != None:
            self.progress.close(self.id_progress)
