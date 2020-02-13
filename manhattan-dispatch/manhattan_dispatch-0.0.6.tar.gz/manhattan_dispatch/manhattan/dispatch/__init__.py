from flask import current_app, url_for
from werkzeug.middleware.dispatcher import DispatcherMiddleware

__all__ = ['Dispatcher']


class Dispatcher:
    """
    Allows one to mount middlewares or applications in a WSGI application.

    This is useful if you want to combine multiple WSGI applications::

        app = DispatcherMiddleware(app, {
            '/app2':        app2,
            '/app3':        app3
        })

    """

    def __init__(self, app, mounts=None):
        self.app = app
        self.mounts = mounts or {}

        # Build a map of paths to apps
        paths = {v: k for k, v in self.mounts.items()}
        paths[self.app] = ''

        self.url_for_resolver = URLForResolver(
            [self.app] + list(self.mounts.values()),
            paths
            )

        # Ensure each app has a reference to the dispatcher
        self.app._dispatcher = self
        for mount, app in self.mounts.items():
            app._dispatcher = self
            app._dispatcher_mount = mount

    def __call__(self, environ, start_response):
        script = environ.get('PATH_INFO', '')
        path_info = ''

        while '/' in script:
            if script in self.mounts:
                app = self.mounts[script]
                break
            script, last_item = script.rsplit('/', 1)
            path_info = '/%s%s' % (last_item, path_info)
        else:
            app = self.mounts.get(script, self.app)

        original_script_name = environ.get('SCRIPT_NAME', '')
        environ['SCRIPT_NAME'] = original_script_name + script

        # Convert empty path info values to a forward slash '/'
        environ['PATH_INFO'] = path_info or '/'

        return app(environ, start_response)

    @property
    def apps(self):
        """Return a list of apps mounted to the dispatcher"""
        return [self.app] + list(self.mounts.values())


class URLForResolver:
    """
    A URL resolver that provides resolution of `url_for` across multiple apps.
    """

    def __init__(self, apps, paths):
        self.apps = apps
        self.paths = paths
        self.cache = {}

        for app in apps:
            app.url_build_error_handlers.append(self)

    def __call__(self, error, endpoint, values):
        """Attempt to resolve a URL any of the registered apps"""

        # Check if we have a cached look up
        if endpoint in self.cache:
            app = self.cache[endpoint]
            if app:

                # We don't want the dispatcher to trigger a recursive loop that
                # kills the server just because a URL can't be built so we add
                # and check for a special flag (with a value of None to prevent
                # it being being part of the output URL) that indicates whether
                # we should raise an error (e.g on subsequent calls).
                if '_raise_error' in values:
                    raise error
                values['_raise_error'] = None

                path = ''
                if app != current_app:
                    path = self.paths[app]

                with app.app_context(), app.test_request_context('/'):
                    return path + url_for(endpoint, **values)

            else:
                raise error

        # Attempt to find an app with the registered endpoint
        for app in self.apps:

            # No point in checking the current app
            if app is current_app:
                continue

            for rule in app.url_map.iter_rules():

                if rule.endpoint == endpoint:
                    # Found - cache the result and call self to return the URL
                    self.cache[endpoint] = app
                    return self(error, endpoint, values)

        # Not found - cache the result and re-raise the error
        self.cache[endpoint] = None
        raise error
