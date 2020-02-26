from pyvirtualdisplay import Display

from django.conf import settings
from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core import mail
from django.shortcuts import reverse
from django.template.loader import render_to_string
from django.test import override_settings
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import factory
from freezegun import freeze_time
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail
from rest_framework import status
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from .factories import UserFactory
from .base import TestEmailMixin
from ripple.auth import generate_verify_email_token


class AuthenticationTestData:

    not_registered_user = factory.build(dict, FACTORY_CLASS=UserFactory)
    # test = UserFactory.build()
    @classmethod
    def setUpTestData(cls):

        cls.user = UserFactory()

        super().setUpTestData()


class LoginViewTestCase(AuthenticationTestData, APITestCase):

    end_point = '/api/account/log_in'

    def test_can_login(self):

        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)

        response = self.client.post(self.end_point, {
            'email': self.user.email,
            'password': self.user.password_confirm
        })

        user = get_user(self.client)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(user.is_authenticated)

    def test_cant_login_with_wrong_password(self):

        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)

        response = self.client.post(self.end_point, {
            'email': self.user.email,
            'password': 'wrong'
        })

        user = get_user(self.client)
        self.assertEqual(response.status_code, 400)
        self.assertFalse(user.is_authenticated)

    def test_cant_login_if_user_doesnt_exist(self):

        response = self.client.post(self.end_point, {
            'email': self.not_registered_user['email'],
            'password': 'not_important'
        })

        self.assertEqual(response.status_code, 400)

    # def test_login_validation_if_fields_blank(self):
        # pass


class LogoutViewTestCase(AuthenticationTestData, APITestCase):

    end_point = '/api/account/log_out'

    def test_can_logout(self):

        self.client.force_login(user=self.user)
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

        self.client.post(self.end_point)
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)


class AccountStatusViewTestCase(
        AuthenticationTestData, APITestCase):

    end_point = '/api/account/status'

    def test_can_retreive_account_data(self):

        self.client.force_authenticate(self.user)

        expected = {
            'id': self.user.id,  # TODO red - do we want id on response?
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'profile_pic': None,  # TODO red - image field testing
            'is_authenticated': self.user.is_authenticated,
            'is_admin': self.user.is_superuser,
            'is_staff': self.user.is_staff,
            'is_email_verified': self.user.is_email_verified,
            'phone_number': self.user.phone_number
        }

        response = self.client.get(self.end_point)
        
        for key in expected.keys():
            self.assertEqual(response.data[key], expected[key])

    def test_can_retreive_anonymous_data(self):

        expected = {
            'is_email_verified': False,
            'is_staff': False,
            'is_admin': False,
            'is_authenticated': False
        }

        response = self.client.get(self.end_point)

        self.assertDictEqual(expected, response.data)

# TODO red - fix TestEmailMixin


class SignUpTests(AuthenticationTestData):

    def get_valid_post_data(self, extra_kwargs={}):

        return {
            **self.not_registered_user,
            'password': self.not_registered_user['password_confirm'],
            **extra_kwargs
        }

    def get_valid_post_response(self, extra_kwargs={}):
        return self.client.post(
            self.end_point,
            self.get_valid_post_data(extra_kwargs)
        )

    def get_user_response_data(self, response):
        return response.json()

    def test_can_sign_up(self):
        response = self.get_valid_post_response()
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            self.get_user_response_data(response),
            {key: self.not_registered_user[key] for key in [
                'first_name', 'last_name', 'email']}

        )
        user = get_user_model().objects.get(
            email=self.not_registered_user['email'])

    def test_cant_sign_up_with_same_email(self):
        response = self.get_valid_post_response(
            {
                'password': self.not_registered_user['password_confirm'],
                'email': self.user.email,
            }
        )

        self.assertEqual(response.status_code, 400)

        # TODO red look in drf for "(model) with this (field)..." exists
        self.assertDictEqual(
            self.get_user_response_data(response),
            {'email': ['user with this email address already exists.']}
        )

    def test_cant_sign_up_with_bad_email(self):

        response = self.get_valid_post_response({'email': "bad"})

        self.assertEqual(response.status_code, 400)

        self.assertDictEqual(
            self.get_user_response_data(response),
            {'email': ['Enter a valid email address.']}
        )

    def test_cant_sign_up_without_names(self):

        # TODO red - currently failing
        # do we want names enforced?
        response = self.get_valid_post_response({'first_name': ''})

        self.assertEqual(response.status_code, 400)

        # TODO red look in drf for "(model) with this (field)..." exists
        self.assertDictEqual(
            self.get_user_response_data(response),
            {'first_name': ['This field may not be blank.']}
        )

    def test_cant_sign_up_without_matching_passwords(self):
        response = self.get_valid_post_response({'password': 'wrong'})

        self.assertEqual(response.status_code, 400)

        self.assertDictEqual(
            self.get_user_response_data(response),
            {'non_field_errors': ['Password mismatch']}
        )


class SignUpViewTestCase(SignUpTests, APITestCase):

    end_point = '/api/account/sign_up'


