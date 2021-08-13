from aiohttp import web
from application import init_func
import asyncio


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_func(loop))
    web.run_app(app)

