from .views import marker, redirect


def setup_routes(app):
    app.router.add_get("/__marker.gif", marker)
    app.router.add_get("/{deeplink_id}", redirect)
