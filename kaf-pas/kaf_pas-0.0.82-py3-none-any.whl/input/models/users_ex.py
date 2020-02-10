import logging

from isc_common.auth.managers.user_manager import UserManager
from isc_common.auth.models.user import User
from isc_common.number import DelProps

logger = logging.getLogger(__name__)


class Users_exManager(UserManager):

    @staticmethod
    def getRecord(record):
        res = {
            "id": record.id,
            "username": record.username,
            "description": record.description,
            "first_name": record.first_name,
            "last_name": record.last_name,
            "email": record.email,
            "middle_name": record.middle_name,
            "short_name": record.get_short_name,
            "short_name1": record.get_short_name1,
            "password": record.password,
            "last_login": record.last_login,
            "lastmodified": record.lastmodified,
            "location_position": record.location_position,
            "editing": record.editing,
            "deliting": record.deliting,
            "color": record.color,
            "bot": User.props.bot,
        }
        return DelProps(res)


class Users_ex(User):
    objects = Users_exManager()

    @property
    def location_position(self):
        from kaf_pas.input.models.user_add_info import User_add_info
        res = []
        for item in User_add_info.objects.filter(user=self.id):
            res.append(f'{item.location.full_name} : {item.position.name}')
        return ', '.join(res)

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Пользователи с должностями'
        proxy = True
