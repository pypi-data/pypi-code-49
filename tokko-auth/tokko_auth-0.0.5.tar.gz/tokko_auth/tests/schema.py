from graphene import ObjectType, String, Schema

from tokko_auth.decorators import has_permission


class QueryTesting(ObjectType):
    protected_query = String()
    protected_query_two_required_scopes = String()
    protected_query_at_least_one_of_required_scopes = String()

    @has_permission("test:testing", has_all=True)
    def resolve_protected_query(self, info):
        return "You're Authorized!"

    @has_permission("test:testing", "my_other:scope", has_all=True)
    def resolve_protected_query_two_required_scopes(self, info):
        return "You're Authorized!"

    @has_permission("test:testing", "my_other:scope", at_least_one=True)
    def resolve_protected_query_at_least_one_of_required_scopes(self, info):
        return "You're Authorized!"


TESTING_SCHEMA = Schema(query=QueryTesting, auto_camelcase=False)
