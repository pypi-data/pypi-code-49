# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from allaccess.views import OAuthCallback, OAuthRedirect
from allaccess.compat import get_user_model
from django.conf import settings
from django.shortcuts import redirect

from backstage_oauth2.client import OAuth2BearerClient


class BackstageOAuthCallback(OAuthCallback):

    info_lookup_field = 'email'
    client_class = OAuth2BearerClient
    reverse_error_redirect = getattr(
        settings,
        'OAUTH_REVERSE_LOGIN_ERROR_REDIRECT',
        'admin:index'
    )
    reverse_login_redirect = getattr(
        settings,
        'OAUTH_REVERSE_LOGIN_REDIRECT',
        None
    )
    create_random_user = getattr(
        settings,
        'ALLACCESS_CREATE_RANDOM_USER',
        True
    )

    def get_error_redirect(self, provider, reason):
        return reverse(self.reverse_error_redirect)

    def get_login_redirect(self, provider, user, access, new=False):
        if (self.reverse_login_redirect and
                (hasattr(user, 'is_staff') and user.is_staff)):
            return reverse(self.reverse_login_redirect)
        return '/'

    def get_client(self, provider):
        return self.client_class(provider)

    def get_user_id(self, provider, info):
        identifier = None
        if hasattr(info, 'get'):
            identifier = info.get(self.info_lookup_field)

        if identifier is not None:
            return identifier

        return super(BackstageOAuthCallback, self).get_user_id(provider, info)

    @staticmethod
    def get_user(user_cls, username, email):
        return user_cls.objects.get(username=username, email=email)

    @staticmethod
    def transform_user_metadata(user_metadata, info, username, email):
        return user_metadata

    def handle_new_user(self, provider, access, info):
        "Create a shell auth.User and redirect."
        user = self.get_or_create_user(provider, access, info)
        if user is None:
            return redirect(self.get_error_redirect(
                provider,
                'Username and email not found on user info'
            ))
        return super(BackstageOAuthCallback, self).handle_new_user(
            provider, access, info
        )

    def get_or_create_user(self, provider, access, info):
        email = info.get('email', '')
        username = info.get('username', email) or email
        if username:
            User = get_user_model()
            try:
                return self.get_user(User, username, email)
            except User.DoesNotExist:
                pass
            username = username
            user_metadata = {
                User.USERNAME_FIELD: username,
                'email': info.get('email', ''),
                'password': None,
                'first_name': info.get('name', ''),
                'last_name': info.get('surname', ''),
            }

            user = User.objects.create_user(
                **self.transform_user_metadata(
                    user_metadata, info, username, email)
            )
            user.is_staff = getattr(settings, 'OAUTH_NEW_USER_IS_STAFF', True)
            user.save()
            return user
        elif self.create_random_user:
            return super(BackstageOAuthCallback, self).get_or_create_user(
                provider, access, info
            )

        return None


class BackstageOAuthRedirect(OAuthRedirect):
    provider = ''

    def get_redirect_url(self, **kwargs):
        return super(BackstageOAuthRedirect, self).get_redirect_url(
            provider=self.provider
        )
