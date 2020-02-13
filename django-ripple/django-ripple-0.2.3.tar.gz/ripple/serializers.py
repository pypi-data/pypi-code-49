from datetime import timedelta

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.sites.shortcuts import get_current_site
from django.core import signing
from django.shortcuts import reverse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import ugettext_lazy as _


from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .auth import generate_verify_email_token
from .models import ImageAsset, Article, ArticleCollection, ArticleOrder, ArticleCollectionOrder, RichTextAsset, TextAsset
from .models import User

user_model = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    is_admin = serializers.BooleanField(source='is_superuser', read_only=True)

    def update(self, instance, validated_data):

        email_changed = False
        
        if not self.partial and validated_data.get('email') is not None:

            email_changed = instance.email != validated_data['email']

        if email_changed:
            instance.is_email_verified = False

        instance = super().update(instance, validated_data)

        if email_changed:
            try:
                instance.send_verification_email()
            except:
                # don't want email send exceptions to block updates
                pass

        return instance

    class Meta:
        model = user_model
        fields = ('id', 'email', 'first_name', 'last_name', 'profile_pic',
                  'phone_number', 'is_authenticated', 'is_admin', 'is_staff',
                  'is_email_verified')
        read_only_fields = ['is_authenticated',
                            'is_admin', 'is_staff', 'is_email_verified']


class ImageAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageAsset

        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Article
        depth = 1
        fields = '__all__'


class ArticleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleOrder

        fields = ['article', 'order']


class ArticleCollectionOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCollectionOrder

        fields = ['article_collection', 'order']


class ArticleCollectionSerializer(serializers.ModelSerializer):

    article_order = ArticleOrderSerializer(
        source='articleorder_set', many=True)
    article_collection_order = ArticleCollectionOrderSerializer(
        source='container_articles', many=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = ArticleCollection
        depth = 1
        fields = '__all__'


class RichTextAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RichTextAsset

        fields = '__all__'


class TextAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextAsset

        fields = '__all__'


class ImageAssetSerializerB(serializers.ModelSerializer):
    class Meta:
        model = ImageAsset

        fields = ('assetid', 'id', 'image', 'published')


class RichTextAssetSerializerB(serializers.ModelSerializer):
    class Meta:
        model = RichTextAsset

        fields = ('assetid', 'id', 'text', 'published')


class TextAssetSerializerB(serializers.ModelSerializer):
    class Meta:
        model = TextAsset

        fields = ('assetid', 'id', 'text', 'published')


class ImageAssetSerializerC(serializers.ModelSerializer):
    class Meta:
        model = ImageAsset

        fields = ('assetid',)


class RichTextAssetSerializerC(serializers.ModelSerializer):
    class Meta:
        model = RichTextAsset

        fields = ('assetid',)


class TextAssetSerializerC(serializers.ModelSerializer):
    class Meta:
        model = TextAsset

        fields = ('assetid',)


class ArticleSerializerB(serializers.ModelSerializer):

    title = TextAssetSerializerC(read_only=True)
    text = RichTextAssetSerializerC(read_only=True)
    image = ImageAssetSerializerC(read_only=True)

    class Meta:
        model = Article
        depth = 1
        fields = ('assetid', 'id', 'title', 'text', 'image', 'published')


class ArticleCollectionSerializerB(serializers.ModelSerializer):

    class Meta:
        model = ArticleCollection
        fields = ('assetid',)


class SignUpSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)

    class Meta:
        model = user_model
        fields = ['email', 'password', 'first_name', 'phone_number',
                  'last_name', 'password_confirm']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        # check password match
        if attrs.get('password') != attrs.get('password_confirm'):
            raise ValidationError(_('Password mismatch'))

        attrs.pop('password_confirm')
        # do password validation check here as we want mismatch
        # to fire before password not allowed

        user = user_model(**attrs)
        try:
            validate_password(attrs.get('password'), user)

        except ValidationError as validation_error:
            raise ValidationError({'password': validation_error.messages})

        return attrs

    def create(self, validated_data):
        user = user_model.objects.create_user(**validated_data)
        return user

    def save(self, **kwargs):

        super().save(**kwargs)

        # self.instance.send_sign_up_email()


class LoginSerializer(serializers.Serializer):

    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):

        user = authenticate(self.context['request'], **data)

        # add some specific checks here like user.is_active
        if user:
            if not user.is_active:
                err_msg = _('User account is disabled')
                raise ValidationError(err_msg)

            data['user'] = user
            return data

        raise ValidationError(_('Unable to login with provided credentials'))


class PasswordChangeSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def __init__(self, *args, **kwargs):

        # need to pass user information to the PasswordChangeForm
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')

        self.user = getattr(self.request, 'user', None)

    def validate_old_password(self, value):

        if not self.user.check_password(value):
            raise serializers.ValidationError(
                _("Current password provided was incorrect."))

        return value

    def validate(self, data):

        self.password_change_form = PasswordChangeForm(self.user, data=data)

        if not self.password_change_form.is_valid():
            raise ValidationError(self.password_change_form.errors)

        return data

    def save(self):

        self.password_change_form.save()
        update_session_auth_hash(self.request, self.user)


class PasswordResetRequestSerializer(serializers.Serializer):

    email = serializers.EmailField()

    def validate_email(self, value):

        reset_form = PasswordResetForm(data=self.initial_data)

        if not reset_form.is_valid():
            raise serializers.ValidationError(reset_form.errors)

        return value

    def get_user(self):

        # email is unique but call .filter().first()
        # to prevent throwing here

        active_user = user_model.objects.filter(
            email__iexact=self.validated_data['email'],
            is_active=True
        ).first()

        if active_user and active_user.has_usable_password:
            return active_user

        return None

    def save(self):

        user = self.get_user()
        # TODO to handle no user found throw ValidationError ?

        if user:
            user.send_password_reset_email()


class PasswordResetConfirmSerializer(serializers.Serializer):

    new_password1 = serializers.CharField(max_length=256)
    new_password2 = serializers.CharField(max_length=256)
    uidb64 = serializers.CharField()
    token = serializers.CharField()

    def validate(self, data):
        self._errors = {}
        # first get user from uid
        try:
            uid = force_text(urlsafe_base64_decode(data['uidb64']))
            self.user = user_model.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, user_model.DoesNotExist):
            raise ValidationError({'uidb64': ['Invalid value']})

        self.set_password_form = SetPasswordForm(
            user=self.user, data=data
        )

        if not self.set_password_form.is_valid():
            raise ValidationError(self.set_password_form.errors)
        if not default_token_generator.check_token(self.user, data['token']):
            raise ValidationError(
                {'token': ['Expiried or is invalid']})

        return data

    def save(self):
        return self.set_password_form.save()


# class SendEmailVerificationSerializer(serializers.Serializer):

#     user_id = serializers.IntegerField()
#     email = serializers.EmailField()

#     def save(self):

#         token = generate_verify_email_token(
#             self.validated_data['user_id'],
#             self.validated_data['email']
#         )

#         # TODO red - this is current hard coded, maybe make it dynamic
#         template_params = {
#             'user': self.context.get('user'),
#             'url': f"{settings.SITE_URL}/verify?token={token}"
#         }

#         msg_plain = render_to_string('verify_email.txt', template_params)
#         msg_html = render_to_string('verify_email.html', template_params)

#         filtered_send_mail(
#             'Ripple Energy - Account Verification Email',
#             msg_plain,
#             'support@example.com',
#             [self.validated_data['email']],
#             html_message=msg_html,
#             fail_silently=False,
#         )


class ConfirmEmailSerializer(serializers.Serializer):

    token = serializers.CharField(max_length=256)

    def __init__(self, *args, **kwargs):
        super(ConfirmEmailSerializer, self).__init__(*args, **kwargs)

    def validate_token(self, value):

        invalid_token_message = ('Invalid Token: Please ensure you have'
                                 ' used the link'
                                 ' provided in the verification email.')

        try:
            unsigned = signing.loads(value, max_age=timedelta(days=1))

        except signing.SignatureExpired:
            raise ValidationError(_('Verification Token Expired'))
        except signing.BadSignature:
            # token tampered with
            raise ValidationError(
                _(invalid_token_message))

        if not unsigned.get('action') == 'verify_email':
            raise ValidationError(_(invalid_token_message))

        self.user = user_model.objects.get(id=unsigned['user_id'])

        if not self.user.email == unsigned['email']:
            raise ValidationError(
                _(('Email address associated with this account does not match'
                   ' with confirmation token'))
            )

        return value

    def validate(self, attrs):

        if self.user.is_email_verified:
            raise ValidationError(
                _("Email has already been verified for this account"))

        return attrs

    def save(self):

        user = self.user
        user.is_email_verified = True
        user.save()
        return user
