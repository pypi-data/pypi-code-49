import logging

from isc_common.auth.models.abstract_user import AbstractUser

logger = logging.getLogger(__name__)


class User(AbstractUser):

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.middle_name} {self.last_name})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        swappable = 'AUTH_USER_MODEL'
