import logging

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db.models import EmailField, ManyToManyField
from django.utils.translation import gettext_lazy as _

from isc_common.auth.managers.user_manager import UserManager
from isc_common.auth.models.abstract_base_user import AbstractBaseUser
from isc_common.auth.models.usergroup import UserGroup
from isc_common.fields.code_field import CodeField
from isc_common.fields.name_field import NameField
from isc_common.models.audit import AuditModel

logger = logging.getLogger(__name__)


class AbstractUser(AbstractBaseUser, AuditModel):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()

    username = CodeField(verbose_name=_('логин'), unique=True, validators=[username_validator], error_messages={'unique': _("Такой пользователь уже существует."), }, )
    first_name = NameField(verbose_name=_('имя'))
    last_name = NameField(verbose_name=_('фамилия'))
    email = EmailField(verbose_name=_('E-mail'), blank=True, null=True)
    middle_name = NameField(verbose_name=_('отчетво'))
    usergroup = ManyToManyField(UserGroup, verbose_name=_('группы'))

    @property
    def is_admin(self):
        res = False
        for group in self.usergroup.all():
            if group.is_admin:
                res = True
                break
        return res

    @property
    def is_develop(self):
        res = False
        for group in self.usergroup.all():
            if group.is_develop:
                res = True
                break
        return res

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('пользователь')
        verbose_name_plural = _('пользователи')
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s %s' % (self.last_name.strip(), self.first_name.strip(), self.middle_name.strip())
        return full_name

    def get_short_name(self):
        """Return the short name for the user."""
        return self.last_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
