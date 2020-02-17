from aiohttp import web

known_token = set()


async def index(request):
    print("Got index request")
#     html = """
# <html>
#     <head>
#         <title> Redirect page </title>
#     </head>
#     <body>
#         <h1> Anyscale Service Proxy </h1>
#         <ul>
#             {}
#         </ul>
#     </body>
# </html>
#     """
    token = request.query.get("token")
    if not token:
        return web.Response(
            text="Token not found, "
                 "maybe you forgot to add `?token=...` field?",
            status=401,
        )

    # TODO(simon): set token on startup
    known_token.add(token)

    # hrefs = ["/tensorboard/"]
    # hrefs = ['<li> <a href="{l}">{l}</a>  </li>'.format(l=h) for h in hrefs]
    # html = html.format("\n".join(hrefs))
    # resp = web.Response(text=html, content_type="text/html")

    resp = web.HTTPFound("/tensorboard/")
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


app = web.Application()
app.add_routes([web.get("/", index), web.get("/authorize", authorize)])
