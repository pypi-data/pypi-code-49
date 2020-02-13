from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _


from .auth import generate_verify_email_token
from .MailFilter import filtered_send_mail

# remove username from the default django user model. (Creating a custom user model based on the original django model)
# email is used as the unique account 'username'


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now,
                          is_email_verified=False, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(
        null=True,
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message=(_(
                    "Phone number format must be entered in the format: (+)9999999 with optional international code e.g (+4499999). Between 8 and 15 digits allowed."
                ))
            )
        ]
    )
    profile_pic = models.ImageField(blank=True, null=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    is_email_verified = models.BooleanField(_('email verified'), default=False,
                                            help_text=_('Designates whether email has been verified '))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def send_verification_email(self):

        token = generate_verify_email_token(self.id, self.email)
        SG_TEMPLATE_ID = "d-f45aba387d824c15a5d6a9b4e97646b7"

        sg_context = {
            'first_name': self.first_name,
            'email': self.email,
            'last_name': self.last_name,
            'verify_url': f"{settings.SITE_URL}/account/verify?token={token}"
        }

        return filtered_send_mail(
            '_',
            '_',
            'info@rippleenergy.com',
            [self.email],
            html_message='_',
            sg_template_id=SG_TEMPLATE_ID,
            sg_context=sg_context
        )

    def send_sign_up_email(self):

        try:

            token = generate_verify_email_token(self.id, self.email)

            template_params = {
                'user': self,
                'url': '%s/account/verify?token=%s' % (settings.SITE_URL, token),
            }

            msg_plain = render_to_string(
                'user_signup_email.txt', template_params)
            msg_html = render_to_string(
                'user_signup_email.html', template_params)

            # TODO how does __rippleweb___ work?

            filtered_send_mail(
                'Welcome to ___rippleweb___',
                msg_plain,
                'support@example.com',
                [self.email],
                html_message=msg_html,
                fail_silently=False,
            )
        except Exception as ex:
            # TODO red log email send failure
            pass

    def send_password_reset_email(self):

        uidb64 = urlsafe_base64_encode(force_bytes(self.pk)).decode()
        token = default_token_generator.make_token(self)

        url = f"{settings.SITE_URL}/account/reset-password-confirm"
        url += f"?uidb64={uidb64}&token={token}"

        SG_TEMPLATE_ID = "d-d56fbf35e1f247ddb7f7f2c372bdea44"

        sg_context = {
            'first_name': self.first_name,
            'url': url
        }

        filtered_send_mail(
            '_',
            '_',
            'support@rippleenergy.com',
            [self.email],
            html_message='_',
            sg_template_id=SG_TEMPLATE_ID,
            sg_context=sg_context
        )

    def send_password_reset_confirmed_email(self):
        # sends a confirmation to someone that their password has been changed
        # TODO red
        pass


class RippleBase(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AssetBase(RippleBase):

    class Meta:
        abstract = True

    assetid = models.CharField(max_length=200, db_index=True)
    module = models.CharField(
        max_length=200, blank=True, default="", db_index=True)
    version = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.assetid


class TextAsset(AssetBase):

    text = models.CharField(max_length=1000, blank=True, default="")


class RichTextAsset(AssetBase):

    text = models.TextField(blank=True, default="")


class ImageAsset(AssetBase):

    target = models.CharField(max_length=200, default="", db_index=True)
    image = models.ImageField()


class Article(AssetBase):

    layout = models.CharField(
        max_length=200, blank=True, default="", db_index=True)
    image = models.ForeignKey(ImageAsset, on_delete=models.CASCADE)
    text = models.ForeignKey(RichTextAsset, on_delete=models.CASCADE)
    title = models.ForeignKey(TextAsset, on_delete=models.CASCADE)


class ArticleCollection(AssetBase):

    layout = models.CharField(
        max_length=200, blank=True, default="", db_index=True)

    image = models.ForeignKey(ImageAsset, on_delete=models.CASCADE)
    text = models.ForeignKey(RichTextAsset, on_delete=models.CASCADE)
    title = models.ForeignKey(TextAsset, on_delete=models.CASCADE)

    articles = models.ManyToManyField(Article, through='ArticleOrder')
    article_collections = models.ManyToManyField('ArticleCollection', through='ArticleCollectionOrder',
                                                 through_fields=('container_article_collection', 'article_collection'))


class ArticleOrder(models.Model):

    article_collection = models.ForeignKey(
        ArticleCollection, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    order = models.IntegerField()


class ArticleCollectionOrder(models.Model):

    container_article_collection = models.ForeignKey(
        ArticleCollection, related_name="container_articles", on_delete=models.CASCADE)
    article_collection = models.ForeignKey(
        ArticleCollection, related_name="contained_articles", on_delete=models.CASCADE)
    order = models.IntegerField()
