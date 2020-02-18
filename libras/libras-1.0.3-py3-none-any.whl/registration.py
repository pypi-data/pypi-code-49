from flask import jsonify, g, request, Response
from .exception import FlaskException
from .response import ResponseBody
import time
import json


class Registration(object):

    @staticmethod
    def global_exception(app):
        @app.errorhandler(FlaskException)
        def handle_invalid_usage(error):
            resp = jsonify(error.__dict__)
            resp.headers['Content-Type'] = 'application/json;charset=UTF-8'
            resp.status_code = error.status_code
            return resp

        @app.errorhandler(Exception)
        def handle_default_error(error):
            # from werkzeug.http import HTTP_STATUS_CODES
            resp = Response()
            code = 400
            if hasattr(error, 'code'):
                code = error.code
            if hasattr(error, 'args') and isinstance(error.args, tuple):
                error_message = error.args
            default_data = ResponseBody(code=code, message='网络不给力',
                                        error_message=getattr(error, 'description',
                                                              error_message)).__dict__
            resp.set_data(json.dumps(default_data))
            resp.headers['Content-Type'] = 'application/json;charset=UTF-8'
            resp.status_code = code
            return resp

    @staticmethod
    def register_before_request(app):
        @app.before_request
        def request_cost_time():
            g.request_start_time = time.time()
            g.request_time = lambda: "%.5f" % (time.time() - g.request_start_time)

    @staticmethod
    def register_after_request(app):
        @app.after_request
        def log_response(resp):
            log_config = app.property('log') if app.property('log') else {"level": 'INFO'}
            message = '[%s] - [%s] -> [%s] costs:%.3f ms' % (
                request.remote_addr,
                request.method,
                request.path,
                float(g.request_time()) * 1000
            )
            if log_config['level'] == 'INFO':
                app.logger.info(message)
            elif log_config['level'] == 'DEBUG':
                req_body = '{}'
                try:
                    req_body = request.get_json() if request.get_json() else request.args
                except:
                    pass
                message += " - p: %s, r: %s " % (
                    json.dumps(req_body, ensure_ascii=False),
                    json.dumps(resp.json, ensure_ascii=False) if resp.is_json else resp.data
                )
                app.logger.debug(message)
            return resp

    @staticmethod
    def register_blueprints(app):
        from .mapping import import_modules
        import_modules(app)

    @staticmethod
    def register_db(app):
        pass
        # if app.prop("SQLALCHEMY_DATABASE_URI"):
        #     pass
            # from .db.mysql import db
            # db.init_app(app)

    @staticmethod
    def register_filter(app):
        from .filter.restful_filter import RestfulFilter
        app.register_filter(RestfulFilter)

        @app.responsefilter(app.property('app.filter'))
        def filter():
            return RestfulFilter
        pass

    @staticmethod
    def register(app):
        Registration.global_exception(app)
        Registration.register_before_request(app)
        Registration.register_after_request(app)
        Registration.register_blueprints(app)
        Registration.register_filter(app)
        Registration.register_db(app)


