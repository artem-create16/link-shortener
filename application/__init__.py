import aiohttp_jinja2
import jinja2
from aiohttp import web

from application.middlewares import setup_middlewares
from application.settings import BASE_DIR
from application.views import index_handler, post_handler


def init_func():
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(
            str(BASE_DIR / 'application' / 'templates')
        )
    )
    setup_middlewares(app)
    app.router.add_get('/', index_handler)
    app.router.add_post('/', index_handler)
    return app