class PasswordChangeViewTestCase(AuthenticationTestData, APITestCase):

    end_point = '/api/account/password/change'

    def test_can_change_password(self):

        self.client.force_login(self.user)
        response = self.client.post(
            self.end_point,
            {
                'old_password': self.user.password_confirm,
                'new_password1': 'some_new_thing1',
                'new_password2': 'some_new_thing1',
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()

        self.assertTrue(self.user.check_password('some_new_thing1'))

    def test_cant_change_with_wrong_old_password(self):

        self.client.force_login(self.user)
        response = self.client.post(
            self.end_point,
            {
                'old_password': 'wrong',
                'new_password1': 'some_new_thing1',
                'new_password2': 'some_new_thing1',
            }
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.user.refresh_from_db()

        self.assertFalse(self.user.check_password('some_new_thing1'))


class PasswordResetRequestViewTestCase(
        AuthenticationTestData, TestEmailMixin, APITestCase):

    end_point = '/api/account/password/reset'

    def test_can_request_reset_email(self):
        response = self.client.post(self.end_point, {
            'email': self.user.email
        })

        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk)).decode()
        token = default_token_generator.make_token(self.user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assert_email_has_been_sent(
            'password_reset_email.txt',
            'password_reset_email.html',
            {
                'email': self.user.email,
                'url': (f"{settings.SITE_URL}/reset-password-confirm"
                        f"?uidb64={uidb64}&token={token}"),
                'user': self.user
            }
        )

    def test_doesnt_send_if_email_not_found(self):

        response = self.client.post(self.end_point, {
            'email': 'not@user.com'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(mail.outbox), 0)

    def test_error_on_bad_email(self):

        response = self.client.post(self.end_point, {
            'email': 'not_an_email'
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(mail.outbox), 0)


class PasswordResetConfirmVewTestCase(AuthenticationTestData, APITestCase):

    end_point = '/api/account/password/reset_confirm'

    def test_can_reset_password(self):

        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk)).decode()
        token = default_token_generator.make_token(self.user)

        response = self.client.post(
            self.end_point,
            {
                'new_password1': 'something_new_1',
                'new_password2': 'something_new_1',
                'uidb64': uidb64,
                'token': token
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user.refresh_from_db()

        self.assertTrue(self.user.check_password('something_new_1'))

        # Don't log in after reset
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_invalid_token_bad_request(self):
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk)).decode()

        response = self.client.post(
            self.end_point,
            {
                'new_password1': 'something_new_1',
                'new_password2': 'something_new_1',
                'uidb64': uidb64,
                'token': 'tampered_with'
            }
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'token': ['Expiried or is invalid']})

        self.user.refresh_from_db()

        self.assertFalse(self.user.check_password('something_new_1'))

    def test_uidb64_for_different_user_bad_request(self):

        other_user = UserFactory()

        other_user_uidb64 = urlsafe_base64_encode(
            force_bytes(other_user.pk)).decode()
        token = default_token_generator.make_token(self.user)

        response = self.client.post(
            self.end_point,
            {
                'new_password1': 'something_new_1',
                'new_password2': 'something_new_1',
                'uidb64': other_user_uidb64,
                'token': token
            }
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'token': ['Expiried or is invalid']})
        self.user.refresh_from_db()

        self.assertFalse(self.user.check_password('something_new_1'))


class SendEmailVerificationViewTestCase(
        AuthenticationTestData, TestEmailMixin, APITestCase):

    end_point = '/api/account/send_verify_email'

    def test_can_request_verification_email(self):

        self.client.force_login(self.user)
        token = generate_verify_email_token(self.user.id, self.user.email)

        response = self.client.get(self.end_point)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assert_email_has_been_sent(
            'verify_email.txt',
            'verify_email.html',
            {
                'url': f"{settings.SITE_URL}/verify?token={token}",
                'user': self.user
            }
        )


class UserUpdateView(AuthenticationTestData, APITestCase):

    def test_can_update_user_data(self):
        self.client.force_login(self.user)
        response = self.client.patch(
            f'/api/account/{self.user.id}/',
            {
                'phone_number': '07777777777'
            },
            format='json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['phone_number'], '07777777777')

    def test_cant_update_someone_elses_details(self):

        user_2 = UserFactory()
        self.client.force_login(self.user)
        response = self.client.patch(
            f'/api/account/{user_2.id}/',
            {
                'phone_number': '07777777777'
            },
            format='json'
        )

        self.assertEqual(response.status_code, 404)

    def test_cant_update_invalid_phone(self):

        user_2 = UserFactory()
        self.client.force_login(self.user)
        response = self.client.patch(
            f'/api/account/{self.user.id}/',
            {
                'phone_number': '777'
            },
            format='json'
        )

        self.assertEqual(response.status_code, 400)


class ConfirmEmailViewTestCase(
        AuthenticationTestData, TestEmailMixin, APITestCase):

    end_point = '/api/account/verify_email'

    def test_can_verify_with_valid_token(self):

        self.assertFalse(self.user.is_email_verified)

        token = generate_verify_email_token(self.user.id, self.user.email)

        response = self.client.post(self.end_point, {'token': token})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user.refresh_from_db()

        self.assertTrue(self.user.is_email_verified)

    def test_can_verify_with_different_email_in_token(self):

        self.assertFalse(self.user.is_email_verified)

        token = generate_verify_email_token(
            self.user.id, 'something_else@test.com')

        response = self.client.post(self.end_point, {'token': token})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {
                'token': [('Email address associated with this account does '
                           'not match with confirmation token')]
            }
        )

        self.user.refresh_from_db()

        self.assertFalse(self.user.is_email_verified)
