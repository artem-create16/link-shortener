from aiohttp import web
from application.views import index_handler


def init_func():
    app = web.Application()
    app.router.add_get("/", index_handler)
    return app



