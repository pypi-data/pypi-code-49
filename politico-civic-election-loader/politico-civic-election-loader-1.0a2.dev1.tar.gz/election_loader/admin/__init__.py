# Imports from Django.
from django.contrib import admin


# Imports from election_loader.
from election_loader.admin.loader_token import LoaderTokenAdmin
from election_loader.models import LoaderToken


admin.site.register(LoaderToken, LoaderTokenAdmin)
