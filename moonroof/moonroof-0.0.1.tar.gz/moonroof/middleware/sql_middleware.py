from django.db.models.sql.compiler import SQLCompiler
from datetime import datetime


def create_execute_sql(request):
    def execute_sql(self, *args, **kwargs):
        start = datetime.now()
        executed = self.moonroof_execute_sql(*args, **kwargs)
        end = datetime.now()
        request.moonroof_sql_count = request.moonroof_sql_count + 1
        request.moonroof_sql_time = request.moonroof_sql_time + (end - start).total_seconds()
        return executed
    return execute_sql


class SQLMiddleware(object):

    def before(self, request):
        request.moonroof_sql_count = 0
        request.moonroof_sql_time = 0
        if not hasattr(SQLCompiler, 'moonroof_execute_sql'):
            SQLCompiler.moonroof_execute_sql = SQLCompiler.execute_sql
        SQLCompiler.execute_sql = create_execute_sql(request)

    def key(self):
        return 'sql'

    def value(self, request, response):
        return {
            'query_count': request.moonroof_sql_count,
            'query_time': request.moonroof_sql_time
        }

