from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from unittest.mock import patch
from freezegun import freeze_time

User = get_user_model()


class AuthLoggerTestCase(TestCase):
    login_url = '/admin/login/'

    @freeze_time("2018-09-21T10:11:12-04:00")
    @patch('auth_logger.signals.handlers.logger')
    def test_login(self, mock_logger):
        """
        Test that successful log in attempts for staff users are logged
        """
        user = User.objects.create_user(username="test", email='test@example.com', password="sometest")
        user.is_staff = True
        user.is_superuser = True
        user.save()

        # Random IP address from https://www.randomlists.com/ip-addresses?qty=12&ipv4=true
        self.client.post(self.login_url,
            data={
                'username': 'test',
                'password': 'sometest',
            },
            HTTP_X_FORWARDED_FOR='32.222.116.183')

        mock_logger.info.assert_called_with(
            "User Login Successful username:[test] email:[test@example.com] ip:[32.222.116.183] datetime:[2018-09-21 14:11:12+00:00]")


    @freeze_time("2018-09-21T10:11:12-04:00")
    @patch('auth_logger.signals.handlers.logger')
    def test_failed_login(self, mock_logger):
        """
        Test that failed log in attempts for staff users are logged
        """
        user = User.objects.create_user(username="test", password="sometest")
        user.is_staff = True
        user.is_superuser = True
        user.save()

        # Random IP address from https://www.randomlists.com/ip-addresses?qty=12&ipv4=true
        self.client.post(self.login_url,
            data={
                'username': 'test',
                'password': 'incorrectpassword',
            },
            HTTP_X_FORWARDED_FOR='32.222.116.183')

        mock_logger.info.assert_called_with(
            "User Login Failed username:[test] email:[] ip:[32.222.116.183] datetime:[2018-09-21 14:11:12+00:00]")


    @freeze_time("2018-09-21T10:11:12-04:00")
    @patch('auth_logger.signals.handlers.logger')
    def test_non_staff_login(self, mock_logger):
        """
        Test that successful log in attempts for non-staff users are not logged
        """
        User.objects.create_user(username="test", password="sometest")

        self.client.post(self.login_url, {'username': 'test', 'password': 'sometest'})
        mock_logger.info.assert_not_called()


    @freeze_time("2018-09-21T10:11:12-04:00")
    def test_authenticate_method(self):
        """
        Django authenticate method can be called with just a token (no user)

        https://docs.djangoproject.com/en/1.11/topics/auth/default/#authenticating-users
        """
        authenticate(token="blarg")
