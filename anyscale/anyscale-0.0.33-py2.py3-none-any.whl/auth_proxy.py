from aiohttp import web

known_token = set()


async def error_page(request):
    # Serve custom error page for the services
    return web.Response(
        text="""
<html>
    <head>
        <title> Retrying </title>
        <meta http-equiv="refresh" content="5">
        <style>
        body {
            font-family: noto sans,sans-serif;
            padding: 25px;
        }
        </style>
    </head>
    <body>
      <h1>
        Loading...
      </h1>

      <h2> ⌛ </h2>
      <p> Service currently unavailable. </p>
      <p> This page will automatically refresh. </p>

    </body>
</html>
        """,
        status=502,  # bad gateway
        content_type="text/html"
    )


async def index(request):
    token = request.query.get("token")
    redirect_to = request.query.get("redirect_to")
    path = {
        "tensorboard": "/tensorboard/",
        "dashboard": "/"
    }

    if not token or not redirect_to or redirect_to not in path.keys():
        return web.Response(
            text="token or redirect_to field not found, "
                 "maybe you forgot to add `?token=..&redirect_to.` field? "
                 "redirect_to={tensorboard, dashboard}.",
            status=401,
        )
    # TODO(simon): set token on startup
    known_token.add(token)

    resp = web.HTTPFound(path[redirect_to])
    resp.set_cookie("anyscale-token", token)
    raise resp


async def authorize(request):
    print(
        "Got authorizatoin request for:",
        request.headers.get("X-Forwarded-Uri", "unknown"),
    )
    cookies = request.cookies
    if cookies.get("anyscale-token") in known_token:
        return web.Response(text="Authorized", status=200)
    else:
        return web.Response(text="Unauthorized", status=401)


auth_app = web.Application()
auth_app.add_routes([
    web.get("/", index),
    web.get("/authorize", authorize),
    web.get("/error_page", error_page)
    ])

app = web.Application()
app.add_subapp("/auth", auth_app)
