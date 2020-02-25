# Imports ##############################################################################################################
from rest_framework.permissions import DjangoModelPermissions

# Permissions ##########################################################################################################


class FullDjangoModelPermissions(DjangoModelPermissions):
    """
    As described in https://www.django-rest-framework.org/api-guide/permissions/#djangomodelpermissions, the base
    DjangoModelPermissions class does not include the 'view' model permission for GET requests. This override the class
    to add this behaviour.
    """
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
