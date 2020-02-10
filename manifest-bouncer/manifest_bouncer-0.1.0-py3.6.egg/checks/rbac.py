from lib.base import CheckBase


class CheckRolesAreListedBeforeRoleBindings(CheckBase):
    whitelist = ['List']
    enable_parameter = 'rbac'
    description = 'check that Roles are listed before RoleBindings'
    default_enabled = True

    def check_roles_before_rolebindings(self, m):
        items = m['items']
        for item in items:
            print(item['metadata']['kind'])
