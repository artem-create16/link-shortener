import aiohttp_jinja2
import aioredis
import jinja2
from aiohttp import web
from aiohttp_session import setup as setup_session
from aiohttp_session.redis_storage import RedisStorage

from application.middlewares import setup_middlewares
from application.routes import setup_routes
from application.settings import BASE_DIR
from application.views import SiteHandler


def config_jinja2(app):
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(
            str(BASE_DIR / 'application' / 'templates')
        ))


async def setup_redis(app, loop):
    pool = await aioredis.create_redis_pool(address=('redis', 6379), loop=loop)

    async def close_redis():
        pool.close()
        await pool.wait_closed()

    app.on_cleanup.append(close_redis)
    app['redis_pool'] = pool
    return pool


async def init_func(loop):
    app = web.Application()
    redis_pool = await setup_redis(app, loop)
    handler = SiteHandler(redis_pool)
    setup_routes(app, handler)
    setup_middlewares(app)
    setup_session(app, RedisStorage(redis_pool))
    config_jinja2(app)
    return app



