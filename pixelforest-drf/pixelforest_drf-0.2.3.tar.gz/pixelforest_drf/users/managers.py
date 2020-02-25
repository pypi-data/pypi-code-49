# Imports ##############################################################################################################
from django.contrib.auth.base_user import BaseUserManager
from pixelforest_drf.companies.models import Service
from pixelforest_drf.utils.querysets import DownIsActiveMixinManager


# Managers #############################################################################################################

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """ Creates and saves a User with the given email and password """
        if not email:
            raise ValueError("'email' must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # Set defaults for the extra fields values passed to the create_user method
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        # Create the user
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        # Set defaults for the extra fields values passed to the create_user method
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('service', Service.superuser_default())

        # Verify that is_superuser is always True for a superuser
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True')

        # Verify that is_superuser must have a Service (In case of SuperUser Pixelforest Data Team)
        if not extra_fields.get('service'):
            raise ValueError('Superuser must have a linked Service')

        # Create the user
        return self._create_user(email, password, **extra_fields)


class UserAndDownIsActiveManager(DownIsActiveMixinManager, UserManager):
    use_in_migrations = True
