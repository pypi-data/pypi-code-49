# Factories allow test objects to be created much more easily than
# fixtures. Rather than defining the data to be created, factories
# define a blueprint for creating objects which can be called multiple
# times

# factory_boy

from typing import Any, Sequence

from django.contrib.auth import get_user_model
from factory import DjangoModelFactory, Faker, post_generation, LazyAttribute


class UserFactory(DjangoModelFactory):

    first_name = Faker("first_name")
    last_name = Faker("last_name")
    # generate the email address from the random username
    phone_number = '99999999999'
    email = LazyAttribute(
        lambda obj: f'{obj.first_name.lower()}.{obj.last_name.lower()}@rippleenergy.com')

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):

        # randomly generate password is one isn't passed in
        password = extracted if extracted is not None else Faker(
            "password",
            length=42,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ).generate(extra_kwargs={})

        # self.password_confirm = password
        if isinstance(self, dict):
            self['password_confirm'] = password
        else:
            self.password_confirm = password

        if create:

            self.set_password(password)

    class Meta:
        model = get_user_model()
        # https://factoryboy.readthedocs.io/en/latest/orms.html#factory.django.DjangoOptions.django_get_or_create
        django_get_or_create = ["email"]
        exclude = ('password_confirm',)
